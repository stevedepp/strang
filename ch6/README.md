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
all eigenvalues of the identity matrix are &lambda; = 1  which means   
no stretching or shrinking   
all vectors are eigenvectors of identity matrix because all vectors are unchanged by the identity matrix   
which is the point of eigenvectors   
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

x<sub>1</sub> and x<sub>2</sub> are in the null space of the A - &lambda;I matrix, (the A - 1•I and A - 0.5•I matrices)

and Ax<sub>1</sub> = &lambda<sub>1<.sub>x<sub>1<.sub>  and Ax<sub>2</sub> = &lambda;<sub>2<.sub>x<sub>2<.sub>

If eigenvector is multiplied by A again, the same eigenvector is produced by the procedure for constructing eigenvalues and eigenvectors.  direction of x does not change as A is multiplied 100 times.  A<sup>100</sup>x = &lambda;<sup>100</sup>x inasmuch as A is still replacing &lambda; and x stays the same.  

When A is squared, the eigenvectors stay the same,  the eigenvalues are squared.  this pattern continues because the eigenvectors stay in their same directions, and never change. The eigenvectors of A<sup>100</sup> are teh same x<sub>1</sub> and x<sub>2</sub> as the eigenvalues become 1<sup>100</sup> = 1 and 0.5<sup>100</sup> = 0

&lambda;<sub>1</sub> and &lambda;<sub>2</sub> eigenvalues via det (A<sup>n</sup> - &lambda;<sup>n</sup>I) = 0 produce the same x<sub>1</sub> and x<sub>2</sub> eigenvectors via (A<sup>n</sup> - &lambda;<sup>n</sup>I)x = 0 for all n.

<img width="522" alt="image" src="https://user-images.githubusercontent.com/38410965/107570798-03fd0480-6bb8-11eb-841b-8f6f99c2c48f.png">

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

this determinant starts with either &lambda;<sup>n</sup> or -&lambda;<sup>n</sup> and this determinant is a polynomial of degree n.

2. find roots of the degree n polynomial det (A - &lambda;I) = 0 which can be solved by quadratic formula.  

the n roots are the eignvalues of A.  
the n roots of det (A - &lambda;I) = 0 make the matrix A - &lambda;I singular.

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

3. for each eigenvalue &lambda;<sub>1</sub> solve (A - &lambda;I) x = 0 to find the eigenvector x<sub>1</sub>.  

each eigenvector is in the null space of its individual matrix (A - &lambda;I)

thoughts that Strang has before the above procedures:


<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107583712-5561bf80-6bc9-11eb-987b-c95a7f59222c.png">

V1 = V2 = V3 = x<sub>1</sub> = Ax<sub>1</sub> = &lambda;x<sub>1</sub> all going the same direction  
V4 = V5 = V6 = x<sub>2</sub> = 2*Ax<sub>2</sub> = 2*&lambda;x<sub>1</sub>, but all going the same direction  

<img width="752" alt="image" src="https://user-images.githubusercontent.com/38410965/107585789-d40c2c00-6bcc-11eb-9ab8-e96305fdf277.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107586694-6e20a400-6bce-11eb-8332-0300dc006019.png">

square A to A<sup>2</sup> and &lambda; to &lambda;<sup>2</sup> and the directions do not change but the magnitude does. you can barely see that the brown line is shorter, but can see the numbers below.

<img width="752" alt="image" src="https://user-images.githubusercontent.com/38410965/107587259-5e558f80-6bcf-11eb-9e08-1e87832d1cd4.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107587178-42ea8480-6bcf-11eb-870f-eb798f50440d.png">


other vectors, not v_1 and v_2 derived from &lambda;s will change direction.  but these other vectors are combinations of the 2 eigenvectors [much in the same way all vectors are combinations of the axes i and j which coincidentally do not change either when acted upon by their A = I; so I am thinking that eigenvalues adjust A and create new eigenvectors as axes of this new space.]

the first column of A is a combination of x<sub>1</sub> and x<sub>2</sub>.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107587623-15eaa180-6bd0-11eb-8a76-004fc6ca7de1.png">

A * (8,2) = eigenvalues * ( weighting * eigenvectors = (8,2) )

so eigenvalues and eigenvectors can do the work of A.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107587969-c8226900-6bd0-11eb-9402-b1e481e49a9e.png">

makes it easier when using powers of matrices: A<sup>99</sup>(8,2) = (weight = 100%)&lambda;<sub>1</sub><sup>99</sup>x<sub>1</sub> + (weight = 20%)&lambda;<sub>2</sub><sup>99</sup>x<sub>2</sub> 

that last number is very small

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107588553-f48ab500-6bd1-11eb-9e5b-f76e61ccf293.png">

