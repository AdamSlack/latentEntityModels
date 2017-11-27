import db
from fyp_utilities import *

def main():
    """ Main """
    conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
    book = 'alice_in_wonderland'
    #fp = '../books/Hitchhiker\'s Guide to the Galaxy - Douglas Adams.txt'
    #fp = '../books/Dirk Gently\'s Holistic Detective Agency - Douglas Adams.txt'
    #fp = '../books/Harry Potter and the Sorcerer\'s Stone - J. K. Rowling.txt'
    fp = '../test_data/' + book + '.txt'
    
    document = read_file(fp)

    entities = extract_entities(document)
    word_map = map_word_occurences(word_tokenize(document))

    getd = time_action(calcuate_GETD, map_entity_idx(entities), word_map)
    tf_getd = getd_tf_idf(getd)

    rows = getd.row_headings
    cols = getd.col_headings

    print('insert into data base')
    for e in cols:
        print('inserting data for: ' + e)
        for t in rows:
            strength=getd.get(col=e, row=t)
            if strength > 0:
                if not db.insert_book_entity_term(book_title=book, entity=e, term=t, strength=getd.get(col=e, row=t), db=conn):
                    print('FAILED TO INSERT: ' + e + ' : ' + t)

if __name__ == '__main__':
    main()