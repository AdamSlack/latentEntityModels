import db as db

def db_conn():
    return db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')


def request_entities(book_title):
    """ request a list of entities from the database """
    print('Requesting Entity for the book:', book_title)    
    res = db.select_book_entities(db_conn(),book_title)
    return [row[0] for row in res]
    

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
    """ Main Process Flow """
    topic_ids = request_topic_ids()
    topic_terms = [request_topic_terms(t_id) for t_id in topic_ids]
    
    book_titles = request_book_titles()
    entities = [request_entities(title) for title in book_titles]

if __name__ == '__main__':
    main()