import psycopg2 as pg

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

def insert_book_entity_term(db, book_title, entity, term, strength):
    """ Insert an entity-term for a book into the DB. """
    cursor = db.cursor()
    try:
        cursor.execute("""
            insert into books (book_title, entity, term, strength)
            values (%s, %s, %s %s)
        """, (book_title, entity, term, strength))
    except:
        db.rollback()
        return False

    cursor.close()
    db.commit()
    return True

def select_book_entities(db, book_title, full=False):
    """ create a cursor for all entities in the DB for a specified book """
    cursor = db.cursor()
    if full:
        cursor.execute('select * from books where book_title = %s', book_title)
    else:
        cursor.execute('select entity from books where book_title = %s', book_title)
    return cursor

def select_book_entity_terms(db, book_title, entity):
    """ create a cursor for all terms in the DB for specified entity and book """
    cursor = db.cursor()

    cursor.execute('select entity from books where book_title = %s', book_title)
    return cursor
