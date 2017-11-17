import numpy as np
from collections import OrderedDict

class Mat:
    
    def __init__(self, col_headings=[], row_headings=[]):
        """ Class Constructor """
        self.col_headings = OrderedDict([(key, idx) for idx, key in enumerate(list(set(col_headings)))])
        self.row_headings = OrderedDict([(key, idx) for idx, key in enumerate(list(set(row_headings)))])
        
        self.data = np.matlib.zeros((len(row_headings), len(col_headings)))
        

    def get(self, col, row):
        """ """
        col_idx = -1
        row_idx = -1
        
        if isinstance(col, str):
            col_idx = self.col_headings[col]
        else:
            col_idx = col
        
        if isinstance(row, str):
            row_idx = self.row_headings[row]
        else:
            row_idx = row
            
        return self.data[row_idx, col_idx]
        
    def set(self, col, row, val):
        """ """
        col_idx = -1
        row_idx = -1
        
        if isinstance(col, str):
            col_idx = self.col_headings[col]
        else:
            col_idx = col
        
        if isinstance(row, str):
            row_idx = self.row_headings[row]
        else:
            row_idx = row
            
        self.data [row_idx, col_idx] = val
    
    
    def get_col(col):
        """ """        
        col_idx = -1
        
        if isinstance(col, str):
            col_idx = self.col_headings[col]
        else:
            col_idx = col


    def get_row():
        """ """

        
m = Mat(['a', 'b', 'c'], ['1','2', '3'])
m.set('a','1',4)

print(m.data)
print(m.row_headings)
print(m.col_headings)

print(m.get('a','1'))