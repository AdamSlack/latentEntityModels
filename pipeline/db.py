import psycopg2 as pg

#
#
#
#
def connect_to_db(host, dbname, user, password):
    """ Connect to Database returning pyscopg2 cursor object """
    try:
        conn_string = "host='" + host + "' dbname='" + dbname + "' user='" + user + "' password='" + password +"'"
        
        print('Connecting to DB: ' + conn_string)
        db = pg.connect(conn_string)

        print('Connected to DB.')
        return db
    except:
        print('Unable to connect to DB')

#
#
#
#
def insert_book_entity_term(db, book_title, entity, term, strength):
    """ Insert an entity-term for a book into the DB. """
    cursor = db.cursor()
    try:
        cursor.execute("""
            insert into books (book_title, entity, term, strength)
            values (%s, %s, %s, %s)
        """, (book_title, entity, term, strength))
    except:
        db.rollback()
        return False

    cursor.close()
    db.commit()
    return True

def insert_entity_topic_model(db,book,entity,topics):
    """ insert a entity topic value for a topic of an entity in a book. """
    for t in topics.keys():
        cursor = db.cursor()
        print ('Inserting into book_entity_topics:', book, entity, t, topics[t])
        try:
            cursor.execute(
                """
                    insert into book_entity_topics (book_title, entity, topic_id, strength)
                    values(%s, %s, %s, %s)
                """,
                (book, entity, t, topics[t])
            )
        except:
            db.rollback()
            return False
            cursor.close()
        cursor.close()
        db.commit()
    return True
#
#
#
#
def select_book_titles(db):
    """ Create a cursor pointing to all book titles"""
    cursor = db.cursor()
    cursor.execute("""select book_title from book_titles""")
    return cursor

#
#
#
#
def select_topic_ids(db):
    """ Create a cursor returining all topic ids"""
    cursor = db.cursor()
    cursor.execute("""select distinct book_title from books""")
    return cursor

def select_book_entity_topics(db):
    cursor = db.cursor()
    cursor.execute("""select * from book_entity_topics""")
    return cursor

#
#
#
#
def insert_book_topic_distribution(db, book, distributions):
    """ insert topic distribution scores for a given book into the database """
    cursor = db.cursor()
    for idx, topic in enumerate(distributions) :
        try:
            cursor.execute("""
                insert into book_topics (book_title, topic_id, score)
                values (%s, %s, %s)
            """, (book, idx, distributions[topic]))
        except:
            db.rollback()
            return False

    cursor.close()
    db.commit()
    return True

#
#
#
#
def select_book_topics(db, book_title):
    """ Create a cursor pointing to all book topics for a given book"""
    cursor = db.cursor()
    cursor.execute("""select * from book_topics where lower(book_title) = lower(%s)""", (book_title,))
    return cursor

#
#
#
#
def select_topic_terms(db, topic_id):
    """ """
    cursor = db.cursor()
    cursor.execute("""select term, strength from topics where topic_id = %s""", (int(topic_id),))
    return cursor

#
#
#
#
def select_topic_ids(db):
    """ """
    cursor = db.cursor()
    cursor.execute("""select distinct topic_id from topics""")
    return cursor

#
#
#
#
def insert_topic_term(db, topic_id, term, strength):
    """ inserts the topic id and associated term """
    cursor = db.cursor()
    try:
        cursor.execute("""
            insert into topics (topic_id, term, strength)
            values (%s, %s, %s)
        """, (topic_id, term, strength))
    except:
        db.rollback()
        return False

    cursor.close()
    db.commit()
    return True

#
#
#
#
def select_book_entities(db, book_title, full=False):
    """ create a cursor for all entities in the DB for a specified book """
    print('Selecting entities for book: ' + book_title)
    cursor = db.cursor()
    if full:
        cursor.execute("""select * from books where lower(book_title) = lower(%s)""", (book_title,))
    else:
        cursor.execute("""select distinct entity from books where lower(book_title) = lower(%s)""", (book_title,))
    return cursor

#
#
#
#
def select_book_entity_terms(db, book_title, entity):
    """ create a cursor for all terms in the DB for specified entity and book """
    cursor = db.cursor()

    cursor.execute('select term, strength from books where lower(book_title) = lower(%s) and lower(entity) = lower(%s) order by strength using >', (book_title, entity))
    return cursor
