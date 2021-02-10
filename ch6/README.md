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

factoring the quadratic into &lambda; -1 and &lambda; -1/2 gives eigenvalues that transform A into singular, symptomized by zero determinant.  

x<sub>1</sub> and x<sub>2</sub> are in the null space of the A - &lamnda;I matrix, (the A - 1•I and A - 0.5•I matrices)

eigenvalues &lambda; and eigenvectors x are found by geometry, determinants and linear algebra.  

to understand:  

start with Ax = &lambda;x and move &lambda;x to LHS and set = 0:  

(A - &lambda;I)x = 0

eigenvectors make up the null space of A - &lambda;I

then with each eigenvalue &lambda; find an eigenvector by solving

(A - &lambda;I)x = 0

but need eigenvalues first because before we can find x: (A - &lambda;I)x = 0 has a non-zero solution, we must first find (A - &lambda;I) matrix that is not invertible: the determinant of A - &lambda;I must be zero, and it is in this equation that eigenvalues are found. 

finding eigenvalues:

&lambda; is an eigenvalue of A if and only if A - = &lambda;I matrix is singular

equation for eigenvalues: 

det (A - &lambda;I) = 0           <-- formular (3)

the "characteristic polynomial" det (A - &lambda;I) involves only &lambda; and not x.  when A is an n x n matrix, the equation (3) has degree n.  then, A has n eigenvalues (where repeats are possible).  

each &lambda; leads to x:

finding eigenvectors:

for each eigenvalue lambda, solve (A - &lambda;I)x = 0 or Ax = &lambda;x to find an eigenvector x.

if A is already singular then 0 will already be one of its eigenvalues: Ax = 0x has solution already [found in the x null space of A]; those solutions are the eigenvectors for the eigenvalue &lambda; = 0.  (A - &lambda;I) = is the way to find all &lambda;'s and x's: always subtract &lambda;I from A.

example: 

A is already singular as the columns and rows are not independent and thus it has a zero determinant already.

subtract &lambda;I from A's diagonal elements and take the determinant.

factor the determinant in to (0 - &lambda;)(5- &lambda;) = &lambda;(&lambda;-5)

solve for eigenvalues 0 and 5 that make the determinant = 0, make A - &lambda;I singular

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107555075-bcb94880-6ba4-11eb-8b01-045d99002bf0.png">

solve (A - &lambda;I )x = 0 vector for each &lambda;<sub>1</sub> = 0 producing x<sub>1</sub> vector = (2,-1) and &lambda;<sub>2</sub> = 5 producing x<sub>2<sub> vector = (1,2), confirming that for both (A - &lambda;I)x = 0 and that those 2 vectors are each in the null space of of their respective matrices: x<sub>1</sub> = (2,-1) in null space of A_lambda_1 and x<sub>1</sub> = (1,2) in the null space of A_lambda_2.  dimensions are conserved: n = n-r + r

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107558099-651cdc00-6ba8-11eb-93b9-4edef2a8517d.png">

there is nothing special about &lambda; = 0.  if A is singular, the eigenvector for &lambda; = 0 fills the null space of Ax = 0x = 0.  if A is invertible, zero is not an eigenvalue.  

this process shifts A by a multiple of I to make it singular.

process:
1. compute A - &lambda;I determinant. 

this determinant starts with either &lambda;<sup>n</sup> or -&lambda;<sup>n</sup> and this determinant is a polynomial of degree n: can be solved by quadratic formula

![\begin{align*}
A &=\begin{bmatrix}
w&x\\
y&z
\end{bmatrix}\\
\\
0 &=det\begin{bmatrix}
w - \lambda I&x\\
y&z-\lambda I
\end{bmatrix}\\
\\
&=\lambda^2 - (w + z)\lambda + wz - xy\\
\\
&= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \\
\\
&= \frac{(w+z) \pm \sqrt{(w+z)^2 - 4*1*(wz-xy)}}{(2*1)} \\
\\
a &= 1\\
\\
b & = -(w+z)\\
\\
c &= (wz - xy)\\
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%26%3D%5Cbegin%7Bbmatrix%7D%0Aw%26x%5C%5C%0Ay%26z%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A0+%26%3Ddet%5Cbegin%7Bbmatrix%7D%0Aw+-+%5Clambda+I%26x%5C%5C%0Ay%26z-%5Clambda+I%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%26%3D%5Clambda%5E2+-+%28w+%2B+z%29%5Clambda+%2B+wz+-+xy%5C%5C%0A%5C%5C%0A%26%3D+%5Cfrac%7B-b+%5Cpm+%5Csqrt%7Bb%5E2+-+4ac%7D%7D%7B2a%7D+%5C%5C%0A%5C%5C%0A%26%3D+%5Cfrac%7B%28w%2Bz%29+%5Cpm+%5Csqrt%7B%28w%2Bz%29%5E2+-+4%2A1%2A%28wz-xy%29%7D%7D%7B%282%2A1%29%7D+%5C%5C%0A%5C%5C%0Aa+%26%3D+1%5C%5C%0A%5C%5C%0Ab+%26+%3D+-%28w%2Bz%29%5C%5C%0A%5C%5C%0Ac+%26%3D+%28wz+-+xy%29%5C%5C%0A%5Cend%7Balign%2A%7D%0A)
