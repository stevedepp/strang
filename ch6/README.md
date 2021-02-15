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
(A - &lambda; I)x = 0  
A - &lambda;I is singular and   
det (A - &lambda; I) = 0  
n eigenvalues

4. check &lambda;'s by  
det A = (&lambda;<sub>1</sub>)(&lambda;<sub>2</sub>) ... (&lambda;<sub>n</sub>) and diagonals sum a<sub>11</sub> + a<sub>22</sub> + ... + <sub>nn</sub> = sum of &lambda;'s.

5. projections have &lambda; = 1 and 0.  reflections have -1 and 1.  rotations have e<sup>i&theta;</sup> and e<sup>-i&theta;</sup>

so far  
Ax = b --> balance, equilibrium, steady state

next is about change.  time enters the picture: continuous time in differential equations ∂ u / ∂ t = A u or time steps in a difference equatoin. u<sub>k+1</sub> = Au<sub>k</sub> in equations that are not solved via elimination. 

key is avoiding matrix related complications.  the solution vector u(t) stays in same direction as fixed vector x.  and then solve only to find the number [&lambda;] changing with time that multiplies x.  a number is easier than a vector.  

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
&lambda; = 2 or 1/2 or -1 or +1 or zero.

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

and Ax<sub>1</sub> = &lambda;</sub>1</sub>x<sub>1</sub>  and Ax<sub>2</sub> = &lambda;<sub>2</sub>x<sub>2</sub>

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

for each eigenvalue &lambda;, solve (A - &lambda;I)x = 0 or Ax = &lambda;x to find an eigenvector x.

if A is already singular then 0 will already be one of its eigenvalues: Ax = 0x has solution already [found in the x null space of A]; those solutions are the eigenvectors for the eigenvalue &lambda; = 0.  (A - &lambda;I) = is the way to find all &lambda;'s and x's: always subtract &lambda;I from A.

example: 

A is already singular as the columns and rows are not independent and thus it has a zero determinant already.

subtract &lambda;I from A's diagonal elements and take the determinant.

factor the determinant in to (0 - &lambda;)(5- &lambda;) = &lambda;(&lambda;-5)

solve for eigenvalues 0 and 5 that make the determinant = 0, make A - &lambda;I singular

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107555075-bcb94880-6ba4-11eb-8b01-045d99002bf0.png">

solve (A - &lambda;I )x = 0 vector for each &lambda;<sub>1</sub> = 0 producing x<sub>1</sub> vector = (2,-1) and  &lambda;<sub>2</sub> = 5 producing x<sub>2</sub> vector = (1,2), confirming that for both (A - &lambda;I)x = 0 and that those 2 vectors are each in the null space of of their respective matrices: x<sub>1</sub> = (2,-1) in null space of A_lambda_1 and x<sub>1</sub> = (1,2) in the null space of A_lambda_2.  dimensions are conserved: n = n-r + r

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
with:&\\
\\
a &= 1\\
\\
b & = -(w+z)\\
\\
c &= (wz - xy)\\
\\
\lambda &= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \\
\\
\\
\lambda_1,\lambda_2&= \frac{(w+z) \pm \sqrt{(w+z)^2 - 4*1*(wz-xy)}}{(2*1)} \\
\\
\\
\\
\lambda_1 + \lambda_2 & = (w+z) = trace_A\\
\\
\lambda_1 * \lambda_2 & = wz-xy = det A = pivot_1 * pivot_2
\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%26%3D%5Cbegin%7Bbmatrix%7D%0Aw%26x%5C%5C%0Ay%26z%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A0+%26%3Ddet%5Cbegin%7Bbmatrix%7D%0Aw+-+%5Clambda+I%26x%5C%5C%0Ay%26z-%5Clambda+I%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%26%3D%5Clambda%5E2+-+%28w+%2B+z%29%5Clambda+%2B+wz+-+xy%5C%5C%0A%5C%5C%0Awith%3A%26%5C%5C%0A%5C%5C%0Aa+%26%3D+1%5C%5C%0A%5C%5C%0Ab+%26+%3D+-%28w%2Bz%29%5C%5C%0A%5C%5C%0Ac+%26%3D+%28wz+-+xy%29%5C%5C%0A%5C%5C%0A%5Clambda+%26%3D+%5Cfrac%7B-b+%5Cpm+%5Csqrt%7Bb%5E2+-+4ac%7D%7D%7B2a%7D+%5C%5C%0A%5C%5C%0A%5C%5C%0A%5Clambda_1%2C%5Clambda_2%26%3D+%5Cfrac%7B%28w%2Bz%29+%5Cpm+%5Csqrt%7B%28w%2Bz%29%5E2+-+4%2A1%2A%28wz-xy%29%7D%7D%7B%282%2A1%29%7D+%5C%5C%0A%5C%5C%0A%5C%5C%0A%5C%5C%0A%5Clambda_1+%2B+%5Clambda_2+%26+%3D+%28w%2Bz%29+%3D+trace_A%5C%5C%0A%5C%5C%0A%5Clambda_1+%2A+%5Clambda_2+%26+%3D+wz-xy+%3D+det+A+%3D+pivot_1+%2A+pivot_2%0A%5C%5C%0A%5Cend%7Balign%2A%7D)

here:   
&lambda;<sup>2</sup> - (w + z)&lambda; + (wz - xy)    
&lambda;<sup>2</sup> - (Trace<sub>A</sub> = w + z = sum of &lambda;s)&lambda; + ( det A = wz - xy = &lambda;<sub>1</sub>*&lambda;<sub>2</sub>)

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107811934-f4f38f00-6d3c-11eb-9918-b512ca6bf45d.png">


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

when a matrix is shifted by I, each &lambda; is shifted by 1 since det I = 1.  since det A needs to be zero, the shift in eigenvalues is 1 --> no change in eigenvalues. 

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107595873-f78ea100-6be3-11eb-8757-78bc6515fc5e.png">

the 2 vectors for P and R stay the same whether on their own, multiplied by P or R or multiplied by their eigenvalues. 

P vectors

<img width="752" alt="image" src="https://user-images.githubusercontent.com/38410965/107596404-9f589e80-6be5-11eb-966b-41dee131a475.png">

R vectors

<img width="752" alt="image" src="https://user-images.githubusercontent.com/38410965/107596434-b5665f00-6be5-11eb-909f-3781ed264f82.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107596452-c1eab780-6be5-11eb-80a6-e5e4dbef9f8d.png">


A - &lambda;I solves for &lambda; eigenvalues when singular, i.e. when det A - &lambda;I = 0   
then both rows of matrix A - &lambda;I are multiples of vector (a,b)  
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
2. Q is skew symmetric matrix; so, each &lambda; is pure imaginary (i.e. not complex)

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


example:
demonstrates
- finding &lambda; via the determinant of the matrix A - &lambda;I set to zero.  
- trace of A = sum of A's &lambda;s
- determinant of A = product of As &lambda;s
- these methods translate to sqaure and inverse of A and to linear combinations of A with I e.g.  [wonder if that works because I has same eigenvectors as A]
- A<sup>2</sup>'s &lambda;s = A's &lambda;s<sup>2</sup>
- A<sup>-1</sup>'s &lambda;s = 1 / A's &lambda;s
- A + 4 * I &lambda;s = A's &lambda;s + 4 * det I = A's &lambda;s + 4 * 1 

A's &lambda;s = 1 and 3  
trace of A = 2 + 2 = 4   
sum of A's &lambda;s = 1 + 3  
det A = 3  
product of A's &lambda;s = 1 * 3  

A<sup>2</sup>'s &lambda;s = 1<sup>2</sup> or 1 and 3<sup>2</sup> or 9  
trace of A<sup>2</sup> = 2 + 2 = 4   
sum of A<sup>2</sup>'s &lambda;s = 1 + 3  
det A<sup>2</sup> = 3  
product of A<sup>2</sup>'s &lambda;s = 1 * 3  