eigenvector is steady state that doesnt chnage because &lambda;<sub>1</sub> = 1

&lambda;<sub>2</sub> is a decaying mode that disappears.  the higher the powers of A the more the columns approach the steady state.

A is a Markov matrix whose largest eigenvalue is 1.  All columns of A<sup>k</sup> will approach its eigenvalue 1's eigenvector.   

for projection matrices, P, one can see when Px is parallel to x: the eigenvectors for &lambda; = 1 and &lambda; = 0 fill the column space and null space.  The column space doesnt change: Px = x because &lambda; = 1 and the null space goes to zero (Px = 0x).  

example: 
this projection matrix P has eigenvalues &lambda;<sub>1</sub> = 1 and &lambda;<sub>2</sub> = 0 and eigenvectors x<sub>1</sub> = (1,1) and x<sub>2</sub> = (1,-1).  Px<sub>1</sub> = x<sub>1</sub> = 1 and Px<sub>2</sub> = x<sub>2</sub> = 0: so :
Px = x for both vectors.    
the first eigenvalue is steady state and the second is null space.

this example illustrates Markov, singular and most important symmetric matrices' special &lambda;'s and x's.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107592590-661b3100-6bdb-11eb-92a2-d2b5b1cd2610.png">

1. Each Markov column's components add to 1.  
2. P is singular so &lambda; = 0 is an eigenvalue: the determinant of P is zero before &lambda; is subtracted.   
3. P is symmetric; so its eigenvalues (1,1) and (1,-1) are perpendicular. 

the only eigenvalues for a projection matrix are 0 and 1  
the eigenvectors for &lambda; = 0 where Px = 0x fill up the null space.  
the eigenvectors for &lambda; = 1 where Px = x fill up the column space.  

the null space is projected to zero.  the column space projects onto itself.  
the projection keeps the column space and destroys the null space.  

example:  
&lambda;<sub>1</sub> = 0  
&lambda;<sub>2</sub> = 1  
v = (1,-1) + (2,2) projects onto Pv = (0,0) + (2,2) = 0•(1,-1) + 1•(2,2) = &lambda;<sub>1</sub>x<sub>1</sub> + &lambda;<sub>2</sub> + x<sub>2</sub>


permutations have all | &lambda; | = 1   

example:
R = permutation = reflection matrix



<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107595465-b3e76780-6be2-11eb-91be-d219585ee141.png">

the first eigenvector is unaffected by R and &lambda;: x = Rx = &lambda;x  

the second eigenvector has its signs reversed by R and &lambda;

evidence that a matrix with no negative entries can have a negative eigenvalue 

the eigenvectors for R are same as for P because 2 • projection P - I = R

when a matrix is shifted by I, each lambda is shifted by 1 since det I = 1.  since det A needs to be zero, the shift in eigenvalues is 1 --> no change in eigenvalues. 

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107595873-f78ea100-6be3-11eb-8757-78bc6515fc5e.png">

the 2 vectors for P and R stay the same whether on their own, multiplied by P or R or multiplied by their eigenvalues. 

P vectors

<img width="752" alt="image" src="https://user-images.githubusercontent.com/38410965/107596404-9f589e80-6be5-11eb-966b-41dee131a475.png">

R vectors

<img width="752" alt="image" src="https://user-images.githubusercontent.com/38410965/107596434-b5665f00-6be5-11eb-909f-3781ed264f82.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107596452-c1eab780-6be5-11eb-80a6-e5e4dbef9f8d.png">


A - &lambda;I solves for &lambda eigenvalues when singular, i.e. when det A - &lambdaI; = 0   
then both rows of matrix A - &lambdaI; are multiples of vector (a,b)  
then eigenvector x is ANY multiple of vector (b,-a)  
repeating example, but previously  the 2nd eigenvector x<sub>2</sub> paired with &lambda;<sub>2</sub> = 5 was (1,2) and now (2,4).  there is a line of eigenvectors = any non-zero multiple of x.  MatLab provides the unit vector equivalent.   

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107666704-cb633680-6c5c-11eb-9448-5b691d9c9546.png">

some 2x2 matrices have only one line of eigenvectors when 2 eigenvectors are equal.  A = I has equal eigenvalues and infinite eigenvectors.  Without a full set of eigenvectors there is no basis and cannot write every v as a combination of eigenvectors which translates into saying 'we cannot diagonalize the matrix without independent eigenvectors'

eigenvalues change from A to U in elimination:  
add a row of A to another row or exchange rows, eigenvalues &lambda; change.  
diagonal of U contains its eigenvalues = the pivots  

&lambda;<sub>1</sub> + &lambda;<sub>2</sub> = sum(A.diagonal()) = trace A  
(A.diagonal() doesnt contain pivots but still can be used)

