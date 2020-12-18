#!/usr/bin/env python

# https://stackoverflow.com/questions/17428621/python-differentiating-between-row-and-column-vectors

"""
In [1]: import numpy as np
In [2]: import ch1
In [3]: a = ch1.row_vector_shape([1,2])
In [4]: b = ch1.col_vector_shape([1,2])
In [5]: c = ch1.row_vector_newaxis([1,2])
In [6]: d = ch1.col_vector_newaxis([1,2])
In [7]: e = ch1.row_vector_bracket([1,2])
In [8]: f = ch1.col_vector_bracket([1,2])
In [9]: np.shape(a), np.shape(b), np.shape(c), np.shape(d), np.shape(e), np.shap
   ...: e(f)
Out[9]: ((1, 2), (2, 1), (1, 2), (2, 1), (1, 2), (2, 1))
"""

import numpy as np
import math

def row_vector_shape(list):
    c = len(list)
    return np.array(list).reshape(1,c)

def row_vector_newaxis(list):
    return np.array(list)[np.newaxis,:]

def row_vector_bracket(list):
    return np.array([list])

def col_vector_shape(list):
    r = len(list)
    return np.array(list).reshape(r,1)

def col_vector_newaxis(list):
    return np.array(list)[:, np.newaxis]

def col_vector_bracket(list):
    return np.array([list]).T

def vector(list):
    return col_vector_shape(list)

def orthog(v,w):
    return (v.T @ w)[0][0] == 0

def length(v):
    return ((v.T @ v)**.5)[0][0]

def mu(v):
    return v / length(v)

def unit(v):
    return mu(v)

def deg(rad):
    return rad * 180 / math.pi

def rad(deg):
    return deg * math.pi / 180

def unit_x(deg):
    rads = rad(deg)
    return math.cos(rads)

def unit_y(deg):
    rads = rad(deg)
    return math.sin(rads)

# always 1
def pythag(deg):
    rads = rad(deg)
    return math.cos(rads)**2 + math.sin(rads)**2

def unit_deg(deg):
    rads = rad(deg)
    return np.array([[math.cos(rads)],[math.sin(rads)]])

def unit_rad(rad):
    return np.array([[math.cos(rad)],[math.sin(rad)]])

def combs(n,r):
    return math.factorial(n)/math.factorial(n-r)/math.factorial(r)

# page 1.15 dont use since only works with 2d vecs
# not sure what to do w it in 3d
def vecangle_0(v):
    return math.acos(mu(v)[0][0])*180/math.pi
def vecangle_1(v):
    return math.asin(mu(v)[1][0])*180/math.pi

def costheta(v, w):
    return (mu(v).T @ mu(w))[0][0]

# page1.16 v=[cos alpha, sin alpha].T w=[cos beta, sin beta]
# theta=beta-alpha
# dotprod = cos alpha*cos beta + sin alpha*sin beta
#         = cos theta = cos beta - alpha if vectors are unitary
# where cos is v1 and w1 and sin is v2 adn w2.  so ...
 
def costheta_unitaries(v,w):
    return mu(v)[0][0]*mu(w)[0][0] + mu(v)[1][0]*mu(w)[1][0]

def costheta_m(v, w):
    return (mu(v).T @ mu(w))[0][0]

def costheta_d(v, w):
    return ((v.T @ w) / (length(v) * length(w)))[0][0]

def vecangle(v, w):
    return math.acos(costheta(v, w)) * 180 / math.pi

def sintheta(v, w):
    return math.sin(vecangle(v, w) * math.pi / 180)[0][0]

def schwartz(v, w):
    print(f'{v} dot {w},\n ||{v}||*||{w}||')
    return abs(v.T @ w)[0][0], length(v)*length(w)

def triangle(v, w):
    return length(v + w), length(v) + length(w)