A<sup>-1</sup>'s &lambda;s = 1/1 and 1/3  
trace of A<sup>-1</sup> = 2/3 + 2/3 = 4/3   
sum of A<sup>-1</sup>'s &lambda;s = 1/1 + 1/3 = 4/3  
det A<sup>-1</sup> = 1/3  
product of A<sup>-1</sup>'s &lambda;s = 1/1 * 1/3 = 1/3  

( A + 4 * I )'s &lambda;s = 1 + 4 * 1 = 5 and 3 + 4 * 1 = 7  
trace of ( A + 4 * I ) = 2 + 4 * 1 + 2 + 4 * 1 = 6 + 6 = 12  
sum of ( A + 4 * I )'s &lambda;s = 1+4 * 1 + 3 + 4 * 1 = 5 + 7 = 12  
det( A + 4 * I ) = 6 * 6 - (-1 * -1) = 35  
product of ( A + 4 * I )'s &lambda;s = 5 * 7 = 35  

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107711816-43018780-6c96-11eb-86d8-cfb2481c39e7.png">

the eigenvectors from A are the same for A<sup>2</sup>, A<sup>-1</sup> and A - 4 * I in that they the eigenvectors from A are n the null space of A, A<sup>2</sup>, A<sup>-1</sup> and A - 4 * I  and in the sense that the eigenvectors do not change direction when multiplied by A, A<sup>2</sup>, A<sup>-1</sup> or A - 4 * I  or when multiplied by the eigenvalues of A, A<sup>2</sup>, A<sup>-1</sup> and A - 4 * I as shown here:

<img width="672" alt="image" src="https://user-images.githubusercontent.com/38410965/107715258-e0f85080-6c9c-11eb-8510-d2295874ae3e.png">



Gershgorin estimation of eigenvales in A

Every eigenvalue of A must be 'near' at least one of the entries a<sub>ii</sub> on the main diagonal.  For &lambda; to be 'near a<sub>ii</sub>' means that |a<sub>ii</sub> - &lambda;| is no more than the sum R<sub>i</sub> of all other |a<sub>ii</sub>| in the row i of the matrix.  Then R<sub>i</sub> = ∑<sub>j≠i</sub> | a<sub>ij</sub> is the radius of a circle centered at a<sub>ii</sub>.

[a<sub>ii</sub> is the center and &lambda; is inside the circle with radius = sum of absolute values of other row items]

every &lambda; is in the circle around one or more diagonal entries a<sub>ii</sub>: | a<sub>ii</sub> - &lambda; | ≤ R<sub>i</sub>

from chapter 2

reasoning: if &lambda; is an eigenvalue, then A-&lambda;•I is not invertible.  then A - &lambda;•I cannot be diagonally dominant.  "usually it takes work to decode if a matrix is invertible.  find a full set of non-zero pivots in elmination and the determinant is the product of the pivots.  but for some matrices, invertibility can be discerned when every number a<sub>ii</sub> on the main diagonal dominates the off diagonal part of that row.  diagonally dominant matrices are invertible.  each a<sub>ii</sub> on the diagonal is larger than the total sum along the rest of the row i:"

|a<sub>ii</sub>| > ∑<sub>j≠i</sub> |a<sub>ij</sub>| means that |a<sub>ii</sub> > |a<sub>i1</sub> + ... (skip |a<sub>ii</sub>|) ... + |a<sub>in</sub>|

see chanpter 2 for reasoning. 

so at least one diagonal entry <sub>ii</sub> - &lambda; is not larger than the sum R<sub>i</sub> of all other entries |a<sub>ij</sub>| in row i.

example: every eigenvalue &lambda; of this A falls into one or both Gershgorin circles whose centers are center<sub>1</sub> = a and center<sub>2</sub> = d and radii are R<sub>1</sub> =  |b| and R<sub>2</sub> = |c| which are the other components of the same row as the diagonal a and d.

first circle: | &lambda; - a | ≤ | b |  
first circle: | &lambda; - d | ≤ | c |

those are circles in the complex plane since &lambda; could be complex.

example 2:  all eigenvalues of A lie in a circle of radius R = 3 around one or more of the diagonal entries d<sub>1</sub>, d<sub>2</sub>, d<sub>3</sub>:

A = 
[
[ d<sub>1</sub>, 1, 2 ],
[ 2, d<sub>2</sub>, 1 ],
[ -1, 2, d<sub>3</sub> ],
]

| &lambda; - d<sub>1</sub> | ≤ 1 + 2 = R<sub>1</sub>  
| &lambda; - d<sub>2</sub> | ≤ 2 + 1 = R<sub>2</sub>  
| &lambda; - d<sub>3</sub> | ≤ 1 + 2 = R<sub>3</sub>  

"near" means not more than 3 away from d<sub>1</sub>, d<sub>2</sub>, d<sub>3</sub>


interesting problems:

if know x eigenvector, the way to find &lambda; is to multiply Ax and know that it should = &lambda;x.


if A has &lambda;<sub>1</sub> = 4 and &lambda;<sub>2</sub> = 5 then det (A - &lambda; • I) = (&lambda;<sub>1</sub> - 4)(&lambda;<sub>2</sub>-5) = &lambda;<sup>2</sup> - 9&lambda; + 20.  Find 3 matrices that have trace a + d = 9 and determinant = 20 and &lambda;s 4 and 5.  Use quadradic formula for hints.  &lambda;<sup>1</sup> = 1, a + d = 9  ad - bc = determinant = 20.  

the eigenvalues of A equal the eigenvalues of A<sup>T</sup> because (A - &lambda; I) has same determinant as (A - &lambda;I)<sup>T</sup> because every square matrix has det M = det M<sup>T</sup>.  

markov matrix M has M<sup>T</sup> (1,1,1) = (1,1,1) means that 1 is a &lambda; since M and M<sup>T</sup> share eignvalues.  Markovs are always singular; so zero is a &lambda; too.  If we konw that trace = 1/2, then we know the 3rd &lambda; is -1/2.  

find three 2x2 matrices that have &lambda;<sub>1</sub> = &lambda;<sub>1</sub> = 0, the trace = 0  and the determinant is zero.  A may not be the zero matrix but A<sup>2</sup> = 0.

1 -1
1 -1

0 1
0 0

0 0
1 0

find matrix singular with rank 1 and 3 &lambda;s and 3 eigenvectors.  


eigenvectors are column space if eigenvalues are ≠ 0.  that is true because Ax = &lambda;x  
eigenvectors are null space if eigenvalues are = 0.  that is true because Ax = 0x  

the eigenvalues of a equal the eigenvalues of A<sup>T</sup> because det (A - &lambda;I) = det (A<sup>T</sup> - &lambda;I) and that is true because every square matrix has det M = det M<sup>T</sup>.  But the eigenvectors of A and A<sup>T</sup> are not the same.  

construct a 3x3 markov matrix M: positive entries down each column add to 1.  show that M<sup>T</sup>(1,1,1) = (1,1,1).  [ would seem obvious from the description of a markov matrix that if you transpose it then the sum of the rows achieved by a vector x = (1,1,1) would be 1s. ] but he's clearly interested in something else.  by the last problem, know that M and M<sup>T</sup> share eigenvalues.  So &lambda; = 1 is also an eigenvalue of M.  a 3x3 singular matrix with trace 1/2 has what &lambda;s?  the eignenvalues must be 1 (because it is a markov) and zero (because it is singular) and -1/2 since the sum of its eigenvalues = 1/2

this matrix is singular with rank 1, duh since it is an outside product, find 3 &lambda;s and 3 eigenvectors:  A = u<sup>T</sup>v (1,2,1)<sup>T</sup>(2,1,2).   
answer: 2 &lambda;s = 0 since it is singular: is this a rule such that same number of non-zero pivots as non-zero &lambda;s?  yes! because this will reduce to 2 rows of zeros and 1 row with a single pivot. still doesnt pove that zero rows contribute zero &lambda;s.  waxman said that since A is singular we know 'at least one eigenvalue = 0'.

since the sum of diagonals is 2+2+2 = 6, then the third &lambda; = 6. 

