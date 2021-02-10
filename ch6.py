# https://stackoverflow.com/questions/42281966/how-to-plot-vectors-in-python-using-matplotlib

import numpy as np
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

