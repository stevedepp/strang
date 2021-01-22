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
    pivot = 0
    print('r',r,'c',c)
    # these multiply from LHS so must be r
    L = np.eye(r)
    E = np.eye(r)
    U = matrix*1.
    for j in range(c):
        print('col',j)
        pivot_nominees = U[pivot:,j]
        print('piv nomineees', pivot_nominees)
        pivot_indexes = np.argwhere(pivot_nominees != 0)
        print('pivot indexes',pivot_indexes, 'len', len(pivot_indexes))
        pivot_exists = len(pivot_indexes)
        print('pivot exists',pivot_exists)
        if pivot_exists:
            print('here')
            print(range(pivot,r))
            if pivot_indexes[0][0] != 0:
                print('next pivot index',pivot+pivot_indexes[0][0])
                print('INSIDE2')
                next_pivot_row = pivot+pivot_indexes[0][0]
                print('swap',U[pivot])
                print('with',U[next_pivot_row])
                U[[pivot, next_pivot_row]] = U[[next_pivot_row, pivot]]
                P = np.eye(r)
                P[[pivot, next_pivot_row]] = P[[next_pivot_row, pivot]]
                E = P @ E
                print(U)
            for i in range(pivot+1, r):
                print('i',i)
                print('j',j)
                print('i,j',U[i,j])
                print('j,j',U[j,j])
                print('dividing')
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
                print('end with\n', U)
            pivot += 1
        elif not pivot_exists:
            print('moving to next column')
    Dinv = np.diag(1/np.diag(U))
    D = np.diag(np.diag(U))
    U = Dinv @ U
    return E, L, D, U 
