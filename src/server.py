import xmlschema
from pprint import pprint
import copy
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import db as db


class Server(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def fetch_book_entity_terms(self, book_title, entity):
        """ """
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        res = db.select_book_entity_terms(db=conn, book_title=book_title, entity=entity)
        res = [{'term': row[0], 'strength': row[1] }for row in res]
        conn.close()
        return res


    def fetch_book_entities(self, book_title, full=False):
        """ """
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        res = db.select_book_entities(db=conn, book_title=book_title, full=full)
        if full:
            res = [{'entity' : row[2], 'term' : row[3], 'strength' : row[4]} for row in res]
        else:
            res = [row[0] for row in res]
        conn.close()
        return res

    def process_GET(self, url):
        """ parse an incoming url """

        components = url.lower().strip('/').split('/')
        comp_len = len(components)
        if comp_len == 0 or comp_len > 4:
            self.send_response(400)
            return 'INVALID URL RECIEVED'
        
        if components[0] != 'books':
            self.send_response(400)
            return 'INVALID URL RECIEVED'    

        if comp_len == 2 :
            book = components[1]
            print(book)
            res = self.fetch_book_entities(book_title=book)
            json_obj = json.dumps({'book' : book, 'entities' : res}, indent = 2)
            self.send_response(200)
            return  json_obj

        if components[2] != 'entities' :
            self.send_response(400)
            return 'INVALID URL RECIEVED'

        if comp_len == 3:
            book = components[1]
            print(book)
            res = self.fetch_book_entities(book_title=book, full = True)
            json_obj = json.dumps({'book' : book, 'entities' : res}, indent = 2)
            self.send_response(200)
            return  json_obj

        if comp_len == 4 :
            book = components[1]
            entity = components[3]
            res = self.fetch_book_entity_terms(book_title=book, entity = entity)
            json_obj = json.dumps({'book' : book, 'entity' : entity, 'terms' : res}, indent = 2)
            self.send_response(200)
            return json_obj

        
        self.send_response(200)
        json_obj = json.loads('{"entity": "Oooh-Weee, Don\'t quite know what you\'re wanting there!"}')
        return  json.dumps(json_obj, indent=2)


    def process_POST():
        """ processess URL from POST Request """


    def do_GET(self):
        

        url = urlparse(self.path)
        output = self.process_GET(url.geturl())
        
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('content-type','application/json')
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
    server = HTTPServer(('localhost', 8081), Server)
    print('Starting server at http://localhost:8081')
    server.serve_forever()


if __name__ == '__main__':
    main()