2 eigenvectors are in the null space of A since it is rank 1 and zero is subtracted from A's first 2 diagonals.  (0,-2,1) and (1,-2,0) the 3rd is u = (1,2,1) which is the original u.

section 6.2

principles:

1. the colmns of AX and XA are Ax<sub>k</sub> = &lambda;<sub>k</sub>x<sub>k</sub>.  
the eigenvalue matrix &Lambda; is diagonal.  

2. n independent eigenvectors in X diagonalize A:  

A = X&Lambda;X<sup>-1</sup> and &Lambda; = AX<sup>-1</sup>A

3. the eigenvector matrix X also diagonalizes all powers A<sup>k</sup>

A<sup>k</sup> = X&Lambda;<sup>k</sup>X<sup>-1</sup> [and &Lambda;<sup>k</sup> = X<sup>-1</sup>A<sup>k</sup>X]

4. solve u<sub>k+1</sub> = Au<sub>k</sub> by u<sub>k</sub> = A<sup>k</sup><sub>u<sub>0</sub></sub> = X&Lambda;<sup>k</sup>X<sup>-1</sup>u<sub>0</sub> = c<sub>1</sub>(&lambda;<sub>1</sub>)<sup>k</sup>x<sub>1</sub> + ... + c<sub>n</sub>(&lambda;<sub>n</sub>)<sup>k</sup>x<sub>n</sub>

5. 
no equal eigenvalues --> A invertible and A can be diagonalized.  

equal eigenvalues --> A might have too few independent eigenvectors and then X<sup>-1</sup> fails

6. every matrix C = B<sup>-1</sup>AB has same eigenvalues as A.  These Cs are similar to A.  


Ax = &lambda;x removes matrix interconnected difficulties and so follows the eigenvectors separately.  &lambda;s are like having a diagonal matrix with no off diagonal interconnections: the 100th power of a diagonal matrix is easy.  

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107833480-69402980-6d61-11eb-810e-ec86f3678451.png">

A --> &Lambda; diagonal matrix via diagonalization.

Diagonalization:  
A is n x n  
A has n linearly independent eigenvectors x<sub>1</sub>, ... , x<sub>n</sub>   
Put A's independent eigenvectors into the columns of eigenvector matrix X.  
X<sup>-1</sup>AX is the eigenvalue matrix &Lambda;

Ax = &lambda;x  
AX = &Lambda;X
X = eigenvector matrix
&Lambda; = eigenvalue matrix

X<sup>-1</sup>AX = &Lambda; = diag(&lambda;<sub>1</sub>, ... , &lambda;<sub>n</sub>)

[ Doing this with variables first: ]

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107838523-33f10700-6d74-11eb-821a-e63f93349a64.png">

and now with numbers in letters.  do it over I would have assigned a, b and d as variables but kept the LL corner as zero. 

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107838835-ca71f800-6d75-11eb-93aa-7951e4c4039b.png">

heres the math and interesting result that X's and Xinv's cancel so that powers of A are translated only to powers of &Lambda; which makes perfect sense since we saw that before.  A<sup>n</sup>x = &lambda;<sup>n</sup>x before --> A<sup>n</sup>X = X&Lambda;<sup>n</sup>X<sup>-1</sup>X = X&Lambda;<sup>n</sup>

A<sup>200</sup> has the same eigenvectors as A in X and eigenvalues powered 200 times in &Lambda;:

note (not shown here) that when n = 0, A<sup>n</sup> = X&Lambda;<sup>n</sup>X<sup>-1</sup> = A<sup>0</sup> = X&Lambda;<sup>0</sup>X<sup>-1</sup> = X&IX<sup>-1</sup> = X&X<sup>-1</sup> = I because inside &Lambda;, each &lambda;<sup>0</sup> = 1 and so only has 1s on the diagonal, which is the identity matrix I.

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107839176-0e65fc80-6d78-11eb-8b16-77c3296b394f.png">

interesting to note that the 2 spaces (A - &lambda;<sub>1</sub>I) andn (A - &lambda;<sub>2</sub>I) used to discover the (never changing, axis-like) eigenvectors are orthogonal.  

by numerical example these row space of one is orthogonal to the colum space of the other, but the resulting eigenvectors are not. 

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107839625-1d01e300-6d7b-11eb-9168-df64cf49d06e.png">

by variables, a, b, c, d; yellow sheets have all the quadratics arriving at lambda_1, lambda_2 but solve does the work!



those long formulars at end are in cells (1,1) (1,2) (2,1) (2,2) respectively in A:  
- all items in off diagonals (1,2) and (2,1) cancel.
- cell (1,1):   
the sqrts are opposite signs so anything they multiply cancel except each other; remember they're each divided by 2
= b*c + aa/4 + dd/4 - 2ad/4 + aa/4 - 2ad/4 - 4bc/4 - dd/4 = 0
- cell (2,2):
the sqrts are opposite signs so anything they multiply cancel except each other; remember they're each divided by 2
= b*c + aa/4 + dd/4 - 2ad/4 + aa/4 - 2ad/4 - 4bc/4 - dd/4 = 0

(1,1): b•c + (a/2 - d/2 - sqrt(a••2 - 2•a•d + 4•b•c + d••2)/2)•(a/2 - d/2 + sqrt(a••2 - 2•a•d + 4•b•c + d••2)/2)  

(1,2): b•(-a/2 + d/2 - sqrt(a••2 - 2•a•d + 4•b•c + d••2)/2) + b•(a/2 - d/2 + sqrt(a••2 - 2•a•d + 4•b•c + d••2)/2)

(2,1): c•(-a/2 + d/2 + sqrt(a••2 - 2•a•d + 4•b•c + d••2)/2) + c•(a/2 - d/2 - sqrt(a••2 - 2•a•d + 4•b•c + d••2)/2) 

(2,2): b•c + (-a/2 + d/2 - sqrt(a••2 - 2•a•d + 4•b•c + d••2)/2)•(-a/2 + d/2 + sqrt(a••2 - 2•a•d + 4•b•c + d••2)/2)

so the row space created from (A - &lambda;1•I) is orthogonal to column space created by (A - &lambda;2•I) since their product = 0

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107840445-baabe100-6d80-11eb-8494-1b2294030ca0.png">

in sum:

(A - &lambda<sub>2</sub>•I) perpendicular to (A - &lambda<sub>1</sub>•I) perpendicular to x<sub>1</sub><sup>T</sup>

(A - &lambda<sub>1</sub>•I) perpendicular to (A - &lambda<sub>2</sub>•I) perpendicular to x<sub>2</sub><sup>T</sup>

this function, quadratic in ch6, provides the same solution as solve.

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107858478-4c0f6780-6e02-11eb-8e59-e6d924fab69e.png">

multiplying X * &Lambda; gives you x<sub>j</sub>&lambda;<sub>j</sub> in each column.

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107859022-fe482e80-6e04-11eb-8637-2db550e1bd92.png">

include this to show that &Lambda;X is not the same but also so to realize that AX = X&Lambda not &Lambda;X which has the x<sub>j</sub>&lambda;<sub>j</sub> in each row.

AX = X&Lambda; --> A = X&Lambda;X<sup>-1</sup> --> &Lambda; = X<sup>-1</sup>AX

A multiplies eigenvectors in columns of X and the first column of AX is Ax<sub>1</sub> = &lambda;x<sub>1</sub>.  Each column x<sub>j</sub> of X multiplies its respective &lambda;<sub>j</sub> in the column j of diagonal matrix &Lambda; 

X&Lambda; = [&lambda;<sub>1</sub>x<sub>1</sub>, ... , &lambda;<sub>j</sub>x<sub>j</sub>, ... , &lambda;<sub>n</sub>x<sub>n</sub>]

keep those matrices in the right order!  AX = X&Lambda; !

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107859279-7cf19b80-6e06-11eb-9950-a4b66700b9b0.png">

diagonalization is replacing A for all the columns of X with &Lambda; for all columns of X where &Lambda; is simpler than A because &Lambda; is diagonal and A is not. 

X has an inverse because its columns (the eigenvectors of A) are assumed to be linearly independent. 

