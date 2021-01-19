import numpy as np
import math

def exch(n):
    m = np.zeros((n, n))
    r = range(n-1, -1, -1)
    for i in r:
        m[-i+n-1,i]=1
    return m

def rotate180(n):
    return np.diag([-1]*n)

def permute(listy):
    listy = [i-1 for i in listy]
    n = len(listy)
    matrix = np.zeros((n,n))
    m = 0
    for i in listy:
        matrix[m, i] = 1
        m += 1
    return matrix       

def r2m(n):
    return np.arange(n).reshape(int(n**.5),int(n**.5))

def rotate(d):
    r = d * math.pi / 180
    x = math.cos(r)
    y = math.sin(r)
    return np.array([[x, -y], [y, x]])

def multiplier(i, j):
    return i/j

# for swapping rows
# https://stackoverflow.com/questions/54069863/swap-two-rows-in-a-numpy-array-in-python

'''
this could be done by finding the mulitpliers l,
inserting each into an identity matrix to make E_ij,
mulitiplying E_ij with the subject matrix in a loop,
one loop iteration for each multiplier l, 
and that would be cleaner code than the following,
but i think the following has fewer multiplications,
since we only multiply the subject pivot row's n items by a multiplier,
ie n multiplications and then subtract.
the cleaner code would have nxn multiplications for each multipler l.
'''

def eliminator(matrix):
    d = matrix.shape
    r, c = d[0], d[1]
    L = np.eye(r)
    E = np.eye(r)
    U = matrix*1.
    for j in range(min(c, r - 1)):
        pivot_col = U[j:,j]
        print('piv col', pivot_col)
        pivot_indexes = np.argwhere(pivot_col != 0)
        print('len piv indexes',len(pivot_indexes))
        if len(pivot_indexes) == 0:
            print('inside1')
            return L, U
        elif pivot_indexes[0][0] != 0:
            print('1st pivot index',j+pivot_indexes[0][0])
            print('INSIDE2')
            next_pivot_row = j+pivot_indexes[0][0]
            print('swap',U[j])
            print('with',U[next_pivot_row])
            U[[j, next_pivot_row]] = U[[next_pivot_row, j]]
            P = np.eye(r)
            P[[j, next_pivot_row]] = P[[next_pivot_row, j]]
            E = P @ E
            print(U)
        for i in range(j + 1, r):
            print('i',i)
            print('j',j)
            print('i,j',U[i,j])
            print('j,j',U[j,j])
            l = U[i,j] / U[j,j]
            print('l',l)
            L[i,j] = l
            E_temp = np.eye(r)
            E_temp[i,j] = -l
            E = E_temp @ E
            print(U[j])
            print(U[j]*l)
            print(U[i])
            U[i] = U[i] - U[j]*l
            print(U)
    return E, L, U, 
