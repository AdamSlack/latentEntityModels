from __future__ import print_function
from time import time
import glob
from os import path
import db as db

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

from fyp_utilities import *

from collections import defaultdict

n_samples = 2000
n_features = 1000
n_topics = 10
n_top_words = 1000
book_dir = '../test_data/harry_potter_summaries/'

def store_top_words(model, feature_names, n_top_words):
    conn = db.connect_to_db(host='localhost', dbname='hp_summary', user='postgres', password='password')
    for topic_idx, topic in enumerate(model.components_):
      count = 0
      for i in topic.argsort()[:-n_top_words - 1:-1]:
        db.insert_topic_term(db=conn, topic_id=topic_idx,term=feature_names[i],strength=topic[i])        
        if count < 10:
          print(topic_idx, feature_names[i],topic[i ])
          count += 1

def read_file(fp):
  with open(fp, encoding='utf-8') as f:
    return f.read()

def read_data_samples(fp, glob_str):
  """ Reads all txt files at a specified location and returns array of data. """
  if(path.isdir(fp)):
    fps = glob.glob(fp + glob_str)
    return list(map(lambda x: read_file(x), fps)), fps

def time_action(action, *args):
  t0 = time()
  res = action(*args)
  print("Action done in: %0.3fs." % (time() - t0))
  return res

def calculate_document_distributions(lda_model, feature_names, n_top_words, data_samples, fps):
  """ Calculates the topic distributions for each document."""

  titles = [fp[len(book_dir): (len(fp) - len('*.txt') + 1) ] for idx, fp in enumerate(fps) ]
  book_distributions = {title: defaultdict(int) for title in titles}

  for idx, sample in enumerate(data_samples):
    distribution = defaultdict(int)
    counts = map_word_frequencies(tag_document(sample))

    for topic_idx, topic in enumerate(lda_model.components_):
      for i in topic.argsort()[:-n_top_words - 1:-1]:
        if counts[feature_names[i].lower()] != 0:
          distribution['topic_' + str(topic_idx)] += counts[feature_names[i].lower()] * topic[i]
    book_distributions[titles[idx]] = distribution        

  return book_distributions

def store_book_proportions(distributions):
  """ """
  conn = db.connect_to_db(host='localhost', dbname='hp_summary', user='postgres', password='password')

  for book in distributions.keys():
    print(book)
    print(distributions[book])
    db.insert_book_topic_distribution(conn, book, distributions[book])

# def filter_entities(data_samples):
#   """ Filter Entities in the corpus using the calculated GETM """
#   conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
#   titles = db.select_book_titles(db)
#   entities = [db.select_book_entities(conn, t) for t in titles]

# def filter_pos_tags(data_samples, pos_tags):
#   """ Filter terms in the document not matching tags in a given set"""


# def filter_missing_entity_terms(data_sameples):
# """ Filter terms in the document that aren't associated with any entity in the GETM."""

def retrieve_entity_set():
  """returns a distinct set of entities from the database."""
  conn = db.connect_to_db(host='localhost', dbname='hp_summary', user='postgres', password='password')
  entities = []
  titles = db.select_book_titles(conn)
  for t in titles:
        for e in db.select_book_entities(conn, t[0]):
          entities.append(e[0])
  return set(entities)

def main():
  print('Loading Books...')
  data_samples, fps = time_action(read_data_samples, book_dir, '*.txt')
  print(str(len(data_samples)) + ' data samples read from file')

  es = retrieve_entity_set()
  print(es)
  print('Extracting tf features for LDA...')
  stop_words = ENGLISH_STOP_WORDS.union(es)
  tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=n_features,
                                  stop_words=stop_words)
  tf = time_action(tf_vectorizer.fit_transform, data_samples)

  print('Fitting LDA models with tf features, n_samples=' + str(n_samples) + ' and n_features=' + str(n_features)  +'...')
  lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=5,
                                  learning_method='online',
                                  learning_offset=50.,
                                  random_state=0)
  time_action(lda.fit, tf)

  print('\nWriting topics in LDA model:')
  tf_feature_names = tf_vectorizer.get_feature_names()
  store_top_words(lda, tf_feature_names, n_top_words)
  print('Completed DB insertion.')
  distributions = calculate_document_distributions(lda, tf_feature_names, n_top_words, data_samples, fps)
  store_book_proportions(distributions)

if __name__ == '__main__':
  main()


