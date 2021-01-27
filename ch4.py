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
