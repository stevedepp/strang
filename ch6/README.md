chapter 6

eigenvalues and eigenvectors

6.1 intro to eigen values

principles

1. eigenvector x lies along the same line as Ax

2. if Ax = &lambda;x  
A<sup>2</sup>x = &lambda;<sup>2</sup>x  
A<sup>-1</sup>x = &lambda;<sup>-1</sup>x  
( A + c I )x = ( &lambda; + c )x

the same x in each case LHS RHS

3. if Ax = &lambda;x  
(A - lamnda I)x = 0  
A - &lambda;I is singular and   
det (A - &lambda; I) = 0  
n eigenvalues

4. check &lambda;'s by  
det A = (&lambda;<sub>1</sub>)(&lambda;<sub>2</sub>) ... (&lambda;<sub>n</sub>) and diagonals sum a<sub>11</sub> + a<sub>22</sub> + ... + <sub>nn</sub> = sum of &lambda;'s.

5. projections have &lambda; = 1 and 0.  reflections have -1 and 1.  rotations have e<sup>i&theta;</sup> and e<sup>-i&theta;</sup>

so far  
Ax = b --> balance, equilibrium, steady state

next is about change.  time enters the picture: continuous time in differential equations ∂ u / ∂ t = A u or time steps in a difference equatoin. u<sub>k+1</sub> = Au<sub>k</sub> in equations that are not solved via elimination. 

key is avoiding matrix related complications.  the solution vector u(t) stays in same direction as fixed vector x.  and then solve only to find the number [lambda] changing with time that multiplies x.  a number is easier than a vector.  

eigenvectors x dont change direction when multiplied by A  

the model comes from matrix powers A, A<sup>2</sup>, A<sup>3</sup>, ... A<sup>100</sup> whose columns are very close to eigenvector (0.6, 0.4)

A<sup>100</sup> is found by using the eigenvalues of A not by multiplying A 100 times.  

eigenvalues &lambda; = 1 and &lambda; = 1/2 are a new way to see the heart of a matrix.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107458654-820ecc00-6b22-11eb-9b7f-4c634e77efcd.png">

eignvector understanding is needed for eignvalue comprehension. 

all vectors change direction when multiplied by A.  

eigenvectors do not change direction when multiplied by A.  the direction of eigenvector x is the same as Ax: multiply an eigenvector by A and the vector Ax is a number &lambda; times the original x

&lambda; is an eigenvalue of A.

&lambda; summarizes A's impact on x:  
&lambda; or eigenvalue indicates whether the vector x is   
stretched or shrunk  
reversed   
left unchanged  when multiplied by A:     
&lambda = 2 or 1/2 or -1 or +1 or zero.

all vectors are eigenvectors of the identity matrix I because A = I then has Ax = x.  
all eigenvalues of the identity matrix are &lambda; = 1  
which is odd because most 2 x 2 matrices have 2 eigenvector directions and 2 eignvectors. 

Ax = &lambda;Ix --> (A - &lambda;I) = 0

finding eigenvalues using det (A - I&lambda;) = 0

example:  
matrix A has 2 eigenvalues &lambda; = 1 and &lambda; = 0.5.  
to find these, look at:   
det (A - &lambda;I)  
set det (A - &lambda;I)  = 0 to find &lambda; that allows a non-zero null space. 
solves for the needed &lambda; via (&lambda; -1)(&lambda; - 0.5) = 0   
where A - &lambda;I becomes singular matrix because of zero determinant.  
the eigenvectors x<sub>1</sub> and x<sub>2</sub> are in the null space of matrices A - 1.0I and A = 0.5I

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107462257-b5088e00-6b29-11eb-87bc-e72f69d1622e.png">
