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

from math import pi, cos, sin, acos, asin

def deg2rad(degrees):
    return pi*degrees/180

def rad2deg(radians):
    return 180*radians/pi

def length_xy(x, y):
    return (x**2 + y**2)**.5

def length(v):
    return ((v.T @ v)**.5)[0]

def make_unit(v):
    return v / length(v)

def degrees_shift_xy(x, y, degrees):
    radians = deg2rad(degrees)
    new_x = cos(radians) * x - sin(radians) * y
    new_y = sin(radians) * x + cos(radians) * y
    return new_x, new_y

def degrees_shift(x_or_X, degrees):
    radians = deg2rad(degrees)
    Q = sp.Matrix([[cos(radians), -sin(radians)],[sin(radians), cos(radians)]])
    return Q @ x_or_X

def v2angle(v):
    v_unit = make_unit(v)
    x_unit = sp.Matrix([1,0])
    cos_theta = (v_unit.T @ x_unit)[0]
    radians = acos(cos_theta)
    degrees = rad2deg(radians)
    return degrees

def angle2v(degrees):
    radians = deg2rad(degrees)
    return sp.Matrix([cos(radians), sin(radians)])