without n independent eigenvectors x<sub>j</sub> we could not diagonalize. 

&lambdas; shift their respective i row of A by &lambdal•1 subtracted from the diagonal element of that row.

4 remarks:

1. any matrix that has no repeated eigenvalues can be diagonalized because its eigenvectors are independent. 

2. eigenvectors can be multiplied by any non-zero constant: A(cx) = &lambda;(cx).  this is because the eigenvectors are in the null space of A-&lambda;•I matrices and remember null space solutions can be multiplied by constants (since their goal is to = 0). Most software packages yield the eigenvector solution that has unit length: ||x|| = 1.

3. the eigenvectors of X come in the same order as the eigenvalues of &Lambda;.  Seems obvious since X&Lambda; = [x<sub>1</sub>, ... , x<sub>n</sub>][&lambda;<sub>1</sub>, ... , &lambda;<sub>n</sub>]

to diagonalize A, use eigenvector matrix. 

4. repeated warning for repeated eigenvalues: matrices with too few eigenvectors cannot be diagonalized. repeated eigenvalues are lead to repeated eigenvectors which are not independent.  if you only have n-1 eigenvectors then your X has non-independent eigenvectors. 

there is no connection between invertibility and diagonalizability: &lambda; = 0 means A singular.  

invertibility relates to eigenvalues: &lambda; zero or non-zero.  
diagonalizability relates to the eigenvectors: too few or enough for X.   
[not sure if the implication is that an x<sub>j</sub> that is paired with &lambda;<sub>j</sub> = 0 would be in the null space of A and independent of another x<sub>j</sub> that is paired with &lambda;<sub>j</sub> != 0 would be in the column space of A ?]


eigenvectors for n different eigenvalues are independent --> diagonalization can

independent eigenvectors x from different eigenvalues &lambda;

eigenvectors x<sub>1</sub>, ... , x<sub>j</sub> that correspond to distinct (all different) eigenvalues are linearly independent.

n x x matrix that has n different eigenvalues (no repeats) must be diagaonlizable. 

theres a proof for when &lambda; eigenvalues are distinct, eigenvectors x are independent.

1. c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> = 0 but no x<sub>j</sub> = 0   
2. multiply that equation by A (use diagonal [&lambda;<sub>1</sub>, &lambda;<sub>2</sub>] in As place) you get c<sub>1</sub>&lambda;<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>&lambda;<sub>2</sub>x<sub>2</sub> = 0   
3. multiply that equation by &lambda;<sub>2</sub> via diagonal [&lambda;<sub>2</sub>, &lambda;<sub>2</sub>]) you get c<sub>1</sub>&lambda;<sub>2</sub>x<sub>1</sub> + c<sub>2</sub>&lambda;<sub>2</sub>x<sub>2</sub> = 0   
4. subtract quantities in 2 and 3 above:  (&lambda;<sub>1</sub>-&lambda;<sub>2</sub>)c<sub>1</sub>x<sub>1</sub>  
5. since &lambda;<sub>1</sub> ≠ &lambda;<sub>2</sub> by assumption, &lambda;<sub>1</sub>-&lambda;<sub>2</sub> > 0.  also all x<sub>j</sub> ≠ 0.  so only c<sub>1</sub> can = 0.  only c can cause the amount in 1 above to be zero. 

A<sup>k</sup> --> zero when all | &Lambda; | < 1

A<sup>k</sup> = 
[
[a<sup>k</sup>, 0],
[0, d<sup>k</sup>]
]


Similar matrices: same eigenvalues

supposed eigenvalues matrix &Lambda; is fixed.  
as change eigenvector matrix X, a whole family of matrices A = X&Lambda;X<sup>-1</sup> emerges all with same eigenvalues in &Lambda;.  these are called "similar matrices"   

... and this category extends to matrices that cannot be diagonalized: choose one constant matrix that is not necessarily &Lambda;, and categorize whole family of matrices A = B C B<sup>-1</sup> that includes all invertible (i.e. with independent columns) matrices B.  A and C are called "similar".

A and C are "similar" in A = BCB<sup>-1</sup> when columns of B are independent. 

C need not be diagonal.  
B might not be eigenvectors [i.e. might not be born from the null space of orthogonal spaces]   
only requirement: B is invertible, [independent columns], its columns contain any basis for R<sup>n</sup>.  

the key fact about these similar matrices A and C is that they contain the same eigenvalues of C. [even if C is not diagonal]

proof:
remember we started with :
"suppose matrix &Lambda; is fixed ... family of different matrices ... same eigenvalues in &Lambda; ... all those matrices A (with the same &Lambda;) are called similar."
then: 
"extends ... cant be diagonalized ... one constant matrix C (not necessarily &Lambda;) ... A = BCB<sup>-1</sup>" for all invertible matrices B.  C not &Lambda; because not necessarily diagonal; B not X because not necessarily eigenvectors = null space of A - &lambda;<sub>A</sub>.  B only need be invertible.  and to be similar, A and C need only share the same eigenvalues. 

Cx = &lambda;x exits   
similar matrix BCB<sup>-1</sup> must have same &lambda; with new eigenvector, call it Bx:

BCB<sup>-1</sup>(Bx) = "reduces to" = B•I•Cx = BCx = "we know C = &lambda;" = B&lambda;x = &lambda;(Bx) 

which is what we said: C has a similar matrix BCB<sup>-1</sup> and that this similar matrix has a new eigenvector (Bx).  Thus since C and BCB<sup>-1</sup> are similar, both reduce to the same &lambda; and the similar BCB<sup>-1</sup> multiplies this eigenvector to be &lambda;(Bx).  

examples of families:

C as Identity matrix I has only one eigenvalue 1 so its family is small.  The only family member is BIB<sup>-1</sup> = I because the identity matric is the only diagonalizable matrix with all eigenvalues = 1.  [no zeros eigenvalues and obviously an eigenvector for each eigenvalue since it is diagonalizable]

a larger family    
with &lambda;s 1 and 1    
but with only one eigenvector (NOT diagonalizable).  

the simplest C [with family]   
Jordan form  
all similar matrices have
2 parameters r and s that are not both zeros  
always has determinant 1 and trace 2   
such as 

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/107869177-1cd81500-6e59-11eb-83a8-055290549463.png">

another important family    
&lambda; = 1 and 0    
whole family is diagonalizable with same eigenvalue matrix &Lambda;    
gives us every 2 x 2 matrix that has eigenvalues 1 and 0 with trace 1 and determinant = zero.    
[note diagonalizable but non-invertible since determinant = 0]   
all matrices A = A<sup>2</sup> including A = &Lambda; when B = I   
When A is symmetric, these are projection matrices.  
eigenvalues 1 and 0 make life easy.   
4 example matrices are below: &Lambda;, A1, A2, A3  

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107869601-054f5b00-6e5e-11eb-8f50-48e7b5c41d1b.png">



famous example: how quickly fibonacci numbers grow

0, 1, 1, 2, 3, 5, 6, 13, ... , F<sub>k+2</sub> = F<sub>k+1</sub> + F<sub>k</sub>

find the fibonacci number F<sub>100</sub> without following the rule one step at a time: F<sub>8</sub> = 21 = F<sub>7</sub> = 13 + F<sub>6</sub> = 8

where this is headed:  
solve u<sub>k+1</sub> = Au<sub>k</sub> by solving u<sub>k</sub> = A<sup>k</sup>u<sub>0</sub> = X&Lambda;<sup>k</sup>X<sup>-1</sup>u<sub>0</sub> = c<sub>1</sub>(&lambda;<sub>1</sub>)<sup>k</sup>x<sub>1</sub> + ... + c<sub>n</sub>(&lambda;<sub>n</sub>)<sup>k</sup>x<sub>n</sub>   
A<sup>k</sup> and its simpler cousin &Lambda;<sup>k</sup> get take u<sub>0</sub> to u<sub>k</sub>  

first step:  
u<sub>k+1</sub> = Au<sub>k</sub>  
is one-step rule for vectors.  
fibonacci is a 2 step rule for scalars.  
employ the 1-step rule for the 2-step need by putting 2 fibonacci [scalar] numbers into a vector.   

