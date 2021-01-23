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
    pivot_idx = 0
    print('r',r,'c',c)
    # these multiply from LHS so must be r
    L = np.eye(r)
    E = np.eye(r)
    U = matrix*1.
    pivot_list = []
    for j in range(c):
        print('col',j)
        pivot_nominees = U[pivot_idx:,j]
        print('piv nomineees', pivot_nominees)
        pivot_indexes = np.argwhere(pivot_nominees != 0)
        print('pivot indexes',pivot_indexes, 'len', len(pivot_indexes))
        pivot_exists = len(pivot_indexes)
        print('pivot exists',pivot_exists)
        if pivot_exists:
            print('here')
            print(range(pivot_idx,r))
            if pivot_indexes[0][0] != 0:
                print('next pivot index',pivot_idx+pivot_indexes[0][0])
                print('INSIDE2')
                next_pivot_row = pivot_idx+pivot_indexes[0][0]
                print('swap',U[pivot_idx])
                print('with',U[next_pivot_row])
                U[[pivot_idx, next_pivot_row]] = U[[next_pivot_row, pivot_idx]]
                P = np.eye(r)
                P[[pivot_idx, next_pivot_row]] = P[[next_pivot_row, pivot_idx]]
                E = P @ E
                print(U)
            pivot_list.append(U[pivot_idx,j])
            print('pivot list', pivot_list)
            for i in range(pivot_idx+1, r):
                print('i',i,'r',r)
                print('i',i)
                print('j',j)
                print('pivot', pivot_idx)
                print('i,j',U[i,j])
                print('pivot_idx,j',U[pivot_idx,j])
                print('U[i,j] is zero',U[i,j]==0)
                if U[i,j] !=0.0:
                    print('dividing')
                    l = U[i,j] / U[pivot_idx,j]
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
            pivot_idx += 1
        elif not pivot_exists:
            print('moving to next column')
    Dinv = np.zeros([r,r])
    D = np.zeros([r,r])
    for i in range(len(pivot_list)):
        Dinv[i,i] = 1/pivot_list[i]
        D[i,i] = pivot_list[i]
    U = Dinv @ U
    return E, L, D, U 

'''
the above errs on A = 
array([[ 1,  2,  1],
       [ 3,  6,  3],
       [ 4,  8, 10]])
the L matrix should have a zero in the 1,1 index
'''
