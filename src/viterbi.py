from nltk.corpus import brown
from nltk.tag.mapping import _UNIVERSAL_TAGS as tagset
from collections import defaultdict
import argparse

#
#
#
#
def max_transition(prev_states, states, curr, trans_p):
    """ 
    Calculate with previous stat is most likely be the source of transition
    for the current state.
    """
    return max(prev_states[prev]['prob'] * trans_p[prev][curr] for prev in states)

#
#
#
#
def initialise_start_probabilities(states, start_p, emit_p, obs):
    """
    create an initial map of state transition probabilities
    where the previous state is None, and the probability of
    each state is a product of the start_p and emit_p
    """
    return { 
        state : {
                'prob': start_p[state] * emit_p[state][obs[0]], 'prev':None 
            } for state in states 
        }

#
#
#
#
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [initialise_start_probabilities(states, start_p, emit_p, obs)]
    
    for o in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = max_transition(prev_states=V[o-1], states=states, curr=st, trans_p=trans_p)
            for prev_st in states:
                if V[o-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * emit_p[st][obs[o]]
                    V[o][st] = {"prob": max_prob, "prev": prev_st}
                    break 
    
    opt = []
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None
    for st, data in V[-1].items():
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break

    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]
    return opt

#
#
#
#
def calc_start_state_probs(corpus_sents, states):
    """calculate the probability of a sentence starting with a perticular state.""" 
    starts = [sent[0][1] for sent in corpus_sents]
    counts = {state : 0 for state in states}
    total = len(starts)
    for state in starts:
        counts[state] += 1
    return defaultdict(int,{state: counts[state]/total for state in states})

#
#
#
#
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

#
#
#
#
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

    return { state : defaultdict(int,{
        ob.lower() : state_obs_counts[state][ob.lower()] / state_counts[state] for ob in obs
    }) for state in states}

#
#
#
#
def sum_sentence_lengths(corpus_sents):
    """ sums accross the length of sentences in a corpus """
    return sum(len(sent) for sent in corpus_sents)

#
#
#
#
def split_Corpus(corpus_sents, corpus_words, pct):
    """ Splits a corpus into training and testing data """
    sent_count = len(corpus_sents)
    word_count = len(corpus_words)

    ten_pct_sent_cnt = int(sent_count * (pct/100))

    training_sents = corpus_sents[0 : sent_count - ten_pct_sent_cnt]
    test_sents = corpus_sents[sent_count - ten_pct_sent_cnt : sent_count]

    test_word_cnt = sum_sentence_lengths(test_sents)
    
    training_words = corpus_words[0 : word_count - test_word_cnt]
    test_words = corpus_words[word_count - test_word_cnt : word_count]

    return training_sents, test_sents, training_words, test_words

#
#
#
#
def evaluate_model(test_sents, test_words, pos_states, pos_starts, pos_trans, pos_emit):
    """ Evaluate a trained HMM model using a provided set of test sentences and words """
    
    tags = [viterbi([ob[0].lower() for ob in sent], pos_states, pos_starts, pos_trans, pos_emit) for sent in test_sents ]

    score = sum(sum(1 if tag == test_sents[s_idx][t_idx][1] else 0 for t_idx, tag in enumerate(sent) ) for s_idx, sent in enumerate(tags))
                    
    return score/len(test_words)

#
#
#
#
def main():

    parser = argparse.ArgumentParser(description="Viterbi Decoded HMM POS tagger.")
    parser.add_argument('words', type=str, nargs='+', help="Word in the sentence to be tagged.")
    args = parser.parse_args()
    
    ##
    ## Main Init...
    ##
    tagged_sents = brown.tagged_sents(tagset='universal')
    tagged_words = brown.tagged_words(tagset='universal')

    training_sents, test_sents, training_words, test_words = split_Corpus(tagged_sents, tagged_words, 10)
    
    print('Corpus Sentence Count:', len(tagged_sents))
    print('Corpus Word Count:', len(tagged_words))

    sent = ['No', 'sentence', 'was', 'found', '.']
    if len(args.words) != 0:
        print('Parsed Args: ', args.words)
        sent = args.words
    pos_obs = [ob.lower() for ob in sent]

    pos_states = tagset

    ##
    ## General Model Evaluation.
    ##
    #print('Calculating Training Set Starting probabilities')
    #pos_starts = calc_start_state_probs(training_sents, pos_states)
    #print('Training Set Starting Probabilities calculated')

    #print('Calculating Training Set Transition Probabilities')
    #pos_trans = calc_trans_probs(training_sents, pos_states)
    #print('Training set Transition probabilities calcualted')

    #print('Calculating Training set Emission Probabilities')
    #pos_emit = calc_emit_probs(training_words, pos_states, [ob[0] for ob in test_words])
    #print('Training Set Emission Probabilities Calculated')

    #print('Evaluating Viterbi Decoded HMM')
    #score = evaluate_model(test_sents, test_words, pos_states, pos_starts, pos_trans, pos_emit)
    #print('Viterbi Decoded HMM Evaluated')

    #print('Model Score:', str(score))

    ##
    ## Sentence Evaluation.
    ##
    pos_starts = calc_start_state_probs(tagged_sents, pos_states)

    pos_trans = calc_trans_probs(tagged_sents, pos_states)

    pos_emit = calc_emit_probs(tagged_words, pos_states, pos_obs)

    print('Applying Model to Sentence: ' + ' '.join(sent))
    tags = viterbi(pos_obs, pos_states, pos_starts, pos_trans, pos_emit)

    for i in range(0, len(tags)):
        print('(Tag, Word):', tags[i] + '\t' + sent[i])
    #print('\t'.join(tags))
    #print('\t'.join(sent))
    

    
if __name__ == '__main__':
    main()