let u<sub>k</sub> = [F<sub>k+1</sub>, F<sub>k</sub>].T  
act on --> u<sub>k</sub>   
with [[1,1],[1,0]].T

the fibonacci rule to be mimmicked with vectors is:

[F<sub>k+2</sub>, F<sub>k+1</sub>].T = [F<sub>k+1</sub> + F<sub>k</sub>, F<sub>k+1</sub>].T 

executed by:

u<sub>k+1</sub> =  
[F<sub>k+2</sub>, 
F<sub>k+1</sub>]
= [
[1, 1],
[1, 0]
]
• u<sub>k</sub>
= [
[1, 1],
[1, 0]
]
• [
F<sub>k+1</sub>, 
F<sub>k</sub>
] 

every step multiplies by A   
after 100 steps, reach u<sub>100</sub> = A<sup>100</sup>u<sub>0</sub>:

![\begin{align*}
let:&
u_k =\begin{bmatrix}
F_{k+1}\\
F_k
\end{bmatrix}\\
translate:&
\begin{matrix}
F_{k+2}\\
F_{k+1}\\ \end{matrix} =\begin{matrix}
F_{k+1}+F_{k}\\
F_{k+1}
\end{matrix}\\
\\
by:&
u_{k+1} =\begin{bmatrix}
1&1\\
1&0
\end{bmatrix} u_k\\
or:&
u_{k+1} =
\begin{bmatrix}
F_{k+2}\\
F_{k+1}
\end{bmatrix} = 
\begin{bmatrix}
F_{k+1}+F_{k}\\
F_{k+1}
\end{bmatrix}=
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}\begin{bmatrix}
F_{k+1}\\
F_{k}
\end{bmatrix}\\
\\
with: & 
A = \begin{bmatrix}
1&1\\
1&0
\end{bmatrix}\\
100 steps:& u_0 = \begin{bmatrix}
1\\
0
\end{bmatrix}
= \begin{bmatrix}
F_1\\
F_0
\end{bmatrix}=\begin{bmatrix}
F_{k+1}\\
F_{k}
\end{bmatrix}; 
u_1 = A^1u_0 = 
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}
\begin{bmatrix}
1\\
0
\end{bmatrix}=
\begin{bmatrix}
F_{2}\\
F_{1}
\end{bmatrix}=
\begin{bmatrix}
1\\
1
\end{bmatrix};
\\
&u_2 = 
A^1u_1 = 
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}
\begin{bmatrix}
1\\
1
\end{bmatrix}=
A^2u_0 = 
\begin{bmatrix}
2&1\\
1&1
\end{bmatrix}
\begin{bmatrix}
1\\
0
\end{bmatrix}=
\begin{bmatrix}
F_{3}\\
F_{2}
\end{bmatrix}=
\begin{bmatrix}
2\\
1
\end{bmatrix};
\\
&u_3 = 
A^1u_2 = 
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}
\begin{bmatrix}
2\\
1
\end{bmatrix}=
A^3u_0 = 
\begin{bmatrix}
3&2\\
2&1
\end{bmatrix}
\begin{bmatrix}
1\\
0
\end{bmatrix}=
\begin{bmatrix}
F_{4}\\
F_{3}
\end{bmatrix}=
\begin{bmatrix}
3\\
2
\end{bmatrix};
\\
&u_100 = 
A^1u_99 = 
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
\begin{bmatrix}
?\\
?
\end{bmatrix}=
A^100u_0 = 
\begin{bmatrix}
573,147,844,013,817,084,101&354,224,848,179,261,915,075\\
354,224,848,179,261,915,075&218,922,995,834,555,169,026
\end{bmatrix}
\begin{bmatrix}
1\\
0
\end{bmatrix}=
\begin{bmatrix}
F_{101}\\
F_{100}
\end{bmatrix}=
\begin{bmatrix}
573,147,844,013,817,084,101\\
354,224,848,179,261,915,075
\end{bmatrix};
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Alet%3A%26%0Au_k+%3D%5Cbegin%7Bbmatrix%7D%0AF_%7Bk%2B1%7D%5C%5C%0AF_k%0A%5Cend%7Bbmatrix%7D%5C%5C%0Atranslate%3A%26%0A%5Cbegin%7Bmatrix%7D%0AF_%7Bk%2B2%7D%5C%5C%0AF_%7Bk%2B1%7D%5C%5C+%5Cend%7Bmatrix%7D+%3D%5Cbegin%7Bmatrix%7D%0AF_%7Bk%2B1%7D%2BF_%7Bk%7D%5C%5C%0AF_%7Bk%2B1%7D%0A%5Cend%7Bmatrix%7D%5C%5C%0A%5C%5C%0Aby%3A%26%0Au_%7Bk%2B1%7D+%3D%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D+u_k%5C%5C%0Aor%3A%26%0Au_%7Bk%2B1%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0AF_%7Bk%2B2%7D%5C%5C%0AF_%7Bk%2B1%7D%0A%5Cend%7Bbmatrix%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0AF_%7Bk%2B1%7D%2BF_%7Bk%7D%5C%5C%0AF_%7Bk%2B1%7D%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%0AF_%7Bk%2B1%7D%5C%5C%0AF_%7Bk%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Awith%3A+%26+%0AA+%3D+%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D%5C%5C%0A100+steps%3A%26+u_0+%3D+%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0AF_1%5C%5C%0AF_0%0A%5Cend%7Bbmatrix%7D%3D%5Cbegin%7Bbmatrix%7D%0AF_%7Bk%2B1%7D%5C%5C%0AF_%7Bk%7D%0A%5Cend%7Bbmatrix%7D%3B+%0Au_1+%3D+A%5E1u_0+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AF_%7B2%7D%5C%5C%0AF_%7B1%7D%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%3B%0A%5C%5C%0A%26u_2+%3D+%0AA%5E1u_1+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%3D%0AA%5E2u_0+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%261%5C%5C%0A1%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AF_%7B3%7D%5C%5C%0AF_%7B2%7D%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%3B%0A%5C%5C%0A%26u_3+%3D+%0AA%5E1u_2+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%3D%0AA%5E3u_0+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A3%262%5C%5C%0A2%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AF_%7B4%7D%5C%5C%0AF_%7B3%7D%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A3%5C%5C%0A2%0A%5Cend%7Bbmatrix%7D%3B%0A%5C%5C%0A%26u_100+%3D+%0AA%5E1u_99+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A0%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%3F%5C%5C%0A%3F%0A%5Cend%7Bbmatrix%7D%3D%0AA%5E100u_0+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A573%2C147%2C844%2C013%2C817%2C084%2C101%26354%2C224%2C848%2C179%2C261%2C915%2C075%5C%5C%0A354%2C224%2C848%2C179%2C261%2C915%2C075%26218%2C922%2C995%2C834%2C555%2C169%2C026%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AF_%7B101%7D%5C%5C%0AF_%7B100%7D%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A573%2C147%2C844%2C013%2C817%2C084%2C101%5C%5C%0A354%2C224%2C848%2C179%2C261%2C915%2C075%0A%5Cend%7Bbmatrix%7D%3B%0A%5Cend%7Balign%2A%7D)

this problem is just right for eigenvalues.  

subtract &lambda; from diagonal of A:

![\begin{align*}
A - &lambda;I = \begin{bmatrix}
1-&lambda;&1\\
1&-&lambda
\end{bmatrix} --> det(A - &lambda;I) = 0 = &lambda;^2 - &lambda; - 1\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+-+%26lambda%3BI+%3D+%5Cbegin%7Bbmatrix%7D%0A1-%26lambda%3B%261%5C%5C%0A1%26-%26lambda%0A%5Cend%7Bbmatrix%7D+--%3E+det%28A+-+%26lambda%3BI%29+%3D+0+%3D+%26lambda%3B%5E2+-+%26lambda%3B+-+1%5C%5C%0A%5Cend%7Balign%2A%7D)

the equation &lambda;<sup>2</sup> - &lambda; - 1 solved by quadratic formula gives:

