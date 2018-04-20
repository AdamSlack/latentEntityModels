import db as db
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from pandas.plotting import radviz
import seaborn as sns

def db_conn():
    return db.connect_to_db(host='localhost', dbname='hp_full', user='postgres', password='password')


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
        if e['strength'] > 0:
            key = e['entity']+'-$-'+e['book']
            entities[key]['entity'] = e['entity']
            entities[key]['book'] = e['book']
            entities[key]['topic_ids'].append(e['topic'])
            entities[key]['topic_str'].append(e['strength'])

    es = [e for e in entities.keys()]
    for e in es:
        t_num = len(entities[e]['topic_str'])
        if entities[e]['topic_str'] == [0]*t_num:
            del entities[e]

    entity_topics = [entities[e]['topic_str'] for e in entities]

    data = np.array(entity_topics)

    kmeans = KMeans(n_clusters = 5).fit(data)

    #first make some fake data with same layout as yours
    entity_frame = pd.DataFrame(data, columns=['Topic ' + str(t) for t in range(0,10)])
    latent_frame = pd.DataFrame(kmeans.cluster_centers_, columns=['Topic ' + str(t) for t in range(0,10)])

    res = kmeans.predict(data)
    entity_frame['class'] = res
    entity_frame = entity_frame[(entity_frame.T != 0).any()]
    entity_frame.to_csv('../results/hp_full_latent_entity_classification.csv')

    for idx, e in enumerate(entities):
        entities[e]['closest_cluster'] = res[idx]
        for idx, l in enumerate(kmeans.cluster_centers_):
            entities[e]['latent_' + str(idx)] = np.linalg.norm(l - entities[e]['topic_str'])
            out_line = [entities[e]['entity'],'latent_' , str(idx), entities[e]['latent_' + str(idx)], entities[e]['book'] , '\n']
            values = ','.join(str(v) for v in out_line)
            fp = '../results/hp_full_entity_' + str(idx) + '.csv'
            with open(fp, 'a+') as f:
                f.write(' '.join(values))
    


    #now plot using pandas 
    # e_plts = scatter_matrix(entity_frame, alpha=0.2, figsize=(6, 6), diagonal='kde')
    # l_plts = scatter_matrix(latent_frame, alpha=0.9, figsize=(6, 6), diagonal='kde')
    
    # set_x_ticks(e_plts, 45, offset_x=0.3, offset_y=-0.5)
    # set_y_ticks(e_plts, 0, offset_x=-1.0,  offset_y=0.3)

    # set_x_ticks(l_plts, 45,  offset_x=0.3, offset_y=-0.5)
    # set_y_ticks(l_plts, 0, offset_x=-1.0, offset_y=0.3)


    # sns.set(style='white')
    # g = sns.PairGrid(
    #     entity_frame,
    #     hue='class' )
    # g = g.map_diag(plt.hist, histtype="step", linewidth=3)
    # g = g.map_offdiag(plt.scatter)


    plt.show()


def set_x_ticks(sm, rotation = 45, offset_x = 0, offset_y = 0):
    #Change label rotation
    [s.xaxis.label.set_rotation(rotation) for s in sm.reshape(-1)]
    [s.get_xaxis().set_label_coords(offset_x, offset_y) for s in sm.reshape(-1)]
    
def set_y_ticks(sm, rotation = 0, offset_x=0, offset_y = 0):
    [s.yaxis.label.set_rotation(rotation) for s in sm.reshape(-1)]
    [s.get_yaxis().set_label_coords(offset_x, offset_y) for s in sm.reshape(-1)]
if __name__ == '__main__':
    main()
