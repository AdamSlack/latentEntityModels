import db as db
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from pandas.plotting import radviz
import seaborn as sns

from itertools import combinations

def db_conn(db_name):
    return db.connect_to_db(host='localhost', dbname=db_name, user='postgres', password='password')


def request_book_entity_topics(db_conn):
    """ request a list of entities from the database """
    res = db.select_book_entity_topics(db_conn)

    return [{
        'entity' : row[0],
        'book' : row[1],
        'topic' : row[2],
        'strength' : row[3]
    } for row in res]
    

#def calculate_latent_entities(le_prefix, db_name, n_le):
def calculate_latent_entities(db_name, n_le):
    print('Latent Entities Connecting to DB')
    conn = db_conn(db_name)
    print('Requesting Entity Topics')
    entity_topics = request_book_entity_topics(conn)

    print('Processing Entity Topics')
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
    entity_names = [entities[e]['entity'] for e in entities]
    entity_books = [entities[e]['book'] for e in entities]


    data = np.array(entity_topics)
    print('Calculating K Means')
    kmeans = KMeans(n_clusters = n_le).fit(data)

    #first make some fake data with same layout as yours
    entity_frame = pd.DataFrame(data, columns=['Topic ' + str(t) for t in range(0,10)])
    latent_frame = pd.DataFrame(kmeans.cluster_centers_, columns=['Topic ' + str(t) for t in range(0,10)])

    res = kmeans.predict(data)
    entity_frame['Class'] = res
    entity_frame['Entity'] = entity_names
    entity_frame['Book'] = entity_books

    entity_frame = entity_frame[(entity_frame.T != 0).any()]
    #entity_frame.to_csv('../results/test/'+le_prefix+'_classification.csv')

    for idx, e in enumerate(entities):
        entities[e]['closest_cluster'] = res[idx]
        for idx, l in enumerate(kmeans.cluster_centers_):
            entities[e]['latent_' + str(idx)] = np.linalg.norm(l - entities[e]['topic_str'])
            out_line = [entities[e]['entity'],'latent_' , str(idx), entities[e]['latent_' + str(idx)], entities[e]['book'] , '\n']
            values = ','.join(str(v) for v in out_line)
            # fp = '../results/test/'+le_prefix + str(idx) + '.csv'
            # with open(fp, 'a+') as f:
            #     f.write(' '.join(values))
    
    return kmeans, entity_frame
    

def main():
    """ Main Process Flow """
    
    summ_kmeans, summ_entities = calculate_latent_entities('summary_entities_50', 'hp_summary', n_le=50)
    full_kmeans, full_entities = calculate_latent_entities('full_entities_50', 'hp_full', n_le=50)

    
    summ_clusters = {
        str(idx) : [] for idx, c in enumerate(summ_kmeans.cluster_centers_)
    }

    full_clusters = {        
        str(idx) : [] for idx, c in enumerate(full_kmeans.cluster_centers_)
    }
    print(full_clusters)
    print(summ_clusters)

    print('mapping summary entities')
    for row in summ_entities.itertuples():
        summ_clusters[str(row.Class)].append((row.Entity, row.Book))

    print('mapping full entities')
    for row in full_entities.itertuples():
        full_clusters[str(row.Class)].append((row.Entity, row.Book))

    print('performing cluster combinations')
    for key in summ_clusters.keys():
        summ_clusters[key] = list(set(combinations(summ_clusters[key], 2)))
        full_clusters[key] = list(set(combinations(full_clusters[key], 2)))

    TP = 0
    FP = 0
    total = 0

    print('Calculating Consistency.')
    for cluster in summ_clusters:
        print('Consistency for Cluster' , str(cluster))
        total += len(summ_clusters[cluster])
        idx = 0
        for pair in summ_clusters[cluster]:
            idx += 1
            print(str(idx),' Out Of ', str(len(summ_clusters[cluster])))
            for other_cluster in full_clusters:
                if pair in full_clusters[other_cluster]:
                    TP += 1
                    print(str(cluster), '-', str(idx), 'Found in', other_cluster)
                    break

    FP = total - TP
    print(TP)
    print(FP)
    print(Total)
    print(str((TP-FP)/total))



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
