##
##  Viterbi Algorithm
##  Source from Wikipedia
##  Modified by Adam Slack
##
from nltk.corpus import brown
from nltk.tag.mapping import _UNIVERSAL_TAGS as tagset
# Example observation:
# ['my', 'name', 'is', 'adam', 'and', 'i', 'like', 'to', 'code']

# Example states
# [Adj, Adv, Con, Det, Noun, Num, Pre, Pro, Verb]

# Example starting probabilities
# []

def max_transition(prev_states, states, curr, trans_p):
    """ 
    Calculate with previous stat is most likely be the source of transition
    for the current state.
    """
    return max(prev_states[prev]['prob'] * trans_p[prev][curr] for prev in states)

def initialise_start_probabilities(states, start_p, emit_p, obs):
    """
    create an initial map of state transition probabilities
    where the previous state is None, and the probability of
    each state is a product of the start_p and emit_p
    """
    return { state : {'prob': start_p[state] * emit_p[state][obs[0]], 'prev':None } for state in states }

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [initialise_start_probabilities(states, start_p, emit_p, obs)]
    
    for o in range(1, len(obs)):
        V.append({})
        
        for st in states:
            # determine where the transition was from.
            max_tr_prob = max_transition(prev_states=V[o-1], states=states, curr=st, trans_p=trans_p)

            for prev_st in states:
                # choose the most likely transition.
                if V[o-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    # give this route a probability.
                    max_prob = max_tr_prob * emit_p[st][obs[o]]
                    V[o][st] = {"prob": max_prob, "prev": prev_st}
                    break # Should we really be breaking?...
    opt = []
    # The highest probability for the final state.
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        # add the content of the most likely end state
        # to an array of optimal routes.
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break
    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        # startin with 
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]
    return opt

def calc_start_state_probs(corpus_sents, states):
    """calculate the probability of a sentence starting with a perticular state.""" 
    starts = [sent[0][1] for sent in corpus_sents]
    counts = {state : 0 for state in states}
    total = len(starts)
    for state in starts:
        counts[state] += 1
    return {state: counts[state]/total for state in states}

def calc_trans_probs(corpus_sents, states):
    """ calculate probability of transitioning from one state to the next."""
    trans_counts = {source : { sink : 0 for sink in states} for source in states}
    for sent in corpus_sents:
        for i in range(0, len(sent)-2):
            trans_counts[sent[i][1]][sent[i+1][1]] += 1

    trans_sums = {state : sum(trans_counts[state].values()) for state in states}
    return { source : {
        sink : trans_counts[source][sink] / trans_sums[source] for sink in states
    } for source in states}


def calc_emit_probs(corpus_words, states, obs):
    """ calculate probability of state emitting a given word"""

    state_counts = {state:0 for state in states}
    state_obs_counts = {state : {ob.lower() : 0 for ob in obs} for state in states}
    for pair in corpus_words:
        state = pair[1]
        word = pair[0].lower()
        state_counts[state] += 1
        if word in state_obs_counts[state]:
            state_obs_counts[state][word] += 1

    return { state : {
        ob.lower() : state_obs_counts[state][ob.lower()] / state_counts[state] for ob in obs
    } for state in states}
        

def main():

    # Wiki Example Data.
    obs = ('normal', 'cold', 'dizzy', 'cold')

    states = ('Healthy', 'Fever', 'dead')

    start_p = {'Healthy': 0.6, 'Fever': 0.4, 'dead':0.0}

    trans_p = {
        'Healthy' : {'Healthy': 0.65, 'Fever': 0.3, 'dead': 0.05},
        'Fever' : {'Healthy': 0.35, 'Fever': 0.55, 'dead': 0.1},
        'dead' : {'Healthy': 0.0, 'Fever': 0.0, 'dead':1.0}
    }

    emit_p = {
        'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
        'dead' : {'normal': 0.0, 'cold' : 1.0, 'dizzy': 0.0}
    }

    pos_obs = [ob.lower() for ob in ['I','am','a','walrus','!']]
    pos_states = tagset
    pos_starts = calc_start_state_probs(brown.tagged_sents(tagset='universal'), pos_states)
    pos_trans = calc_trans_probs(brown.tagged_sents(tagset='universal'), pos_states)
    pos_emit = calc_emit_probs(brown.tagged_words(tagset='universal'), pos_states, pos_obs)
    # need to build a set of data in a structure similar to above...
    
    tags = viterbi(pos_obs, pos_states, pos_starts, pos_trans, pos_emit)

    print('\t'.join(tags))
    print('\t'.join(pos_obs))

if __name__ == '__main__':
    main()
