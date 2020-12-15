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
