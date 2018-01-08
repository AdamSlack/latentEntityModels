from nltk.corpus import brown
from nltk.tag.mapping import _UNIVERSAL_TAGS as tagset

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

def sum_sentence_lengths(corpus_sents):
    """ sums accross the length of sentences in a corpus """
    return sum(len(sent) for sent in corpus_sents)

def split_Corpus(corpus_words, corpus_sents, pct):
    """ Splits a corpus into training and testing data """
    sent_count = len(corpus_sents)
    word_count = len(word_count)

    ten_pct_sent_cnt = sent_count * (1/pct)

    training_sents = [::-ten_pct_sent_cnt]
    test_sents = [ten_pct_sent_cnt::]

    print('Training Sent Length', len(training_sents))
    print('Test Sent Length', len(test_sents))

    
    
    
def main():
    tagged_sents = brown.tagged_sents(tagset='universal')
    tagged_words = brown.tagged_words(tagset='universal')

    split_Corpus(tagged_sents, tagged_words, 10)
    
    print('Corpus Sentence Count:', len(tagged_sents))
    print('Corpus Word Count:', len(tagged_words))
    
    pos_obs = [ob.lower() for ob in ['I','am','a','walrus','!']]

    pos_states = tagset

    pos_starts = calc_start_state_probs(tagged_sents, pos_states)
    pos_trans = calc_trans_probs(tagged_sents, pos_states)

    pos_emit = calc_emit_probs(tagged_words, pos_states, pos_obs)
        
    tags = viterbi(pos_obs, pos_states, pos_starts, pos_trans, pos_emit)

    print('\t'.join(tags))
    print('\t'.join(pos_obs))

if __name__ == '__main__':
    main()
