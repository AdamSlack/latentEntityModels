from __future__ import print_function
from time import time
import glob
from os import path
import db as db
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from fyp_utilities import *

n_samples = 2000
n_features = 1000
n_topics = 25
n_top_words = 1000

def store_top_words(model, feature_names, n_top_words):
    conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
    for topic_idx, topic in enumerate(model.components_):
      for i in topic.argsort()[:-n_top_words - 1:-1]:
        db.insert_topic_term(db=conn, topic_id=topic_idx,term=feature_names[i],strength=topic[i])

def read_file(fp):
  with open(fp, encoding='utf-8') as f:
    return f.read()

def read_data_samples(fp, glob_str):
  """ Reads all txt files at a specified location and returns array of data. """
  if(path.isdir(fp)):
    fps = glob.glob(fp + glob_str)
    return list(map(lambda x: read_file(x), fps))

def time_action(action, *args):
  t0 = time()
  res = action(*args)
  print("Action done in: %0.3fs." % (time() - t0))
  return res

def calculate_document_distributions(model, feature_names, n_top_words, tf):
  """ Calculates the topic distributions for each document."""

def main():
  print('Loading Books...')
  data_samples = time_action(read_data_samples, '../books/', '*.txt')
  print(str(len(data_samples)) + ' data samples read from file')

  print('Extracting tf features for LDA...')
  tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=n_features,
                                  stop_words='english')
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
  proportions = calculate_document_distributions(lda, tf_feature_names, n_top_words)

if __name__ == '__main__':
  main()
