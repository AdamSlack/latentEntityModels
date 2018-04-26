##
##
##  Calculate Entity Topic distributions using LDA and GETM.
##  Involves going through each entity, and calculating its topic distributions
##  when influenced by the GETM.
##
##  Read All Topics & Terms.
##  For Each Entity,
##      Get its GETM Terms and Strength of associations.
##      For each Topic
##
import db as db

def db_conn():
    return db.connect_to_db(host='localhost', dbname='hp_full', user='postgres', password='password')


def request_entities(book_title):
    """ request a list of entities from the database """
    print('Requesting Entity for the book:', book_title)    
    res = db.select_book_entities(db_conn(),book_title, True)
    return [{
        'book': row[1],
        'entity': row[2],
        'term' : row[3],
        'strength' : row[4]
    } for row in res]
    

def request_entity_terms(book_title, entity):
    """ request a list terms for an entity"""
    print('Requesting Entity terms. Book:', book_title, 'Entity:', entity)
    res = db.select_book_entity_terms(db_conn(),book_title, entity)
    return [{'term': row[0], 'strength': row[1] }for row in res]


def request_topic_ids():
    """ request a list of topic ids from the database """
    print('Requesting Topic IDs')
    res = db.select_topic_ids(db_conn())
    return [t[0] for t in res]


def request_topic_terms(topic_id):
    """request a list of topic terms from the database """ 
    print('Requesting Topic', str(topic_id), 'IDs')
    res = db.select_topic_terms(db_conn(),topic_id)
    return [{'term' : t[0], 'strength' : t[1]} for t in res]


def request_book_titles():
    """ request book titles from the database """
    res = db.select_book_titles(db_conn())
    return [title[0] for title in res]

def main():
    the_db = db_conn()
    """ Main Process Flow """
    topic_ids = request_topic_ids()
    topic_terms = [request_topic_terms(t_id) for t_id in topic_ids]

    topics = dict(dict())
    for idx, topic in enumerate(topic_terms):
        topics[idx] = {}
        for term in topic:
            topics[idx][term['term']] = term['strength']
    
    book_titles = request_book_titles()
    entities = [request_entities(title) for title in book_titles]
    entity_terms = []

    entity_map = {}
    for idx, t in enumerate(book_titles):
        for e in entities[idx]:
            entity_map[t + '---' + e['entity']] = {
                'entity' : e['entity'],
                'book' : e['book'],
                'terms' : {},
                'term_array' : []
            }
        
    for idx, t in enumerate(book_titles):
        for e in entities[idx]:
            entity_map[t+'---'+ e['entity']]['terms'][e['term']] = e['strength']
            entity_map[t+'---'+ e['entity']]['term_array'].append({
                'term':e['term'],
                'strength':e['strength']})

    for e in entity_map:
        entity_terms.append(entity_map[e])

    # for idx, t in enumerate(book_titles):
    #     book_entities = []
    #     for e in entities[idx]:
    #         terms = request_entity_terms(book_titles[idx], e)
    #         term_map = {}
    #         for term in terms:
    #             term_map[term['term']] = term['strength']

    #         entity_terms.append({
    #             'entity': e,
    #             'book' : book_titles[idx],
    #             'terms' : term_map,
    #             'term_array' : terms
    #         })

    for e in entity_terms:
        e['topics'] = {}
        
        total = 0
        new_total = 0
        
        for idx, topic in enumerate(topics):
            e['topics'][idx] = 0
            for term in e['term_array']:
                e_term = term['term']
                e_str = term['strength']
                if e_term in topics[idx]:
                    e['topics'][idx] += e_str*topics[idx][e_term]
            total += e['topics'][idx]
        
        for t in e['topics'].keys():
            if total > 0: 
                e['topics'][t] = (e['topics'][t]/total)*100
            new_total += e['topics'][t]

        db.insert_entity_topic_model(the_db,e['book'], e['entity'], e['topics'])
    
if __name__ == '__main__':
    main()
