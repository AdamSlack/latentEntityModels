import glob
from os import path
import fyp_utilities as fyp
from nltk.tokenize import word_tokenize

def read_file(fp):
      with open(fp, encoding='utf-8') as f:
        lines = [l.split(',') for l in f.read().replace(' ', '').split('\n')]
        lines = [l for l in lines if len(l) > 1]
        return sorted(lines, key=lambda x: x[3])[0:5]

def read_data_samples(fp, glob_str):
  """ Reads all txt files at a specified location and returns array of data. """
  if(path.isdir(fp)):
    fps = glob.glob(fp + glob_str)
    return list(map(lambda x: read_file(x), fps)), fps

def main():
    docs = read_data_samples('../results/test/', 'full_*.csv')
    filenames = docs[1]
    orderings = docs[0]

    with open('../results/table.tex', 'a+') as f:
        for idx, top in enumerate(orderings):
            print(top)
            f.write("""
            \\resizebox{0.33\\textwidth}{!}{%
                \\begin{tabular}{c | c | c }
                \\multicolumn{3}{c}{Latent Entity """ +  str(idx) + """}\\\\
                Entity    & Distance & Origins\\\\
                \\hline
                """
            )
            for res in top:
                line = res[0] + '\t&\t' + res[3][0:4] + '\t&\t' + res[4] + ' \\\\' 
                f.write(line+'\n')
            f.write('\\end{tabular}}')

if __name__ == '__main__':
    main()
