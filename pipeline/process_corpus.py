import db
from fyp_utilities import *
import glob, os

def assimilate_document(fp, book, conn):
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

def main():
    """ Main """
    conn = db.connect_to_db(host='localhost', dbname='hp_summary', user='postgres', password='password')

    dir_path = '../test_data/harry_potter_summaries/'
    glob_str = '*.txt'
    print('Begginging Process of assimilation')
    for fp in glob.glob(dir_path + glob_str):
        book = fp[len(dir_path): (len(fp) - len(glob_str) + 1) ]
        print('Starting to process: ' + book)
        assimilate_document(fp, book, conn)
        print(book + ' Processed')

if __name__ == '__main__':
    main()
