from time import time
import glob
from os import path
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from collections import defaultdict
import pandas as pd
from nltk.tokenize import RegexpTokenizer
import string
import math
from mat import Mat
import numpy as np

GAUSSIAN005 = 0.03989422804

def create_stanford_tagger():
    classifiers = '../stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz'
    jar_location = '../stanford-ner-2017-06-09/stanford-ner-3.8.0.jar'
    return StanfordNERTagger(classifiers, jar_location, encoding='utf-8')

def read_file(fp):
    if path.isfile(fp):
        with open(fp, encoding='utf-8') as f:
            print('Opening File: ' + fp)
            return f.read()
    else:
        print('Provided file path does not point at a file.')

def load_data_samples(dirpath, seperator='/', globule='*.txt'):
    """ Reads all txt files at a specified location and returns array of data. """
    print('Reading Data')
    if(path.isdir(dirpath)):
        fps = glob.glob(dirpath + seperator + globule)
        return [read_file(fp) for fp in fps]
 
def time_action(action, *args):
    """ Time an action (or function) """
    start = time()
    res = action(*args)
    print("Action done in: %0.3fs." % (time() - start))
    return res

def valid_entity(entity, e_type):
    """ Validate a tuple generated by stanford NER tagger. """
    return e_type != 'O' and len(entity) > 1
    
def map_type_entity_idx(entity_array):
    """ 
    produces a dict of entity types mapping to a dict of entity
    names and associated document index. 
    """
    
    type_map = {e[2] : defaultdict(dict) for e in entity_array}
    
    for idx, n, t in entity_array:
        type_map[t][n] = []
        
    for idx, n, t in entity_array:
        type_map[t][n].append(idx)
    
    return type_map
    

def map_entity_idx(entity_array):
    """ """
    print('Mapping Entity occurence index')
    entities = defaultdict(list)
    for idx, e, t in entity_array:
        entities[e].append(idx)
        
    return entities

def cherry_entity_tuple(entity_array, element_idx):
    """ extracts the element at element_idx for each entity tuple in entity_array"""
    return [e[element_idx] for e in entity_array]

def map_word_occurences(document):
    """ """
    print('Mapping Word Occurrences')
    occurences = defaultdict(list)
    for idx, w in enumerate(document):
        occurences[w.lower()].append(idx)
    return occurences

def extract_tagged_entities(doc):
    """ recursively extract entities in tagged tree """
    entity_array = [(idx, e[0], e[1]) for idx, e in enumerate(doc) if valid_entity(e[0], e[1])]    
    return entity_array
    # return list(filter(lambda e: e[1] != 'O' and len(e[0]) > 1, doc))
    
def extract_entities(document):
    """ """
    print('Extracting Entities')
    tagged_document = tag_document(document)
    entities = extract_tagged_entities(tagged_document)
    return entities
    
def tag_document(document):
    """ tokenise Document into chunked sentences. """
    # tokenised_sentences = [word_tokenize(sent) for sent in sent_tokenize(document)]
    # return ne_chunk_sents([pos_tag(sent) for sent in tokenised_sentences])
    tagger = create_stanford_tagger()
    tokenised_words = word_tokenize(document)
    return tagger.tag(tokenised_words)
    

def filter_punctuation(document):
    tokens = word_tokenize(document)
    punc = set(string.punctuation)
    punc.add ('’')
    return filter(lambda w: w not in punc, tokens)

def calcuate_GETD(entity_map, term_map):
    """ constructs a matrix of entity-term associations. indexable by entity and term"""
    print('Building Gaussion Entity Term Matrix')
    e_keys = entity_map.keys()
    t_keys = term_map.keys()
    e_cnt = len(e_keys)
    t_cnt = len(t_keys)
    print(str(e_cnt) + ' Entity Keys - ' + str(t_cnt) + ' Term Keys' )

    getd = Mat(col_headings=[e.lower() for e in e_keys],
               row_headings=[t.lower() for t in t_keys])

    for idx, e_key in enumerate(e_keys):
        print('Completed ' + str(idx) + ' / ' + str(e_cnt))
        for t_key in t_keys:
            val = 0
            for e in entity_map[e_key]:
                for t in term_map[t_key]:
                    val += gaussian_filter(e - t, 0.001)
            if val > 0.0005:
                getd.set(col=e_key.lower(), row=t_key.lower(), val=1.0)
    return getd
    
def gaussian_filter(x, a):
    """ returns g(x) for x when g(x).a = a """
    return math.sqrt(a / math.pi) * math.pow( math.e , -a * math.pow( x ,2 ))
    
def gaussian_filter_005(x):
    """ returns G(x) for x when a = .005  """
    return GAUSSIAN005 * math.pow(math.e,-0.005*math.pow(x,2))


def getd_tf_idf(getd: 'Mat'):
    """ """
    print('perfoming tf-idf on gaussian entity')
    entities = getd.col_headings
    words = getd.row_headings
    corupus_counts = np.zeros(len(words))
    for e in entities:
        print(e)
        col = getd.get_col(col=e)
        print(col)
        corupus_counts = np.add(corupus_counts, col)

    print(corupus_counts)
    for e in entities:
        for idx, w in enumerate(getd.get_col(e)):
            print(idx)  
            tf_idf = w * (1/corupus_counts[idx])
            getd.set(col=e, row=words[idx], val=tf_idf)

    return getd