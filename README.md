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
(1,0,0), (0,1,0) and (0,0,1) are in R<sup>3</sup>


if u, v, w, x and 0 are column vectors  
then [u v w] is a matrix

if u, v, w are in R<sub>3</sub> then [u v w] is square  

if [u v w] x = 0 where again 0 represents a vector  
then [u v w] lie on a plane  
because some combination x of the 3 vectors the zero vector
or said another way
some combination of 2 vectors equals the 3rd vector
which means you can add 2 of the vectors 
and return to zero on the 3rd vector 
which is only possible in a plane.
or better said its because you only have 2 vectors 
and the 3rd is just a combination of the first 3.


the slope of the vector (v1, v2) is v2/v1  
the slope of the vector (v1, v2, v3) in any of the three 2d spaces is  
- v2/v1
- v3/v2
- v3/v1
