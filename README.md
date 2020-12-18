making row and col vectors
https://stackoverflow.com/questions/17428621/python-differentiating-between-row-and-column-vectors

ch1 notes
[mostly what cannot be captured in ch1.py]

(x, y, z) and [x y z].T represent column vectors.  [x y z] is a row vector. 

numpy represents these as:

colum vector

    np.array([[1],[2],[3]])
    array([[x],
           [y],
           [z]])

row vector = column vector.T

   np.array([[1,2,3]])
   array([[1, 2, 3]])

(1,0,0) and (2,0,0) are on a line
(1,0,0) and (0,1,0) are on a plane
(1,0,0), (0,1,0) and (0,0,1) are in R^3


