#cython: lenguage_level = 3

cimport cython

cdef intercambia(A, int x, int y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp

cdef Particionar(A, int p, int r):
    x = A[r]
    cdef int i = p - 1
    cdef int j
    for j in range(p, r):
        if (A[j] <= x):
            i = i + 1
            intercambia (A, i, j)
    intercambia(A, i+1, r)
    return i + 1

cdef QuickSort(A, int p, int r):
    if (p < r):
        q = Particionar(A, p, r)
        #print (A[p:r])
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    return A

def ordenar(A):
    cdef int p,r,q
    p = 0
    r = len(A) - 1
    q = int((p + r) / 2)
    return QuickSort(A, p, r)