from fyp_utilities import *
import matplotlib.pyplot as plt
import numpy as np

def main():
    fp = '../test_data/alice_in_wonderland.txt'
    #fp = '../books/Hitchhiker\'s Guide to the Galaxy - Douglas Adams.txt'
    #fp = '../books/Dirk Gently\'s Holistic Detective Agency - Douglas Adams.txt'
    #fp = '../books/Harry Potter and the Sorcerer\'s Stone - J. K. Rowling.txt'
    document = read_file(fp)
    entities = extract_entities(document)
    word_map = map_word_occurences(word_tokenize(document))
    getd = time_action(calcuate_GETD, map_entity_idx(entities), word_map)
    getd = getd_tf_idf(getd)
    rows = getd.row_headings
    cols = getd.col_headings

    #document_array = filter_punctuation(document)
    #word_occurences = map_word_occurences(document_array)

    #entity_idxs = cherry_entity_tuple(entities, 0)
    #entity_names = cherry_entity_tuple(entities, 1)
    
    plt.matshow(getd.data, fignum=100, aspect='auto')
    plt.xticks(np.arange(len(cols)), cols, rotation=45)
    plt.yticks(np.arange(len(rows)), rows, rotation=-45)
    plt.show()


if __name__=='__main__':
    main()