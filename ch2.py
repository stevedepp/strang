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


