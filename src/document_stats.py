import glob
from os import path
import fyp_utilities as fyp
from nltk.tokenize import word_tokenize

def read_file(fp):
      with open(fp, encoding='utf-8') as f:
        return f.read()

def read_data_samples(fp, glob_str):
  """ Reads all txt files at a specified location and returns array of data. """
  if(path.isdir(fp)):
    fps = glob.glob(fp + glob_str)
    return list(map(lambda x: read_file(x), fps)), fps

def main():
    docs = read_data_samples('../test_data/harry_potter_summaries/', '*.txt')
    text = ''

    lengths = [len(word_tokenize(book)) for book in docs[0]]
    print(lengths)
    print(sum(lengths))
    

if __name__ == '__main__':
    main()
