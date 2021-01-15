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


def eliminator(matrix):
    d = matrix.shape
    r, c = d[0], d[1]
    L = np.zeros(matrix.shape)
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
            print('1st pivot index',pivot_indexes[0][0])
            print('INSIDE2')
            next_pivot_row = pivot_indexes[0][0]
            print('swap',U[j])
            print('with',U[next_pivot_row])
            U[[j, next_pivot_row]] = U[[next_pivot_row, j]]
            print(U)
        for i in range(j + 1, r):
            print('i',i)
            print('j',j)
            print('i,j',U[i,j])
            print('j,j',U[j,j])
            l = U[i,j] / U[j,j]
            print('l',l)
            L[i,j] = l
            print(U[j])
            print(U[j]*l)
            print(U[i])
            U[i] = U[i] - U[j]*l
            print(U)
    return L, U
