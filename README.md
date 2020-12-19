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

the angle beteen the dot product elements has cos theta in radians

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

-1 <= u_v @ u_w <= 1  
v @ w > 0 --> acute heading toward 0  
v @ w < 0 --> obtuse heading toward 180  

cos 90 deg = 0
sin 90 deg = 1

deg = rad * 180 / math.pi
rad = deg * math.pi / 180

unit vector = (cos theta, sin theta)

unit_x = cos(rad) and unit_y = sin(rad)

since x and y vector components form a hypotenuse vector to unit circle:

cos(rad)<sup>2</sup> + sin(rad)<sup>2</sup> = 1

number of dimensions -> angles between vector pairs  
numbering C(n=d,r=2)= d!/(d-2)/2
   
the 'rule' cos theta = u_v @ u_w --> vecangle(v,w) = acos(u_v @ u_w)*180/pi
if v is the x-axis then this 'rule' is taking acos(w's x-axis component  
and not its y-axis component since vector u_v is (1,0)  
multiplies u_w = (w1,w2).  as u_v moves away from x-axis, the rule takes  
progressively less of the w vector's x component  
and starts to take the w vectors y-component.

u_v = (cos theta, sin theta)
u_w = (cos theta, sin theta)
at 90 degrees u_v @ u_w = cos(theta)<sup>2</sup> + sin(theta)<sup>2</sup> = 1

so if measure u_v vs x axis to get its angle
u_v angle is theta in cos(theta)

and if measure w_v vs x axis to get its angle
u_w angle is theta in cos(theta)

and angle between them is cos(theta_v) - cos(theta_w) = cos(theta_v-theta_w)?


schwartz inequality:  

cos theta <=1 
= u_v @ u_w <=1
= (v @ w) / (||v|| * ||w||) <= 1  

--> cos<sup>2</sup>theta + sin<sup>2</sup>theta <= 1

--> v @ w <= ||v|| * ||w||

triangle inequality:
||v + w|| <= ||v|| + ||w||
where ||v + w|| is length of the v+w parallelogram's diagonal
sum of ||v|| and ||w|| separates going to diagonal endpoint 
cannot be shorter than the diagonal itself.

can we also get ?
cos theta = cos<sup>2</sup>theta + sin<sup>2</sup>theta <= 1
what we do with this? all 3 sides need to be divided by cos theta

||v+w|| is the geometric mean i think






if one vector is multiple of the other
then the angle is zero or 180 degrees:
-  abs(cos theta) = 1 = abs(v @ w)/(||v||*||w||)  
-  ||v + w|| = ||v|| + ||w||


<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/102666823-d9617300-4155-11eb-937b-be0c6308f16a.png">

sum of angles for a n-d vector to all axes have sum of cos<sup>2</sup>theta = 1

law of cosines says how the hypotenuse between v and w
differs from pythagorean 
depending on whether 
angle theta is > or < 90
cos theta is < or > zero

||v-w||<sup>2</sup> = ||v||<sup>2</sup> - 2 * ||v|| * ||w|| * costheta(v, w) + ||w||<sup>2</sup> 

actually more generally
any hypotenuse v+w or v-w length can be gotten to via costheta

cos theta v,w = v • w / ||v|| * ||w||   
v • w = cos theta v,w * ||v|| * ||w||  

using these vector algebra rules
v • w = w • v  
u • (v + w) = u • v + u • w   
(c * v) • w = c * (v • w)  

||v|| = (v • v)<sup>0.5</sup>  
||v-w|| = (([v-w] • [v-w])<sup>0.5</sup>)  
||v+w|| = (([v+w] • [v+w])<sup>0.5</sup>)  

||v||<sup>2</sup> = ((v • v)<sup>0.5</sup>)<sup>2</sup>  
||v-w||<sup>2</sup> = (([v-w] • [v-w])<sup>0.5</sup>))<sup>2</sup>   
||v+w||<sup>2</sup> = (([v+w] • [v+w])<sup>0.5</sup>))<sup>2</sup>  

