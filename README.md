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

graphically:

2 vectors v and w  
- v + w is the vector from zero along diagonal between v amd w
to the 4th corner of the parallelogram  

- v - w is the vector from zero along diagonal between v and -w

- 1*v + 0*w is the vector v and 0*v + 1*w is the vector w  

- .5*v + .5*w is the vector from zero   
to the point mid way on the line between v and w

- .25*v + .75*w is the vector from zero  
to the point on the line between v and w  
3/4 of the way from v to w

- .25*v + .25*w is the vector  
extending from zero 1/2 of the distance to 0.5*v + 0.5*w;  
the endpoint of the vector lies on the line between 0.5*v and 0.5*w

- 0.75*v + 0.75*w is 50% longer than and on same line as 0.5*v + 0.5*w

- in R<sup>3</sup> space, (1/3)*u + (1/3)*v + (1/3)*w 
lies in the middle of a triangle 
formed by the points of the tips of u, v, w.

v @ w = 0 --> perpendicular

length = ||v|| = (v @ v)**.5

mu = unit vector = v / ||v|| = u such that ||u|| = 1

angle between v and w has cos theta = v @ w / (||v||*||w||)  
or if u_v and u_w are unit vectors: u_v=v/||v|| and u_w=w/||w||  
then angle between v and w has cos theta = u_v @ u_w

acos(u_v @ u_w) = radians angle between v and w  
acos(u_v @ u_w) * 180 / math.pi = degrees angle between v and w

absolute value of u_v @ u_w = |v @ w| <= 1

if u_v @ u_w = 1  
then u_v and u_w are the same unit vector  
and u and v are vectors on the same line.
ie unit vectors with 
zero degrees angle between them

if u_v @ u_w = -1   
then u_v and u_w are opposite unit vectors  
ie unit vectors with  
180 degrees angle between them  
180/math.pi radians angle between them  
and u and v are vectors are on the same line,  
just pointing away from each other  

if u_v @ u_w = 0 or v @ w = 0  
then 90 degrees angle between them = u_v @ u_w * 180 / math.pi

eg  

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/102623971-561e2e00-4111-11eb-90fa-96f384f88a4f.png">
