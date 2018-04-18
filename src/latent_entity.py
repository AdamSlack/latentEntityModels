import db as db
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

def db_conn():
    return db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')


def request_book_entity_topics():
    """ request a list of entities from the database """
    res = db.select_book_entity_topics(db_conn())

    return [{
        'entity' : row[0],
        'book' : row[1],
        'topic' : row[2],
        'strength' : row[3]
    } for row in res]

def main():
    """ Main Process Flow """
    entity_topics = request_book_entity_topics()

    e_keys = [e['entity']+'-$-'+e['book'] for e in entity_topics]

    entities = {e:{'topic_ids' : [], 'topic_str' : []} for e in e_keys}

    for e in entity_topics:
        key = e['entity']+'-$-'+e['book']
        entities[key]['entity'] = e['entity']
        entities[key]['book'] = e['book']
        entities[key]['topic_ids'].append(e['topic'])
        entities[key]['topic_str'].append(e['strength'])

    entity_topics = [entities[e]['topic_str'] for e in entities]

    data = np.array(entity_topics)

    kmeans = KMeans(n_clusters = 5).fit(data)

    #first make some fake data with same layout as yours
    entity_frame = pd.DataFrame(data, columns=['Topic ' + str(t) for t in range(0,10)])
    latent_frame = pd.DataFrame(kmeans.cluster_centers_, columns=['Topic ' + str(t) for t in range(0,10)])


    #now plot using pandas 
    scatter_matrix(entity_frame, alpha=0.2, figsize=(6, 6), diagonal='hist')
    scatter_matrix(latent_frame, alpha=0.2, figsize=(6, 6), diagonal='hist')

    plt.show()

if __name__ == '__main__':
    main()
