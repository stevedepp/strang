import numpy as np
import sympy as sp

def projection(b, a):
    A = sp.Matrix(a)
    b = sp.Matrix(b)
    At = A.T
    AtA = At @ A
    AtAinv = AtA.inv()
    xhat = AtAinv @ At @ b
    p = A @ xhat
    e = b - p
    P = A @ AtAinv @ At
    print("A, b, At, AtA, AtAinv, xhat, p, e, P")
    return A, b, At, AtA, AtAinv, xhat, p, e, P


def ls_doc(A, xhat, b, p):
    '''documents least squares; assumes projection outputs'''
    C = xhat[0]
    D = xhat[1]
    a1 = A[:,0]
    a2 = A[:,1]
    At = A.T
    AtA = At @ A
    e = b - p
    print('a1, C, a2, D, p, b')
    for i in range(len(b)):
        print(a1[i],C,'+',a2[i],D,'=',p[i],'!=',b[i], 'by',e[i])
    print('normal equation: AtA', AtA, 'times xhat', xhat, '= Atb', At @ b)
    return a1, C, a2, D, p, b
