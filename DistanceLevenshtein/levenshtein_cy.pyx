#cython: lenguage_level = 3

cimport cython
import numpy as np

@cython.locals(pmatrix = 'int[:,:]')

def levenshtein(str seq1, str seq2):  
    cdef int size_x = len(seq1) + 1
    cdef int size_y = len(seq2) + 1
    cdef int x,y,edit
    
    #draw matrix
    pmatrix=np.zeros ((size_x, size_y), np.int32)
    for x in range(size_x):
        pmatrix [x, 0] = x
    for y in range(size_y):
        pmatrix [0, y] = y
    #compute
    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:     
                edit = 0                    
            else:
                edit = 1
            x1y = pmatrix[x-1,y] + 1         #[x - 1, y]
            x1y1 = pmatrix[x-1,y-1] + edit   #[x - 1, y - 1]
            xy1 = pmatrix[x,y-1] + 1         #[x, y - 1]
            pmatrix [x,y] = min(x1y, x1y1, xy1)
    return (pmatrix[size_x - 1, size_y - 1])