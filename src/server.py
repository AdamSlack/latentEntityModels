import xmlschema
from pprint import pprint
import copy
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
from os import curdir, sep
import db as db
from urllib.parse import unquote


class Server(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def fetch_book_entity_terms(self, book_title, entity):
        """ """
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        res = db.select_book_entity_terms(db=conn, book_title=book_title, entity=entity)
        res = [{'term': row[0], 'strength': row[1] }for row in res]
        print(book_title)
        conn.close()
        return res
    
    def fetch_book_topics(self, book_title):
        """ """
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        res = db.select_book_topics(db=conn, book_title=book_title)
        res = [{'topic_id': row[2], 'score': row[3] } for row in res]
        print(book_title)
        conn.close()
        return res

    def fetch_topic_terms(self, topic_id):
        """ """
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        res = db.select_topic_terms(conn, topic_id)
        terms =[t[0] for t in res]
        conn.close()
        return terms

    def fetch_topic_ids(self):
        """ """
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        res = db.select_topic_ids(conn)
        topic_ids = [t[0] for t in res]
        conn.close()
        return topic_ids

    def fetch_book_entities(self, book_title, full=False):
        """ """
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        res = db.select_book_entities(db=conn, book_title=book_title, full=full)
        print(book_title)
        if full:
            res = [{'entity' : row[2], 'term' : row[3], 'strength' : row[4]} for row in res]
        else:
            res = [row[0] for row in res]
        conn.close()
        return res


    def fetch_book_titles(self):
        """ """
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        return [title[0] for title in db.select_book_titles(conn)]

    def process_GET(self, url):
        """ parse an incoming url """
            
        components = url.lower().strip('/').strip('api/').split('/')
        print(components)
        comp_len = len(components)
        if comp_len == 0 or comp_len > 4:
            self.send_response(400)
            return 'INVALID URL RECIEVED'
        
        if comp_len == 1 and components[0] == 'topics':
            res = self.fetch_topic_ids()
            json_obj = json.dumps({'topic_ids': res}, indent=2)
            self.send_response(200)
            return json_obj

        if comp_len == 2 and components[0] == 'topics':
            topic_id = components[1]
            res = self.fetch_topic_terms(topic_id)
            json_obj = json.dumps({'topic_id': topic_id, 'terms': res})
            return json_obj

        if comp_len == 1 and components[0] == 'books':
            res = self.fetch_book_titles()
            json_obj = json.dumps({'books' : res}, indent = 2)
            self.send_response(200)
            return json_obj

        if comp_len == 2 and components[0] == 'books':
            book = components[1]
            print(book)
            print(unquote(book))
            entities = self.fetch_book_entities(book_title=unquote(book))
            topics = self.fetch_book_topics(book_title=unquote(book))

            json_obj = json.dumps({'book' : book, 'entities' : entities, 'topics': topics}, indent = 2)
            self.send_response(200)
            return  json_obj

        if comp_len == 3 and components[2] == 'entities' and components[0] == 'books':
            book = components[1]
            print(book)
            res = self.fetch_book_entities(book_title=unquote(book), full = True)
            json_obj = json.dumps({'book' : book, 'entities' : res}, indent = 2)
            self.send_response(200)
            return  json_obj

        if comp_len == 3 and components[2] == 'topics' and components[0] == 'books':
            book = components[1]
            print(book)
            res = self.fetch_book_topics(book_title=unquote(book))
            json_obj = json.dumps({'book' : book, 'topics' : res}, indent = 2)
            self.send_response(200)
            return  json_obj

        if comp_len == 4 and components[2] == 'entities' :
            book = components[1]
            entity = components[3]
            res = self.fetch_book_entity_terms(book_title=unquote(book), entity = entity)
            json_obj = json.dumps({'book' : book, 'entity' : entity, 'terms' : res}, indent = 2)
            self.send_response(200)
            return json_obj

        
        self.send_response(400)
        json_obj = json.loads('{"Invalid URL": "Oooh-Weee, Don\'t quite know what you\'re wanting there!"}')
        return  json.dumps(json_obj, indent=2)


    def process_POST():
        """ processess URL from POST Request """

    def process_root(self, url):
        """ process requests for files at root. """
        file = url.strip('/').split('/')
        print(file)
        if len(file[0]) == 0:
            fp = 'index.html'
        else:
            fp = file[0]
        print(fp)
        print(curdir + sep + fp)
        return open(curdir + sep + fp, 'rb')
        
    def do_GET(self):
        url = urlparse(self.path)
        urlstr = url.geturl()
        print(urlstr)
        if len(urlstr.strip('/').split('/')) == 1:
            output = self.process_root(urlstr)
            self.send_header('content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(output.read())
            output.close()
        else:
            output = self.process_GET(urlstr)
            self.send_header('content-type','application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(output + '\n', "utf8"))

        return

    def do_POST(self):
        self.send_response(200)

        self.send_header('Content-type','text/html')
        self.end_headers()

        url = urlparse(self.path)
        print('POST URL:' + url.geturl())

        self.wfile.write(bytes('POST REQUEST RECV' + '\n', "utf8"))
        return

def main():
    """ main """
    server = HTTPServer(('localhost', 12345), Server)
    print('Starting server at http://localhost:12345')
    server.serve_forever()


if __name__ == '__main__':
    main()
