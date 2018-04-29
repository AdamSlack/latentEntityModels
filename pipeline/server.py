from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from os import curdir, sep
from urllib.parse import unquote
import json

## DB Utilities
import db as db
import latent_entity as latent_entity

## POS tagging
import viterbi as viterbi
from nltk.corpus import brown
from nltk.tag.mapping import _UNIVERSAL_TAGS as tagset


class Server(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

        ## Viterbi Setup

        #self.tagged_sents = brown.tagged_sents(tagset='universal')
        #self.tagged_words = brown.tagged_words(tagset='universal')
        #self.pos_states = tagset
        #self.pos_starts = viterbi.calc_start_state_probs(self.tagged_sents, self.pos_states)
        #self.pos_trans = viterbi.calc_trans_probs(self.tagged_sents, self.pos_states)


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
        terms =[{'term' : t[0], 'strength' : t[1]} for t in res]
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

    def request_closest_ten_entities(self, latent_entity):
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        res = db.request_closest_ten_entities(conn, latent_entity)
        res = [{'distance' : row[0], 'entity' : row[1], 'book' : row[2]} for row in res]
        conn.close()
        return res

    def calculate_latent_entities(self, n_entities):
        return latent_entity.calculate_latent_entities('books', n_entities)

    def fetch_book_enitity_topics(self, book_title, entity):
        """ selects all topics for a given book and entity """
        print('Selecting topic distributions for: ', book_title, '---', entity)
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        res = db.select_entity_topic_model(conn, book_title, entity)
        entity_topics = [{
            'entity': row[0],
            'book': row[1],
            'topicID': row[2],
            'strength':row[3]
        } for row in res]
        print(entity_topics)
        return entity_topics

    def fetch_book_titles(self):
        """ """
        conn = db.connect_to_db(host='localhost', dbname='books', user='postgres', password='password')
        return [title[0] for title in db.select_book_titles(conn)]

    def process_GET(self, url):
        """ parse an incoming url """
        clean_url = url.lower().strip('/').replace('api/','')
        split_url = clean_url.split('?')
        components = split_url[0].split('/')
        print('URL:', components)
        if len(split_url) > 1:
            query_components = [c.split('=') for c in split_url[1].split('&')]
            query = {c[0] : c[1] for c in query_components}
            print('QUERY:', query)
        comp_len = len(components)
        
        if comp_len == 1 and components[0] == 'latent_entities':
            print('Latent Entity Request Recieved.')
            print('Number of Entities:', query['number'])
            if 'number' not in query:
                self.send_response(400)
                return
            kmeans, _ = self.calculate_latent_entities(int(query['number']))
            json_obj = json.dumps({'latent_entities': [[p for p in c] for c in kmeans.cluster_centers_]})
            self.send_response(200)
            return json_obj

        if comp_len == 2 and components[0] == 'latent_entities' and components[1] == 'closest':
            print('Fetching closest 10 Entities.')
            # latent_entities/closest?1=0&2=0&3=0
            print(query)
            num_topics = len(query)
            strengths = []
            for i in range(0, num_topics):
                if 'topic_'+str(i) not in query:
                    self.send_response(400)
                    return json.dumps({'INVALID_TOPICS': query})
                strengths.append(query['topic_'+str(i)])
            entity_topic_models = self.request_closest_ten_entities(strengths)
            json_obj = json.dumps({
                'latent_entity' : strengths,
                'query' : query,
                'closest': entity_topic_models
            })
            self.send_response(200)
            return json_obj

        if comp_len == 1 and components[0] == 'topics':
            res = self.fetch_topic_ids()
            json_obj = json.dumps({'topic_ids': res}, indent=2)
            self.send_response(200)
            return json_obj

        if comp_len == 2 and components[0] == 'topics':
            topic_id = components[1]
            res = self.fetch_topic_terms(topic_id)
            json_obj = json.dumps({'topic_id': topic_id, 'terms': res})
            self.send_response(200)
            return json_obj
        
        if comp_len == 3 and components[0] == 'topics':
            book_title = unquote(components[1])
            entity_name = unquote(components[2])
            res = self.fetch_book_enitity_topics(book_title, entity_name)
            json_obj = json.dumps({'topics' : res}, indent=2)
            self.send_response(200)
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
        print(curdir + sep + 'dist' + sep + fp)
        return open(curdir + sep + 'dist'+ sep + fp, 'rb')
        
    def do_GET(self):
        url = urlparse(self.path)
        urlstr = url.geturl()
        print(urlstr)
        if len(urlstr.strip('/').split('/')) == 1:
            output = self.process_root(urlstr)
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
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
    port = 8000
    url = 'localhost'
    server = HTTPServer((url, port), Server)
    print('Starting server at ' + url + ':' + str(port))
    server.serve_forever()

    ## Initialise corpus
    tagged_sents = brown.tagged_sents(tagset='universal')
    tagged_words = brown.tagged_words(tagset='universal')

    ## fetch tagset    
    pos_states = tagset

    ## calc HMM state probabilities.
    pos_starts = viterbi.calc_start_state_probs(tagged_sents, pos_states)
    pos_trans = viterbi.calc_trans_probs(tagged_sents, pos_states)
    # pos_emit = calc_emit_probs(tagged_words, pos_states, pos_obs)
    # tags = viterbi(pos_obs, pos_states, pos_starts, pos_trans, pos_emit)




if __name__ == '__main__':
    main()
