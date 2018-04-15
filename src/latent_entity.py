import db as db

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
    print(entity_topics)
    entities = {}
    #for e in entity_topics:
        

if __name__ == '__main__':
    main()