&lambda;<sub>1</sub> = 1.618 = ( 1 + √5 ) / 2 

&lambda;<sub>2</sub> = 0.618 = ( 1 - √5 ) / 2 

2 eigenvalues lead to 2 eigenvectors via (A - &lambda;I)x = 0:

x<sub>1</sub> = (&lambda;<sub>1</sub>, 1)
x<sub>2</sub> = (&lambda;<sub>2</sub>, 1)

![\begin{align*}
\begin{bmatrix}
1-&lambda;&1\\
1&-&lambda;
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}&=
\begin{bmatrix}
x - &lambda;x+y = -(&lambda;x-x-y)\\
x-&lambda;y
\end{bmatrix}
\\ x_1 = x_2 \begin{bmatrix}
x\\
y
\end{bmatrix} = \begin{bmatrix}
&lambda;\\
1
\end{bmatrix}...&= \begin{bmatrix}
-(&lambda;&lambda;-x-1) = -(&lambda;^2-x-1) = (A -&lambda;I) = 0)\\
&lambda;-&lambda;*1=&lambda;-&lambda;=0
\end{bmatrix}= \begin{bmatrix}
0\\
0
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cbegin%7Bbmatrix%7D%0A1-%26lambda%3B%261%5C%5C%0A1%26-%26lambda%3B%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax+-+%26lambda%3Bx%2By+%3D+-%28%26lambda%3Bx-x-y%29%5C%5C%0Ax-%26lambda%3By%0A%5Cend%7Bbmatrix%7D%0A%5C%5C+x_1+%3D+x_2+%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D+%3D+%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D...%26%3D+%5Cbegin%7Bbmatrix%7D%0A-%28%26lambda%3B%26lambda%3B-x-1%29+%3D+-%28%26lambda%3B%5E2-x-1%29+%3D+%28A+-%26lambda%3BI%29+%3D+0%29%5C%5C%0A%26lambda%3B-%26lambda%3B%2A1%3D%26lambda%3B-%26lambda%3B%3D0%0A%5Cend%7Bbmatrix%7D%3D+%5Cbegin%7Bbmatrix%7D%0A0%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

that will lead to A<sub>100</sub> = &lambda;<sub>100</sub>  
by way of &lambdal<sub>1</sub> = (1 + √5)/2 and &lambda;<sub>2</sub> = (1-√5)/2     
acting on x<sub>1</sub> = (&lambda;<sub>1</sub>, 1) and x<sub>2</sub> =  (&lambda;<sub>2</sub>,1)  
but fibonacci starts with u<sub>0</sub> = (1,0)  
to act on u<sub>0</sub> with &lambda; eigenvaluess,   
need to make a u<sub>0</sub> from eigenvectors   
step 2 finds the combinations of these eigenvectors that gives u<sub>0</sub> = (1,0):  

![\begin{align*}
u_0 = \begin{bmatrix}
1\\
0
\end{bmatrix} = \frac{1}{&lambda;_1-&lambda;_2} ((x_1=
\begin{bmatrix}
&lambda;_1\\
1
\end{bmatrix})-(x_2=
\begin{bmatrix}
&lambda;_2\\
1
\end{bmatrix}))=
\frac{1}{&lambda;_1-&lambda;_2} (
\begin{bmatrix}
&lambda;_1\\
1
\end{bmatrix}-
\begin{bmatrix}
&lambda;_2\\
1
\end{bmatrix})=
\begin{bmatrix}
\frac{(1)&lambda;_1-(1)&lambda;_2}{&lambda;_1-&lambda;_2}\\
\frac{1}{&lambda;_1-&lambda;_2}-\frac{1}{&lambda;_1-&lambda;_2}
\end{bmatrix}
=\begin{bmatrix}
0\\
0
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au_0+%3D+%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D+%3D+%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%28%28x_1%3D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%29-%28x_2%3D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_2%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%29%29%3D%0A%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%28%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D-%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_2%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%29%3D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B%281%29%26lambda%3B_1-%281%29%26lambda%3B_2%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D-%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A0%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

so if need u<sub>0</sub> take a linear combination of x<sub>1</sub> = (&lambda;<sub>1</sub>).T and x<sub>2</sub> = (&lambda;<sub>1</sub>).T  with this factor. c and -c where c = 1/(&lambda;<sub>1</sub> - &lambda;<sub>2</sub>):


![\begin{align*}
u_0 &= \begin{bmatrix}
1\\
0
\end{bmatrix} = (\frac{1}{&lambda;_1-&lambda;_2} )x_1- (\frac{1}{&lambda;_1-&lambda;_2} )x_2
=\begin{bmatrix}
1\\
0
\end{bmatrix}
\\when:&\\
x_1 &=\begin{bmatrix}
&lambda;_1\\
1
\end{bmatrix}
\\
x_2 &=\begin{bmatrix}
&lambda;_2\\
1
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au_0+%26%3D+%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D+%3D+%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29x_1-+%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29x_2%0A%3D%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%0A%5C%5Cwhen%3A%26%5C%5C%0Ax_1+%26%3D%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0Ax_2+%26%3D%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_2%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)


step 3 multiplys u<sub>0</sub> by A<sup>100</sup> or its eigenvalues to find u<sub>100</sub>.  

the eigenvectors x<sub>1</sub> and x<sub>2</sub> are separate multiplied by &lambda;<sub>1</sub><sup>100</sup> and &lambda;<sub>2</sub><sup>100</sup>:

need only F<sub>100</sub> = second component of u<sub>100</sub>.  
the 2nd component of x<sub>1</sub> and x<sub>2</sub> is 1 and so can substitute 1 for x<sub>1</sub> and x<sub>2</sub>.  

notice that &lambda;<sub>2</sub><sup>k</sup> goes to zero as k goes to 100.

![\begin{align*}
Au_0 =
u_100 = \begin{bmatrix}
F_101\\
F_100
\end{bmatrix} 
&=
c_1&lambda;_1^100x_1 + c_2&lambda;_2^100x_2\\
&=
(\frac{1}{&lambda;_1-&lambda;_2} )&lambda;_1^100x_1 - 
(\frac{1}{&lambda;_1-&lambda;_2} )&lambda;_2^100x_2\\
&= 
(\frac{1}{&lambda;_1-&lambda;_2} )&lambda;_1^100 \begin{bmatrix}
&lambda;_2\\
1
\end{bmatrix} - 
(\frac{1}{&lambda;_1-&lambda;_2} )&lambda;_2^100 \begin{bmatrix}
&lambda;_1\\
1
\end{bmatrix}
\\
where&\\
c_1&=(\frac{1}{&lambda;_1-&lambda;_2} )\\
c_1&=-(\frac{1}{&lambda;_1-&lambda;_2} )
\\
\\
need&\\
F_100&= 
(\frac{1}{&lambda;_1-&lambda;_2} )&lambda;_1^100 \begin{bmatrix}
1
\end{bmatrix} - 
(\frac{1}{&lambda;_1-&lambda;_2} )&lambda;_2^100 \begin{bmatrix}
1
\end{bmatrix}\\
&= 
(\frac{&lambda;_1^100}{&lambda;_1-&lambda;_2} ) - 
(\frac{&lambda;_2^100}{&lambda;_1-&lambda;_2} )\\
&= 
\frac{&lambda;_1^100-&lambda;_2^100}{&lambda;_1-&lambda;_2} \\
&= 
\frac{1}{\sqrt{5}}(\frac{1+\sqrt{5}}{2})^100 \\
because&\\
\\
&lambda;_1&=\frac{1+\sqrt{5}}{2};&lambda;_1^100=(\frac{1+\sqrt{5}}{2})^100\\
and&\\
\\
&lambda;_2^100
&= zero\\
and&\\
\\
&lambda;_1-&lambda;_2&=\sqrt{5}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AAu_0+%3D%0Au_100+%3D+%5Cbegin%7Bbmatrix%7D%0AF_101%5C%5C%0AF_100%0A%5Cend%7Bbmatrix%7D+%0A%26%3D%0Ac_1%26lambda%3B_1%5E100x_1+%2B+c_2%26lambda%3B_2%5E100x_2%5C%5C%0A%26%3D%0A%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29%26lambda%3B_1%5E100x_1+-+%0A%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29%26lambda%3B_2%5E100x_2%5C%5C%0A%26%3D+%0A%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29%26lambda%3B_1%5E100+%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_2%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D+-+%0A%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29%26lambda%3B_2%5E100+%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0Awhere%26%5C%5C%0Ac_1%26%3D%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29%5C%5C%0Ac_1%26%3D-%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29%0A%5C%5C%0A%5C%5C%0Aneed%26%5C%5C%0AF_100%26%3D+%0A%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29%26lambda%3B_1%5E100+%5Cbegin%7Bbmatrix%7D%0A1%0A%5Cend%7Bbmatrix%7D+-+%0A%28%5Cfrac%7B1%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29%26lambda%3B_2%5E100+%5Cbegin%7Bbmatrix%7D%0A1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3D+%0A%28%5Cfrac%7B%26lambda%3B_1%5E100%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29+-+%0A%28%5Cfrac%7B%26lambda%3B_2%5E100%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%29%5C%5C%0A%26%3D+%0A%5Cfrac%7B%26lambda%3B_1%5E100-%26lambda%3B_2%5E100%7D%7B%26lambda%3B_1-%26lambda%3B_2%7D+%5C%5C%0A%26%3D+%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B5%7D%7D%28%5Cfrac%7B1%2B%5Csqrt%7B5%7D%7D%7B2%7D%29%5E100+%5C%5C%0Abecause%26%5C%5C%0A%5C%5C%0A%26lambda%3B_1%26%3D%5Cfrac%7B1%2B%5Csqrt%7B5%7D%7D%7B2%7D%3B%26lambda%3B_1%5E100%3D%28%5Cfrac%7B1%2B%5Csqrt%7B5%7D%7D%7B2%7D%29%5E100%5C%5C%0Aand%26%5C%5C%0A%5C%5C%0A%26lambda%3B_2%5E100%0A%26%3D+zero%5C%5C%0Aand%26%5C%5C%0A%5C%5C%0A%26lambda%3B_1-%26lambda%3B_2%26%3D%5Csqrt%7B5%7D%0A%5Cend%7Balign%2A%7D)

the ratio of F<sub>101</sub>/F<sub>100</sub> =  (1 + √5)/2 must be close to a limiting ratio with k = 100.  The greeks called this ratio the golden mean.  For some reason a rectangle with side 1.618 / 1 is graceful.


fibonacci is a difference equation  
u<sub>k+1</sub> = Au<sub>k</sub>   
each step multiplies by A   
solution is u<sub>k</sub> = A<sup>k</sup>u<sub>0</sub>  

diagonalizing matrices computes A<sup>k</sup> quick via &Lambda<sup>k</sup>.

u<sub>k+1</sub> = A<sub>k</sub> is a difference equation that structures the solution u<sub>k</sub> = A<sup>k</sup>u<sub>0</sub>

find u<sub>k</sub> in 3 steps:  

will compute powers of A via factoring A into &Lambda; matrix of eigenvalues and X matrix of eigenvectors; the trick to the speed is that XX<sup>-1</sup>=I inside of A<sup>k</sup>u<sub>0</sub> = X&Lambda;X<sup>-1</sup> • ... • X&Lambda;X<sup>-1</sup>u<sub>0</sub>= X&Lambda;<sup>k</sup>X<sup>-1</sup>u<sub>0</sub>

1. write u<sub>0</sub> as combination u<sub>0</sub> = c<sub>1</sub>x<sub>1</sub> + ... + c<sub>n</sub>x<sub>n</sub> of the eigenvectors.  to find c: c = X<sup>-1</sup>u<sub>0</sub>  

the eigenvectors of X lead to the c's inthe combinations u<sub>0</sub> = c<sub>1</sub>x<sub>1</sub> + ... + c<sub>n</sub>x<sub>n</sub>

u<sub>0</sub> = (x<sub>1</sub> ... x<sub>n</sub>).T c<sub>1</sub> ... c<sub>n</sub>) = Xc

