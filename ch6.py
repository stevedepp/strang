# https://stackoverflow.com/questions/42281966/how-to-plot-vectors-in-python-using-matplotlib

import numpy as np
from sympy import *
import matplotlib.pyplot as plt


def plotvec(vectors):
    '''takes a list of vectors as lists'''
    vectors = [list(map(float, vectors[i])) for i in range(len(vectors))]
    M = np.vstack(vectors)
    rows,cols = M.T.shape
    #Get absolute maxes for axis ranges to center origin
    #This is optional
    maxes = 1.1*np.amax(abs(M), axis = 0)
    for i,l in enumerate(range(0,cols)):
        xs = [0,M[i,0]]
        ys = [0,M[i,1]]
        plt.plot(xs,ys)

    plt.plot(0,0,'ok') #<-- plot a black point at the origin
    #plt.axis('equal')  #<-- set the axes to the same scale
    plt.xlim([-maxes[0],maxes[0]]) #<-- set the x axis limits
    plt.ylim([-maxes[1],maxes[1]]) #<-- set the y axis limits
    plt.legend(['V'+str(i+1) for i in range(cols)]) #<-- give a legend
    plt.grid(b=True, which='major') #<-- plot grid lines
    plt.show()


def plotvec2(vectors):

    '''takes a list of vectors as lists'''
    M = np.vstack(vectors)
    rows,cols = M.T.shape

    #Get absolute maxes for axis ranges to center origin
    #This is optional
    maxes = 1.1*np.amax(abs(M), axis = 0)
    colors = ['b','r','k']

    for i,l in enumerate(range(0,cols)):
        plt.axes().arrow(0,0,M[i,0],M[i,1],head_width=0.05,head_length=0.1,color = colors[i])

    plt.plot(0,0,'ok') #<-- plot a black point at the origin
    plt.axis('equal')  #<-- set the axes to the same scale
    plt.xlim([-maxes[0],maxes[0]]) #<-- set the x axis limits
    plt.ylim([-maxes[1],maxes[1]]) #<-- set the y axis limits
    plt.grid(b=True, which='major') #<-- plot grid lines
    plt.show()

def quadratic(a, b, c):
    '''( -b  +/- squareroot (b**2 - 4ac) ) / 2a when a != 0'''
    if a == 0:
        return 0, 0, 'a is zero; solution undefined'
    return (-b+(b**2-4*a*c)**.5)/2*a,(-b-(b**2-4*a*c)**.5)/2*a, f'a is not zero; b**2-4ac = {b**2} minus {4*(a*c)}'

import numpy as np
import matplotlib.pyplot as plt

def rand_polar():
    np.random.seed(19680801)
    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    print(type(r), type(theta))
    area = 200 * r**2
    colors = theta
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.show()


def rand_polar_unit():
    np.random.seed(19680801)
    N = 150
    r = np.array(N * [1])
    theta = 2 * np.pi * np.random.rand(N)
    area = 200 * r**2
    colors = theta
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.show()

def perfect_polar_unit():
    np.random.seed(19680801)
    N = 33
    r = np.array(N * [1])
    theta = np.array([i*2*np.pi/32 for i in range(33)])
    area = 200 * r**2
    colors = theta
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.show()

def eulers_spiral(show=False):
    np.random.seed(19680801)
    N = 32
    theta = np.array([i*2*np.pi/N for i in range(N+1)])
    x = np.cos(theta)
    y = -np.sin(theta)
    U_n = [Matrix([x[i], y[i]]) for i in range(len(x))]
    area = 200 * 1**2
    colors = theta
    fig = plt.figure()
    ax = fig.add_subplot(111)
    c = ax.scatter(x, y, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.show()
    if show:
        return U_n

def eulers_spiral_backward(show=False):
    np.random.seed(19680801)
    N = 32
    theta = np.array([i*2*np.pi/N for i in range(N+1)])
    delta_t = (np.pi * 2) / N
    A_backward = Matrix([[1, -delta_t],[delta_t, 1]])
    A_backward_inv = A_backward.inv()
    U_0 = Matrix([1, 0])
    U_n = []
    U_n.append(U_0)
    x = []; y = []; x.append(U_0[0]); y.append(U_0[1])
    for i in range(N):
        U_next = A_backward_inv * U_n[-1]
        U_n.append(U_next)
        x.append(U_next[0])
        y.append(U_next[1])
    area = 200 * 1**2
    colors = theta
    fig = plt.figure()
    ax = fig.add_subplot(111)
    c = ax.scatter(x, y, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.show()
    if show:
        return U_n

def eulers_spiral_forward(show=False):
    np.random.seed(19680801)
    N = 32
    theta = np.array([i*2*np.pi/N for i in range(N+1)])   
    delta_t = (np.pi * 2) / N
    A_forward = Matrix([[1, delta_t],[-delta_t, 1]])
    U_0 = Matrix([1, 0])
    U_n = []
    U_n.append(U_0)
    x = []; y = []; x.append(U_0[0]); y.append(U_0[1])
    for i in range(N):
        U_next = A_forward * U_n[-1]
        U_n.append(U_next)
        x.append(U_next[0])
        y.append(U_next[1])
    area = 200 * 1**2
    colors = theta
    fig = plt.figure()
    ax = fig.add_subplot(111)
    c = ax.scatter(x, y, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.show()
    if show:
        return U_n