&lambda;<sub>1</sub> * &lambda;<sub>2</sub> = det A 
= pivot<sub>1</sub>*pivot<sub>2</sub>  
(of course pivots can only be found in U)

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107671362-c48af280-6c61-11eb-93a1-f92e0f8557fb.png">

example: the trace =  sum of diagonals is 3 and determinant is 2 for all 3 matrices

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107674371-e8036c80-6c64-11eb-93fa-1060941b802c.png">

the eigenvalues of a triangular matrix lie along its diagonal because in determinants the non-zero part multiplies the zero part. 

imaginary eigenvalues 

https://docs.python.org/3/library/cmath.html

eigenvalues may be complex numbers 

example  
R = Q = rotation = 
[
[0, -1],
[1, 0]
]

has no real eigenvectors.  

R = Q's eigenvalues are &lambda;<sub>1</sub> = i and &lambda;<sub>2</sub> = -i  
then since i = √-1, 

&lambda;<sub>1</sub> + &lambda;<sub>2</sub> = i + -i = 0 = trace A

&lambda;<sub>1</sub> • &lambda;<sub>2</sub> = i • -i = -1 = det A

after rotation by &lambda; • I, no real vector Qx stays in same direction as x (except zero vector which is useless).  there cannot be an real eigenvector but there can be an imaginary eigenvector.

If Q is rotation through 90 degrees, then Q<sup>2</sup> is rotation through 180 which fits :

Q<sup>2</sup>x = -Ix = &lambda;<sup>2</sup>x = i<sup>2</sup> = -1<sup>2</sup> = -1x  

&lambda;s come from (Q - &lambda;I) = 0 as usual --> &lambda;<sup>2</sup> + 1 = 0 whose roots are i and -i.

complex eigenvectors x<sub>1</sub> = -i • (1,i) and x<sub>2</sub> = i • (i, 1) keep direction as rotated.  
[somehow the math doesnt work at the end of this example i • [1,i] = [-i,1] but it does something else]  

important: real matrices can easily have complex eigenvalues and eigenvectors

<img width="672" alt="image" src="https://user-images.githubusercontent.com/38410965/107687592-a975ae00-6c74-11eb-8425-03a278b95489.png">

these two eigenvalues i and -i illustrate:
1. Q is an orthogonal matrix; so the absolute value of each &lambda; is | &lambda; | = 1   
2. Q is skew symmetric matrix; so, each &lamnda; is pure imaginary (i.e. not complex)

symmetric matrix S<sup>T</sup> = S is compared with real number.

a skew symmetric matrix A<sup>T</sup> = -A is compared with an imaginary number.  

an orthogonal matrix Q<sup>T</sup>Q = I corresponds to a complex number with | &lambda; | = 1

for eigenvalues of S, A, Q those are more than analogies.  They are facts.  

the eigenvectors for all these special matrices S, A, Q are perpendicular.  
(i,1) and (1,i) are perpendicular.  


Eigenvealues of AB and A+B

eigenvalue of A times eigenvalue of B usually doesnt equal eigenvalue of AB   

ABx = A&lambda;<sub>B</sub>x   
ABx = &lambda;<sub>A</sub>Bx  
doesnt mean 
ABx = &lambda;<sub>A</sub>&lambda;<sub>B</sub>x

unless x is an eigenvector for A and B when this proof would be correct.  

for same reason, eigenvalues of A + B are not generally the sum of the eigenvalues of A and B


if x is an eigenvector for A and B then can multiply eigenvalues.  

the test for shared eigenvectors is important in quantum mechanics.  

A and B share the same n independent eigenvectors if and only if 

AB = BA  

Heisenbergs uncertainty principle: 

Review
1. Ax = &lambda;x says eigenvectors keep the same directoin when multiplied by A  
2. Ax = &lambda;x says det (A - &lambda;I) = 0 which determines n eigenvalues &lambda;s.  
3. eigenvalues of A<sup>2</sup> and A<sup>-1</sup> are &lambda;<sup>2</sup> and &lambda;<sup>-1</sup> with the same eigenvectors.  
4. the sum of the &lambda;s equals the sum down main diagonal of A = trace.    
5. the product of the &lambda;s equals the determinant of A = product of the pivots of A which are likely NOT the digaonals of A since A is not reduced to U.  
6. projections P, reflections R, 90 degree rotations Q have special eigenvalues 1, 0, -1, i, -i.  Singular matrices have &lambda; = 0.  Triangular matrices have &lambda;s on their diagonals.  
7. special properties of a matrix lead to special eigenvalues and eigenvectors. this is major theme of this chaper. 