these coefficients are c = X<sup>-1</sup>u<sub>0</sub>

2. multiply each eigenvector x<sub>1</sub> by &lambda;<sub>1</sub><sup>k</sup>.  
thus &Lambda;<sup>k</sup>

multiply by U<sup>k</sup> to get :

u<sub>k</sub> =  ∑<sub>j=1,n</sub> c<sub>j</sub>(&Lambda;<sub>j</sub>)<sup>k</sup>x<sub>j</sub>


3. add up the pieces c<sub>j</sub>&lambda;<sub>j</sub>x<sub>j</sub> to find solution u<sub>k</sub> = A<sup>k</sup>u<sub>0</sub> which is 

A<sup>k</sup>u<sub>0</sub> = X&Lambda;<sup>k</sup>X<sup>-1</sup>u<sub>0</sub> = X&Lambda;<sup>k</sup>c = u<sub>k+1</sub>

because X<sup>-1</sup>u<sub>0</sub> = c

the result is exactly u<sub>k</sub> = c<sub>1</sub>(&lambda;<sub>1</sub>)<sup>k</sup>x<sub>1</sub> + ... + c<sub>n</sub>(&lambda;<sub>n</sub>)<sup>k</sup>x<sub>n</sub>

u<sub>k+1</sup> = Au<sub>k</sup>

![\begin{align*}
A^ku_0 &= X&Lambda;^kX^{-1}u_0 = X&Lambda^{k}c = \begin{bmatrix}x_1 ... x_n\end{bmatrix}\begin{bmatrix}(&lambda;_1)^k&&\\&..&\\&&(&lambda;_n)^k\end{bmatrix}
\begin{bmatrix}
c_1\\
...\\
c_n
\end{bmatrix}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA%5Eku_0+%26%3D+X%26Lambda%3B%5EkX%5E%7B-1%7Du_0+%3D+X%26Lambda%5E%7Bk%7Dc+%3D+%5Cbegin%7Bbmatrix%7Dx_1+...+x_n%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%28%26lambda%3B_1%29%5Ek%26%26%5C%5C%26..%26%5C%5C%26%26%28%26lambda%3B_n%29%5Ek%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%5C%5C%0A...%5C%5C%0Ac_n%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D%0A)


example

Fibonacci like but rule is F<sub>k+2</sub> = F<sub>k+1</sub> + 2F<sub>k</sub>.   
start similar to Fibonacci 0,1,1,3, ... but grow faster because eignevalue &lambda; = 2

the basics:

A, eigenvalue &lambda;<sub>1</sub> and &lambda;<sub>2</sub>, eigenvectors x<sub>1</sub> and x<sub>2</sub>, x's Ax's and &lambda;x's all in same direction, but notice that As and &lambda;s eigenvalues times eigenvectors x's do not produce the right F0, F1, F2, F3, etc.  F<sub>0</sub>, F<sub>1</sub>, F<sub>2</sub>, F<sub>3</sub>, ... , F<sub>k</sub> are a product of A<sup>k</sup>u<sub>0</sub> where u<sub>0</sub> is a vector (not a scalar like F<sub>k</sub>) that looks like (F<sub>k+1</sub>, F<sub>k</sub>).T = A<sup>k</sup>u<sub>0</sub> with the example here k=3.  To get to the right F one needs to move to the 3 steps.

<img width="672" alt="image" src="https://user-images.githubusercontent.com/38410965/107902003-363d9780-6f13-11eb-8b6f-a5a086c8a6ad.png">

now the 3 steps:   
1. express u<sub>0</sub> as linear combination of the eigenvectors so that the eigenvalues can replace A and arrive at the same outcomes.  
2. multiply the linear combination by &Lambda;  
3. inject the actual values.  

linear combination.  the goal is:  
u<sub>0</sub> = c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub>   
u<sub>k</sub> = c<sub>1</sub>&lambda;<sup>k</sup>x<sub>1</sub> + c<sub>2</sub>&lambda;<sup>k</sup>x<sub>2</sub>   
where e.g. ...
u<sub>0</sub> = c<sub>1</sub>&lambda;<sup>k=0</sup>x<sub>1</sub> + c<sub>2</sub>&lambda;<sup>k=0</sup>x<sub>2</sub>   

arrive at c:  start with k=0
u<sub>0</sub> = (1,0).T = c(x<sub>1</sub> + x<sub>2</sub>) = c ( (2,1).T + (1,-1).T ) = c (3,0).T --> c = (1/3)
u<sub>0</sub> = (1,0).T = (1/3)x<sub>1</sub> + (1/3)x<sub>2</sub>

u<sub>0</sub>[index 1] = F<sub>0</sub>

add in &lambda;s:

u<sub>k</sub> = A<sup>k</sup>u<sub>0</sub> = c<sub>1</sub>&lambda;<sup>k</sup>x<sub>1</sub> + c<sub>2</sub>&lambda;<sup>k</sup>x<sub>2</sub> = (1/3)(2)<sup>k</sup>(2,1).T + (1/3)(-1)<sup>k</sup>(1,-1).T = (F<sub>k+1</sub>, F<sub>k</sub>)

only take the 2nd component (indexed 1):

u<sub>k</sub>[1] = A<sup>k</sup>[1] = F<sub>k</sub> = (2<sup>k</sup> - (-1)<sup>k</sup>) / 3

for example: 0,1,1,3 ... F<sub>4</sub> = (2<sup>4</sup> - (-1)<sup>4</sup>) / 3 = (16 - (-1)<sup>4</sup>)/3 = 15/3 = 5

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107902556-c6301100-6f14-11eb-8fc4-5a9a27eed40f.png">

non-diagonalizable matrices

&lambda; is an eigenvalue of A discovered in one of two ways:

- eigenvectors (geometric) ... there are non-zero solutions to Ax = &lambda;x   
- eigenvalues (algebraic) ... the determinant of (A - &lambda;I) = 0

&lambda may be a "simple" eigenvalue or a "multiple" eigenvalue.  

[for multiple eigenvalues,] we want to know the eigenvalue's multiplicity.  

most eigenvalues have multiplicity of M = 1 (simple eigenvalues).    
then there is a single line of eigenvectors. [line created by a scalar like c in previous examples; cx still solves (A - &lambda;I)cx = 0]    
det(A - &lambda;I) does not have a double factor [&lambda;<sup>2</sup>]    

for exceptional matrices, an eigenvalue can be repeated.   
there are 2 different ways to count multiplicity.   
1. geometric multiplicity = GM  
GM counts the independent eigenvectors for &lambda;   
GM is dimension of the null space of (A - &lambda;I)  

[notice there may be multiple &lambda; that satisfy det (A-&lambda;I) = 0, e.g. 0,0 in the example below, but this isnt what this null space is about.  this is about after you use det(A - &lamnda;I) = 0 to find your &lambda;s and are plugging one of them back into (A-&lambda;I), you find that there are a number of dimensions to the null space, i.e. more than one x eigenvector satisfies (A-&lambda;I)x = 0]   GM is about eigenvectors; null space of  A-&lambda;I.  AM is about eigenvalues; det A-&lambda;I.

[eigenvectors per &lambda;]  
2. algebraic multiplicity = AM  
AM counts the number of repetitions of &lambda; among the eigenvalues.  
AM looks at the n roots of det(A - &lambda;) = 0 

if A has &lambda; = 4, 4, 4 then that eigenvalue has AM = 3 but may have GM of 1,2 or 3. 

example 1:  

A = [ [ 0, 1 ], [ 0, 0 ] ]  
AM = 2   
GM = 1  
det A - &lambda; I = &lambda;<sup>2</sup> 

det A has a double factor aka double root
&lambda; = 0, 0   
2 eigenvalues --> AM = 2
1 eigenvector = (1,0) 1 dimension in null space of (A - &lambda;I) --> GM = 1

**the shortage of eigenvectors when GM < AM means that A is not diagonalizable.**

example 2:  

all 3 matrices have same shortage of eigenvectors.   their repeated eigenvalue is &lambda; = 5.   
trace - 10 in all cases (&lambda;<sub>1</sub> + &lambda;<sub>2</sub>, d<sub>1</sub> + d<sub>2</sub>) and determinants are 25 (&lambda;<sub>1</sub> * &lambda;<sub>2</sub>).

each has 1 line of eigenvectors to solve (A - &lambda;I) = 0: A1 has x<sub>1</sub> = (1, 0).T, A2 has x<sub>1</sub> = (1, 1).T, A3 has x<sub>1</sub> = (1, -1).T 

AM = 2 because there are 2 &lambda; eigenvalue roots to det(A - &lambda;) = 0   
GM = 1 because there is 1 eigenvector in the null space of (A - &lambda;) = only 1 line of eigenvectors that solves (A - &lambda;)x = 0 for &lambda; = 5.  these matrices are not diagonalizable because GM < AM. 

<img width="442" alt="image" src="https://user-images.githubusercontent.com/38410965/107976959-5c514f00-6f88-11eb-8d0a-a7c57c45ac9f.png">


review:
1. if A has n independent eignevectors, x<sub>1</sub>, ... , x<sub>n</sub> they go into the columns of X  

A is diagonalized by X.

X<sup>-1</sup>AX = &Lambda;  
X&Lambda;X<sup>-1</sup> = A  

2. the powers of A are A<sup>k</sup> = X&Lambda;<sup>k</sup>X<sup>-1</sup>  

the eigenvectors in X are unchanged by powers.

3. the eigenvalue of A<sup>k</sup> are (&Lambda;<sub>1</sub>)<sup>k</sup>, ... , (&Lambda;<sub>n</sub>)<sup>k</sup> in the matric &Lambda;<sup>k</sup>  

4. the solution to U<sub>k+1</sub> = Au<sub>k</sub> starting from u<sub>0</sub> is u<sub>k</sub> = A<sup>k</sup>u<sub>0</sub> = X&Lambda;<sup>k</sup>X<sup>-1</sup>u<sub>0</sub>: 

u<sub>k</sub> = c<sub>1</sub>(&lambda;<sub>1</sub>)<sup>k</sup>x<sub>1</sub> + ... + c<sub>n</sub>(&lambda;<sub>n</sub>)<sup>k</sup>x<sub>n</sub> provided u<sub>0</sub> = c<sub>1</sub>x<sub>1</sub> + ... + c<sub>n</sub>x<sub>n</sub>

that shows Steps 1, 2, 3: c's from X<sup>-1</sup>u<sub>0</sub>, &lambda;<sup>k</sup> from &Lambda;<sup>k</sup> and x's from X.

5. A is diagonalizable if every eigenvalue (GM) has enough eigenvectors (AM): GM = AM.

Lukas numbers (1, 3, 4, 7, 11, 18, ... ) use the same rule L<sub>k+2</sub> = L<sub>k+1</sub> + L<sub>k</sub> as Fibonacci (0,1, 1, 2, 3, 5, 8, 13, 21, ... ) = F<sub>k+2</sub> = F<sub>k+1</sub> + F<sub>k</sub>, but start at 1 rather than 0.

L<sub>100</sub> = &lambda;<sub>1</sub><sup>100</sup> + &lambda;<sub>2</sub><sup>100</sup>

as with Fibonacci u<sub>k+1</sub> = [ [ 1, 1 ], [1, 0 ] ] u<sub>k</sub> where u<sub>k</sub> = [ [L<sub>k+1</sub>], [L<sub>k</sub>] ] as with Fibonacci: 

u<sub>k+1</sub> = [ [ 1, 1 ], [1, 0 ] ] u<sub>k</sub> =  [ [ 1, 1 ], [1, 0 ] ] [ [L<sub>k+1</sub>], [L<sub>k</sub>] ] = [ [L<sub>k+2</sub>], [L<sub>k+1</sub>] ] = [ [L<sub>k+1</sub> + L<sub>k</sub>], [L<sub>k+1</sub>] ]
