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

(A - &lambda;<sub>2</sub>•I) perpendicular to (A - &lambda;<sub>1</sub>•I) perpendicular to x<sub>1</sub><sup>T</sup>

(A - &lambda;<sub>1</sub>•I) perpendicular to (A - &lambda;<sub>2</sub>•I) perpendicular to x<sub>2</sub><sup>T</sup>

this function, quadratic in ch6, provides the same solution as solve.

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107858478-4c0f6780-6e02-11eb-8e59-e6d924fab69e.png">

multiplying X * &Lambda; gives you x<sub>j</sub>&lambda;<sub>j</sub> in each column.

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107859022-fe482e80-6e04-11eb-8637-2db550e1bd92.png">

include this to show that &Lambda;X is not the same but also so to realize that AX = X&Lambda; not &Lambda;X which has the x<sub>j</sub>&lambda;<sub>j</sub> in each row.

AX = X&Lambda; --> A = X&Lambda;X<sup>-1</sup> --> &Lambda; = X<sup>-1</sup>AX

A multiplies eigenvectors in columns of X and the first column of AX is Ax<sub>1</sub> = &lambda;x<sub>1</sub>.  Each column x<sub>j</sub> of X multiplies its respective &lambda;<sub>j</sub> in the column j of diagonal matrix &Lambda; 

X&Lambda; = [&lambda;<sub>1</sub>x<sub>1</sub>, ... , &lambda;<sub>j</sub>x<sub>j</sub>, ... , &lambda;<sub>n</sub>x<sub>n</sub>]

keep those matrices in the right order!  AX = X&Lambda; !

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/107859279-7cf19b80-6e06-11eb-9950-a4b66700b9b0.png">

diagonalization is replacing A for all the columns of X with &Lambda; for all columns of X where &Lambda; is simpler than A because &Lambda; is diagonal and A is not. 

X has an inverse because its columns (the eigenvectors of A) are assumed to be linearly independent. 

without n independent eigenvectors x<sub>j</sub> we could not diagonalize. 

&lambda;s shift their respective i row of A by &lambda;•1 subtracted from the diagonal element of that row.

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
by way of &lambda;<sub>1</sub> = (1 + √5)/2 and &lambda;<sub>2</sub> = (1-√5)/2     
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

diagonalizing matrices computes A<sup>k</sup> quick via &Lambda;<sup>k</sup>.

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

&lambda; may be a "simple" eigenvalue or a "multiple" eigenvalue.  

[for multiple eigenvalues,] we want to know the eigenvalue's multiplicity.  

most eigenvalues have multiplicity of M = 1 (simple eigenvalues).    
then there is a single line of eigenvectors. [line created by a scalar like c in previous examples; cx still solves (A - &lambda;I)cx = 0]    
det(A - &lambda;I) does not have a double factor [&lambda;<sup>2</sup>]    

for exceptional matrices, an eigenvalue can be repeated.   
there are 2 different ways to count multiplicity.   
1. geometric multiplicity = GM  
GM counts the independent eigenvectors for &lambda;   
GM is dimension of the null space of (A - &lambda;I)  

[notice there may be multiple &lambda; that satisfy det (A-&lambda;I) = 0, e.g. 0,0 in the example below, but this isnt what this null space is about.  this is about after you use det(A - &lambda;I) = 0 to find your &lambda;s and are plugging one of them back into (A-&lambda;I), you find that there are a number of dimensions to the null space, i.e. more than one x eigenvector satisfies (A-&lambda;I)x = 0]   GM is about eigenvectors; null space of  A-&lambda;I.  AM is about eigenvalues; det A-&lambda;I.

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

example:

the terminal example can be improved. 

Lukas numbers (1, 3, 4, 7, 11, 18, ... ) use the same rule L<sub>k+2</sub> = L<sub>k+1</sub> + L<sub>k</sub> as Fibonacci (0,1, 1, 2, 3, 5, 8, 13, 21, ... ) = F<sub>k+2</sub> = F<sub>k+1</sub> + F<sub>k</sub>, but start at 1 rather than 0.

L<sub>100</sub> = &lambda;<sub>1</sub><sup>100</sup> + &lambda;<sub>2</sub><sup>100</sup>

as with Fibonacci u<sub>k+1</sub> = [ [ 1, 1 ], [1, 0 ] ] u<sub>k</sub> where u<sub>k</sub> = [ [L<sub>k+1</sub>], [L<sub>k</sub>] ] as with Fibonacci: 

u<sub>k+1</sub> = [ [ 1, 1 ], [1, 0 ] ] u<sub>k</sub> =  [ [ 1, 1 ], [1, 0 ] ] [ [L<sub>k+1</sub>], [L<sub>k</sub>] ] = [ [L<sub>k+2</sub>], [L<sub>k+1</sub>] ] = [ [L<sub>k+1</sub> + L<sub>k</sub>], [L<sub>k+1</sub>] ]

the eigenvalues and eigenvectors of A = [ [ 1, 1 ], [1, 0 ] ] still come from det (A - &lambda;I) = &lambda;<sup>2</sup> - &lambda; - 1 --> ( 1 +/- √5 ) / 2 via quadratic formula and eigenvectors come from (A - &lambda;<sub>1</sub>I)x<sub>2</sub> and (A - &lambda;<sub>2</sub>I)x<sub>2</sub>: x<sub>1</sub> = (&lambda;<sub>1</sub>, 1).T and x<sub>2</sub> = (&lambda;<sub>2</sub>, 1).T

u<sub>1</sub> = [L<sub>2</sub>, L<sub>1</sub>] = [3,1] = A<sup>0</sup>u<sub>1</sub>   
u<sub>k</sub> = [L<sub>k+1</sub>, L<sub>k</sub>] = [L<sub>k+1</sub>,L<sub>k</sub>] = A<sup>k-1</sup>u<sub>1</sub>  
u<sub>100</sub> = [L<sub>100+1</sub>, L<sub>100</sub>] = [L<sub>100+1</sub>,L<sub>100</sub>] = A<sup>100-1</sup>u<sub>1</sub> = X&Lambda;<sup>99</sup>X<sup>-1</sup>u<sub>1</sub> = X&Lambda;<sup>99</sup>c  
because u<sub>1</sub> = [3,1] = c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> = Xc, and so c = X<sup>-1</sup>u<sub>1</sub>  

with x<sub>1</sub> = [&lambda;<sub>1</sub>, 1],  x<sub>2</sub> = [&lambda;<sub>2</sub>, 1], &lambda;<sub>1</sub> = (1+√5)/2, and &lambda;<sub>2</sub> = (1-√5)/2, solve for c<sub>1</sub> = &lambda;<sub>1</sub> and c<sub>2</sub> = &lambda;<sub>2</sub>.


![\begin{align*}
u_1 =&
\begin{bmatrix}
3\\
1\\
\end{bmatrix}=
c_1x_1 + c_2x_2 = &lambda;_1x_1 + &lambda;_2x_2 = 
&lambda;_1\begin{bmatrix}
&lambda;_1\\
1\\
\end{bmatrix}+
&lambda;_2\begin{bmatrix}
&lambda;_2\\
1\\
\end{bmatrix}= 
(\frac{1+\sqrt{2}}{2})\begin{bmatrix}
(\frac{1+\sqrt{2}}{2})\\
1\\
\end{bmatrix}+
(\frac{1-\sqrt{2}}{2})\begin{bmatrix}
(\frac{1-\sqrt{2}}{2})\\
1\\
\end{bmatrix}\\=&
&lambda;_1\begin{bmatrix}
&lambda;_1\\
1\\
\end{bmatrix}+
&lambda;_2\begin{bmatrix}
&lambda;_2\\
1\\
\end{bmatrix} =
\begin{bmatrix}
&lambda;_1^2\\
&lambda;_1\\
\end{bmatrix}+
\begin{bmatrix}
&lambda;_2^2\\
&lambda;_2\\
\end{bmatrix} =
\begin{bmatrix}
&lambda;_1^2+&lambda;_2^2\\
&lambda;_1+&lambda;_2\\
\end{bmatrix}=
\begin{bmatrix}
trace_{A^2}\\
trace_A\\
\end{bmatrix}\\ \\
u_100=&
A_99 u_1=X&Lambda;^99X^{-1}u_1 
= X&Lambda;^99c
=\begin{bmatrix}
x_1&x_2\\
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2\\
\end{bmatrix}^99
\begin{bmatrix}
c_1\\
c_2\\
\end{bmatrix}=
\begin{bmatrix}
&lambda;_1&&lambda;_2\\
1&1
\end{bmatrix}
\begin{bmatrix}
&lambda;_1^99&\\
&&lambda;_2^99\\
\end{bmatrix}
\begin{bmatrix}
&lambda;_1\\
&lambda;_2\\
\end{bmatrix}=
\begin{bmatrix}
&lambda;_1&&lambda;_2\\
1&1
\end{bmatrix}
\begin{bmatrix}
&lambda;_1^100\\
&lambda;_2^100\\
\end{bmatrix}=
\begin{bmatrix}
&lambda;_1^101+&lambda;_2^101\\
&lambda;_1^100+&lambda;_2^100\\
\end{bmatrix}\\
L_100 =& u_100[1] = &lambda;_1^100+&lambda;_2^100
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au_1+%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A3%5C%5C%0A1%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0Ac_1x_1+%2B+c_2x_2+%3D+%26lambda%3B_1x_1+%2B+%26lambda%3B_2x_2+%3D+%0A%26lambda%3B_1%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5C%5C%0A1%5C%5C%0A%5Cend%7Bbmatrix%7D%2B%0A%26lambda%3B_2%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_2%5C%5C%0A1%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%0A%28%5Cfrac%7B1%2B%5Csqrt%7B2%7D%7D%7B2%7D%29%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7B1%2B%5Csqrt%7B2%7D%7D%7B2%7D%29%5C%5C%0A1%5C%5C%0A%5Cend%7Bbmatrix%7D%2B%0A%28%5Cfrac%7B1-%5Csqrt%7B2%7D%7D%7B2%7D%29%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7B1-%5Csqrt%7B2%7D%7D%7B2%7D%29%5C%5C%0A1%5C%5C%0A%5Cend%7Bbmatrix%7D%5C%5C%3D%26%0A%26lambda%3B_1%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5C%5C%0A1%5C%5C%0A%5Cend%7Bbmatrix%7D%2B%0A%26lambda%3B_2%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_2%5C%5C%0A1%5C%5C%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5E2%5C%5C%0A%26lambda%3B_1%5C%5C%0A%5Cend%7Bbmatrix%7D%2B%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_2%5E2%5C%5C%0A%26lambda%3B_2%5C%5C%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5E2%2B%26lambda%3B_2%5E2%5C%5C%0A%26lambda%3B_1%2B%26lambda%3B_2%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0Atrace_%7BA%5E2%7D%5C%5C%0Atrace_A%5C%5C%0A%5Cend%7Bbmatrix%7D%5C%5C+%5C%5C%0Au_100%3D%26%0AA_99+u_1%3DX%26Lambda%3B%5E99X%5E%7B-1%7Du_1+%0A%3D+X%26Lambda%3B%5E99c%0A%3D%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%5C%5C%0A%5Cend%7Bbmatrix%7D%5E99%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%5C%5C%0Ac_2%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%26lambda%3B_2%5C%5C%0A1%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5E99%26%5C%5C%0A%26%26lambda%3B_2%5E99%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5C%5C%0A%26lambda%3B_2%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%26lambda%3B_2%5C%5C%0A1%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5E100%5C%5C%0A%26lambda%3B_2%5E100%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5E101%2B%26lambda%3B_2%5E101%5C%5C%0A%26lambda%3B_1%5E100%2B%26lambda%3B_2%5E100%5C%5C%0A%5Cend%7Bbmatrix%7D%5C%5C%0AL_100+%3D%26+u_100%5B1%5D+%3D+%26lambda%3B_1%5E100%2B%26lambda%3B_2%5E100%0A%5Cend%7Balign%2A%7D%0A)

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/108013583-fe4d5780-6fd9-11eb-9a5c-738d3feb49b7.png">


second example:

find the inverse and eigenvalues and determinant of matrix A.  describe the eigenvector matrix X that gives X<sup>-1</sup>AX = &Lambda; 

A = 5 * eye(4) - ones(4) = 4s down the diagonal and -1's everywhere else

the eigenvalues of eye = 1,1,1,1  
the eigenvalues of 5 * eye = 5,5,5,5  

the eigenvalues of ones:   
its rank is certainly 1  
so 3 eigenvalues are zero  
the trace is 4  
so the 4th eigenvalue is 4

det A = det ( 5 • eye(4) ) - det ( ones(4) ) =  5•5•5•5 - 4•0•0•0 = 1•5•5•5 = difference of the products of eigenvalues  

the determinant of A is 125 = 1 • 5 • 5 • 5 

A - &lambda;<sub>1</sub> • I = 4 * eye(4) - ones(4) = 3s down diagonal and -1s everywhere else.  the diagonal is reduced by 1 because &lambda;<sub>1</sub> = 1.   
thus, the eigenvector for &lambda;<sub>1</sub> = 1 is x<sub>1</sub> =  (1,1,1,1) or (c,c,c,c).
the other 3 eigenvectors for &lambda;s<sub>2</sub>,&lambda;s<sub>3</sub>, &lambda;s<sub>4</sub> = 5 are perpendicular to x<sub>1</sub> because A is symmetric.  The nicest eigenvector matrix X is the symmetric orthogonal matrix, Hadamard matrix H.  The (1/2) factor produces unit column vectors.  H<sup>T</sup> = H<sup>-1</sup>

the eigenvalues of A<sup>-1</sup> are 1, 1/5, 1/5, 1/5 = 1/&lambda;<sub>1</sub>, 1/&lambda;<sub>2</sub>, 1/&lambda;<sub>3</sub>, 1/&lambda;<sub>4</sub>.

the eigenvectors are not changed by inversion.  so A<sup>-1</sup> = H&Lambda;<sup>-1</sup>H<sup>-1</sup>.  

A<sup>-1</sup> = (1/5) • ( (eye(4) + ones(4) ) which has 2s down diagonal and 1s everywhere else. 

A is a rank-one change from 5•I = 5*eye(4)   
so A<sup>-1</sup> is a rank one change from I / 5


![\begin{align*}
A = &
5*\begin{bmatrix}
1&&&\\
&1&&\\
&&1&\\
&&&1
\end{bmatrix}-
\begin{bmatrix}
1&1&1&1\\
1&1&1&1\\
1&1&1&1\\
1&1&1&1
\end{bmatrix}=
\begin{bmatrix}
+4&-1&-1&-1\\
-1&+4&-1&-1\\
-1&-1&+4&-1\\
-1&-1&-1&+4
\end{bmatrix}\\
X = &
\frac{1}{2}*\begin{bmatrix}
+1&+1&+1&+1\\
+1&-1&+1&-1\\
+1&+1&-1&-1\\
+1&-1&-1&+1
\end{bmatrix} = H^T =H^{-1}\\
A^{-1}= & 
\frac{1}{5}*\begin{bmatrix}
2&1&1&1\\
1&2&1&1\\
1&1&2&1\\
1&1&1&2
\end{bmatrix} 
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%3D+%26%0A5%2A%5Cbegin%7Bbmatrix%7D%0A1%26%26%26%5C%5C%0A%261%26%26%5C%5C%0A%26%261%26%5C%5C%0A%26%26%261%0A%5Cend%7Bbmatrix%7D-%0A%5Cbegin%7Bbmatrix%7D%0A1%261%261%261%5C%5C%0A1%261%261%261%5C%5C%0A1%261%261%261%5C%5C%0A1%261%261%261%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A%2B4%26-1%26-1%26-1%5C%5C%0A-1%26%2B4%26-1%26-1%5C%5C%0A-1%26-1%26%2B4%26-1%5C%5C%0A-1%26-1%26-1%26%2B4%0A%5Cend%7Bbmatrix%7D%5C%5C%0AX+%3D+%26%0A%5Cfrac%7B1%7D%7B2%7D%2A%5Cbegin%7Bbmatrix%7D%0A%2B1%26%2B1%26%2B1%26%2B1%5C%5C%0A%2B1%26-1%26%2B1%26-1%5C%5C%0A%2B1%26%2B1%26-1%26-1%5C%5C%0A%2B1%26-1%26-1%26%2B1%0A%5Cend%7Bbmatrix%7D+%3D+H%5ET+%3DH%5E%7B-1%7D%5C%5C%0AA%5E%7B-1%7D%3D+%26+%0A%5Cfrac%7B1%7D%7B5%7D%2A%5Cbegin%7Bbmatrix%7D%0A2%261%261%261%5C%5C%0A1%262%261%261%5C%5C%0A1%261%262%261%5C%5C%0A1%261%261%262%0A%5Cend%7Bbmatrix%7D+%0A%5Cend%7Balign%2A%7D%0A)


problems

4. TF if columns of X (eigenvectors of A) are linearly independent,  ...
... A is invertible. FALSE because eigenvalues can still be zero in which case Ax = 0 which means at least one of the eigenvalues is in the null space.  
... A is dagonalizable.  TRUE.  the matrix of eigenvectors X has an inverse   
... X is invertible.  TRUE.  X has full rank and so is invertible.   
... X is diagonalizable.  FALSE.  to know this we need X's eigenvalues: X could have repeated eigenvalues and therefore a non computable set of eigenvectors.

5. If eigenvectors of A are columns of I, then A is diagonal:  X = I = X<sup>-1<sup> means A = X&Lambda;X<sup>-1</sup> = &Lambda;

6. If eigenvector matrix X is triangular then X<sup>-1</sup> is triangular and A is triangular.   Since &Lambda;X is triangular, two triangulars multiplying = triangular. 

if X diagonalizes A then all multiples of X diagaonlize A since X is the null set of A-&lambda;I.  all non-zero multiples of X also diagonalize A<sup>-1</sup>

9. if G<sub>k+2</sub> is the average of 2 previous numbers G<sub>k+1</sub> and G<sub>k</sub>, can use the same process as with Fibonacci to digaonalize A = [ [ .5, .5 ], [ 1, 0 ] ]

<img width="522" alt="image" src="https://user-images.githubusercontent.com/38410965/108092889-275a0080-704b-11eb-9f7b-fb40a9cf34b3.png">

11.  TF if eigenvalues of A are 2,2,5 then A is CERTAINLY ...    
... invertible.  TRUE.  no zero eigenvalues. this is true because if eigenvalues = 0 then A-&lambda;I = A and if det (A) ≠ 0 then invertible.  
... diagonalizable.  FALSE.  repeated eigenvalue 2 may have only one line of eigenvectors.  
... not diagonalizable.  FALSE.  repeated eigenvalue 2 may have a full set of eigenvectors.  

GM counts the independent eigenvectors for eigenvalue.  Then GM is the dimension of the null space of A - &lambda;I

AM counts the repetitions of an eigenvalue among eigenvalues.  look at the roots of det (A-&lambda;I)

TF if the ONLY eigenvector of A is a multiple of (1,4) then A has ...   
... no inverse.  FALSE.  dont kow if eigenvalues are zero.   
... a repeated eigenvalue.  TRUE. an eigenvector is missing which can only happen for a repeated eigenvalue.   
... no diagonalizable X&Lambda;X<sup>-1</sup>  TRUE.  we konw there is only one line of eigenvectors.  there are not enough eigenvectors to fill the eigenvector matrix X.   

14. the matrix A = [ [ 3,1 ], [ 0,3 ] ] is not diagonalizable because the rank of A - &lambda;I is one.  What to change to make it diagonalizable?  
Changing any entry except a(1,2) = 1 would make it diagonalizable as the new A will have different eigenvalues.   
The rank of A - 3I = one.  Since rank + null space dim must = n = 2, then the null space has dim = 2 - 1 = 1 and therefore there is not a complete set of 2 eigenvectors for the &lambda; = 3 eigenvalue.  

markov matrices have at least one eigenvalue = 1 and so A<sup>k</sup> will not go to zero as k goes to infnity.  if a matrix has eigenvalues that are all < 1 then A<sup>k</sup> will go to zero as k goes to infnity

diagonalize A = [ [ .6, .4 ], [ .4, .6 ] ]   
since we know it is a Markov, we know one eigenvalue = 1  
using trace and determinant rules:  &lambda;<sub>1</sub> + &lambda;<sub>2</sub> = 1.2 = trace and det A = &lambda;<sub>1</sub> • &lambda;<sub>2</sub> = 0.2   
thus, &lambda;<sub>1</sub> = 1 then &lambda;<sub>2</sub> = .2   
X can be solved to [ [ 1,1], [ 1,-1 ] ] and Xinv solved to 0.5 • [ [ 1,1], [ 1,-1 ] ]  
at lmit A<sup>k</sup> k to infinity, &lambda;<sub>2</sub><sup>k</sup> = 0  
so &Lambda;<sup>k</sup> = [ [ 1,0], [ 0,0 ] ] with k = infinity  
and A<sup>infinity</sup> = 0.5 • [ [ 1,1], [ 1,-1 ] ]


17. find &Lambda; and X to diagonalize A in problem 15.  What is A<sup>10</sup>u<sub>0</sub> for these u<sub>0</sub>?  

for &lambda;<sub>1</sub> = 0.3, the eigenvector is given by the null space of (A - 0.3 • I) or the span of (-3,1).T  
for &lambda;<sub>2</sub> = 0.9, the eigenvector is given by the null space of (A - 0.9 • I) or the span of (3,1).T  

this span enables us to take a linear combination of eigenvectors to express u<sub>0</sub> in the form of eigenvectors and a scalar that would ordinarily be found in special solutions of null space.

<img width="522" alt="image" src="https://user-images.githubusercontent.com/38410965/108105123-36947a80-705a-11eb-9e01-41742ef0454a.png">

to evaluate A<sup>10</sup>u<sub>0</sub>, decompose aka factor u<sub>0</sub> in a basis provided by the eigenvectors of A.  
c<sub>1</sub> and c<sub>2</sub> will scale x<sub>1</sub> and x<sub>2</sub> to express each u<sub>0</sub> as a linear combination of the x's.  XC = that linear combination = U<sub>0</sub>

u<sub>0_1</sub> = (3,1).T = c<sub>1_1</sub>x<sub>1</sub> + c<sub>2_1</sub>x<sub>2</sub>   
u<sub>0_2</sub> = (3,1).T = c<sub>1_2</sub>x<sub>1</sub> + c<sub>2_2</sub>x<sub>2</sub>   
u<sub>0_3</sub> = (3,1).T = c<sub>1_3</sub>x<sub>1</sub> + c<sub>2_3</sub>x<sub>2</sub>   

since U<sub>0</sub> = [u<sub>0_1</sub>, u<sub>0_2</sub>, u<sub>0_3</sub>] = XC, then C = X<sup>-1</sup>U<sub.0</sub> which is named C<sub>values</sub> here for clarity.

![\begin{align*}
A^ku_0 =&A^kXc = X&Lambda;^kX^{-1}u_0 = X&Lambda;^kX^{-1}Xc = X&Lambda;^kc\\
A^kU_0 =&A^kXC = X&Lambda;^kX^{-1}U_0 = X&Lambda;^kX^{-1}XC = X&Lambda;^kC \\
\begin{bmatrix}
a_1&a_2\\
\end{bmatrix}^{k}
\begin{bmatrix}
u_1&u_2&u_3\\
\end{bmatrix}=&
\begin{bmatrix}
a_1&a_2\\
\end{bmatrix}^{k}
\begin{bmatrix}
x_1&x_2\\
\end{bmatrix}
\begin{bmatrix}
c_1&c_2&c_3\\
\end{bmatrix}\\
\begin{bmatrix}
x_1&x_2\\
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2\\
\end{bmatrix}^k
\begin{bmatrix}
x_1&x_2\\
\end{bmatrix}^{-1}
\begin{bmatrix}
u_1&u_2&u_3\\
\end{bmatrix}=&
\begin{bmatrix}
x_1&x_2\\
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2\\
\end{bmatrix}^k
\begin{bmatrix}
x_1&x_2\\
\end{bmatrix}^{-1}
\begin{bmatrix}
x_1&x_2\\
\end{bmatrix}
\begin{bmatrix}
c_1&c_2&c_3\\
\end{bmatrix}=
\begin{bmatrix}
x_1&x_2\\
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2\\
\end{bmatrix}^k
\begin{bmatrix}
c_1&c_2&c_3\\
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA%5Eku_0+%3D%26A%5EkXc+%3D+X%26Lambda%3B%5EkX%5E%7B-1%7Du_0+%3D+X%26Lambda%3B%5EkX%5E%7B-1%7DXc+%3D+X%26Lambda%3B%5Ekc%5C%5C%0AA%5EkU_0+%3D%26A%5EkXC+%3D+X%26Lambda%3B%5EkX%5E%7B-1%7DU_0+%3D+X%26Lambda%3B%5EkX%5E%7B-1%7DXC+%3D+X%26Lambda%3B%5EkC+%5C%5C%0A%5Cbegin%7Bbmatrix%7D%0Aa_1%26a_2%5C%5C%0A%5Cend%7Bbmatrix%7D%5E%7Bk%7D%0A%5Cbegin%7Bbmatrix%7D%0Au_1%26u_2%26u_3%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Aa_1%26a_2%5C%5C%0A%5Cend%7Bbmatrix%7D%5E%7Bk%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%26c_2%26c_3%5C%5C%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%5C%5C%0A%5Cend%7Bbmatrix%7D%5Ek%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%5C%5C%0A%5Cend%7Bbmatrix%7D%5E%7B-1%7D%0A%5Cbegin%7Bbmatrix%7D%0Au_1%26u_2%26u_3%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%5C%5C%0A%5Cend%7Bbmatrix%7D%5Ek%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%5C%5C%0A%5Cend%7Bbmatrix%7D%5E%7B-1%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%26c_2%26c_3%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%5C%5C%0A%5Cend%7Bbmatrix%7D%5Ek%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%26c_2%26c_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/108109458-e4565800-705f-11eb-8e15-a1721e8faf3b.png">

20.  for diagonalizable matrices A = X&Lambda;X<sup>-1</sup>, determinants of both sides prove that det A = det &Lambda; = &lambda;<sub>1</sub>&lambda;<sub>2</sub>...&lambda;<sub>n-1</sub>&lambda;<sub>n</sub>:

det A = (det X)(det&Lambda;)(det X<sup>-1</sup>) = det&Lambda; = &lambda;<sub>1</sub>&lambda;<sub>2</sub>...&lambda;<sub>n-1</sub>&lambda;<sub>n</sub> because (det X)(det X<sup>-1</sup>)=1 since X has independent columns and because det X = 1/(det X).

trace XY = trace YX

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108115937-dbb64f80-7068-11eb-9b11-e0d693c3bec7.png">

now if choose Y = &Lambda;X<sup>-1</sup>, then X&Lambda;X<sup>-1</sup> has the same trace as &Lambda;X<sup>-1</sup>X = &Lambda; which proves that the trace of A = trace of &Lambda; = sum of eigenvalues.

again this assume that A is diagonalizable.  

for a general m x m matrix the product AB has elements given by ∑<sub>k=1</sub><sup>m</sup>a<sub>ik</sub>b<sub>kj</sub> and the product BA has the terms given by ∑<sub>k=1</sub><sup>m</sup>b<sub>ik</sub>a<sub>kj</sub>.  so the trace AB is given by summing diagonal terms of AB = Tr(AB) = ∑<sub>i=1</sub><sup>m</sup>(∑<sub>k=1</sub><sup>m</sup>a<sub>ik</sub>b<sub>ki</sub>) while the trace BA is given by summing the diagonal terms of BA or Tr(BA) = ∑<sub>i=1</sub><sup>m</sup>(∑<sub>k=1</sub><sup>m</sup>b<sub>ik</sub>b<sub>ki</sub>) and these expressions are euqal which shows the traces are equal. 


if A = X&Lambda;X<sup>-1</sup> and B is blockform as shown, then decompose (factor) B as shown.   
thus, eigenvalue matrix for block represents A and 2A with &Lambda; and 2&Lambda; and the eigenvector matrix of B is their respective X's which are the same since A and 2A have the same eigenvectors. 

![\begin{align*}
B=&
\begin{bmatrix}
A&0\\
0&2A
\end{bmatrix}=
\begin{bmatrix}
X&Lambda;X^{-1}&0\\
0&X(2&Lambda;)X^{-1}
\end{bmatrix}=
\begin{bmatrix}
X&0\\
0&X
\end{bmatrix}
\begin{bmatrix}
&lambda;&0\\
0&2&lambda;\\
\end{bmatrix}
\begin{bmatrix}
X^{-1}&0\\
0&X^{-1}
\end{bmatrix} = 
\begin{bmatrix}
X&0\\
0&X
\end{bmatrix}
\begin{bmatrix}
&lambda;X^{-1}&0\\
0&2&lambda;X^{-1}\\
\end{bmatrix}=
\begin{bmatrix}
X&lambda;X^{-1}&0\\
0&X(2&lambda;)X^{-1}\\
\end{bmatrix}=
\begin{bmatrix}
A&0\\
0&2A
\end{bmatrix}\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AB%3D%26%0A%5Cbegin%7Bbmatrix%7D%0AA%260%5C%5C%0A0%262A%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AX%26Lambda%3BX%5E%7B-1%7D%260%5C%5C%0A0%26X%282%26Lambda%3B%29X%5E%7B-1%7D%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AX%260%5C%5C%0A0%26X%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B%260%5C%5C%0A0%262%26lambda%3B%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AX%5E%7B-1%7D%260%5C%5C%0A0%26X%5E%7B-1%7D%0A%5Cend%7Bbmatrix%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0AX%260%5C%5C%0A0%26X%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3BX%5E%7B-1%7D%260%5C%5C%0A0%262%26lambda%3BX%5E%7B-1%7D%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AX%26lambda%3BX%5E%7B-1%7D%260%5C%5C%0A0%26X%282%26lambda%3B%29X%5E%7B-1%7D%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AA%260%5C%5C%0A0%262A%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cend%7Balign%2A%7D)

24. for all 4 x 4 matrices A that are diagonalized by the same fixed eigenvector matrix X, A forms a subspace = cA and A<sub>1</sub> + A<sub>2</sub> for which all have the same X.  

S set = { A | X&Lambda;X<sup>-1</sup>} for a given X.  then if A<sub>1</sub> and A<sub>2</sub> are in S we know:  

A<sub>1</sub> + A<sub>2</sub> = X&Lambda;<sub>1</sub>X<sup>-1</sup> + X&Lambda;<sub>2</sub>X<sup>-1</sup> = X(&Lambda;<sub>1</sub> + &Lambda;<sub>2</sub>)X<sup>-1</sup>

A<sub>1</sub> + A<sub>2</sub> is in S  
if A<sub>1</sub> element of S then cA<sub>1</sub> = X(c&Lambda;<sub>1</sub>)X<sup>-1</sup> is element of S.  
S is a subspace thusly.  



when X = Identity, the As with those eigenvectors give the subspace of diagonal matrices.  the dim of that matrix space is 4 since the matrices are 4 x 4.  

25.  A<sup>2</sup> = A  
A multiplies each column of A  
which of the 4 subspaces contains the eigenvectors with &lambda; = 1?  [column space of A]
which subspace contains the eigenvectors with &lambda; = 0?  [null space of A]
from the dim of those subspaces, A has a full set of independent eigenvectors so the matrix A<sup>2</sup> = A can be diagonalized.   

the column space of A contains the eigenvectors with &lambda; = 1: the columns of A has dim = n = number of columns of X since in order to be diagonalized, X's columns must be independent.  

a &lambda; = 0 implies that Ax = 0 when x is not = zero.which is the null space of A or else it implies that A is singular which it is not.  A is not singular since (A-&lambda;I)x = 0 but (A-zero•I)x ≠ 0 which would prevents singularity.   
so &lambda; ≠ 0 imparts invertibility.  
and &lambda; = 0 only occurs in null space not in column space. 

wax:  
suppose A<sup>2</sup> = A ...  
then the column space of A contains eigenvectors with &lambda; = 1  
in fact, all vectors in column space of A are eigenvectors with eigenvalues = 1.  
the vectors with &lambda; = 0 lie in the null space and from the 1st fundamental theorem of linear algebra, the dim of the col space plus dim of null space = n.  [col space contains independent columns; null space contains dependent ones]  
A will be diagonalizable since we guaranteed to have enough n eigenvectors. 

if A has cols x<sub>1</sub> ... x<sub>n</sub> then col by col A<sup>2</sup>=A means every Ax<sub>i</sub> = x<sub>i</sub>.  {because x = A in that]  All vectors in col space combinations of the x<sub>i</sub> columns are eigenvectors with &lambda; = 1.  
always null space has &lambda; = 0.  A might have dependent columns; so there could be less than n eigenvectors with &lambda; = 1.  dimenions of those spaces columns and null add to n.

26.  Ax = &lambda;x 
if &lambda; = 0 then x is in the null space of A.
if &lambda; ≠ 0, then x is in the columns space of A.  
those spaces have dim n-r and r totalling n.   
if they total n, why doesnt every square matrix have n linearly independent eigenvectors?

null space and column space overlap.
[null space is the set of coefficients that combine the columns and column space is the columns]
x that is the null space coefficients can be in the column space too.  
there might also NOT be r independent eigenvectors in the column space. 

when A has non-empty null space, then n-r > 0 non linearly independent eigenvectors.  
if x is not in the null space of A, there is no guarantee that Ax = &lambda;x for any constant &lambda;   
thus, the r vectors in the column space of A may have no basis such that Ax = &lambda;x.  
In addiont the null space and column space can overlap if one of the null space vectors is in fact a column of the original A. 

[eigenvectors are in the null space of A-&lambda;•I but if &lambda; = 0 then that eigenvector is in the null space of A too]

29. the same X diagonalizes both A and B. they have the same eigenvectors in A = X&Lambda;<sub>1</sub>X<sup>-1</sup> and B = X&Lambda;<sub>2</sub>X<sup>-1</sup>.  prove AB = BA.
AB = X&Lambda;<sub>1</sub>X<sup>-1</sup>X&Lambda;<sub>2</sub>X<sup>-1</sup> = X&Lambda;<sub>1</sub>&Lambda;<sub>2</sub>X<sup>-1</sup> = X&Lambda;<sub>2</sub>&Lambda;<sub>1</sub>X<sup>-1</sup> = X&Lambda;<sub>2</sub>X<sup>-1</sup>X&Lambda;<sub>1</sub>X<sup>-1</sup> = BA since diagonal matrices commute: &Lambda;<sub>1</sub>&Lambda;<sub>2</sub> = &Lambda;<sub>2</sub>&Lambda;<sub>1</sub>

30. if A = U as shown and determinant of A - &lambda; • I = (&lambda; - a)(&lambda; - d) then Cayley Hamilton Theorem says that (A - a • I)(A - b • I) = 0 or that the respective (A - &lambda;<sub>1</sub> • I) and (A - &lambda;<sub>2</sub> • I) are perpendicular which makes sense since we have been saying that this diagonalization creates perpendicular axes.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108156630-03c8a180-70af-11eb-8c51-c794b0f562a7.png">

works on A not U as well

34.  the nth power of rotation through &theta; is a rotation through n &theta;

prove this formular by diagonalizing A = X&Lambda;X<sup>-1</sup>.

the eigenvalues are:  
&lambda;<sub>1</sub> = e<sup>i&theta;</sup>  
&lambda;<sub>2</sub> = e<sup>-i&theta;</sup>  

verify the trace = 2cos&theta; and determinant = 1

the eigenvector columns are:
(1,i).T and (i,1).T

Euler's formular is:  
e<sup>i&theta;</sup> = cos&theta; + isin&theta;  
e<sup>-i&theta;</sup> = cos&theta; - isin&theta;

geometrically then, n rotations by &theta; give one rotation through n&theta;:

![\begin{align*}
A&=
\begin{bmatrix}
cos\theta&-sin\theta\\
sin\theta&cos\theta
\end{bmatrix}\\
\\
determinant:&
\\
|A-&lambda;I|&=
det\begin{bmatrix}
cos\theta-\lambda&-sin\theta\\
sin\theta&cos\theta-\lambda
\end{bmatrix}\\
&=\lambda^2 + cos^2\theta - 2&lambda;cos\theta-sin^2\theta \\
&=(\lambda - (cos\theta + isin\theta))(\lambda -(cos\theta - isin\theta))\\
\\
because&\\
&=\lambda^2 -\lambda(cos\theta + isin\theta)-\lambda(cos\theta - isin\theta) + (cos\theta+sin\theta)(cos\theta-sin\theta)\\
&=\lambda^2 -2&lambda;cos\theta - i&lambda;sin\theta + i&lambda;sin\theta+ cos^2\theta-sin^2\theta\\
&=\lambda^2 -2&lambda;cos\theta + cos^2\theta-sin^2\theta\\
&=\lambda^2 + cos^2\theta-2&lambda;cos\theta -sin^2\theta\\
\\
eigenvalues:&\\
\\
|A-&lambda;I|&=0\\
where&\\
\lambda_1&=(cos\theta + i sin\theta) = e^{i\theta}\\
\lambda_2&=(cos\theta - i sin\theta) =e^{-i\theta}\\
\\
confirming&\\
trace&\\
\lambda_1+\lambda_2&=e^{i\theta}+e^{-i\theta}=2cos\theta = d_1+d_2\\
\\
determinant&\\
\lambda_1\lambda_2&=cos^2\theta-(-sin^2theta)=cos^2\theta+sin^2theta=1\\
\\
eigenvectors:\\
\\
since&\\
A-&lambda;_1I&=
\begin{bmatrix}
cos\theta-e^{i\theta}&-sin\theta\\
sin\theta&cos\theta-e^{i\theta}
\end{bmatrix}
=\begin{bmatrix}
cos\theta-(cos\theta + i sin\theta)&-sin\theta\\
sin\theta&cos\theta-(cos\theta + i sin\theta)
\end{bmatrix}
=\begin{bmatrix}
-i sin\theta&-sin\theta\\
sin\theta&-i sin\theta
\end{bmatrix}\\
x_1&=\begin{bmatrix}
1\\
-i
\end{bmatrix}\\
\\
and&\\
A-&lambda;_2I&=
\begin{bmatrix}
cos\theta-e^{-i\theta}&-sin\theta\\
sin\theta&cos\theta-e^{-i\theta}
\end{bmatrix}
=\begin{bmatrix}
cos\theta-(cos\theta - i sin\theta)&-sin\theta\\
sin\theta&cos\theta-(cos\theta - i sin\theta)
\end{bmatrix}
=\begin{bmatrix}
+i sin\theta&-sin\theta\\
sin\theta&+i sin\theta
\end{bmatrix}\\
x_1&=\begin{bmatrix}
1\\
i
\end{bmatrix}\\
\\
diagonalizing:&
\\
X&=
\begin{bmatrix}
1&1\\
-i&i
\end{bmatrix}\\
\Lambda&=
\begin{bmatrix}
e^{i\theta}&\\
&e^{-i\theta}
\end{bmatrix}\\
X^{-1}&=
\frac{1}{2i}\begin{bmatrix}
i&-1\\
i&1
\end{bmatrix}\\
\\
powers&\\
\\
A^k&=X&Lambda;X^{-1}=
\begin{bmatrix}
1&1\\
-i&i
\end{bmatrix}
\begin{bmatrix}
e^{i\theta}&\\
&e^{-i\theta}
\end{bmatrix}^k
\frac{1}{2i}\begin{bmatrix}
i&-1\\
i&1
\end{bmatrix}=
\begin{bmatrix}
1&1\\
-i&i
\end{bmatrix}
\begin{bmatrix}
e^{ik\theta}&\\
&e^{-ik\theta}
\end{bmatrix}
\frac{1}{2i}\begin{bmatrix}
i&-1\\
i&1
\end{bmatrix}=
\begin{bmatrix}
1*e^{ik\theta}&1*e^{-ik\theta}\\
-i*e^{ik\theta}&i*e^{-ik\theta}
\end{bmatrix}
\frac{1}{2i}\begin{bmatrix}
i&-1\\
i&1
\end{bmatrix}\\
\\&= 
\frac{1}{2i}
\begin{bmatrix}
i*1*e^{ik\theta}+i*1*e^{-ik\theta}&-1*1*e^{ik\theta}+1*1*e^{-ik\theta}\\
i*(-i)*e^{ik\theta}+i*i*e^{-ik\theta}&(-1)*-i*e^{ik\theta}+1*i*e^{-ik\theta}
\end{bmatrix}
\\&= 
\frac{1}{2i}
\begin{bmatrix}
i*e^{ik\theta}+i*e^{-ik\theta}&-e^{ik\theta}+e^{-ik\theta}\\
(+1)*e^{ik\theta}+(-1)*e^{-ik\theta}&i*e^{ik\theta}+i*e^{-ik\theta}
\end{bmatrix}
\\&= 
\begin{bmatrix}
\frac{i*e^{ik\theta}+i*e^{-ik\theta}}{2i}&\frac{-e^{ik\theta}+e^{-ik\theta}}{2i}\\
\frac{(+1)*e^{ik\theta}+(-1)*e^{-ik\theta}}{2i}&\frac{i*e^{ik\theta}+i*e^{-ik\theta}}{2i}
\end{bmatrix}
\\&= 
\begin{bmatrix}
\frac{e^{ik\theta}+e^{-ik\theta}}{2}&\frac{e^{-ik\theta}-e^{ik\theta}}{2i}\\
\frac{e^{ik\theta}-e^{-ik\theta}}{2i}&\frac{e^{ik\theta}+e^{-ik\theta}}{2}
\end{bmatrix}
\\&= 
\begin{bmatrix}
\frac{(cos^k\theta+isin^k\theta)+(cos^k\theta-isin^k\theta)}{2}&\frac{(cos^k\theta-isin^k\theta)-(cos^k\theta+isin^k\theta)}{2i}\\
\frac{(cos^k\theta+isin^k\theta)-(cos^k\theta-isin^k\theta)}{2i}&\frac{(cos^k\theta+isin^k\theta)+(cos^k\theta-isin^k\theta)}{2}
\end{bmatrix}
\\&= 
\begin{bmatrix}
\frac{2cos^k\theta}{2}&\frac{-2isin^k\theta}{2i}\\
\frac{2isin^k\theta}{2i}&\frac{2cos^k\theta}{2}
\end{bmatrix}
\\&= 
\begin{bmatrix}
\cos^k\theta&-sin^k\theta\\
\sin^k\theta&\cos^k\theta
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Acos%5Ctheta%26-sin%5Ctheta%5C%5C%0Asin%5Ctheta%26cos%5Ctheta%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Adeterminant%3A%26%0A%5C%5C%0A%7CA-%26lambda%3BI%7C%26%3D%0Adet%5Cbegin%7Bbmatrix%7D%0Acos%5Ctheta-%5Clambda%26-sin%5Ctheta%5C%5C%0Asin%5Ctheta%26cos%5Ctheta-%5Clambda%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3D%5Clambda%5E2+%2B+cos%5E2%5Ctheta+-+2%26lambda%3Bcos%5Ctheta-sin%5E2%5Ctheta+%5C%5C%0A%26%3D%28%5Clambda+-+%28cos%5Ctheta+%2B+isin%5Ctheta%29%29%28%5Clambda+-%28cos%5Ctheta+-+isin%5Ctheta%29%29%5C%5C%0A%5C%5C%0Abecause%26%5C%5C%0A%26%3D%5Clambda%5E2+-%5Clambda%28cos%5Ctheta+%2B+isin%5Ctheta%29-%5Clambda%28cos%5Ctheta+-+isin%5Ctheta%29+%2B+%28cos%5Ctheta%2Bsin%5Ctheta%29%28cos%5Ctheta-sin%5Ctheta%29%5C%5C%0A%26%3D%5Clambda%5E2+-2%26lambda%3Bcos%5Ctheta+-+i%26lambda%3Bsin%5Ctheta+%2B+i%26lambda%3Bsin%5Ctheta%2B+cos%5E2%5Ctheta-sin%5E2%5Ctheta%5C%5C%0A%26%3D%5Clambda%5E2+-2%26lambda%3Bcos%5Ctheta+%2B+cos%5E2%5Ctheta-sin%5E2%5Ctheta%5C%5C%0A%26%3D%5Clambda%5E2+%2B+cos%5E2%5Ctheta-2%26lambda%3Bcos%5Ctheta+-sin%5E2%5Ctheta%5C%5C%0A%5C%5C%0Aeigenvalues%3A%26%5C%5C%0A%5C%5C%0A%7CA-%26lambda%3BI%7C%26%3D0%5C%5C%0Awhere%26%5C%5C%0A%5Clambda_1%26%3D%28cos%5Ctheta+%2B+i+sin%5Ctheta%29+%3D+e%5E%7Bi%5Ctheta%7D%5C%5C%0A%5Clambda_2%26%3D%28cos%5Ctheta+-+i+sin%5Ctheta%29+%3De%5E%7B-i%5Ctheta%7D%5C%5C%0A%5C%5C%0Aconfirming%26%5C%5C%0Atrace%26%5C%5C%0A%5Clambda_1%2B%5Clambda_2%26%3De%5E%7Bi%5Ctheta%7D%2Be%5E%7B-i%5Ctheta%7D%3D2cos%5Ctheta+%3D+d_1%2Bd_2%5C%5C%0A%5C%5C%0Adeterminant%26%5C%5C%0A%5Clambda_1%5Clambda_2%26%3Dcos%5E2%5Ctheta-%28-sin%5E2theta%29%3Dcos%5E2%5Ctheta%2Bsin%5E2theta%3D1%5C%5C%0A%5C%5C%0Aeigenvectors%3A%5C%5C%0A%5C%5C%0Asince%26%5C%5C%0AA-%26lambda%3B_1I%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Acos%5Ctheta-e%5E%7Bi%5Ctheta%7D%26-sin%5Ctheta%5C%5C%0Asin%5Ctheta%26cos%5Ctheta-e%5E%7Bi%5Ctheta%7D%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0Acos%5Ctheta-%28cos%5Ctheta+%2B+i+sin%5Ctheta%29%26-sin%5Ctheta%5C%5C%0Asin%5Ctheta%26cos%5Ctheta-%28cos%5Ctheta+%2B+i+sin%5Ctheta%29%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A-i+sin%5Ctheta%26-sin%5Ctheta%5C%5C%0Asin%5Ctheta%26-i+sin%5Ctheta%0A%5Cend%7Bbmatrix%7D%5C%5C%0Ax_1%26%3D%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-i%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Aand%26%5C%5C%0AA-%26lambda%3B_2I%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Acos%5Ctheta-e%5E%7B-i%5Ctheta%7D%26-sin%5Ctheta%5C%5C%0Asin%5Ctheta%26cos%5Ctheta-e%5E%7B-i%5Ctheta%7D%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0Acos%5Ctheta-%28cos%5Ctheta+-+i+sin%5Ctheta%29%26-sin%5Ctheta%5C%5C%0Asin%5Ctheta%26cos%5Ctheta-%28cos%5Ctheta+-+i+sin%5Ctheta%29%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A%2Bi+sin%5Ctheta%26-sin%5Ctheta%5C%5C%0Asin%5Ctheta%26%2Bi+sin%5Ctheta%0A%5Cend%7Bbmatrix%7D%5C%5C%0Ax_1%26%3D%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0Ai%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Adiagonalizing%3A%26%0A%5C%5C%0AX%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A-i%26i%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5CLambda%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7Bi%5Ctheta%7D%26%5C%5C%0A%26e%5E%7B-i%5Ctheta%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0AX%5E%7B-1%7D%26%3D%0A%5Cfrac%7B1%7D%7B2i%7D%5Cbegin%7Bbmatrix%7D%0Ai%26-1%5C%5C%0Ai%261%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Apowers%26%5C%5C%0A%5C%5C%0AA%5Ek%26%3DX%26Lambda%3BX%5E%7B-1%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A-i%26i%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7Bi%5Ctheta%7D%26%5C%5C%0A%26e%5E%7B-i%5Ctheta%7D%0A%5Cend%7Bbmatrix%7D%5Ek%0A%5Cfrac%7B1%7D%7B2i%7D%5Cbegin%7Bbmatrix%7D%0Ai%26-1%5C%5C%0Ai%261%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A-i%26i%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7Bik%5Ctheta%7D%26%5C%5C%0A%26e%5E%7B-ik%5Ctheta%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B2i%7D%5Cbegin%7Bbmatrix%7D%0Ai%26-1%5C%5C%0Ai%261%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%2Ae%5E%7Bik%5Ctheta%7D%261%2Ae%5E%7B-ik%5Ctheta%7D%5C%5C%0A-i%2Ae%5E%7Bik%5Ctheta%7D%26i%2Ae%5E%7B-ik%5Ctheta%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B2i%7D%5Cbegin%7Bbmatrix%7D%0Ai%26-1%5C%5C%0Ai%261%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%26%3D+%0A%5Cfrac%7B1%7D%7B2i%7D%0A%5Cbegin%7Bbmatrix%7D%0Ai%2A1%2Ae%5E%7Bik%5Ctheta%7D%2Bi%2A1%2Ae%5E%7B-ik%5Ctheta%7D%26-1%2A1%2Ae%5E%7Bik%5Ctheta%7D%2B1%2A1%2Ae%5E%7B-ik%5Ctheta%7D%5C%5C%0Ai%2A%28-i%29%2Ae%5E%7Bik%5Ctheta%7D%2Bi%2Ai%2Ae%5E%7B-ik%5Ctheta%7D%26%28-1%29%2A-i%2Ae%5E%7Bik%5Ctheta%7D%2B1%2Ai%2Ae%5E%7B-ik%5Ctheta%7D%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26%3D+%0A%5Cfrac%7B1%7D%7B2i%7D%0A%5Cbegin%7Bbmatrix%7D%0Ai%2Ae%5E%7Bik%5Ctheta%7D%2Bi%2Ae%5E%7B-ik%5Ctheta%7D%26-e%5E%7Bik%5Ctheta%7D%2Be%5E%7B-ik%5Ctheta%7D%5C%5C%0A%28%2B1%29%2Ae%5E%7Bik%5Ctheta%7D%2B%28-1%29%2Ae%5E%7B-ik%5Ctheta%7D%26i%2Ae%5E%7Bik%5Ctheta%7D%2Bi%2Ae%5E%7B-ik%5Ctheta%7D%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7Bi%2Ae%5E%7Bik%5Ctheta%7D%2Bi%2Ae%5E%7B-ik%5Ctheta%7D%7D%7B2i%7D%26%5Cfrac%7B-e%5E%7Bik%5Ctheta%7D%2Be%5E%7B-ik%5Ctheta%7D%7D%7B2i%7D%5C%5C%0A%5Cfrac%7B%28%2B1%29%2Ae%5E%7Bik%5Ctheta%7D%2B%28-1%29%2Ae%5E%7B-ik%5Ctheta%7D%7D%7B2i%7D%26%5Cfrac%7Bi%2Ae%5E%7Bik%5Ctheta%7D%2Bi%2Ae%5E%7B-ik%5Ctheta%7D%7D%7B2i%7D%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7Be%5E%7Bik%5Ctheta%7D%2Be%5E%7B-ik%5Ctheta%7D%7D%7B2%7D%26%5Cfrac%7Be%5E%7B-ik%5Ctheta%7D-e%5E%7Bik%5Ctheta%7D%7D%7B2i%7D%5C%5C%0A%5Cfrac%7Be%5E%7Bik%5Ctheta%7D-e%5E%7B-ik%5Ctheta%7D%7D%7B2i%7D%26%5Cfrac%7Be%5E%7Bik%5Ctheta%7D%2Be%5E%7B-ik%5Ctheta%7D%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B%28cos%5Ek%5Ctheta%2Bisin%5Ek%5Ctheta%29%2B%28cos%5Ek%5Ctheta-isin%5Ek%5Ctheta%29%7D%7B2%7D%26%5Cfrac%7B%28cos%5Ek%5Ctheta-isin%5Ek%5Ctheta%29-%28cos%5Ek%5Ctheta%2Bisin%5Ek%5Ctheta%29%7D%7B2i%7D%5C%5C%0A%5Cfrac%7B%28cos%5Ek%5Ctheta%2Bisin%5Ek%5Ctheta%29-%28cos%5Ek%5Ctheta-isin%5Ek%5Ctheta%29%7D%7B2i%7D%26%5Cfrac%7B%28cos%5Ek%5Ctheta%2Bisin%5Ek%5Ctheta%29%2B%28cos%5Ek%5Ctheta-isin%5Ek%5Ctheta%29%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B2cos%5Ek%5Ctheta%7D%7B2%7D%26%5Cfrac%7B-2isin%5Ek%5Ctheta%7D%7B2i%7D%5C%5C%0A%5Cfrac%7B2isin%5Ek%5Ctheta%7D%7B2i%7D%26%5Cfrac%7B2cos%5Ek%5Ctheta%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Ccos%5Ek%5Ctheta%26-sin%5Ek%5Ctheta%5C%5C%0A%5Csin%5Ek%5Ctheta%26%5Ccos%5Ek%5Ctheta%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

coordinates in e:

imaginary on the vertical (y) axis = sin theta 
real on the horizontal (x) axis = cos theta

j = (-1)**.5

unit circle:

z = cos theta + j•sin theta

variable r circle

z = r•cos theta + j•r•sin theta

the Euler equations:

e<sup>j&theta;</sup> = cos&theta; + j sin&theta;

e<sup>-j&theta;</sup> = cos&theta; - j sin&theta;

the two LHS sum to 1

e<sup>j&theta;</sup> + e<sup>-j&theta;</sup> = 1

the two RHS sum to 1

cos&theta; + j sin&theta; + cos&theta; - j sin&theta; = 1

effect of j = 90 degrees: (also shown in example below)

j•z = j•(cos theta + j•sin theta) = j•cos theta - sin theta)

j*z = j*e**( j*theta)

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108246606-a0c32300-711f-11eb-80cb-966e6855457e.png">


34.  the transpose of A = X&Lambda;X<sup>-1</sup> is A<sup>T</sup> = (X<sup>-1</sup>)<sup>T</sup>&Lambda;X<sup>T</sup>.  
the eigenvectors y in A<sup>T</sup> = &lambda;y are the columns of that matrix (X<sup>-1</sup>)<sup>T</sup>.  
they are clled the 'left eigenvectors' of A because y<sup>T</sup>A = &lambda;y<sup>T</sup>.  
how do you multiply matrices to find the formula for A.  

A = X&Lambda;X<sup>-1</sup> = &lambda;<sub>1</sub>x<sub>1</sub>y<sub>1</sub><sup>T</sup> + ... + &lambda;<sub>n</sub>x<sub>n</sub>y<sub>n</sub><sup>T</sup>


section 6.3

systems of differential equations

starting with the example 2 which shows where this chapter is heading.  otherwise it is too abstract and wandering up front to follow.  

first a review of whats to come since the book is a bit obtuse in this section:   

- this chapter started with Ax = &lambda;x  where Ax and &lambda;x are scalars and A<sup>k</sup>x = &lambda;<sup>k</sup>x.    
- then the chapter moved to vector u<sub>k</sub> = A<sup>k</sup>u</sub>0</sub> = vector =  X&Lambda;<sup>k</sup>X<sup>-1</sup>u<sub>0</sub> and put u<sub>0</sub> in terms of a linear combination of X's columns, the eigenvectors via coefficients c.    
- So until now, the function has been linear constants of A multiplying scalar x or vector u.    Here it is function u of t where A is again constants that act on t in function u.   when taking the derivative of u with respect to t, ∂u/∂t, the result is the constant A times u: ∂u/∂t = Au.  This derivative only occurs when u is the exponential constant to the power of At: only u(t) = e<sup>At</sup> has ∂u/∂t = Au.  So, ∂u/∂t can only be solved by u(t) = e<sup>At</sup>, but this has infinite solutions and more specifically ("particularly" in technical terms) solved by e<sup>At</sup> with initial condition u<sub>0</sub>: ∂u/∂t = Au is solved by u(t) = e<sup>At</sup>u<sub>0</sub>  We are solving ∂u/∂t = Au = Ae<sup>At</sup> with u(t) = Xe<sup>&Lambda;t</sup>X<sup>-1</sup>u<sub>t=0</sub>.  for many c's, &lambda;s and x's, u<sub>t=0</sub> = c<sub>0</sub>e<sup>A•(t=0)</sup>x = c<sub>0</sub>(I)x.  u(0) = Xc or c = X<sup>-1</sup>u<sub>0</sub>, giving us u(t) = Xe<sup>&Lambda;t</sup>c.

very helpful link:
http://heath.cs.illinois.edu/scicomp/notes/cs450_chapt09.pdf

then this one which has the example in this book
http://web.mit.edu/18.06/www/Spring17/Matrix-Exponentials.pdf

![\begin{align*}
1 \, equation:&\\
\\
y'&=ay\\
solution:&\\
\\
y(t) &= e^{at}y(0)
\\
\\
n \, equations:&\\
\\
y'&=Ay\\
\\
solution:&\\
y(t) &= e^{At}y(0)
\\
\\
exponentials :\\
\\
e^{x} &= \sum_{i=0}^{\infty} \frac{(x)^i}{i!}\\
\\
\\
e^{At} &= \sum_{i=0}^{\infty} \frac{(At)^i}{i!}\\
\\
& each \,one  \,is  \,a  \,matrix\\
\\
&= \frac{(At)^0}{0!} +\frac{(At)^1}{1!} +\frac{(At)^2}{2!}++\frac{(At)^3}{3!}+\, ... +\frac{(At)^\infty}{\infty!} \\
\\
&= I +At +\frac{1}{2}(At)^2+\frac{1}{6}(At)^3+\, ... +\frac{(At)^\infty}{\infty!} 
\\
(e^{At})' &=\\
\\
\frac{\partial (e^{At})}{\partial t} & = (I +At +\frac{1}{2}(At)^2+\frac{1}{6}(At)^3+\, ... )'\\
\\
& = constant +A +\frac{1}{2}(A^2)(2t)+\frac{1}{6}(A^3)3t^2+\, ... \\
\\
& = A +A^2t+\frac{1}{2}A^3t^2+\, ... \\
\\
& = A( I+At+\frac{1}{2}(At)^2+\, ... \\
\\
& = Ae^{At} \\
\\
\\
y'=\frac{\partial (e^{At}y(0))}{\partial t} &= (I*y(0) +At*y(0) +\frac{1}{2}(At)^2*y(0)+\frac{1}{6}(At)^3*y(0)+\, ... )'\\
\\
&due \, to \, product \, rule \, and \, y(0) \, is \, a \, constant\\
\\
&= (I +At +\frac{1}{2}(At)^2+\frac{1}{6}(At)^3+\, ... )'y(0)\\
\\
&= Ae^{At}y(0) \\
\\
&=Ay
\\
\\
diagonalization \,of \, y:&
\\
y&= (I + X&Lambda;X^{-1}t + \frac{1}{2}X&Lambda;^2X^{-1}t^2 + \frac{1}{6}X&Lambda;^3X^{-1}t^3)*y(0)
\\
&= X(I + &Lambda;t + \frac{1}{2}&Lambda;^2t^2 + \frac{1}{6}&Lambda;^3t^3)X^{-1}*y(0)
\\
&= Xe^{&Lambda;t}X^{-1}*y(0)
\\
&=X*(\sum^\infty(I+&Lambda;t+\frac{1}{2}(&Lambda;t)^2+...+\frac{1}{\infty!}(&Lambda;t)^\infty))*X^{-1}*y(0)
\\
&= X *(\sum^\infty(
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&1
\end{bmatrix} +
\begin{bmatrix}
&lambda;_1t&0&0\\
0&&lambda;_2t&0\\
0&0&&lambda;_3t
\end{bmatrix} +
\frac{1}{2}\begin{bmatrix}
(&lambda;_1t)^2&0&0\\
0&(&lambda;_2t)^2&0\\
0&0&(&lambda;_3t)^2
\end{bmatrix} +
...+
\frac{1}{\infty!}\begin{bmatrix}
(&lambda;_1t)^\infty&0&0\\
0&(&lambda;_2t)^\infty&0\\
0&0&(&lambda;_3t)^\infty
\end{bmatrix}
))*X^{-1}*y(0)\\
\\
\\
&\begin{matrix}
each&cell&in&the&above&exponential&series&of&matrices&containing&&lambda;t&sums&to&e^{&lambda;t}
\end{matrix}
\\
& for \, example\,add\,cell(1,1)\,across\,all\,matrices\, \\ &=(&lambda;_1t)^0+(&lambda;_1t)^1+(&lambda;_2t)^2 + (&lambda;_it)^i + ... + (&lambda;_1t)^{\infty} 
=1+&lambda;_1t+(&lambda;_1t)^2 + (&lambda;_1t)^i + ... + (&lambda;_1t)^{\infty} 
= e^{&lambda;_1t}\\
& found \,below \,in \,cell \,(1,1)
\\
\\
&= X\begin{bmatrix}
e^{&lambda;_1t}&0&0\\
0&e^{&lambda;_2t}&0\\
0&0&e^{&lambda;_3t}
\end{bmatrix}
X^{-1}*y(0)\\
\\
\\
&= Xe^{&Lambda;t}X^{-1}*y(0)
\\
\\
where:&\\
y(0) &= c_1 e^{&lambda;_1t} x_1 +c_2e^{&lambda;_2t}x_2 +c_3e^{&lambda;_3t}x_3\\
\\
&=
\begin{bmatrix}
x_1&x_2&x_3\\
\end{bmatrix}
\begin{bmatrix}
e^{&lambda;_1(t=0)}&0&0\\
0&e^{&lambda;_2(t=0)}&0\\
0&0&e^{&lambda;_3(t=0)}
\end{bmatrix}
\begin{bmatrix}
c_1\\c_2\\c_3\\
\end{bmatrix}
\\
&=
\begin{bmatrix}
x_1&x_2&x_3\\
\end{bmatrix}
\begin{bmatrix}
c_1\\c_2\\c_3\\
\end{bmatrix}
\\
&=Xc
\\
so \, ...&\\
\\
X^{-1}y(0) &=
\begin{bmatrix}
c_1\\c_2\\c_3\\
\end{bmatrix}
\\
\\
thus \, ...&\\
\\
y & = 
\begin{bmatrix}
x_1&x_2&x_3\\
\end{bmatrix}
\begin{bmatrix}
e^{&Lambda;_1t}&0&0\\
0&e^{&Lambda;_2t}&0\\
0&0&e^{&Lambda;_3t}
\end{bmatrix}
\begin{bmatrix}
c_1\\c_2\\c_3\\
\end{bmatrix}
\\
&=X e^{&Lambda;t}c\\
\\
\\
and \, ...&\\
\\
y'=\frac{\partial (e^{At}y(0))}{\partial t} &=
A\begin{bmatrix}
x_1&x_2&x_3\\
\end{bmatrix}
\begin{bmatrix}
e^{&Lambda;_1t}&0&0\\
0&e^{&Lambda;_2t}&0\\
0&0&e^{&Lambda;_3t}
\end{bmatrix}
\begin{bmatrix}
c_1\\c_2\\c_3\\
\end{bmatrix}
\\
&=AX e^{&Lambda;t}c\\
\\
\\
&=Ay\\
\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A1+%5C%2C+equation%3A%26%5C%5C%0A%5C%5C%0Ay%27%26%3Day%5C%5C%0Asolution%3A%26%5C%5C%0A%5C%5C%0Ay%28t%29+%26%3D+e%5E%7Bat%7Dy%280%29%0A%5C%5C%0A%5C%5C%0An+%5C%2C+equations%3A%26%5C%5C%0A%5C%5C%0Ay%27%26%3DAy%5C%5C%0A%5C%5C%0Asolution%3A%26%5C%5C%0Ay%28t%29+%26%3D+e%5E%7BAt%7Dy%280%29%0A%5C%5C%0A%5C%5C%0Aexponentials+%3A%5C%5C%0A%5C%5C%0Ae%5E%7Bx%7D+%26%3D+%5Csum_%7Bi%3D0%7D%5E%7B%5Cinfty%7D+%5Cfrac%7B%28x%29%5Ei%7D%7Bi%21%7D%5C%5C%0A%5C%5C%0A%5C%5C%0Ae%5E%7BAt%7D+%26%3D+%5Csum_%7Bi%3D0%7D%5E%7B%5Cinfty%7D+%5Cfrac%7B%28At%29%5Ei%7D%7Bi%21%7D%5C%5C%0A%5C%5C%0A%26+each+%5C%2Cone++%5C%2Cis++%5C%2Ca++%5C%2Cmatrix%5C%5C%0A%5C%5C%0A%26%3D+%5Cfrac%7B%28At%29%5E0%7D%7B0%21%7D+%2B%5Cfrac%7B%28At%29%5E1%7D%7B1%21%7D+%2B%5Cfrac%7B%28At%29%5E2%7D%7B2%21%7D%2B%2B%5Cfrac%7B%28At%29%5E3%7D%7B3%21%7D%2B%5C%2C+...+%2B%5Cfrac%7B%28At%29%5E%5Cinfty%7D%7B%5Cinfty%21%7D+%5C%5C%0A%5C%5C%0A%26%3D+I+%2BAt+%2B%5Cfrac%7B1%7D%7B2%7D%28At%29%5E2%2B%5Cfrac%7B1%7D%7B6%7D%28At%29%5E3%2B%5C%2C+...+%2B%5Cfrac%7B%28At%29%5E%5Cinfty%7D%7B%5Cinfty%21%7D+%0A%5C%5C%0A%28e%5E%7BAt%7D%29%27+%26%3D%5C%5C%0A%5C%5C%0A%5Cfrac%7B%5Cpartial+%28e%5E%7BAt%7D%29%7D%7B%5Cpartial+t%7D+%26+%3D+%28I+%2BAt+%2B%5Cfrac%7B1%7D%7B2%7D%28At%29%5E2%2B%5Cfrac%7B1%7D%7B6%7D%28At%29%5E3%2B%5C%2C+...+%29%27%5C%5C%0A%5C%5C%0A%26+%3D+constant+%2BA+%2B%5Cfrac%7B1%7D%7B2%7D%28A%5E2%29%282t%29%2B%5Cfrac%7B1%7D%7B6%7D%28A%5E3%293t%5E2%2B%5C%2C+...+%5C%5C%0A%5C%5C%0A%26+%3D+A+%2BA%5E2t%2B%5Cfrac%7B1%7D%7B2%7DA%5E3t%5E2%2B%5C%2C+...+%5C%5C%0A%5C%5C%0A%26+%3D+A%28+I%2BAt%2B%5Cfrac%7B1%7D%7B2%7D%28At%29%5E2%2B%5C%2C+...+%5C%5C%0A%5C%5C%0A%26+%3D+Ae%5E%7BAt%7D+%5C%5C%0A%5C%5C%0A%5C%5C%0Ay%27%3D%5Cfrac%7B%5Cpartial+%28e%5E%7BAt%7Dy%280%29%29%7D%7B%5Cpartial+t%7D+%26%3D+%28I%2Ay%280%29+%2BAt%2Ay%280%29+%2B%5Cfrac%7B1%7D%7B2%7D%28At%29%5E2%2Ay%280%29%2B%5Cfrac%7B1%7D%7B6%7D%28At%29%5E3%2Ay%280%29%2B%5C%2C+...+%29%27%5C%5C%0A%5C%5C%0A%26due+%5C%2C+to+%5C%2C+product+%5C%2C+rule+%5C%2C+and+%5C%2C+y%280%29+%5C%2C+is+%5C%2C+a+%5C%2C+constant%5C%5C%0A%5C%5C%0A%26%3D+%28I+%2BAt+%2B%5Cfrac%7B1%7D%7B2%7D%28At%29%5E2%2B%5Cfrac%7B1%7D%7B6%7D%28At%29%5E3%2B%5C%2C+...+%29%27y%280%29%5C%5C%0A%5C%5C%0A%26%3D+Ae%5E%7BAt%7Dy%280%29+%5C%5C%0A%5C%5C%0A%26%3DAy%0A%5C%5C%0A%5C%5C%0Adiagonalization+%5C%2Cof+%5C%2C+y%3A%26%0A%5C%5C%0Ay%26%3D+%28I+%2B+X%26Lambda%3BX%5E%7B-1%7Dt+%2B+%5Cfrac%7B1%7D%7B2%7DX%26Lambda%3B%5E2X%5E%7B-1%7Dt%5E2+%2B+%5Cfrac%7B1%7D%7B6%7DX%26Lambda%3B%5E3X%5E%7B-1%7Dt%5E3%29%2Ay%280%29%0A%5C%5C%0A%26%3D+X%28I+%2B+%26Lambda%3Bt+%2B+%5Cfrac%7B1%7D%7B2%7D%26Lambda%3B%5E2t%5E2+%2B+%5Cfrac%7B1%7D%7B6%7D%26Lambda%3B%5E3t%5E3%29X%5E%7B-1%7D%2Ay%280%29%0A%5C%5C%0A%26%3D+Xe%5E%7B%26Lambda%3Bt%7DX%5E%7B-1%7D%2Ay%280%29%0A%5C%5C%0A%26%3DX%2A%28%5Csum%5E%5Cinfty%28I%2B%26Lambda%3Bt%2B%5Cfrac%7B1%7D%7B2%7D%28%26Lambda%3Bt%29%5E2%2B...%2B%5Cfrac%7B1%7D%7B%5Cinfty%21%7D%28%26Lambda%3Bt%29%5E%5Cinfty%29%29%2AX%5E%7B-1%7D%2Ay%280%29%0A%5C%5C%0A%26%3D+X+%2A%28%5Csum%5E%5Cinfty%28%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A0%261%260%5C%5C%0A0%260%261%0A%5Cend%7Bbmatrix%7D+%2B%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1t%260%260%5C%5C%0A0%26%26lambda%3B_2t%260%5C%5C%0A0%260%26%26lambda%3B_3t%0A%5Cend%7Bbmatrix%7D+%2B%0A%5Cfrac%7B1%7D%7B2%7D%5Cbegin%7Bbmatrix%7D%0A%28%26lambda%3B_1t%29%5E2%260%260%5C%5C%0A0%26%28%26lambda%3B_2t%29%5E2%260%5C%5C%0A0%260%26%28%26lambda%3B_3t%29%5E2%0A%5Cend%7Bbmatrix%7D+%2B%0A...%2B%0A%5Cfrac%7B1%7D%7B%5Cinfty%21%7D%5Cbegin%7Bbmatrix%7D%0A%28%26lambda%3B_1t%29%5E%5Cinfty%260%260%5C%5C%0A0%26%28%26lambda%3B_2t%29%5E%5Cinfty%260%5C%5C%0A0%260%26%28%26lambda%3B_3t%29%5E%5Cinfty%0A%5Cend%7Bbmatrix%7D%0A%29%29%2AX%5E%7B-1%7D%2Ay%280%29%5C%5C%0A%5C%5C%0A%5C%5C%0A%26%5Cbegin%7Bmatrix%7D%0Aeach%26cell%26in%26the%26above%26exponential%26series%26of%26matrices%26containing%26%26lambda%3Bt%26sums%26to%26e%5E%7B%26lambda%3Bt%7D%0A%5Cend%7Bmatrix%7D%0A%5C%5C%0A%26+for+%5C%2C+example%5C%2Cadd%5C%2Ccell%281%2C1%29%5C%2Cacross%5C%2Call%5C%2Cmatrices%5C%2C+%5C%5C+%26%3D%28%26lambda%3B_1t%29%5E0%2B%28%26lambda%3B_1t%29%5E1%2B%28%26lambda%3B_2t%29%5E2+%2B+%28%26lambda%3B_it%29%5Ei+%2B+...+%2B+%28%26lambda%3B_1t%29%5E%7B%5Cinfty%7D+%0A%3D1%2B%26lambda%3B_1t%2B%28%26lambda%3B_1t%29%5E2+%2B+%28%26lambda%3B_1t%29%5Ei+%2B+...+%2B+%28%26lambda%3B_1t%29%5E%7B%5Cinfty%7D+%0A%3D+e%5E%7B%26lambda%3B_1t%7D%5C%5C%0A%26+found+%5C%2Cbelow+%5C%2Cin+%5C%2Ccell+%5C%2C%281%2C1%29%0A%5C%5C%0A%5C%5C%0A%26%3D+X%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B%26lambda%3B_1t%7D%260%260%5C%5C%0A0%26e%5E%7B%26lambda%3B_2t%7D%260%5C%5C%0A0%260%26e%5E%7B%26lambda%3B_3t%7D%0A%5Cend%7Bbmatrix%7D%0AX%5E%7B-1%7D%2Ay%280%29%5C%5C%0A%5C%5C%0A%5C%5C%0A%26%3D+Xe%5E%7B%26Lambda%3Bt%7DX%5E%7B-1%7D%2Ay%280%29%0A%5C%5C%0A%5C%5C%0Awhere%3A%26%5C%5C%0Ay%280%29+%26%3D+c_1+e%5E%7B%26lambda%3B_1t%7D+x_1+%2Bc_2e%5E%7B%26lambda%3B_2t%7Dx_2+%2Bc_3e%5E%7B%26lambda%3B_3t%7Dx_3%5C%5C%0A%5C%5C%0A%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B%26lambda%3B_1%28t%3D0%29%7D%260%260%5C%5C%0A0%26e%5E%7B%26lambda%3B_2%28t%3D0%29%7D%260%5C%5C%0A0%260%26e%5E%7B%26lambda%3B_3%28t%3D0%29%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%5C%5Cc_2%5C%5Cc_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%5C%5Cc_2%5C%5Cc_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%26%3DXc%0A%5C%5C%0Aso+%5C%2C+...%26%5C%5C%0A%5C%5C%0AX%5E%7B-1%7Dy%280%29+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%5C%5Cc_2%5C%5Cc_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%5C%5C%0Athus+%5C%2C+...%26%5C%5C%0A%5C%5C%0Ay+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B%26Lambda%3B_1t%7D%260%260%5C%5C%0A0%26e%5E%7B%26Lambda%3B_2t%7D%260%5C%5C%0A0%260%26e%5E%7B%26Lambda%3B_3t%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%5C%5Cc_2%5C%5Cc_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%26%3DX+e%5E%7B%26Lambda%3Bt%7Dc%5C%5C%0A%5C%5C%0A%5C%5C%0Aand+%5C%2C+...%26%5C%5C%0A%5C%5C%0Ay%27%3D%5Cfrac%7B%5Cpartial+%28e%5E%7BAt%7Dy%280%29%29%7D%7B%5Cpartial+t%7D+%26%3D%0AA%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B%26Lambda%3B_1t%7D%260%260%5C%5C%0A0%26e%5E%7B%26Lambda%3B_2t%7D%260%5C%5C%0A0%260%26e%5E%7B%26Lambda%3B_3t%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%5C%5Cc_2%5C%5Cc_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%26%3DAX+e%5E%7B%26Lambda%3Bt%7Dc%5C%5C%0A%5C%5C%0A%5C%5C%0A%26%3DAy%5C%5C%0A%5C%5C%0A%5Cend%7Balign%2A%7D)

an example without enough eigenvectors:

solving for y1 and y2 can follow the example and then back substitute: dy1/dt = y2 and so y1 = t* constant and d2/dt = 0 --> y2 = constant. (unsure why.)

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108647777-807cc680-7487-11eb-9c6c-6e54204d1227.png">


**principles:**

1. if Ax = &lambda;x and looking to solve ∂u/∂t = Au = &lambda;u by finding u, then u(t) = e<sup>&lambda;t</sup> works.  Each &lambda; and x give a solution e<sup>&lambda;t</sup>x to satisfy the diagonalization procedures discussed in previous section: Ax = &lambda;x --> ∂u/∂t = Au = e<sup>&lambda;t</sup>x

2. if Ax = X&Lambda;X<sup>-1</sup> then [as done in previous section, express any u(t) as a function acting on the initial value u(0). &Lambda; is the function A and u(0) is denominated as a function = linear combination of the eigenvectors, X.  Remember, u(0) = XC and then X<sup>-1</sup>u(0) = C where C is inserted into X&Lambda;X<sup>-1</sup>u(0) replacing X<sup>-1</sup>u(0).

u(t) = e<sup>At</sup> = Xe<sup>&Lambda;t</sup>X<sup>-1</sup>u(0) = c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup>x<sub>1</sub> + ... + c<sub>n</sub>e<sup>&lambda;<sub>n</sub>t</sup>x<sub>n</sub> 

3. matrix A is stable and u(t) --> 0 and e<sup>At</sup> --> 0 when all eigenvalues of A have a real part < 0.

4. matrix exponential e<sup>At</sup> = I + At + ... + (At)<sup>n</sup> / n! + ... = Xe<sup>&Lambda;t</sup>X<sup>-1</sup> if A is diagonalizable. 

[I + At + ... + (At)<sup>n</sup> / n! + ... might also be written as (At)<sup>zero</sup> / zero! + (At)<sup>1</sup> / 1! + ... + (At)<sup>n</sup> / n! + ... where I = (At)<sup>zero</sup> and zero! = 1

5. second order equation
first order system
u'' + Bu' + Cu = 0 is equivalent to [ [u], [u'] ]' = [ [ 0,1 ], [ -C, -B ] ] [ [u], [u'] ]

few equations from previous sections:

A<sup>k</sup> = X&Lambda;<sup>k</sup>X<sup>-1</sup>   
A<sup>k</sup>u<sub>0</sub> = X&Lambda;<sup>k</sup>X<sup>-1</sup>u<sub>0</sub> = X&Lambda;<sup>k</sup>c   
A<sup>k</sup>U<sub>0</sub> = X&Lambda;<sup>k</sup>X<sup>-1</sup>u<sub>0</sub> = X&Lambda;<sup>k</sup>C 

Au = ∂u/∂t can be diagonalized with eigenvalues and eigenvectors as well. 

∂ e<sup>&lambda;t</sup> / ∂t = &lambda;e<sup>&lambda;t</sup>.

Need to know that for ∂u/∂t = u, the only function that does this is e<sup>t</sup>:  
u = e<sup>t</sup> has ∂u/∂t = e<sup>t</sup>  
u = e<sup>&lambda;t</sup> has ∂u/∂t = &lambda;e<sup>&lambda;t</sup>  

the point of this section is   
constant coefficient differential equations translated into linear algebra.   

so these equatoins are [only] solved by expoentials: ∂u/∂t = u and ∂u/∂t = &lambda;u

∂u/∂t = u is solved by u(t) = Ce<sup>t</sup>   
∂u/∂t = &lambda;u is solved by u(t) = Ce<sup>&lambda;t</sup>   

at t = 0 those solutions include e<sup>0</sup> = 1     
which gives the initial value u(0) = Ce<sup>0</sup> = C
[generally:
∂u/∂t = u is solved by u(t) = u(0)e<sup>t</sup> = Ce<sup>t</sup>    
∂u/∂t = &lambda;u is solved by u(t) = u(0)e<sup>&lambda;t</sup> = Ce<sup>&lambda;t</sup>   

So that solves a 1x1 problem. 

Linear algebra moves to n x n where u is a now a vector
with initial vector u(0) = (u<sub>1</sub>(0), ... , u<sub>n</sub>(0) ).T  
with n equations contain a square matrix A   
we expect u(t) with n e<sup>&lambda;t</sup> from 10 &lambda;s.

system of equations: ∂u/∂t = Au starting with u(0) = ( u<sub>1</sub>(0) , ... , u<sub>n</sub>(0) ) at time t=0

the differential equations [in that system of equations] are linear: if u(t) and v(t) are solutions [to finding u in ∂u/∂t] then so is C • u(t) + D • v(t).  there will be n constants like C and D to match the n components of u(0).  

first job is finding n "pure exponential solutions" u = e<up>&lambda;t</sup>x by using Ax = &lambda;x
[x is an eigenvector]

A is a constant matrix   
- doesnt change as t changes (as in other linear equations)   
- doesnt change as u changes (as in non-linear equations)   
∂u/∂t = Au is linear with constant coefficients.

solve linear constant coefficient equations by exponentials e<sup>&lambda;t</sup>x

**solution to ∂u/∂t = Au**

pure exponential solution to ∂u/∂t = Au is finding the u which is = e<sup>lambda;t</sup> times a fixed vector x or the eigenvector. 

substitute u = e<sup>lambda;t</sup>x into ∂u/∂t = Au = A e<sup>lambda;t</sup>x

[lots of unintelligible words here. not including.]

all components of this solution u = e<sup>&lambda;t</sup>x share the same  e<sup>&lambda;t</sup>.

the solution grows when &lambda;>0, decays when &lambda; < 0.  

if &lambda; is complex, the real part decides growth and decay, and imaginary part *w* gives oscillation e<sup>i*w*t</sup> like a sin wave. 

example: solve ∂u/∂t = Au = [[0,1],[1,0]]u starting with u(0) = (4,2).T

this is a vector equation for u containing 2 scalar equations for the components for the components y and z.  

the 2 scalar equations are coupled together because A is not diagonal.  

if diagonal, like the identity matrix, then ∂u/∂t = ∂ (y,z)/∂t produces ∂y/∂t = y and ∂z/∂t = z and so y and z would not be coupled.  

![\begin{align*}
A&=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}\\
\frac{\partial 
\begin{bmatrix}
y\\
z
\end{bmatrix}
}{\partial t} &=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\begin{bmatrix}
y\\
z
\end{bmatrix}
=\begin{bmatrix}
y\\
z
\end{bmatrix}\\
\\
thus:\\
\\
\frac{\partial y}{\partial t} &= y
\\
and\\
\\
\frac{\partial z}{\partial t} &= z
\\
\\
\\
but \, if:
\\
A&=
\begin{bmatrix}
0&1\\
1&0
\end{bmatrix}\\
\frac{\partial 
\begin{bmatrix}
y\\
z
\end{bmatrix}
}{\partial t} &=
\begin{bmatrix}
0&1\\
1&0
\end{bmatrix}
\begin{bmatrix}
y\\
z
\end{bmatrix}
=\begin{bmatrix}
z\\
y
\end{bmatrix}\\
\\
thus:\\
\\
\frac{\partial y}{\partial t} &= z
\\
and\\
\\
\frac{\partial z}{\partial t} &= y
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A0%261%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D%0A%7D%7B%5Cpartial+t%7D+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A0%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Athus%3A%5C%5C%0A%5C%5C%0A%5Cfrac%7B%5Cpartial+y%7D%7B%5Cpartial+t%7D+%26%3D+y%0A%5C%5C%0Aand%5C%5C%0A%5C%5C%0A%5Cfrac%7B%5Cpartial+z%7D%7B%5Cpartial+t%7D+%26%3D+z%0A%5C%5C%0A%5C%5C%0A%5C%5C%0Abut+%5C%2C+if%3A%0A%5C%5C%0AA%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%261%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D%0A%7D%7B%5Cpartial+t%7D+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%261%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0Az%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Athus%3A%5C%5C%0A%5C%5C%0A%5Cfrac%7B%5Cpartial+y%7D%7B%5Cpartial+t%7D+%26%3D+z%0A%5C%5C%0Aand%5C%5C%0A%5C%5C%0A%5Cfrac%7B%5Cpartial+z%7D%7B%5Cpartial+t%7D+%26%3D+y%0A%5Cend%7Balign%2A%7D)

the use of eigenvectors is to move from 2 equations to 1 by 1 problems. 

eigenvalues = 1, -1  
eigenvectors = (1,1).T and (1,-1).T  

pure exponential equation moves from ∂u/∂t = Au to eigenvalue times a function: u<sub>1</sub> and u<sub>2</sub> take the form e<sup>&lambda;t</sup>x.  

u<sub>1</sub> = e<sup>&lambda;<sub>1</sub>t</sup>x<sub>1</sub> = e<sup>t</sub> • (1,1).T

u<sub>2</sub> = e<sup>&lambda;<sub>2</sub>t</sup>x<sub>2</sub> = e<sup>-t</sub> • (1,-11).T

the u's satisfy Au<sub>1</sub> = u<sub>1</sub> and Au<sub>2</sub> = u<sub>2</sub>. 

the factors e<sup>t</sup> and e<sup>-t</sup> change with time.  

those factors give ∂u<sub>1</sub>/∂t = u<sub>1</sub> = Au<sub>1</sub> and ∂u<sub>2</sub>/∂t = -u<sub>2</sub> = Au<sub>2</sub>. 

2 solutions to ∂u/∂t = Au.  

all other solutions come from multiplying those special solutions by any number C and D and adding.

Complete solution 
= u(t) = Ce<sup>t<sup>(`1,1).T + De<sup>-t<sup>(1,-11).T 
= [ [ Ce<sup>t<sup> + De<sup>-t<sup> ], [ Ce<sup>t<sup> + De<sup>-t<sup> ] ]

find C and D by setting t=0 so e<sup>t<sup> and e<sup>-t<sup> = 1 and set u<sub>0</sub> = (4,2).T = (x<sub>1</sub>, x<sub>2</sub>).T • (C, D) solving for CD via X<sup>-1</sup> --> C = 3, D = solving the initial value problem.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108650207-08b19a80-748d-11eb-983b-89bbca869eb9.png">

1. write u(0) as combination of c<sub>1</sub>x<sub>1</sub> + ... + c<sub>n</sub>x<sub>n</sub> of eigenvectors of A:

u(0) = c<sub>1</sub>x<sub>1</sub> + ... + c<sub>n</sub>x<sub>n</sub>

2. multiply each eigenvector x<sub>i</sub> by its growth factor e<sup>&lambda;<sub>i</sub>t</sup>.  

u(t) = c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup>x<sub>1</sub> + ... + c<sub>n</sub>e<sup>&lambda;<sub>i</sub>t</sup>x<sub>n</sub>

3.  the solution is the same combination of those pure solutions e<sup>&lambda;t</sup>x  

∂u/∂t = Au has solution found when u(t) is found = u(t) = c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup>x<sub>1</sub> + ... + c<sub>n</sub>e<sup>&lambda;<sub>i</sub>t</sup>x<sub>n</sub>

the differential has the A ...
both the differential and u have the initial value u(0) ...


example 2:

solve ∂u/∂t = Au, that is find the function u, knowing the constant A, the eigenvalues and eigenvectors of A and the initial value of the function u aka u<sub>0</sub>:

- eigenvalues of A are &lambda;<sub>1</sub>, &lambda;<sub>2</sub>, &lambda;<sub>3</sub> are 1, 2, 3.     
- eigenvaectors of A are x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> are (1,0,0)<sup>T</sup>, (1,1,0)<sup>T</sup>, (1,1,1)<sup>T</sup>.   
- the initial value of u is u<sub>0</sub> = (9,7,4)<sup>T</sup>.

we know the derivative of function u with respect to t, ∂u/∂t equals some constant coefficient matrix A times variable u.    
the only function u whose derivative is a constant times that function is u = e<sup>At</sup> whose ∂u/∂t = Ae<sup>At</sup>.      

the goal is to replace A with eigenvalues and eigenvectors. until now this has meant Ax = &lambda;x


step 1: vector u(0) = (9,7,4)<sup>T</sup> is u(0) = (c<sub>1</sub>)(e<sup>&lambda;<sub>1</sub>(t=0)</sup>)((x<sub>1</sub>) + (c<sub>2</sub>)(e<sup>&lambda;<sub>2</sub>(t=0)</sup>)((x<sub>2</sub>) + (c<sub>3</sub>)(e<sup>&lambda;<sub>3</sub>(t=0)</sup>)((x<sub>3</sub>) = 2(x<sub>1</sub>) + 3((x<sub>2</sub>) + 4((x<sub>3</sub>) revealing (c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub>) = (2,3,4)

step 2: factors e<sup>&lambda;t</sup> for the exponential solutions: e<sup>1t</sup>x<sub>1</sub>, e<sup>2t</sup>x<sub>2</sub>, e<sup>3t</sup>x<sub>3</sub>

step 3: the combination that starts from u(0) is   
u(t)   
= 2(e<sup>(&lambda;<sub>1</sub>=1)(t)</sup>)(x<sub>1</sub>) + 3(e<sup>(&lambda;<sub>2</sub>=2)(t)</sup>)((x<sub>2</sub>) + 4(e<sup>(&lambda;<sub>3</sub>=3)(t)</sup>)((x<sub>3</sub>)   
= 2e<sup>t</sup>x<sub>1</sub> + 3e<sup>2t</sup>x<sub>2</sub> + 4e<sup>3t</sup>x<sub>3</sub> 

where of course c<sub>1</sub> = 2, c<sub>2</sub> = 3, c<sub>3</sub> = 4 come from Xc = u(0) --> X<sup>-1</sup>u(0) = c as shown here:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108641995-9b900c00-7470-11eb-83f6-a8ddfb176502.png">


next  
equations of second derivatives  ?
does u(t) approach zero or blow up or just oscillate ?
expoential e<sup>At</sup>:  the short formular e<sup>At</sup>u(0) solves the equation ∂u/∂t = Au in the same way that A<sup>k</sup>u<sub>0</sub> solves the equation u<sub>k+1</sub> = Au<sub>k</sub>.  Example 3 shows difference equation solving differential equations. 

up till now:

Au = &lambda;u = [x<sub>k+1</sub>, x<sub>k</sub>]

Au = ∂u / ∂t = u

now:

Au = ∂u /∂t = [ y', y ]

**second order equations**

exampe for this section is the most important equation in mechanics

second order equations contain the second derivative y'' = ∂<sup>2</sup>y / ∂t<sup>2</sup>.  
this second order equation is linear because it has constant coefficients.

m • y'' + b • y' + k • y = 0

m • y'' = F = - b • y' - k • y

- the first term is mass m times acceleration = a = y''.  m • a or m • y'' balances the force F from Newton's Law that includes:    
- the second term which is dampening = - b • y' and 
- the third term which is elastic force = - k • y proportional to distance moved.  [ y = distance moved? ]

y = e<sup>&lambda;t</sup> is the solution in a differential problem.   
each derivative of y brings down a factor &lambda;   
here again, y = e<sup>&lambda;t</sup> solves the equation:  

m • ∂<sup>2</sup>y / ∂t<sup>2</sup> + b • ∂y / ∂t + k • y = 0   

which thus becomes ...

m • &lambda;<sup>2</sup> • e<sup>&lambda;t</sup>' + b • &lambda; • e<sup>&lambda;t</sup> + k • e<sup>&lambda;t</sup> = 0

( m • &lambda;<sup>2</sup> + b • &lambda; + k ) • e<sup>&lambda;t</sup> = 0

because ... 

y = e<sup>&lambda;t</sup>
y' = &lambda; • e<sup>&lambda;t</sup>
y'' = &lambda;<sup>2</sup> • e<sup>&lambda;t</sup>

if m • &lambda;<sup>2</sup> + b • &lambda; + k = 0 has two roots: &lambda;<sub>1</sub> and &lambda;<sub>2</sub>,   
then the equaton for y has 2 **pure** solutions y<sub>1</sub> = e<sup>&lambda;<sub>1</sub>t</sup> and y<sub>2</sub> = e<sup>&lambda;<sub>2</sub>t</sup>       
and the **complete** solution is the combination c<sub>1</sub> • y<sub>1</sub> + c<sub>2</sub> • y<sub>2</sub>   
unless &lambda;<sub>1</sub> = &lambda;<sub>2</sub>
   
scalar equations with y'' done.   
vector equations with y and y' next. notice only the first derivative y' in vector equations.

example:

mass m = 1   
find u = (y, y').T  
given ∂u / ∂t = Au

∂u / ∂t where u = [ y, y' ].T  would be ∂u / ∂t = [ y', y'' ].T where:   
- ∂y / ∂t is on top = y'   
- ∂y' / ∂t is on bottom = y'' and we know y'' = - b • y' - k • y from m = 1 and the equation above m • y'' = - b • y' - k • y   
so ..

where u = [ y, y' ].T, ∂u / ∂t = ...
∂y / ∂t = y' 
∂y' / ∂t = y'' = - k • y - b • y' 

which converts to vector equations

![\begin{align*}
\begin{matrix}
\frac{\partial 
y
}{\partial t}\\
\frac{\partial 
y'
}{\partial t}
\end{matrix}=
\begin{matrix}
y'\\
-ky-by'
\end{matrix}
--->\frac{\partial 
u
}{\partial t} = \frac{\partial 
\begin{bmatrix}
y\\
y'
\end{bmatrix}
}{\partial t} &=
Au =\begin{bmatrix}
0&1\\
-k&-b
\end{bmatrix}
\begin{bmatrix}
y\\
y'
\end{bmatrix}=  
\begin{bmatrix}
y'\\
-ky-by'=my''=y''
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cbegin%7Bmatrix%7D%0A%5Cfrac%7B%5Cpartial+%0Ay%0A%7D%7B%5Cpartial+t%7D%5C%5C%0A%5Cfrac%7B%5Cpartial+%0Ay%27%0A%7D%7B%5Cpartial+t%7D%0A%5Cend%7Bmatrix%7D%3D%0A%5Cbegin%7Bmatrix%7D%0Ay%27%5C%5C%0A-ky-by%27%0A%5Cend%7Bmatrix%7D%0A---%3E%5Cfrac%7B%5Cpartial+%0Au%0A%7D%7B%5Cpartial+t%7D+%3D+%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Ay%27%0A%5Cend%7Bbmatrix%7D%0A%7D%7B%5Cpartial+t%7D+%26%3D%0AAu+%3D%5Cbegin%7Bbmatrix%7D%0A0%261%5C%5C%0A-k%26-b%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Ay%27%0A%5Cend%7Bbmatrix%7D%3D++%0A%5Cbegin%7Bbmatrix%7D%0Ay%27%5C%5C%0A-ky-by%27%3Dmy%27%27%3Dy%27%27%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)


the second equation ( - k • y - b • y' ) is key because it connects or "couples" y'' to y' to y in the matrix as it does in the equation m • y'' = - b • y' - k • y

in the matrix the off diagonals do this magic: cell A(1,2) = 1 brings y' into component 1 and cell (2,1) = -k brings k * y into the second component with y'.

together the first and second equation connect u' to u as is needed to solve ∂u / ∂t = u' = Au    

start with eigenvalues of A: &lambda;<sub>1</sub> and &lambda;<sub>2</sub>.  we can use this generic &lambda; because the determinant &lambda;<sup>2</sup> + b • &lambda; + k = the original base equation  = m • &lambda;<sup>2</sup> + b • &lambda; + k defined above to be = 0 when m = 1 as is defined as well.   

then eigenvectors are x<sub>1</sub> = [ 1, &lambda;<sub>1</sub> ].T and x<sub>2</sub> = [ 1, &lambda;<sub>2</sub> ].T

the complete solution u(t) =  c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup>x<sub>1</sub> + c<sub>2</sub>e<sup>&lambda;<sub>2</sub>t</sup>x<sub>2</sub> = c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup>[ 1, &lambda;<sub>2</sub> ].T + c<sub>2</sub>e<sup>&lambda;<sub>2</sub>t</sup>[ 1, &lambda;<sub>2</sub> ].T

the 1st (top) component of the vector u(t) has y =  c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup>•1 + c<sub>2</sub>e<sup>&lambda;<sub>2</sub>t</sup>•1 = c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup> + c<sub>2</sub>e<sup>&lambda;<sub>2</sub>t</sup>

the second component of the vector u(t) has velocity ∂y / ∂t = y' = c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup>&lambda;<sub>1</sub> + c<sub>2</sub>e<sup>&lambda;<sub>2</sub>t</sup>x<sub>2</sub>&lambda;<sub>2</sub> = &lambda;<sub>1</sub>c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup> + &lambda;<sub>2</sub>c<sub>2</sub>e<sup>&lambda;<sub>2</sub>t</sup>x<sub>2</sub> with the &lambda;<sub>i</sub> that come down 

so the vector problem solution is consistent with the scalar problem solution. 

2 x 2 matrix A is termed the companion matrix = companion to second order equation.  

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108778026-bcb93100-7532-11eb-812b-fe14952e707a.png">


**example 3**

motion around circle:

y'' + y = 0
y = cos(t)

this is the master aka base equation with mass m = 1, dampening d = 0, stiffness k = 1.  

substitute y = e<sup>&lambda;t</sup> into y'' + y = 0 = &lambda;<sup>2</sup>e<sup>&lambda;t</sup> + e<sup>&lambda;t</sup> = (&lambda;<sup>2</sup> + 1)e<sup>&lambda;t</sup> = 0.  With &lambda;<sup>2</sup> + 1 = 0 [ since e<sup>&lambda;t</sup> ≠ 0 ], the roots are &lambda;<sub>1</sub> = i and &lambda;<sub>1</sub> = -i  [ i  = √1 ]

then half of e<sup>it</sup> + e<sup>-it</sup> = (e<sup>it</sup> + e<sup>-it</sup>) / 2 = cos (t) 

[ i think that y = cos t isnt an initial value but it is an anchoring value maybe: 
this gives the complete solution since y = cos (t) where c<sub>1</sub> = c<sub>2</sub> = 1/2 and y = cos(t) = c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup> + c<sub>2</sub>e<sup>&lambda;<sub>2</sub>t</sup> = ( e<sup>it</sup> + e<sup>-it</sup> ) / 2 and according to Eurler's:   
e<sup>i&theta;</sup> = cos&theta; + i sin&theta;   
e<sup>-i&theta;</sup> = cos&theta; - i sin&theta;    
ergo:    
e<sup>i&theta;</sup> + e<sup>-i&theta;</sup> = cos&theta; + i sin&theta; + cos&theta; - i sin&theta;    
which reduces to ...    
(e<sup>i&theta;</sup> + e<sup>-i&theta;</sup>) / 2 = cos&theta;     
]

the initial values, ...    
y(0) =  cos(0) = ( e<sup>i•0</sup> + e<sup>-i•0</sup> ) / 2 = 1   
y'(0)   
= (e<sup>i•t</sup> + e<sup>-i•t</sup>)'(0) = i • e<sup>i•0</sup> - i • e<sup>-i•0</sup> = (i • 1 - i • 1) = 0   
= (cos&theta;)'(0) = -sin(&theta;=(0) = 0   
... go into u(0) = [1,0].T

above is scalar equations; now vector equations

from given equations, we know:  y'' - y = 0 which means y'' = ∂y' / ∂t = - y   
and by definition ∂y / ∂t = y'

![\begin{align*}
\frac{\partial u}{\partial t}=\frac{\partial \begin{bmatrix}y\\y'\end{bmatrix}}{\partial t} = Au =\begin{bmatrix}0&1\\-1&0\end{bmatrix}
\begin{bmatrix}y\\y'\end{bmatrix}=
\begin{bmatrix}y'\\-y\end{bmatrix} 
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D%3D%5Cfrac%7B%5Cpartial+%5Cbegin%7Bbmatrix%7Dy%5C%5Cy%27%5Cend%7Bbmatrix%7D%7D%7B%5Cpartial+t%7D+%3D+Au+%3D%5Cbegin%7Bbmatrix%7D0%261%5C%5C-1%260%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7Dy%5C%5Cy%27%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7Dy%27%5C%5C-y%5Cend%7Bbmatrix%7D+%0A%5Cend%7Balign%2A%7D%0A)

same as before:   
- find eigenvalues from determinant of A - &lambda; * I   
- find eigenvectors from the null space of those matrices (A - &lambda;<sub>i</sub> * I)     
- employ 3 steps:    
1. combine the eigenvectors by finding c from u<sub>0</sub> = [1,0].T and X<sup>-1</sup> as shown below: u<sub>0</sub> = ∑<sub>i=1</sub><sup>n</sup> c<sub>i</sub>x<sub>i</sub> by using c = X<sup>-1</sup>u<sub>0</sub>
confirm u<sub>0</sub> = X<sup>-1</sup>c   

2. apply the growth factor eigenvalues e<sup>&lambda;<sub>i</sub>t</sup> to respective eigenvectors give exponential solutions.      
3. combination u(t) that starts from u(0) is the combination of the pure solutions.     
u(t) = ∑<sub>i=1</sub><sup>n</sup> c<sub>i</sub>x<sub>i</sub>e<sup>&lambda;<sub>i</sub>t</sup> = X&Lambda;c      

here Euler's algebra:  
e<sup>i &theta;</sup> = cos&theta; + i sin&theta;
e<sup>-i &theta;</sup> = cos&theta; - i sin&theta;
thus (using &theta; instead of t here):

1st component of u(t):  
( 1 / 2 ) • ( e<sup>i &theta;</sup> + e<sup>-i &theta;</sup> ) = (1 / 2) • (cos&theta; + i • sin&theta; + cos&theta; - i • sin&theta; ) = cos&theta; = y(t)

2nd component of u(t):  
( 1 / 2 ) • ( i ) • ( e<sup>i &theta;</sup>) + ( 1 / 2 ) • ( - i ) • ( e<sup>-i &theta;</sup>) = ( i / 2 ) • ( cos&theta; + i • sin&theta;) - (cos&theta; - i • sin&theta;) = ( i / 2 ) • 2 • ( i • sin&theta; - - i • sin&theta;) = i • i • sin&theta; = -sin&theta; = y'(t) = ∂y / ∂&theta; ∂ cos&theta; / ∂&theta since (cos&theta;)' = -sin&theta; 

so u(t) =  [ cos&theta;, -sin&theta; ]

![\begin{align*}
u(t)& = \frac{1}{2}\, e^{it} \,
\begin{bmatrix}
1\\
i\\
\end{bmatrix} +
\frac{1}{2} \,e^{-it}\,
\begin{bmatrix}
1\\
-i\\
\end{bmatrix}=
\begin{bmatrix}
\frac{1}{2}\,(1)\,(e^{i&theta;} + e^{-i&theta;})\\
\frac{1}{2}\,(i)\,(e^{i&theta;} - e^{-i&theta;})\\
\end{bmatrix}=
\begin{bmatrix}
cos t\\
-sin t\\
\end{bmatrix}=
\begin{bmatrix}
y(t)\\
y'(t)\\
\end{bmatrix}\\
\\
&=c_1 \, e^{&lambda;_1t} \, x_1 + c_2 \, e^{&lambda;_2t} \, x_2\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au%28t%29%26+%3D+%5Cfrac%7B1%7D%7B2%7D%5C%2C+e%5E%7Bit%7D+%5C%2C%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0Ai%5C%5C%0A%5Cend%7Bbmatrix%7D+%2B%0A%5Cfrac%7B1%7D%7B2%7D+%5C%2Ce%5E%7B-it%7D%5C%2C%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-i%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B2%7D%5C%2C%281%29%5C%2C%28e%5E%7Bi%26theta%3B%7D+%2B+e%5E%7B-i%26theta%3B%7D%29%5C%5C%0A%5Cfrac%7B1%7D%7B2%7D%5C%2C%28i%29%5C%2C%28e%5E%7Bi%26theta%3B%7D+-+e%5E%7B-i%26theta%3B%7D%29%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0Acos+t%5C%5C%0A-sin+t%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0Ay%28t%29%5C%5C%0Ay%27%28t%29%5C%5C%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%26%3Dc_1+%5C%2C+e%5E%7B%26lambda%3B_1t%7D+%5C%2C+x_1+%2B+c_2+%5C%2C+e%5E%7B%26lambda%3B_2t%7D+%5C%2C+x_2%5C%5C%0A%5Cend%7Balign%2A%7D)

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108797909-6a8c0600-755a-11eb-9bad-4c7e661ae978.png">

so at t = 0, &theta;/2, &theta;, 3&theta;/2, 2&theta;, ... u(t) = [ cos&theta;, -sin&theta;] = [1, 0].T, [0, -1].T, [-1, 0].T, [0, 1].T, [1, 0].T ... clockwise.

**difference equations**

motion around a circle in example 3 employed y'' = -y and y = cos t  

to display a circle on a screen, replace y'' = -y with one of 3 difference equations using this method:  

Y( t + &Delta;t ) - 2Y( t ) + Y( t-&Delta;t )  

to approximate y'', divide by ( 2&Delta; ) <sup>2</sup>:

y'' ~ Y( t + &Delta;t ) - 2Y( t ) + Y( t-&Delta;t ) / ( 2&Delta; ) <sup>2</sup> 

3 methods:  

( Y<sub>n+1</sub> - 2 • Y<sub>n</sub> + Y<sub>n-1</sub> ) / ( &Delta;t )<sup>2</sup> = - Y<sub>n-1</sub> or = - Y<sub>n</sub> or = - Y<sub>n+1</sub>

adds Y from a delta ahead and a delta behind and subtracts 2 of current Y divides by square &theta; change = &Delta;&theta;<sup>2</sup> to equal negative of one of those Y measurements

in theory one of those &Delta;&theta; can be moved from denominator on LHS to numerator on RHS and then brought back to the the LHS.

y(t) = cos(t) makes a complete circle at t = 2&theta;

2 of these Fourier Euler spirals miss by spiralling in (backward) or out (foreard) but one approximates well (leapfrog) as &Delta;t = 2&theta; / 32 

![\begin{align*}
F \,\, &Forward \, from \, n-1: \, \, \, \, \, \frac{Y_{n+1} -2Y_n + Y_{n-1}}{(&Delta;t)^2} = - Y_{n-1} \, \, \, (I I F) \\ 
C\, \, &Centered \, at \, time \, n: \, \, \, \, \, \, \, \, \, \,   \frac{Y_{n+1} -2Y_n + Y_{n-1}}{(&Delta;t)^2} = - Y_{n} \, \, \, \, \, \, \, \, \, \,  (I I C) \\ 
B \, \, &Backward \, from \, n+1: \,  \frac{Y_{n+1} -2Y_n + Y_{n-1}}{(&Delta;t)^2} = - Y_{n+1} \, \, \, \,  (I I B) \\ 
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AF+%5C%2C%5C%2C+%26Forward+%5C%2C+from+%5C%2C+n-1%3A+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5Cfrac%7BY_%7Bn%2B1%7D+-2Y_n+%2B+Y_%7Bn-1%7D%7D%7B%28%26Delta%3Bt%29%5E2%7D+%3D+-+Y_%7Bn-1%7D+%5C%2C+%5C%2C+%5C%2C+%28I+I+F%29+%5C%5C+%0AC%5C%2C+%5C%2C+%26Centered+%5C%2C+at+%5C%2C+time+%5C%2C+n%3A+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+++%5Cfrac%7BY_%7Bn%2B1%7D+-2Y_n+%2B+Y_%7Bn-1%7D%7D%7B%28%26Delta%3Bt%29%5E2%7D+%3D+-+Y_%7Bn%7D+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C++%28I+I+C%29+%5C%5C+%0AB+%5C%2C+%5C%2C+%26Backward+%5C%2C+from+%5C%2C+n%2B1%3A+%5C%2C++%5Cfrac%7BY_%7Bn%2B1%7D+-2Y_n+%2B+Y_%7Bn-1%7D%7D%7B%28%26Delta%3Bt%29%5E2%7D+%3D+-+Y_%7Bn%2B1%7D+%5C%2C+%5C%2C+%5C%2C+%5C%2C++%28I+I+B%29+%5C%5C+%0A%5Cend%7Balign%2A%7D%0A)

Forward |&lambda;| > 1 --> spiral out 
Centered |&lambda;| = 1 --> best
Backward |&lambda;| < 1 --> spiral in

these 2 step equtions in equations 11F, 11C and 11B reduce to 1 step systems U<sub>n+1<sub> = AU<sub>n</sub>.

instead of u = ( y, y' )  
the discrete unknown is U<sub>n</sub> = (Y<sub>n</sub>, Z<sub>n</sub>)
with n time steps &Delta;t starting from U<sub>0</sub>  
[notice U is a matrix here where before u was a vector]

these are like Y' = Z and Z' = Y   
these are first order equations involving times n and n+1.  Eliminating Z woudl be back the forward second order equation (11 F) above. [ to see how, know that Z<sub>n</sub> = ]

![\begin{align*}
\begin{matrix}
Forward
\end{matrix}
\begin{matrix}
Y_{n+1} = Y_n + &Delta;t Z_n\\
Z_{n+1} = Z_n - &Delta;t Y_n
\end{matrix}
\begin{matrix}
becomes
\end{matrix}
U_{n+1}=
\begin{bmatrix}
Y_{n+1}\\
Z_{n+1}\\
\end{bmatrix}=
\begin{bmatrix}
1&&Delta;t\\
-&Delta;t&1\\
\end{bmatrix}
\begin{bmatrix}
Y_n\\
Z_n\\
\end{bmatrix}
=AU_n
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cbegin%7Bmatrix%7D%0AForward%0A%5Cend%7Bmatrix%7D%0A%5Cbegin%7Bmatrix%7D%0AY_%7Bn%2B1%7D+%3D+Y_n+%2B+%26Delta%3Bt+Z_n%5C%5C%0AZ_%7Bn%2B1%7D+%3D+Z_n+-+%26Delta%3Bt+Y_n%0A%5Cend%7Bmatrix%7D%0A%5Cbegin%7Bmatrix%7D%0Abecomes%0A%5Cend%7Bmatrix%7D%0AU_%7Bn%2B1%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AY_%7Bn%2B1%7D%5C%5C%0AZ_%7Bn%2B1%7D%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%26%26Delta%3Bt%5C%5C%0A-%26Delta%3Bt%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AY_n%5C%5C%0AZ_n%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3DAU_n%0A%5Cend%7Balign%2A%7D)


question is :   
do points (Y<sub>n</sub>, Z<sub>n</sub>) stay on the circle Y<sup>2</sup> + Z<sup>2</sup> = 1   
with powers of A<sup>n</sup> not powers of e<sup>&lambda;t</sup>, we test the magnitude of |&lambda;| and not the real parts of the eigenvalues. 

Eigenvalues of A: &Lambda; = 1 &pm; i&Delta;t, Then, |&Lambda;| > 1 --> (Y<sub>n</sub>, Z<sub>n</sub>) spirals out as with the forward Euler spiral formula above and plotted below.  

The backward approximation will do the opposite, spiral inwards.  Notice the new A matrix which unlike forward approximation must be inverted to give U<sub>n+1</sub> like in forward approximation instead of U<sub>n</sub>


![\begin{align*}
\begin{matrix}
Backward
\end{matrix}
\begin{matrix}
Y_{n+1} = Y_n + &Delta;t Z_{n+1}\\
Z_{n+1} = Z_n - &Delta;t Y_{n+1}
\end{matrix}
& \begin{matrix} is \end{matrix} \, \, \, \, \, \, \, \, \,  \, \, \, \, \, \, 
Au_{n+1} =
\begin{bmatrix}
1&-&Delta; \, t\\
&Delta; \, t&1\\
\end{bmatrix}
\begin{bmatrix}
Y_{n+1}\\
Z_{n+1}\\
\end{bmatrix}=
\begin{bmatrix}
Y_{n}\\
Z_{n}\\
\end{bmatrix}=
U_{n}\\
& \begin{matrix} inverted \end{matrix}
U_{n+1} =
\begin{bmatrix}
Y_{n+1}\\
Z_{n+1}\\
\end{bmatrix}=
\frac{1}{(&Delta;t)^2} 
\begin{bmatrix}
1&&Delta; \, t\\
-&Delta; \, t&1\\
\end{bmatrix}
\begin{bmatrix}
Y_{n}\\
Z_{n}\\
\end{bmatrix}=A^{-1}U_n
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cbegin%7Bmatrix%7D%0ABackward%0A%5Cend%7Bmatrix%7D%0A%5Cbegin%7Bmatrix%7D%0AY_%7Bn%2B1%7D+%3D+Y_n+%2B+%26Delta%3Bt+Z_%7Bn%2B1%7D%5C%5C%0AZ_%7Bn%2B1%7D+%3D+Z_n+-+%26Delta%3Bt+Y_%7Bn%2B1%7D%0A%5Cend%7Bmatrix%7D%0A%26+%5Cbegin%7Bmatrix%7D+is+%5Cend%7Bmatrix%7D+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C++%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%5C%2C+%0AAu_%7Bn%2B1%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-%26Delta%3B+%5C%2C+t%5C%5C%0A%26Delta%3B+%5C%2C+t%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AY_%7Bn%2B1%7D%5C%5C%0AZ_%7Bn%2B1%7D%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AY_%7Bn%7D%5C%5C%0AZ_%7Bn%7D%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0AU_%7Bn%7D%5C%5C%0A%26+%5Cbegin%7Bmatrix%7D+inverted+%5Cend%7Bmatrix%7D%0AU_%7Bn%2B1%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0AY_%7Bn%2B1%7D%5C%5C%0AZ_%7Bn%2B1%7D%5C%5C%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cfrac%7B1%7D%7B%28%26Delta%3Bt%29%5E2%7D+%0A%5Cbegin%7Bbmatrix%7D%0A1%26%26Delta%3B+%5C%2C+t%5C%5C%0A-%26Delta%3B+%5C%2C+t%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AY_%7Bn%7D%5C%5C%0AZ_%7Bn%7D%5C%5C%0A%5Cend%7Bbmatrix%7D%3DA%5E%7B-1%7DU_n%0A%5Cend%7Balign%2A%7D)

Y is horizontal axis and Z is the vertical

Forward difference makes Y<sub>n+1</sub> and Z<sub>n+1</sub> forward value from Y<sub>n</sub> and Z<sub>n</sub> added to some &Delta;t increment. Forward Y<sub>n+1</sub> is the sum of current Y<sub>n</sub> plus a &Delta;t increment of current Z<sub>n</sub>.  Forward Z<sub>n+1</sub> is the sum of current Z<sub>n</sub> plus a &Delta;t increment of current Y<sub>n</sub>.  The forward method starts with U<sub>0</sub> at its correct value [ 1, 0 ] and then goes off course as it spirals outward.

Backward difference makes Y<sub>n</sub> and Z<sub>n</sub> backward value from Y<sub>n+1</sub> and Z<sub>n+1</sub> added to some &Delta;t increment. Backward Y<sub>n</sub> is the sum of forward Y<sub>n+1</sub> plus a &Delta;t increment of forward Z<sub>n+1</sub>.  Backward Z<sub>n</sub> is the sum of forward Z<sub>n+1</sub> plus a &Delta;t increment of forward Y<sub>n+1</sub>.  The backward method starts with U<sub>0</sub> at its correct value [ 1, 0 ] and then goes off course as it spirals inward.

both travel in clockwise fashion.

to see the results:  these do the perfect unit circle from [cos&theta;, -sin&theta;], euler's forward spiral approximation, and euler's backward spiral approximation.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108892683-28a4a380-75de-11eb-9413-df872a44ca46.png">

<img width="752" alt="image" src="https://user-images.githubusercontent.com/38410965/108891445-ba131600-75dc-11eb-9940-a66d2f3882b7.png">

<img width="752" alt="image" src="https://user-images.githubusercontent.com/38410965/108891510-ceefa980-75dc-11eb-9bc4-9ec4fce3df17.png">

<img width="752" alt="image" src="https://user-images.githubusercontent.com/38410965/108891564-ddd65c00-75dc-11eb-99e1-953485810584.png">

with this code:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108892835-5558bb00-75de-11eb-8a89-8164dc2db795.png">

the &lambda;'s tell all.

both the forward and original backward matrix A have eigenvalues 1 &pm; i&Delta;t   
test the magnitude |&lambda;| not the real parts.   

the inverted A from backward method has &lambda; magnitudes <1 and so spirals inwards.

- i = 0 + i
- | i | = | - i | = 1
- | 1 + i | = | - ( 1 + i ) | = | 1 - i | =  | - ( 1 - i ) |  = | -1 + i | =  | - ( -1 - i ) |  = 1.41 = √2

magnitude is computed same as vector length for complex number a + bi, magnitude = | a + b | = ( a<sup>2</sup> + b<sup>2</sup> )<sup>0.5</sup>

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108898247-fa769200-75e4-11eb-9fb3-cb34bd658c75.png">

notice that the original backward method would spiral out like the forward method because it has the EXACT same &lambda;s as forward approximation that are > 1.  this is because backward method is initially approximating U<sub>n</sub> from U<sub>n+1</sub>.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108899208-2a726500-75e6-11eb-9880-f24b1895fe79.png">

&lambda;s for original backward approximation A are 1 &pm; i&Delta;t whose magnitude is | 1 &pm; &Delta;t | > 1 

can see that below where LAMBDA for &lambda;s are 1 &pm; i&Delta; in the first highlighted line

for the inverse of backwards approximation A, the | &lambda;s | are < 1 as shown in the second highlighted line where &lambda;s are < 1 because they equal 1 divided by 1 &pm; i&Delta;t  that is > 1.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108904163-2b0dfa00-75ec-11eb-88a1-92f11bd61524.png">


in the leapfrog method   
32 steps are taken with the centered choice and stays on the circle.   
in equations 11C, the leapfrog method's second difference Y<sub>n+1</sub> - 2Y<sub>n</sub> + Y<sub>n-1</sub> leaps over the center value Y<sub>n</sub>

in reality, y is the unknown, a vector.   
the coefficient of y'' is a mass matrix M with n masses.  
the coefficient of y is a stiffness matrix K (not a number k).   
the coefficient of y' is a dampening matrix which might be zero.  
the vector equatoin My'' + Ky = f is a major part of computational mechanics.  it is controlled by the eigenvalues of M<sup>-1</sup>K in Kx = &lambda;Mx [I am guessing that is because M<sup>-1</sup>Kx = &lambda;x]

**Stability of 2 x 2 matrices**

Does the solution to ∂u / ∂t = Au approach u = 0 as t approaches ∞ ?

stable dissipates energy.

e<sup>t</sup> is unstable.  

stability depends on a the eigenvalues &lambda;s of A.

the complete solution u(t) is built from the pure solutions e<sup>&lambda;t</sup>x   
if the eigenvalue is real, we know exactly when e<sup>&lambda;t</sup> will approach zero.   
&lambda; must be negative [because then e<sup>&lambda;t</sup> is < 1]   
if the eigenvalue is complex, &lambda; = r + is then the real part r must be negative  
when e<sup>&lambda;t</sup> splits in to e<sup>r•t</sup> and e<sup>is•t</sup>, the factor e<sup>is•t</sup> has absolute value fixed at 1 because:   
e<sup>is•t</sup> = cos(s • t) + i • sin(s • t)   
which has    
| e<sup>is • t</sup> |<sup>2</sup> = cos<sup>2</sup>(s • t) + i • sin<sup>2</sup>(s • t) = 1    
[ notice magnitude absolute value is taken before the squaring so the i drops away ]

the real part of &lambda; controls the growth ( real part r > 0 ) ir decay ( real part r < 0 )   
[because the imaginary part e<sup>is • t</sup> always stays on the circle |e<sup>is • t</sup>|<sup>2</sup> = 1]

the question is which matrices have negative eigenvalues?  when are the real parts of &lambda;s all negative.  2x2 matrices allow a clear answer.  

**stability**

A is stable and u(t) --> 0 when all eigenvalues &lambda; have negative real parts.  

2 x 2 A must pass 2 tests: the trace T = a + d = &lambda;<sub>1</sub> + &lambda;<sub>2</sub> < 0 and the determinant D = ad - bc = &lambda;<sub>1</sub>&lambda;<sub>2</sub> > 0

IFF both are real and negative, then their sum must be negative: T = a + d < 0  
IFF both signs are the same, then their product must be positive: D = ad - bc > 0

IFF means the logic works in reverse:

if D = ad - bc = &lambda;<sub>1</sub>&lambda;<sub>2</sub> > 0, the both share the same sign. 
then, if T = a + d = &lambda;<sub>1</sub> + &lambda;<sub>2</sub> < 0 then both are real and their shared signs will be [real and] negative. 

if the &lambda;s are complex numbers, they must have the paired form r + is and r - is.  
otherwise T = a + d = &lambda;<sub>1</sub> + &lambda;<sub>2</sub> and T = ad - bc = &lambda;<sub>1</sub>&lambda;<sub>2</sub> will not be real.  [the imaginary bits won't cancel.]    

the determinant is automatically positive since ( r + is ) ( r - is ) = ( r<sub>2</sub> + s<sub>2</sub> )

the trace T is r + is  + r - is = 2r is real.  
a negative trace T means the real part is negative.  and thus the matrix is stable Q.E.D.

the figure shows parabola T<sup>2</sup> = 4D separating real &lambda;s from complex &lambda;s.  

the matrices in general would:      
- be stable in the 4th quadrant:    
  - on the LHS of the vertical axis D where T = a + d = &lambda;<sub>1</sub> + &lambda;<sub>2</sub> < 0    
  - AND above the horizontal axis T where D = ad - bc = &lambda;<sub>1</sub>&lambda;<sub>2</sub> > 0 indicating that signs for both &lambda;s are the same.    
- be unstable in the 1st quadrant:    
  - on the RHS of the veritcal axis D where T = a + d = &lambda;<sub>1</sub> + &lambda;<sub>2</sub> < 0 and so at least one &lambda; > 0    
  - AND above the horizontal axis T where D = ad - bc = &lambda;<sub>1</sub>&lambda;<sub>2</sub> > 0 indicating that signs for both &lambda;s are the same and thus both &lambda;s > 0.    
- be unstable in the 2nd and 3rd quadrants below the horizontal axis T where determinant D = ad - bc = &lambda;<sub>1</sub>&lambda;<sub>2</sub> < 0 indicating that &lambda;<sub>1</sub> < 0 and &lambda;<sub>2</sub> > 0.    
- have real &lambda;s above the parabola since the roots quadratic for the determinant of [ A - &lambda; I ] = 0 are found in equation &lambda; = T &pm; (T^2 - 4D)<sup>1/2</sup>.  This means that when the roots of &lambda;<sup>2</sup> - T&lambda; + D are derived from the quadratic formula if the term (T<sup>2</sup> - 4D) < 0 then both &lambda;s are complex.  This is shown by the parabola which represents points for matrices' (T, D) pairs where D = T<sup>2</sup> / 4.  If below the parabola, then D < T<sup>2</sup> / 4  and both &lambda;s are complex.   

the example matrices in the plot are:     
- stable matrix has T = a + d = 0 - 3 = - 3 < 0 and D = ad - bc = 2 > 0 so both &lambda;s are < 0 indicating stability since u(t) --> 0 as t --> ∞.  Since D = 0 + 2 < T<sup>2</sup> / 4 = (-3)<sup>2</sup> / 4 = 9/4, both &lambda;s are complex.    PURPLE.
- unstable matrix has T = a + d = 0 - 6 = - 6 < 0 and D = ad - bc = -20 < 0 so they have mixed signs such that the 1st &lambda;s is > 0 and the 2nd &lambda;s is < 0.  D < 0 indicates instability for this reason.   Since D = -20 < T<sup>2</sup> / 4 = (-6)<sup>2</sup> / 4 = 9, both &lambda;s are complex.  AQUA
- neutral matrix has T = a + d = 0 and so neither < 0 or > 0 and D = ad - bc = 49 > 0 indicating that the product of the &lambda;s > 0 indicating they have the same sign.  Zero for &lambda;s is neutral.  Since D = 49 > T<sup>2</sup> / 4 = (0)<sup>2</sup> / 4 = 0, both &lambda;s are real. YELLOW.

![\begin{align*}
\begin{bmatrix}
0&-1 \\
2&-3 \\
\end{bmatrix} &--> \begin{matrix}T = a+d = -3; \, D = ad-bc = 2; & D = 2 < \frac{T^2}{4} = \frac{9}{4}\end{matrix} --> \begin{matrix}
stable ; &complex 
\end{matrix}
\\
\begin{bmatrix}
0&4 \\
5& -6\\
\end{bmatrix} &--> \begin{matrix} T = a+d = -6; \, D = ad-bc = -20; & \, D = -20 < \frac{T^2}{4} = \frac{36}{4} \end{matrix}
 --> \begin{matrix}
unstable ; &complex 
\end{matrix}
\\
\begin{bmatrix}
0&-7 \\
7&0 \\
\end{bmatrix} &--> \begin{matrix} T = a+d = 0; \, D = ad-bc = 49; & \, D = 49 > \frac{T^2}{4} = \frac{0}{4} \end{matrix}
 --> \begin{matrix}
neutral ; &real 
\end{matrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cbegin%7Bbmatrix%7D%0A0%26-1+%5C%5C%0A2%26-3+%5C%5C%0A%5Cend%7Bbmatrix%7D+%26--%3E+%5Cbegin%7Bmatrix%7DT+%3D+a%2Bd+%3D+-3%3B+%5C%2C+D+%3D+ad-bc+%3D+2%3B+%26+D+%3D+2+%3C+%5Cfrac%7BT%5E2%7D%7B4%7D+%3D+%5Cfrac%7B9%7D%7B4%7D%5Cend%7Bmatrix%7D+--%3E+%5Cbegin%7Bmatrix%7D%0Astable+%3B+%26complex+%0A%5Cend%7Bmatrix%7D%0A%5C%5C%0A%5Cbegin%7Bbmatrix%7D%0A0%264+%5C%5C%0A5%26+-6%5C%5C%0A%5Cend%7Bbmatrix%7D+%26--%3E+%5Cbegin%7Bmatrix%7D+T+%3D+a%2Bd+%3D+-6%3B+%5C%2C+D+%3D+ad-bc+%3D+-20%3B+%26+%5C%2C+D+%3D+-20+%3C+%5Cfrac%7BT%5E2%7D%7B4%7D+%3D+%5Cfrac%7B36%7D%7B4%7D+%5Cend%7Bmatrix%7D%0A+--%3E+%5Cbegin%7Bmatrix%7D%0Aunstable+%3B+%26complex+%0A%5Cend%7Bmatrix%7D%0A%5C%5C%0A%5Cbegin%7Bbmatrix%7D%0A0%26-7+%5C%5C%0A7%260+%5C%5C%0A%5Cend%7Bbmatrix%7D+%26--%3E+%5Cbegin%7Bmatrix%7D+T+%3D+a%2Bd+%3D+0%3B+%5C%2C+D+%3D+ad-bc+%3D+49%3B+%26+%5C%2C+D+%3D+49+%3E+%5Cfrac%7BT%5E2%7D%7B4%7D+%3D+%5Cfrac%7B0%7D%7B4%7D+%5Cend%7Bmatrix%7D%0A+--%3E+%5Cbegin%7Bmatrix%7D%0Aneutral+%3B+%26real+%0A%5Cend%7Bmatrix%7D%0A%5Cend%7Balign%2A%7D)


<img width="752" alt="image"
src="https://user-images.githubusercontent.com/38410965/108933015-5d355100-7618-11eb-9811-4d790f4f839b.png">


<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108933056-750cd500-7618-11eb-88fd-9e89bc507584.png">

plotted by this code

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/108941568-5829cf00-7623-11eb-946c-6465f82e9e3b.png">


**the exponet of a matrix**

u(t) = e<sup>At</sup>u(0) 

for a clue as to what does e<sup>At</sup> mean, look at:

e<sup>x</sup> = 1/0! x<sup>0</sup> + 1/1! x<sup>1</sup> + 1/2! x<sup>2</sup> + ... + 1/n! x<sup>n</sup>  

change x to a square matrix At this series defines matrix expoential e<sup>At</sup>   

matrix exponential e<sup>At</sup> = I + At + 1/2 (At)<sup>2</sup> + 1/6 (At)<sup>3</sup> + ... = ∑<sub>1=0</sub><sup>∞</sup> 1 / ( i ! ) • ( At )<sup>i</sup>

matrix exponential's t derivative = Ae<sup>At</sup> = Au = A + A<sup>2</sup>t + 1/2 A<sup>3</sup>t<sup>2</sup> + 1/6 A<sup>4</sup>t<sup>3</sup> + ... = A • ∑<sub>1=0</sub><sup>∞</sup> 1 / ( i ! ) • ( At )<sup>i</sup>

eigenvalues of are  e<sup>&lambda;t</sup> = (I + &lambda;t + 1/2! (&lambda;t)<sup>2</sup> + 1/3! (&lambda;t)<sup>3</sup> + ... + 1/∞! (&lambda;t)<sup>∞</sup>)x = (∑<sub>1=0</sub><sup>∞</sup> 1 / ( i ! ) • ( &lambda;t )<sup>i</sup>)x 

[ I am not sure about that x at the end of the last formulae]

e<sup>At</sup>u(0) solves EVEN IF there is a shortcoming of eigenvectors, as shown in the formula way above. 

u' = Au --> u(t) = e<sup>At</sup>u(0)

with n independent eigenvectors A is diagonalizable allowing X&Lambda;X<sup>-1</sup> substitution into the series e<sup>At</sup> and whenever X&Lambda;X<sup>-1</sup>X&Lambda;X<sup>-1</sup> appears in the series, cancel the X<sup>-1</sup>X in the middle to get back to X&Lambda;X<sup>-1</sup>

start with:  
e<sup>At</sup>u(0) = ∑<sub>j=0</sub><sup>∞</sup> (1/j!)(At)<sup>j</sup> = I + At + (At)<sup>2</sup>/2 + (At)<sup>3</sup>/6 + ... + (At)<sup>∞</sup>/∞!

diagonalize A:  
e<sup>At</sup>u(0) = ∑<sub>j=0</sub><sup>∞</sup> (1/j!)(X&Lambda;X<sup>-1</sup>t)<sup>j</sup> = I + X&Lambda;X<sup>-1</sup>t + (X&Lambda;X<sup>-1</sup>t)<sup>2</sup>/2 + (X&Lambda;X<sup>-1</sup>t)<sup>3</sup>/6 + ... + (X&Lambda;X<sup>-1</sup>t)<sup>∞</sup>/∞!

factor out X<sup>-1</sup>X from the middle of the powers of (X&Lambda;X<sup>-1</sup>t)<sup>i</sup>:   
e<sup>At</sup>u(0) = X∑<sub>j=0</sub><sup>∞</sup> (1/j!)(&Lambda;t)<sup>j</sup>X<sup>-1</sup> = X ( I + &Lambda;t + (&Lambda;t)<sup>2</sup>/2 + (&Lambda;t)<sup>3</sup>/6 + ... + (&Lambda;)<sup>∞</sup>/∞!) X<sup>-1</sup>

the sum of the (&lambda;<sub>i</sub>t)<sup>i</sup>/( i !) appearing in each of the (i,i) cells of each &Lambda; in the last equation equals e<sup>&lambda;t<sub>i</sub></sup> in the diagonal matrix represented by e<sup>&Lambda;t</sup> in this equation:   
e<sup>At</sup> = Xe<sup>&Lambda;t</sup>X<sup>-1</sup>

e<sup>At</sup> has the same eigenvector matrix X as A.  
then &Lambda; is a diagonal matrix and so is e<sup>&Lambda;t</sup> with e<sup>&lambda;<sub>i</sub>t</sup> on its diagonal.

Multiply Xe<sup>&Lambda;t</sup>X<sup>-1</sup> by u(0) to recognize u(t))



![\begin{align*}
\\
u(t) & = e^{At}u(0) = Xe^{&Lambda;t}X^{-1}u(0) =  
\begin{bmatrix}
x_1&x_2&x_3\\
\end{bmatrix}
\begin{bmatrix}
e^{&Lambda;_1t}&0&0\\
0&e^{&Lambda;_2t}&0\\
0&0&e^{&Lambda;_3t}
\end{bmatrix}
\begin{bmatrix}
c_1\\c_2\\c_3\\
\end{bmatrix}
=X e^{&Lambda;t}c\\
\\
\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5C%5C%0Au%28t%29+%26+%3D+e%5E%7BAt%7Du%280%29+%3D+Xe%5E%7B%26Lambda%3Bt%7DX%5E%7B-1%7Du%280%29+%3D++%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B%26Lambda%3B_1t%7D%260%260%5C%5C%0A0%26e%5E%7B%26Lambda%3B_2t%7D%260%5C%5C%0A0%260%26e%5E%7B%26Lambda%3B_3t%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ac_1%5C%5Cc_2%5C%5Cc_3%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3DX+e%5E%7B%26Lambda%3Bt%7Dc%5C%5C%0A%5C%5C%0A%5C%5C%0A%5Cend%7Balign%2A%7D)


the solution e<sup>At</sup>u(0) is the same answer that came in equations from 3 steps:   
1. u(0) = c<sub>1</sub>x<sub>1</sub> + ... + c<sub>n</sub>x<sub>n</sub> = Xc  
for this we need independent eigenvectors  
2. multiply each x<sub>j</sub> by its growth factor e<sup>&lambda;<sub>i</sub>t</sup> to follow it forward in time [with t in the next step; t only enters the following equation with &lambda;s]    
3. the best form of e<sup>At</sup>u(0) is u(t) = c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup>x<sub>1</sub> + ... + c<sub>n</sub>e<sup>&lambda;<sub>n</sub>t</sup>x<sub>n</sub>

**example 4**

substitute y = e<sup>&lambda;t</sup> into y'' - 2y' + y = 0 to get an equation with repeated roots.   
[Here, Strang skips this step presented that was presented earlier.]  

(e<sup>&lambda;t</sup>)'' - 2 (e<sup>&lambda;t</sup>) + e<sup>&lambda;t</sup> = 0     
&lambda;<sup>2</sup>e<sup>&lambda;t</sup> - &lambda;e<sup>&lambda;t</sup> + e<sup>&lambda;t</sup> = 0   
( &lambda;<sup>2</sup> - &lambda; + 1 ) e<sup>&lambda;t</sup> = 0   
which factors to  
( &lambda; - 1 )<sup>2</sup> = 0   
producing &lambda;<sub>1</sub> = &lambda;<sub>2</sub> = 1.

A differentials equations course would propose e<sup>t</sup> and te<sup>t</sup> as 2 independent solutions.  Why ?

y'' - 2y' +y = 0 reduces to a vector equation for u = ( y, y' ) 

∂ [ y, y' ] / ∂ t  = [ [ y ], [ 2y' - y ] is derived from knowing ∂ y = y' in general and ∂ y' = y'' = 2y' - y in our original equation y'' - 2y' + y = 0 converts to y'' = 2y' - y    

u = [ y, y' ] then ∂u / ∂t = Au = [ [ 0, 1 ], [ -1, 2 ] ] • u = [ [ 0, 1 ], [ -1, 2 ] ] • [ y, y' ] = [ [ y ], [ 2y' - y ]  

A has  
- repeated eigenvalues &lambda;<sub>1</sub> = &lambda;<sub>2</sub> = 1 
- trace T = 2  
- determinant D = 1 

det [ A - &lambda; • I ] = det [ [ 0 - &lambda;, 1 ], [ -1, 2 - &lambda; ] ] = 0 = &lambda;<sup>2</sup> - 2&lambda; + 1 = (&lambda; - 1)<sup>2</sup> --> &lambda;<sub>1</sub> = &lambda;<sub>2</sub> = 1 

the only eigenvectors in the null space of det [ A - &lambda; • I ]  = det [ A - I ] are multiples of x = ( 1, 1 ):  

[ [ -1, 1 ], [ -1, 1 ] ] • [ 1, 1 ] = [ 0, 0 ]

Diagonalization is not possible,  A has only one line of eigenvectors.  

Instead compute e<sup>At</sup> from its definition as a series:  

e<sup>At</sup> = I + At + (At)<sup>2</sup> + ..., but A<sup>2</sup> = 0 

e<sup>At</sup> = e<sup>It</sup>e<sup>(A-I)t</sup> = e<sup>t</sup>[ I ] e<sup>( A-I ) t </sup> 

[ regard the first factor = e<sup>It</sup> = e<sup>t</sup> and the second factor = e<sup>(A-I)t</sup> as the expoential for the series (A-I)t which would start as all exponential series do with ( ( A-I )t )<sup>0</sup> / 0! = I; so e<sup>( A - I ) t</sup> = [ I + (A - I )t and the two factors together are e<sup>t</sup>[ I + (A - I )t ] as shown.]

e<sup>At</sup> = e<sup>t</sup> [ I + ( A - I ) t ] 

∂u / ∂t = Au where u = [ y, y' ] = e<sup>At</sup> = e<sup>t</sup>[ I + ( A - I ) t ] [ y(0), y'(0) ] 

from this, see 1st component contains the answer of e<sup>At</sup>u(0) is our answer y(t) :

![\begin{align*}
e^{At}u(0)=
\begin{bmatrix}
y\\
y'
\end{bmatrix}
&=
e^t \, 
\begin{bmatrix}
I+
\begin{bmatrix}
-1&1\\
-1&1
\end{bmatrix} \, t 
\end{bmatrix} 
\begin{bmatrix}
y(0)\\
y'(0)
\end{bmatrix}\\
&=
\begin{bmatrix}
e^t y(0)\\
e^t y'(0)
\end{bmatrix} 
+
e^t
\begin{bmatrix}
-t&t\\
-t&t
\end{bmatrix}
\begin{bmatrix}
y(0)\\
y'(0)
\end{bmatrix}\\
&=
\begin{bmatrix}
e^t y(0)\\
e^t y'(0)
\end{bmatrix} 
+
\begin{bmatrix}
-te^t &te^t \\
-te^t &te^t 
\end{bmatrix}
\begin{bmatrix}
y(0)\\
y'(0)
\end{bmatrix}\\
&=
\begin{bmatrix}
e^t y(0)-te^ty(0) +te^ty(0) \\
e^t y'(0)-te^ty'(0) +te^ty'(0) 
\end{bmatrix}
\, \, \, \, --> 
y(t) = e^ty(0)-te^t y(0) + te^t y'(0)
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ae%5E%7BAt%7Du%280%29%3D%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Ay%27%0A%5Cend%7Bbmatrix%7D%0A%26%3D%0Ae%5Et+%5C%2C+%0A%5Cbegin%7Bbmatrix%7D%0AI%2B%0A%5Cbegin%7Bbmatrix%7D%0A-1%261%5C%5C%0A-1%261%0A%5Cend%7Bbmatrix%7D+%5C%2C+t+%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ay%280%29%5C%5C%0Ay%27%280%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5Et+y%280%29%5C%5C%0Ae%5Et+y%27%280%29%0A%5Cend%7Bbmatrix%7D+%0A%2B%0Ae%5Et%0A%5Cbegin%7Bbmatrix%7D%0A-t%26t%5C%5C%0A-t%26t%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ay%280%29%5C%5C%0Ay%27%280%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5Et+y%280%29%5C%5C%0Ae%5Et+y%27%280%29%0A%5Cend%7Bbmatrix%7D+%0A%2B%0A%5Cbegin%7Bbmatrix%7D%0A-te%5Et+%26te%5Et+%5C%5C%0A-te%5Et+%26te%5Et+%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ay%280%29%5C%5C%0Ay%27%280%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5Et+y%280%29-te%5Ety%280%29+%2Bte%5Ety%280%29+%5C%5C%0Ae%5Et+y%27%280%29-te%5Ety%27%280%29+%2Bte%5Ety%27%280%29+%0A%5Cend%7Bbmatrix%7D%0A%5C%2C+%5C%2C+%5C%2C+%5C%2C+--%3E+%0Ay%28t%29+%3D+e%5Ety%280%29-te%5Et+y%280%29+%2B+te%5Et+y%27%280%29%0A%5Cend%7Balign%2A%7D)


**example 5**

inifite series reveals e<sup>At</sup> for A = [ 0, 1 ] [ -1, 0 ]  

notice A<sup>4</sup> = I

powers of A repeat:   
A<sup>1</sup>, A<sup>2</sup>, A<sup>3</sup>, A<sup>4</sup>   
A<sup>5</sup>, A<sup>6</sup>, A<sup>7</sup>, A<sup>8</sup>
repeat: TR corner repeats 1, 0, -1, 0 in powers of A.

the infinite series for e<supAt</sup> features 
t - (1/6) t<sup>3</sup> in the TR corner
1 - (1/2) t<sup>2</sup> in the TL corner

e<sup>At</sup> = ∑<sub>j=0</sub><sup>∞</sup> (At)<sup>j</sup> / ( j ! )

the top row of this matrix shows the inifite series for cos and sin

![\begin{align*}
A &= \begin{bmatrix}
0&1\\
-1&0
\end{bmatrix}
&A^2 = \begin{bmatrix}
-1&0\\
0&-1
\end{bmatrix}
&&A^3 = \begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
&&A^4 = \begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%26%3D+%5Cbegin%7Bbmatrix%7D%0A0%261%5C%5C%0A-1%260%0A%5Cend%7Bbmatrix%7D%0A%26A%5E2+%3D+%5Cbegin%7Bbmatrix%7D%0A-1%260%5C%5C%0A0%26-1%0A%5Cend%7Bbmatrix%7D%0A%26%26A%5E3+%3D+%5Cbegin%7Bbmatrix%7D%0A0%26-1%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D%0A%26%26A%5E4+%3D+%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A0%261%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)


![\begin{align*}
e^{At}= I  &&+ \frac{(At)^1}{1!} &&+ \frac{(At)^2}{2!} && +\frac{(At)^3}{3!} && 
+\frac{(At)^4}{4!} &&+ \. ... \\
&TR&1&& 0& & -1&& 0 \\
&TL & 0 && -1 && 0 && 1 \\
&BR & 0 && -1 && 0 && 1 \\
&BL & -1 && 0 && 1 && 0 \\
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ae%5E%7BAt%7D%3D+I++%26%26%2B+%5Cfrac%7B%28At%29%5E1%7D%7B1%21%7D+%26%26%2B+%5Cfrac%7B%28At%29%5E2%7D%7B2%21%7D+%26%26+%2B%5Cfrac%7B%28At%29%5E3%7D%7B3%21%7D+%26%26+%0A%2B%5Cfrac%7B%28At%29%5E4%7D%7B4%21%7D+%26%26%2B+%5C.+...+%5C%5C%0A%26TR%261%26%26+0%26+%26+-1%26%26+0+%5C%5C%0A%26TL+%26+0+%26%26+-1+%26%26+0+%26%26+1+%5C%5C%0A%26BR+%26+0+%26%26+-1+%26%26+0+%26%26+1+%5C%5C%0A%26BL+%26+-1+%26%26+0+%26%26+1+%26%26+0+%5C%5C%0A%5Cend%7Balign%2A%7D%0A)



![\begin{align*}
e^{At} &= I  + \,
\begin{bmatrix}
-\frac{1}{2}t^2+...&t-\frac{1}{6}t^3+...\\
-t+\frac{1}{6}t^3+...&-\frac{1}{2}t^2+...
\end{bmatrix}\\
&=
\begin{bmatrix}
1-\frac{1}{2}t^2+...&t-\frac{1}{6}t^3+...\\
-t+\frac{1}{6}t^3+...&1-\frac{1}{2}t^2+...
\end{bmatrix}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ae%5E%7BAt%7D+%26%3D+I++%2B+%5C%2C%0A%5Cbegin%7Bbmatrix%7D%0A-%5Cfrac%7B1%7D%7B2%7Dt%5E2%2B...%26t-%5Cfrac%7B1%7D%7B6%7Dt%5E3%2B...%5C%5C%0A-t%2B%5Cfrac%7B1%7D%7B6%7Dt%5E3%2B...%26-%5Cfrac%7B1%7D%7B2%7Dt%5E2%2B...%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1-%5Cfrac%7B1%7D%7B2%7Dt%5E2%2B...%26t-%5Cfrac%7B1%7D%7B6%7Dt%5E3%2B...%5C%5C%0A-t%2B%5Cfrac%7B1%7D%7B6%7Dt%5E3%2B...%261-%5Cfrac%7B1%7D%7B2%7Dt%5E2%2B...%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D%0A)


![\begin{align*}
A &= \begin{bmatrix}
0&1\\
-1&0
\end{bmatrix}\\
e^{At} &= \begin{bmatrix}
cos t&sin t\\
-sin t&cos t
\end{bmatrix}\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%26%3D+%5Cbegin%7Bbmatrix%7D%0A0%261%5C%5C%0A-1%260%0A%5Cend%7Bbmatrix%7D%5C%5C%0Ae%5E%7BAt%7D+%26%3D+%5Cbegin%7Bbmatrix%7D%0Acos+t%26sin+t%5C%5C%0A-sin+t%26cos+t%0A%5Cend%7Bbmatrix%7D%5Cend%7Balign%2A%7D%0A)


![\begin{align*}
A &= \begin{bmatrix}
0&1\\
-1&0
\end{bmatrix}\\
e^{At} &= \begin{bmatrix}
cos t&sin t\\
-sin t&cos t
\end{bmatrix}\\
|A - &lambda;I| &= \begin{bmatrix}
-&lambda;&1\\
-1&-&lambda;
\end{bmatrix}\\
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%26%3D+%5Cbegin%7Bbmatrix%7D%0A0%261%5C%5C%0A-1%260%0A%5Cend%7Bbmatrix%7D%5C%5C%0Ae%5E%7BAt%7D+%26%3D+%5Cbegin%7Bbmatrix%7D%0Acos+t%26sin+t%5C%5C%0A-sin+t%26cos+t%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%7CA+-+%26lambda%3BI%7C+%26%3D+%5Cbegin%7Bbmatrix%7D%0A-%26lambda%3B%261%5C%5C%0A-1%26-%26lambda%3B%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cend%7Balign%2A%7D%0A)

A is an antisymmetric matrix (A<sup>T</sup> = -A)  
A's exponential e<sup>At</sup> is an orthogonal matrix.

The eigenvalues of A are i and -i  

![\begin{align*}
|A-&lambda;I| &= \begin{bmatrix}
-&lambda;&0\\
-1&-&lambda;
\end{bmatrix} = (-&lambda;^2 + 1) = (-&lambda; - i)(-&lambda; + i) --> -&lambda; = i, -i
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%7CA-%26lambda%3BI%7C+%26%3D+%5Cbegin%7Bbmatrix%7D%0A-%26lambda%3B%260%5C%5C%0A-1%26-%26lambda%3B%0A%5Cend%7Bbmatrix%7D+%3D+%28-%26lambda%3B%5E2+%2B+1%29+%3D+%28-%26lambda%3B+-+i%29%28-%26lambda%3B+%2B+i%29+--%3E+-%26lambda%3B+%3D+i%2C+-i%0A%5Cend%7Balign%2A%7D)

The eigenvalues of e<sup>At</sup> are e<sup>it</sup> and e<sup>-it</sup>

![\begin{align*}
|e^{At}-&lambda;I| &= \begin{bmatrix}
cos t-&lambda;&sin t\\
-sin t&cos t-&lambda;
\end{bmatrix} = (&lambda;^2 -2&lambda; cos t + cos^2t + sin^2t) 
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%7Ce%5E%7BAt%7D-%26lambda%3BI%7C+%26%3D+%5Cbegin%7Bbmatrix%7D%0Acos+t-%26lambda%3B%26sin+t%5C%5C%0A-sin+t%26cos+t-%26lambda%3B%0A%5Cend%7Bbmatrix%7D+%3D+%28%26lambda%3B%5E2+-2%26lambda%3B+cos+t+%2B+cos%5E2t+%2B+sin%5E2t%29+%0A%5Cend%7Balign%2A%7D)




three rules:
1. e<sup>At</sup> always has the inverse e<sup>-At</sup>   
2. the eigenvalues of e<sup>At</sup> are always e<sup>&lambda;t</sup>   
3. when A is antisymmetric e<sup>At</sup> is orthogonal: inverse = transpose

anti-symmetric = skew symmetric  
- have pure imaginary eigenvalues
- then e<sup>At</sup> has eigenvalues e<sup>it</sup> and e<sup>-it</sup> with absolute value 1: | e<sup>i</sup> | = 1
- so || u(t) || = || u(0) ||

[ | (e<sup>i</sup>)<sup>3</sup> =  e<sup>3i</sup> = -0.9899924966004455+0.1411200080598674j | = 1 ]
- natural stability, pure oscillation, energy is conserved

**example 6**

triangular A  
thus eigenvector matrix X is triangular   
thus X<sup>-1</sup> is triangular  
and of course e<sup>At</sup> is triangular  

2 forms of solution:  
- a combination of eigenvectors    
- short form e<sup>At</sup>u(0)   

solve ∂u/∂t = Au = [[1,1],[0,2]]u for u(t) starting from u(0) = (2,1) at t = 0

the eigenvalues of A are on the diagonal since it is triangular.  
the eigenvectors of A are x<sub>1</sub> = (1,0) and x<sub>2</sub> = (1,1)   
the starting u(0) = (2,1) = x<sub>1</sub> + x<sub>2</sub> and so c<sub>1</sub> = c<sub>2</sub> = 1   
can confirm with Xc = u(0)   
then u(t)  is same combination of pure exponentials.   
there is not te<sup>&lambda;t when &lambda; = 1 and 2:    
solution to u' = Au is u(t)  = e<sup>t</sup>[1,0] + e<sup>2t</sup>[1,1]  
that is the clearest form but the matrix form with e<sup>At</sup> produces u(t) for every u(0)


the last matrix is e<sup>At</sup> [solution to ∂u/∂t = Au is always e<sup>At</sup> = Xe<sup>&Lambda;t</sup>X<sup>-1</sup>]

It's nice because A is triangular.   
the situationis the same as for Ax = b and inverses.  we dont need A<sup>-1</sup> to find X and we dont need e<sup>At</sup> to solve ∂u/∂t = Au.

But as quick formulas for the answers, A<sup>-1</sup>b and e<sup>At</sup>u(0) are unbeatable. 

![\begin{align*}
\begin{bmatrix}
1&1\\
0& 1
\end{bmatrix} 
\begin{bmatrix}
e^t& \\
& e^{2t}
\end{bmatrix} 
\begin{bmatrix}
1&-1\\
0& 1
\end{bmatrix} \, u(0)= 
\begin{bmatrix}
e^t&e{2t}+e^t\\
0& e{2t}
\end{bmatrix} \, u(0)
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A0%26+1%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ae%5Et%26+%5C%5C%0A%26+e%5E%7B2t%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A1%26-1%5C%5C%0A0%26+1%0A%5Cend%7Bbmatrix%7D+%5C%2C+u%280%29%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ae%5Et%26e%7B2t%7D%2Be%5Et%5C%5C%0A0%26+e%7B2t%7D%0A%5Cend%7Bbmatrix%7D+%5C%2C+u%280%29%0A%5Cend%7Balign%2A%7D%0A)


**Review of key ideas**

1. the equation u' = Au is linear with constrant coefficients in A.    

2. start with u(0): its solution is usually a combination of exponentials involving &lambda; and x.

independent eigenvectors u(t) = c<sub>1</sub>e<sup>&lambda;<sub>1</sub>t</sup>x<sub>1</sub> + ... + c<sub>n</sub>e<sup>&lambda;<sub>n</sub>t</sup>x<sub>n</sub> 

3. the constants c<sub>1</sub>, ... , c<sub>n</sub> are determined by u(0) = c<sub>1</sub>x<sub>1</sub> + ... + c<sub>n</sub>x<sub>n</sub> = Xc

4. u(t) approaches zero (stability) if every &lambda; has negative real parts: All e<sup>&lambda;t</sup> --> 0

5. solutions have the short form u(t) = e<sup>At</sup>u(0) with the matrix exponential e<sup>At</sup>.

6. equations with y'' reduce to u' = Au by combining y and y' into the vector u.



**Worked examples**

6.3A solve y'' + 4y' +3y = 0 by substituting e<&lambda;t and also by linear algebra.

substituting y = e<&lambda;t</sup> yields (&lambda;<sup>2</sup> + 4&lambda; + 3)e<sup>&lambda;t</sup> = 0 = (&lambda; + 1)(&lambda; + 3) = 0 yielding &lambda;<sub>1</sub> = -1 and &lambda;<sub>2</sub> = -3 and thusly yields pure solutions y<sub>1</sub> = e<sup>-t</sup> and y<sub>2</sub> = e<sup>-3t</sup> and a complete solution y = c<sub>1</sub>y<sub>1</sub> + c<sub>2</sub>y<sub>2</sub> approaches zero [as t-->∞], [but witouth u(0) cannot know the c<sub>i</sub>.]

linear algebra sets u = (y, y') and then the vector equation to u' = Au:  

∂y/∂t = y' and ∂y'/∂t = -3y - 4y' convert to ∂u/∂t = [[0,1],[-3,-4]] u

so that ∂ [y, y'] / ∂t = [[0,1],[-3,-4]] [y, y'] = [y', -3y-4y']

this A is 'companion matrix' and its eigenvalues are -1 and -3 from det (A - &lambda;I) = det [[-&lambda;, 1],[-3, -4 - &lambda;]] = &lambda;<sup>2</sup> + 4&lambda; + 3 = 0 

the eigenvectors of A are (1, &lambda;<sub>1</sub>) and (1, &lambda;<sub>2</sub>). 

the decay in y(t) comes from the e<sup>-t</sup> and e<sup>-3t</sup>.  with constant coefficients, calculus leads to linear algebra: Ax = &lambda;x

note: in linear algebra there is a danger of shortage of eigenvectors.  our eigenvectors (1,&lambda;) and (1, &lambda;) are the same if &lambda;<sub>1</sub> = &lambda;<sub>2</sub> and then one cannot diagonalize A.  In this case, there are not 2 independent solutionsto ∂u/∂t = Au.

In differential calculus the danger is also repeated &lambda;.  After y = e<sup>&lambda;t</sup>, a second solutionhas to be found.  this second solutions turns out to be y = te<sup>&lambda;t</sup>.  This "impure" solution (with an extra t) appears in the exponential e<sup>At</sup> as was shown in example 4.


6.3B find eigenvalues and eigenvectors of A and write u(0) = (0, 2√2, 0) as a combination of the eigenvectors.  solve both equations u' = Au and u'' = Au.  

∂u/∂t = [[-2,1,0], [1,-2,1], [0,1,-2]] u   
∂<sup>2</sup>u/∂t<sup>2</sup> = [[-2,1,0], [1,-2,1], [0,1,-2]] u with ∂u/∂t(0) = 0

![\begin{align*}
\frac{\partial u}{\partial t} &= Au = 
\begin{bmatrix}
-2&1&0\\
1&-2&1\\
0&-1&-2
\end{bmatrix} \, u \\
\\
\frac{\partial^2 u}{\partial t^2} &= Au = 
\begin{bmatrix}
-2&1&0\\
1&-2&1\\
0&-1&-2
\end{bmatrix} \, u  
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%26%3D+Au+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-2%261%260%5C%5C%0A1%26-2%261%5C%5C%0A0%26-1%26-2%0A%5Cend%7Bbmatrix%7D+%5C%2C+u+%5C%5C%0A%5C%5C%0A%5Cfrac%7B%5Cpartial%5E2+u%7D%7B%5Cpartial+t%5E2%7D+%26%3D+Au+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-2%261%260%5C%5C%0A1%26-2%261%5C%5C%0A0%26-1%26-2%0A%5Cend%7Bbmatrix%7D+%5C%2C+u++%0A%5Cend%7Balign%2A%7D)

u' = Au   
similar to heat equation ∂u/∂t = ∂<sup>2</sup>u/∂x<sup>2</sup>.   
its solution u(t) will decay (A has negative eigenvalues).  

u'' = Au  
similar to wave equation ∂<sup>2</sup>u/∂t<sup>2</sup> = ∂<sup>2</sup>u/∂x<sup>2</sup>.   
its solution will oscillate ( square roots of &lambda; are imaginary).


solution:   
the eigenvalues and eigenvectors come from det(A -&lambda; I) = 0 

det [ [ -2 - &lambda;, 1, 0 ], [ 1, -2 - &lambda;], [ 0, 1, -2 - &lambda;] ]    
= ( -2 - &lambda; ) [ ( - 2 - &lambda; )<sup>2</sup> - 1 ] - 1 ( -2 - y )  
= ( -2 - &lambda; ) [ ( - 2 - &lambda; )<sup>2</sup> - 2 ] = 0
= ( -2 - &lambda; ) [ &lambda;<sup>2</sup> + 4&lambda; - 2 ] = 0
&lambda;<sub>1</sub> = 2 from ( -2 - &lambda; )
&lambda;<sub>2</sub> and &lambda;<sub>3</sub> from quadratic soliution to &lambda;<sup>2</sup> + 4&lambda; - 2: -2 &pm; √2

![\begin{align*}
det A - &lambda;I &=
det \begin{bmatrix}
-2- &lambda;&1&0\\
1&-2- &lambda;&1\\
0&-1&-2- &lambda;
\end{bmatrix} \\
\\
&= (-2 - &lambda;) [(-2- &lambda;)^2 - 1] -1(-2- &lambda;)\\
&= (-2 - &lambda;) [(-2- &lambda;)^2 -2 ] \\
& = (-2 -&lambda;)(&lambda;^2 + 4&lambda;+2) 
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Adet+A+-+%26lambda%3BI+%26%3D%0Adet+%5Cbegin%7Bbmatrix%7D%0A-2-+%26lambda%3B%261%260%5C%5C%0A1%26-2-+%26lambda%3B%261%5C%5C%0A0%26-1%26-2-+%26lambda%3B%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%5C%5C%0A%26%3D+%28-2+-+%26lambda%3B%29+%5B%28-2-+%26lambda%3B%29%5E2+-+1%5D+-1%28-2-+%26lambda%3B%29%5C%5C%0A%26%3D+%28-2+-+%26lambda%3B%29+%5B%28-2-+%26lambda%3B%29%5E2+-2+%5D+%5C%5C%0A%26+%3D+%28-2+-%26lambda%3B%29%28%26lambda%3B%5E2+%2B+4%26lambda%3B%2B2%29+%0A%5Cend%7Balign%2A%7D)

&lambda;<sub>1</sub> = -2 --> x<sub>1</sub> = [1,0,-1]   
&lambda;<sub>2</sub> = -2 - √2 --> x<sub>2</sub> = [1,-√2, 1]   
&lambda;<sub>3</sub> = -2 + √2 --> x<sub>3</sub> = [1, √2, 1]   

![\begin{align*}
&lambda;_1=-2: (A -- 2I) \, x_1 &= 
\begin{bmatrix}
0&1&0\\
1&0&1\\
0&1&0
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}=
\begin{bmatrix}
0\\
0\\
0
\end{bmatrix} \,
\, for x_1 = 
\begin{bmatrix}
1\\
0\\
-1
\end{bmatrix}\\
\\
&lambda;_2=-2-\sqrt{2}: 
(A -(-2-\sqrt{2})I) \, x_2 &= \begin{bmatrix}
\sqrt{2}&1&0\\
1&\sqrt{2}&1\\
0&1&\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix}=
\begin{bmatrix}
0\\
0\\
0
\end{bmatrix} \,
for x_2 = 
\begin{bmatrix}
1\\
-\sqrt{2}\\
1
\end{bmatrix}\\
\\
&lambda;_3=-2+\sqrt{2}: 
(A -(-2+\sqrt{2})I)\, x_3 &= \begin{bmatrix}
-\sqrt{2}&1&0\\
1&-\sqrt{2}&1\\
0&1&-\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix}=
\begin{bmatrix}
0\\
0\\
0
\end{bmatrix} \,
for x_3 = 
\begin{bmatrix}
1\\
\sqrt{2}\\
1
\end{bmatrix}\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%26lambda%3B_1%3D-2%3A+%28A+--+2I%29+%5C%2C+x_1+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A0%261%260%5C%5C%0A1%260%261%5C%5C%0A0%261%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C%0A0%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D+%5C%2C%0A%5C%2C+for+x_1+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%26lambda%3B_2%3D-2-%5Csqrt%7B2%7D%3A+%0A%28A+-%28-2-%5Csqrt%7B2%7D%29I%29+%5C%2C+x_2+%26%3D+%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%261%260%5C%5C%0A1%26%5Csqrt%7B2%7D%261%5C%5C%0A0%261%26%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C%0A0%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D+%5C%2C%0Afor+x_2+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-%5Csqrt%7B2%7D%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%26lambda%3B_3%3D-2%2B%5Csqrt%7B2%7D%3A+%0A%28A+-%28-2%2B%5Csqrt%7B2%7D%29I%29%5C%2C+x_3+%26%3D+%5Cbegin%7Bbmatrix%7D%0A-%5Csqrt%7B2%7D%261%260%5C%5C%0A1%26-%5Csqrt%7B2%7D%261%5C%5C%0A0%261%26-%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C%0A0%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D+%5C%2C%0Afor+x_3+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A%5Csqrt%7B2%7D%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cend%7Balign%2A%7D)

the eigenvectors are orthogonal (proved in secrtion 6.4) for all symmetric matrices).    
all 3 &lambda;s are negative.  This A is negative definite and e<sup>At</sup> decays to zero (stability). 

the starting u(0) = (0,2√2,0) is x<sub>3</sub> - x<sub>2</sub> meaning c<sub>2</sub> = -1 and c<sub>3</sub> = +1    
therefore the complete solution is u(t) = e<sup>&lambda;<sub>3</sub>t</sup>x<sub>3</sub> - e<sup>&lambda;<sub>2</sub>t</sup>x<sub>2</sub>

Heat equation

figure 6.6a    
temperature at center starts at 2√2 [ you can see this in u<sub>0</sub> = ( 0, 2√2, 0 )  
heat diffuses into neighboring boxes and then to outside boxes that are frozen at zero degrees.   
the rate of flow between boxes is the temperature difference    
[ temp is (2√2) in box 2 and zero in boxes 0 and 4 and (2√2)/2 in 1 and 3; I surmise the rate is (2√2)/2; I think the next statement confirms that: ]   
from box 2 heat flows L and R at the rate u<sub>1</sub> = u<sub>2</sub> and u<sub>3</sub> = u<sub>2</sub> [ surmise these are negative rates since it is flow out i.e. termperature reductions. ]   
so the flow out is u<sub>1</sub> - 2•u<sub>2</sub> + u<sub>3</sub> in the second row of Au [ think he means the second row of A which is 1, -2, 1.

![\begin{align*}
\frac{\partial u}{\partial t} = Au &= 
\begin{bmatrix}
-2&1&0\\
1&-2&1\\
0&-1&-2
\end{bmatrix} \, u \\
\\
u(t) & = Xe^{&Lambda;t}X^{-1}u(0) = Xe^{&Lambda;t}c = 
\begin{bmatrix}
1&1&1\\
0&-\sqrt{2}&\sqrt{2}\\
-1&1&1
\end{bmatrix} 
\begin{bmatrix}
e^{-2}&&\\
&e^{-2-\sqrt{2}}&\\
&&e^{-2+\sqrt{2}}
\end{bmatrix}
\begin{bmatrix}
0\\
-1\\
1
\end{bmatrix}\\
\\
\\ I \, think:
\\
\frac{\partial u}{\partial t} = Au & = AXe^{&Lambda;t}X^{-1}u(0) = AXe^{&Lambda;t}c = 
A\begin{bmatrix}
1&1&1\\
0&-\sqrt{2}&\sqrt{2}\\
-1&1&1
\end{bmatrix} 
\begin{bmatrix}
e^{-2}&&\\
&e^{-2-\sqrt{2}}&\\
&&e^{-2+\sqrt{2}}
\end{bmatrix}
\begin{bmatrix}
0\\
-1\\
1
\end{bmatrix}\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%3D+Au+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-2%261%260%5C%5C%0A1%26-2%261%5C%5C%0A0%26-1%26-2%0A%5Cend%7Bbmatrix%7D+%5C%2C+u+%5C%5C%0A%5C%5C%0Au%28t%29+%26+%3D+Xe%5E%7B%26Lambda%3Bt%7DX%5E%7B-1%7Du%280%29+%3D+Xe%5E%7B%26Lambda%3Bt%7Dc+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26-%5Csqrt%7B2%7D%26%5Csqrt%7B2%7D%5C%5C%0A-1%261%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B-2%7D%26%26%5C%5C%0A%26e%5E%7B-2-%5Csqrt%7B2%7D%7D%26%5C%5C%0A%26%26e%5E%7B-2%2B%5Csqrt%7B2%7D%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C%0A-1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%5C%5C+I+%5C%2C+think%3A%0A%5C%5C%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%3D+Au+%26+%3D+AXe%5E%7B%26Lambda%3Bt%7DX%5E%7B-1%7Du%280%29+%3D+AXe%5E%7B%26Lambda%3Bt%7Dc+%3D+%0AA%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26-%5Csqrt%7B2%7D%26%5Csqrt%7B2%7D%5C%5C%0A-1%261%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B-2%7D%26%26%5C%5C%0A%26e%5E%7B-2-%5Csqrt%7B2%7D%7D%26%5C%5C%0A%26%26e%5E%7B-2%2B%5Csqrt%7B2%7D%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C%0A-1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cend%7Balign%2A%7D)

<img width="825" alt="image" src="https://user-images.githubusercontent.com/38410965/109299233-ca0c3f00-7802-11eb-99bc-869638ae06e6.png">

wave exchange 
∂<sup>2</sup>u/∂t<sup>2</sup> = Au   
same eigenvectors x   
eigenvalues lead to oscillations: &lambda; = e<sup>iwt</sup>x and e<sup>-iwt</sup>x whose frequencies come from w<sup>2</sup> = -&lambda;:

∂<sup>2</sup>(e<sup>iwt</sup>x)/∂t<sup>2</sup> = A(e<sup>iwt</sup>x) = ... 
becomes ...
= (iw)<sup>2</sup>e<sup>iwt</sup>x = &lambda;e<sup>iwt</sup>x and w<sup>2</sup> = -&lambda;

there are 2 square roots of -&lambda; so e<sup>iwt</sup> and e<sup>-iwt</sup> [as &lambda;s] with 3 eigenvectors [each] which makes 6 solutions to u'' = Au.  
a combination will match the 6 components of u(0) and u'(0).   
since u' = 0 in this problem, e<sup>iwt</sup>x and e<sup>iwt</sup>x produce 2 cos wtx 

6.3C solve 4 equations   
∂a/∂t = 0   
∂b/∂t = a  
∂c/∂t = 2b  
∂z/∂t = 3c  
in that order starting from u(0) = (a(0), b(0), c(0), z(0))  
solve the same equations by matrix exponential in u(t) = e<sup>At</sup>u(0) 

four equations   
&lambda; = 0, 0, 0, 0  
eigenvalues on the diagonal  


![\begin{align*}
\frac{\partial u}{\partial t} &= 
\frac{\partial 
\begin{bmatrix}
a\\
b\\
c\\
z
\end{bmatrix}}{\partial t} = 
Au =
\begin{bmatrix}
0&0&0&0\\
1&0&0&0\\
0&2&0&0\\
0&0&3&0
\end{bmatrix}
\begin{bmatrix}
a\\
b\\
c\\
z
\end{bmatrix}
\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%26%3D+%0A%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Aa%5C%5C%0Ab%5C%5C%0Ac%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D%7D%7B%5Cpartial+t%7D+%3D+%0AAu+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%260%260%260%5C%5C%0A1%260%260%260%5C%5C%0A0%262%260%260%5C%5C%0A0%260%263%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aa%5C%5C%0Ab%5C%5C%0Ac%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%5Cend%7Balign%2A%7D)

find A<sup>2</sup>, A<sup>3</sup>, A<sup>4</sup> and e<sup>At</sup> = I + At + (At)<sup>3</sup>/6   
why does the series stop?   
why is it true that (e<sup>A</sup>)(e<sup>A</sup>) = (e<sup>2A</sup>)
**always e<sup>As</sup> times e<sup>At</sup> = e<sup>A(s+t)</sup>**

solution 1:  
integrate ∂a/∂t = 0 then ∂b/∂t = a, then ∂c/∂t = 2b and ∂z/∂t = 3c:

this 4x4 matrix which is multiplying a(0), b(0), c(0), z(0) to produce a(t), b(t), c(t), z(t) must be the same e<sup>At</sup> as below.

[the first line is ∂a/∂t integrated: a(0] is c from the integral]   
[the second line: a(0) is a constant.   t appears when ∫ ∂b/∂t ]    
[third line: ∂c/∂t = 2b so the 2 remains with teh b part but is absorbed with the t<sup>2</sup> part.]

![\begin{align*}
solution \, 1:&
\\
a(t) & =a(0)\\
a(t) & =ta(0)+b(0) \\
a(t) & =t^2a(0)+2tb(0)+c(0)\\
a(t) & =t^3a(0)+3t^2b(0) + 3tc(0)+z(0)\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Asolution+%5C%2C+1%3A%26%0A%5C%5C%0Aa%28t%29+%26+%3Da%280%29%5C%5C%0Aa%28t%29+%26+%3Dta%280%29%2Bb%280%29+%5C%5C%0Aa%28t%29+%26+%3Dt%5E2a%280%29%2B2tb%280%29%2Bc%280%29%5C%5C%0Aa%28t%29+%26+%3Dt%5E3a%280%29%2B3t%5E2b%280%29+%2B+3tc%280%29%2Bz%280%29%5C%5C%0A%5Cend%7Balign%2A%7D)


Solution 2:   
the powers of A (strictly triangular) are all zero after A<sup>3</sup>:   
the diagonals move down at each step.  
so, the series for e<sup>At</sup> stops after 4 terms.   
the square of e<sup>A</sup> is e<sup>2A</sup>   
but e<sup>A</sup>e<sup>B</sup> and e<sup>B</sup>e<sup>A</sup> and e<sup>A+B</sup> can all be different.

![\begin{align*}
solution \, 2:&
\\
A^1 &=
\begin{bmatrix}
0&0&0&0\\
1&0&0&0\\
0&2&0&0\\
0&0&3&0
\end{bmatrix} \, \,
A^2 =
\begin{bmatrix}
0&0&0&0\\
0&0&0&0\\
2&0&0&0\\
0&6&0&0\\
\end{bmatrix} \, \,A^3 =
\begin{bmatrix}
0&0&0&0\\
0&0&0&0\\
0&0&0&0\\
6&0&0&0\\
\end{bmatrix} \, \,
A^4 = 0
\\
Same \,  e^{At} \, as \, Solution \,1:&
\\
e^{At} &= I + At + \frac{(At)^2}{2}+ \frac{(At)^3}{6} = 
\begin{bmatrix}
1&&&\\
t&1&&\\
t^2&2t&1&\\
t^3&3t^2&3t&1\\
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Asolution+%5C%2C+2%3A%26%0A%5C%5C%0AA%5E1+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%260%260%260%5C%5C%0A1%260%260%260%5C%5C%0A0%262%260%260%5C%5C%0A0%260%263%260%0A%5Cend%7Bbmatrix%7D+%5C%2C+%5C%2C%0AA%5E2+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%260%260%260%5C%5C%0A0%260%260%260%5C%5C%0A2%260%260%260%5C%5C%0A0%266%260%260%5C%5C%0A%5Cend%7Bbmatrix%7D+%5C%2C+%5C%2CA%5E3+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%260%260%260%5C%5C%0A0%260%260%260%5C%5C%0A0%260%260%260%5C%5C%0A6%260%260%260%5C%5C%0A%5Cend%7Bbmatrix%7D+%5C%2C+%5C%2C%0AA%5E4+%3D+0%0A%5C%5C%0ASame+%5C%2C++e%5E%7BAt%7D+%5C%2C+as+%5C%2C+Solution+%5C%2C1%3A%26%0A%5C%5C%0Ae%5E%7BAt%7D+%26%3D+I+%2B+At+%2B+%5Cfrac%7B%28At%29%5E2%7D%7B2%7D%2B+%5Cfrac%7B%28At%29%5E3%7D%7B6%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%26%26%26%5C%5C%0At%261%26%26%5C%5C%0At%5E2%262t%261%26%5C%5C%0At%5E3%263t%5E2%263t%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)


section 6.4 

selected problems

1. find 2 &lambda;s and x's so that u = e<sup>&lambda;t</sup>x solves:

∂u/∂t = [[4,3],[0,1]] u 

what combination of u = c<sub>1</sub>e<sup>&lambda;t</sup>x<sub>1</sub> + c<sub>2</sub>e<sup>&lambda;t</sup>x<sub>2</sub> starts from u(0) = (5,-2) ?

from eigenvalues trace and determinant identities:   
&lambda;<sub>1</sub> + &lambda;<sub>2</sub> = 5  
&lambda;<sub>1</sub>&lambda;<sub>2</sub> = 4  
determine &lambda;<sub>1</sub> =1, &lambda;<sub>2</sub> = 4  

for &lambda;<sub>1</sub> the eigenvector is given by the null space of [[3,3],[0,0]] or x<sub>2</sub> = (1,-1)

for &lambda;<sub>2</sub> the eigenvector is given by the null space of [[0,3],[0-3]] or x<sub>2</sub> = (1,0)

thus the 2 pure solutions to the given differential equation are:

x<sub>1</sub>(t) = [1,-1]<sup>T</sup>e<sup>1t</sup>   
x<sub>2</sub>(t) = [1,0]<sup>T</sup>e<sup>4t</sup>

the general [complete] solution is a linear combination of pure solutions.   
to have a general solution equal to the initial condition, set c<sub>1</sub> and c<sub>2</sub>:

u(0) = [5,2]<sup>T</sup> = c<sub>1</sub>[1,-1]<sup>T</sup> + c<sub>2</sub>[1,0]<sup>T</sup>

X = [[1,-1],[1,0]] --> X<sup>-1</sup> = [[0,1],[-1,1]  

X<sup>-1</sup>u(0) = c = [-2,7]<sup>T</sup>

u(0) = [5,2]<sup>T</sup> = -2•[1,-1]<sup>T</sup> + 7•[1,0]<sup>T</sup>

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/109374432-45153a00-7883-11eb-825c-81b88c79f820.png">

2. solve problem 1 for u = (y,z) by back substitution, z before y.    
solve ∂z/∂t = z from z(0) = -2  
solve ∂y/∂t = 4y + 3z from y(0) = 5

∂ [y, z]<sup>T</sup> / ∂t = c<sub>1</sub>[1,-1]<sup>T</sup>e<sup>1(t=0)</sup> + c<sub>2</sub>[1,0]<sup>T</sup>e<sup>4(t=0)</sup>

z takes the second component of each eigenvector, or -1 and 0, making c<sub>1</sub> the only available coefficient to determine.   

z(0) = -2 = c<sub>1</sub>-1e<sup>1(t=0)</sup> + c<sub>2</sub>0<sup>T</sup>e<sup>4(t=0)</sup> = c<sub>1</sub>-1e<sup>1(t=0)</sup> --> c_1 = -2 and z(t) = (-2)(-1)e<sup>1t</sup> = 2e<sup>t</sup>

plug z(t) = 2e<sup>t</sup> into ∂y/∂t = 4y + 3z to derive ∂y/∂t =  4y + 3(2e<sup>t</sup>) 

then knowing c<sub>1</sub> = 2 and y's getting the first component of each eigenvector, set y(0) = 5 = (c<sub>1</sub>=2)(1)e<sup>1(t=0)</sup> + c<sub>2</sub>(1)e<sup>4(t=0)</sup> = 2 + c<sub>2</sub> deriving c<sub>2</sub> = 3. thus y(t) = 2e<sup>t</sup> + 3e<sup>4t</sup> as in problem 1 because y(0) has same value as u's first component.




3. 
a. if every column of A adds to zero then the rows add to the zero row because the matrix is singular with dependent columns AND rows and thus &lambda; = 0 is one of the eigenvalues.  
b. with negaitve diagonal and positive off diagonal adding to zero, u' = Au will be a continuous Markov equation.  find eigenvalues and eigenvectors and steady state as t --> ∞.  

solve ∂u/∂t = [[-2,3],[2,-3]] u with u(0) = [4,1]<sup>T</sup>  
see below for answer using specific X, but generally the u(t) that solves ∂u/∂t is x<sup>1</sup> + e<sup>-5t</sup>x<sup>2</sup>   

what is u(∞)   
since e<sup>-5t</sup> --> 0 as t --> ∞, steady state u(∞) = (3,2) as shown by the answer below when t = 1000 since exp(-5000 is &lambda;t) = 0

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109375628-2cf5e880-788c-11eb-86ef-1adf00454452.png">


4. door opened between room sholding v(0) = 30 people and w(0) = 10 people.  the movement between rooms is proportional to the difference v - w from which we can take ∂v/∂t = w - v = positive inflow if w contains more people or negative outflow if w contains fewer people at  and ∂w/∂t = v - w.  show that the total v + w is constant at 40 people.   find the matrix in ∂u/∂t = Au and its eigenvalues and eigenvectors.  what are v and w at t=1 and t=∞.

∂u/∂t where u = [v,w]<sup>T</sup> 

∂u/∂t = ∂[v,w]<sup>T</sup>/∂tAu must be = [[-1,1],[1,-1]][v,w]<sup>T</sup> = [[w-v],[v-w]]

the python code show diagonalization of the singular matrix and steady state is 20 persons in each room. 

differential equations ∂w/∂t = v-w and ∂v/∂t = w-v  
consider y = v+w and ∂<sup>∞</sup>y/∂t<sup>∞</sup> is the steady state of people is more easily derived by knowing ∂y/∂t = ∂(v+w)/∂t = ∂v/∂t + ∂w/∂t = w - v + v - w = 0  
so the function y(t) = v(t) + w(t) is constant for all time.  
y(t) thus is always equal to its initial condition y(t) = y(0) = v(0) + w(0) = 30 + 10 = 40

defining vector of unknowns u as u = [v(t],w(t)] then we have that u satisfies ∂u/∂t = [w-v. v-w] = [[-1,1][1.-1]][v,w]<sup>T</sup> = Au.


<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109376057-db4f5d00-788f-11eb-918e-6c8cb5fbd527.png">

![\begin{align*}
\frac{\partial u}{\partial t} &= 
\frac{\partial 
\begin{bmatrix}
v(t)\\
w(t)
\end{bmatrix}}{\partial t} = 
\begin{bmatrix}
w-v\\
v-w
\end{bmatrix} = 
\begin{bmatrix}
-1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
v\\w
\end{bmatrix}\\
u(0) &= 
\begin{bmatrix}
30\\
10
\end{bmatrix} =
c_1
\begin{bmatrix}
1\\
-1
\end{bmatrix}+
c_2
\begin{bmatrix}
1\\
1
\end{bmatrix}
\\
u(t) &= 
10 
\begin{bmatrix}
1\\
-1
\end{bmatrix}
e^{-2t}
+20 
\begin{bmatrix}
1\\
1
\end{bmatrix}
e^{0t}\\
&= 
\begin{bmatrix}
v(t)\\
w(t)
\end{bmatrix} =
\begin{bmatrix}
10*1*e^{-2t} + 20*1*e^{0t}\\
10*-1*e^{-2t} + 20*1*e^{0t}
\end{bmatrix} =
\begin{bmatrix}
10*e^{-2t} + 20\\
-10*e^{-2t} + 20
\end{bmatrix}\\
u(t=1) &= 
\begin{bmatrix}
v(t=1)\\
w(t=1)
\end{bmatrix}=
\begin{bmatrix}
10*e^-2 + 20\\
-10*e^-2 + 20
\end{bmatrix}\\
u(t=\infty) &= 
\begin{bmatrix}
v(t=\infty)\\
w(t=\infty)
\end{bmatrix}=
\begin{bmatrix}
10*e^{-2\infty} + 20\\
-10*e^{-2\infty} + 20
\end{bmatrix}
=\begin{bmatrix}
20\\
20
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%26%3D+%0A%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D%7D%7B%5Cpartial+t%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Aw-v%5C%5C%0Av-w%0A%5Cend%7Bbmatrix%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-1%261%5C%5C%0A1%26-1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Av%5C%5Cw%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%280%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A30%5C%5C%0A10%0A%5Cend%7Bbmatrix%7D+%3D%0Ac_1%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%2B%0Ac_2%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0Au%28t%29+%26%3D+%0A10+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B-2t%7D%0A%2B20+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B0t%7D%5C%5C%0A%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A10%2A1%2Ae%5E%7B-2t%7D+%2B+20%2A1%2Ae%5E%7B0t%7D%5C%5C%0A10%2A-1%2Ae%5E%7B-2t%7D+%2B+20%2A1%2Ae%5E%7B0t%7D%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A10%2Ae%5E%7B-2t%7D+%2B+20%5C%5C%0A-10%2Ae%5E%7B-2t%7D+%2B+20%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%28t%3D1%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%3D1%29%5C%5C%0Aw%28t%3D1%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A10%2Ae%5E-2+%2B+20%5C%5C%0A-10%2Ae%5E-2+%2B+20%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%28t%3D%5Cinfty%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%3D%5Cinfty%29%5C%5C%0Aw%28t%3D%5Cinfty%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A10%2Ae%5E%7B-2%5Cinfty%7D+%2B+20%5C%5C%0A-10%2Ae%5E%7B-2%5Cinfty%7D+%2B+20%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A20%5C%5C%0A20%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

5. reverse the diffusion of peple in problem 4 ∂u/∂t = -Au: ∂y/∂t = v-w and ∂w/∂t = w-v  
total ∂(v+w)/∂t is unchanged = (w-v)+(v-w) = 0 

∂u/∂t = -Au means that the &lambda;'s change, or in this case, the one non-zero &lambda; changes sign.  since &lambda is positive and > 1 it blows up.

eigenvalues swap sign.  
eigenvectors are unchanged because all we are doing is changing the direction of A from 1 to -1.

v(t) on top goes to infinity and w(t) on bottom goes to -infinity

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109377228-f58d3900-7897-11eb-8061-7f12d27760b0.png">

![\begin{align*}
\frac{\partial u}{\partial t} &= 
\frac{\partial 
\begin{bmatrix}
v(t)\\
w(t)
\end{bmatrix}}{\partial t} = 
\begin{bmatrix}
v-w\\
w-v
\end{bmatrix} = 
\begin{bmatrix}
1&-1\\
-1&1
\end{bmatrix}
\begin{bmatrix}
v\\w
\end{bmatrix}\\
u(0) &= 
\begin{bmatrix}
30\\
10
\end{bmatrix} =
c_1
\begin{bmatrix}
1\\
1
\end{bmatrix}+
c_2
\begin{bmatrix}
1\\
-1
\end{bmatrix}
\\
u(t) &= 
20 
\begin{bmatrix}
1\\
1
\end{bmatrix}
e^{0t}
+10 
\begin{bmatrix}
1\\
-1
\end{bmatrix}
e^{2t}\\
&= 
\begin{bmatrix}
v(t)\\
w(t)
\end{bmatrix} =
\begin{bmatrix}
20*1*e^{0t} + 10*1*e^{2t}\\
20*1*e^{0t} + 10*-1*e^{2t}
\end{bmatrix} =
\begin{bmatrix}
20 + 10*e^{2t}\\
20 - 10*e^{2t}
\end{bmatrix}\\
u(t=1) &= 
\begin{bmatrix}
v(t=1)\\
w(t=1)
\end{bmatrix}=
\begin{bmatrix}
20 + 10*e^2\\
20 -10*e^2
\end{bmatrix}\\
u(t=\infty) &= 
\begin{bmatrix}
v(t=\infty)\\
w(t=\infty)
\end{bmatrix}=
\begin{bmatrix}
20 + 10*e^{2\infty}\\
 20 -10*e^{2\infty}
\end{bmatrix}
=\begin{bmatrix}
+\infty\\
-\infty
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%26%3D+%0A%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D%7D%7B%5Cpartial+t%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av-w%5C%5C%0Aw-v%0A%5Cend%7Bbmatrix%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%26-1%5C%5C%0A-1%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Av%5C%5Cw%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%280%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A30%5C%5C%0A10%0A%5Cend%7Bbmatrix%7D+%3D%0Ac_1%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%2B%0Ac_2%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0Au%28t%29+%26%3D+%0A20+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B0t%7D%0A%2B10+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B2t%7D%5C%5C%0A%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A20%2A1%2Ae%5E%7B0t%7D+%2B+10%2A1%2Ae%5E%7B2t%7D%5C%5C%0A20%2A1%2Ae%5E%7B0t%7D+%2B+10%2A-1%2Ae%5E%7B2t%7D%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A20+%2B+10%2Ae%5E%7B2t%7D%5C%5C%0A20+-+10%2Ae%5E%7B2t%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%28t%3D1%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%3D1%29%5C%5C%0Aw%28t%3D1%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A20+%2B+10%2Ae%5E2%5C%5C%0A20+-10%2Ae%5E2%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%28t%3D%5Cinfty%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%3D%5Cinfty%29%5C%5C%0Aw%28t%3D%5Cinfty%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A20+%2B+10%2Ae%5E%7B2%5Cinfty%7D%5C%5C%0A+20+-10%2Ae%5E%7B2%5Cinfty%7D%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A%2B%5Cinfty%5C%5C%0A-%5Cinfty%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)


6.
a and b are real  
A = [[a,1],[1,a]] has real eigenvalues   
B = [[b,-1],[1,b]] [has complex eigenvalues    

find conditions on a and b so all solutions ∂u/∂t = Au and ∂v/∂t = Bv approach zero as t --> 0 i.e. Re&lambda; < 0 for all eigenvalues.   

for A, stability requires:  
T<sub>A</sub> = a + a =  2a < 0 or a < 0  for at least one &lambda; < 0
AND
D<sub>A</sub> = a<sup>2</sup> - 1 > 0 or a<sup>2</sup> > 1 or -1 > a > 1 for both signs to be the same
so a < -1

for B, stability requires:  
T<sub>B</sub> = b + b =  2b < 0 or b < 0  
D<sub>B</sub> = b<sup>2</sup> + 1 > 0 or b<sup>2</sup> > -1or b > i   
not sure how to evaluate the D part so will say b < 0

for a 2x2 this is not necessary:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/109391654-285e1e00-78e6-11eb-8d04-e32e35acdfc7.png">

7.  P is projection matrix onto 45 degree line y = x in R<sup>2</sup>.  what are eigenvalues

if ∂u/∂t = -Pu what is the limit of u(t) as t --> ∞ starting from u(0) = (3,1)?

a = (1,1)

P = aa<sup>T</sup>/a<sup>T</sup> = [[1,1],[1,1]] / 2

projection matrix has eigenvalues of 1 and 0.  
[for &lambda;<sub>1</sub>] eigenvectors Px = 1x fill the subspace P projects onto x = (1,1).  
[for &lambda;<sub>2</sub>] eigenvectors with Px = 0x fill the perpendicular subspace: x = (1,-1)

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109399060-725afa00-790e-11eb-99ad-13ac2f0cfd68.png">

to solve u' = -P change signs for &lambda;s: but eigenvectors stay the same so u(0) still has c = [2,1]:

u(0) = 2[1,1]<sup>T</sup> + 1[1,-1]<sup>T</sup>

notice the -&lambda;s:

u(t) = e<sup>-1t</sup>[2,2]<sup>T</sup> + e<sup>-0t</sup>[1,-1]<sup>T</sup> which approaches [1,-1]<sup>T</sup> as t--> ∞ because the first eigenvalue causes the first part to go to zero.

-P coefficient matrix is -1 times P which means Px = &lambda;x becomes -Ax = -&lambda;x; eigenvectors of -P are same as P and eigenvalues of -P are the negative of P.

8.  the rabbit population grows 6r but declines due to wolves -2w.  
the wolf population grows always: -w<sup>2</sup> would control the wolves. 

r/t = 6r - 2w  
w/t = 2r + w

find eigenvalues and eigenvectors.  
if r(0) = w(0) = 30 what are the populations at t?   
after a long time what is the ratio rabbits to wolves?   


<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109400075-94f01180-7914-11eb-8ab4-ece1bf27e339.png">

r(t) and w(t) must satisfy ∂r/∂t = 6r - 2w and ∂w/∂t = 2r + w as shown in matrix form below.  this coefficient matrix has eignvalues 2 and 5.  for their respective &lambda;s, the eigenvectors are given by the null spaces shown below A - &lambda; I and the total solutions is given by the linear combination of the two solutions here:

x<sub>1</sub>(t) = [1,2]<sub>T</sub>e<sup>2t</sup>  
x<sub>2</sub>(t) = [2,1]<sub>T</sub>e<sup>5t</sup>  

the initial condition u(0) forces c<sub>1</sub> and c<sub>2</sub> to satisfy u(0) = Xc which produces c = (10,10) for an entire solution of u(t) = 10[1,2]<sub>T</sub>e<sup>2t</sup> + 10[2,1]<sub>T</sub>e<sup>5t</sup> 

the population of rabbits and wolves is from the components of the complete solution:  
r(t) = 10e<sup>2t</sup> + 20e<sup>5t</sup>    
w(t) = 20e<sup>2t</sup> + 10e<sup>5t</sup>   
and the ratio after a while r/w is (10e<sup>2t</sup> + 20e<sup>5t</sup> )/(20e<sup>2t</sup> + 10e<sup>5t</sup>) = 2 since the eigenvector [2,1]<sub>T</sub> with the &lambda; = 5 dominates the the other eigenvector with &lambda; = 2.



![\begin{align*}
u(t) & = 
\begin{bmatrix}
r(t)\\
w(t)
\end{bmatrix}=
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}
\begin{bmatrix}
e^{2t}&\\
&e^{5t}
\end{bmatrix}
\begin{bmatrix}
10\\
10
\end{bmatrix}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au%28t%29+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ar%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%261%5C%5C%0A1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B2t%7D%26%5C%5C%0A%26e%5E%7B5t%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A10%5C%5C%0A10%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D%0A)


9. write (4,0) as combination of these two eigenvectors c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> of A:

Au = &lambda;u:  
[[0,1],[-1,0]] [1,i].<sup>T</sup> = i [1,i].<sup>T</sup>  
[[0,1],[-1,0]] [1,i].<sup>T</sup> =  -i [1,i].<sup>T</sup>

the solution to ∂u/∂t = Au starting from (4,0) is c<sub>1</sub>e<sup>it</sup>x<sub>1</sub> + c<sub>2</sub>e<sup>-it</sup>x<sub>2</sub>.  substitute e<sup>it</sup> = cos t + i sin t and e<sup>-it</sup> = cost t -i sin t to find u(t)

can see the derivation of c: u<sub>0<sub> = 2 [1,i]<sup>T</sup> + 2[1,-i]<sup>T</sup> = [4,0]<sup>T</sup>   
could also have eyeballed the 2 x's given and seen that 2 works for c's.

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109404173-83693280-7931-11eb-9215-0bd92edbae1e.png">


if substitute Euler's into the complete solution:

2e<sup>it</sup>[1,i]<sup>T</sup> + c<sub>2</sub>e<sup>-it</sup>[1,-i]<sup>T</sup>

[Strang and Waxworth computed a 4 cost not -4cost for 2nd component.]

![\begin{align*}
u_t &= 
2e^{it}\begin{bmatrix}1\\i\end{bmatrix}+
2e^{-it}\begin{bmatrix}1\\-i\end{bmatrix} \\ &= 
2(cost + isint)\begin{bmatrix}1\\i\end{bmatrix}+
2(cost - isint)\begin{bmatrix}1\\-i\end{bmatrix} \\ &= 
\begin{bmatrix}
2cost + 2isint + 2cost - 2isint\\
2icost + 2i^2sint -2icost - -2i^2sint
\end{bmatrix} \\ &= 
\begin{bmatrix}
4cost \\
-4sint 
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au_t+%26%3D+%0A2e%5E%7Bit%7D%5Cbegin%7Bbmatrix%7D1%5C%5Ci%5Cend%7Bbmatrix%7D%2B%0A2e%5E%7B-it%7D%5Cbegin%7Bbmatrix%7D1%5C%5C-i%5Cend%7Bbmatrix%7D+%5C%5C+%26%3D+%0A2%28cost+%2B+isint%29%5Cbegin%7Bbmatrix%7D1%5C%5Ci%5Cend%7Bbmatrix%7D%2B%0A2%28cost+-+isint%29%5Cbegin%7Bbmatrix%7D1%5C%5C-i%5Cend%7Bbmatrix%7D+%5C%5C+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2cost+%2B+2isint+%2B+2cost+-+2isint%5C%5C%0A2icost+%2B+2i%5E2sint+-2icost+-+-2i%5E2sint%0A%5Cend%7Bbmatrix%7D+%5C%5C+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A4cost+%5C%5C%0A-4sint+%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

10. find A to change scalar equation y'' = 5y' + 4y into a vector equation for u = (y, y'):

∂u/∂t = [y',y'']<sup>T</sup> = ∂[y,y']<sup>T</sup>/∂t = [[0,1],[4,5]] [y,y'] = Au 

what are the eigenvalues of A.  
find them by substituting y = e<sup>&lambda;t</sup> into y'' = 5y' + 4y

substitution: &lambda;t<sup>2</sup>e<sup>&lambda;t</sup> = &lambda;t5e<sup>&lambda;t</sup> + 4e<sup>&lambda;t</sup> --> &lambda;t<sup>2</sup>e<sup>&lambda;t</sup> - &lambda;t5e<sup>&lambda;t</sup> - 4e<sup>&lambda;t</sup> = (&lambda;t<sup>2</sup> - 5&lambda; - 4)e<sup>&lambda;t</sup> = 0 --> &lambda;t<sup>2</sup> - 5&lambda; - 4 = 0 --> &lambda;<sub>1</sub>, &lambda;<sub>2</sub> = 5 &pm; (41)<sup>1/2</sup>/2

[and find the traditional way for me]
A - &lambda; I = [[-&lambda;,1],[4,5-&lambda;]]  
det(A - &lambda; I) = &lambda;<sup>2</sup> - 5&lambda; - 4 = 0 which is the same quadratic found by subsitution of e<sup>&lambda;t</sup>

11. the solution to y'' = 0 is a straight line y = C + Dt.  Convert to a matrix equation.  

[are we double integrating when we move from y'' to y?]

∂ [y,y']<sup>T</sup>/∂t = [[0,1],[0,0]] [y,y']<sup>T</sup> has the solution [y,y']<sup>T</sup> = e<sup>At [y(0),y'(0)]<sup>T</sup>

[with this matrix, ∂y/∂t in 1st component is [0,1]<sup>T</sup>[y,y']=y' and ∂y/∂t = 0]
[coupling allows us to use component 2 (y') to solve component 1 (∂y/∂t) and when diagonalized it is uncoupled into pure solutions that can be recombined with c.]

so y'' = 0y +0y'

[this was the same A as seen earlier which could not be diagonalized.]

&lambda;<sub>1</sub> = &lambda;<sub>2</sub> = 0   
and so this matrix cannot be diagonalized;   

[it's columns are not independent since column 1 = a multiple zero fo column 2]

find A<sup>2</sup> and compute e<sup>At</sup> = I + At + (1/2)A<sup>2</sup>t<sup>2</sup> + ...    
then multiply the computed e<sup>At</sup> times [y(0), y'(0)] to check the straight line y(t) = y(0) + y'(0)t   
[that will be ∂u/∂t = Au]

let vector u be defined as u(t) = [y,y']   
then ∂u/∂t = [y,y']' = [y',y'']  = [[0,1],[0,0]] [y,y'] which has it's complete solution u(t) = [y(t),y'(t)] = e<sup>At</sup>[y(0),y'(0)].

**good**
[the complete solution is injected to the problem as ∂u(t)/∂t = [[0,1],[0,0]] [y(t),y'(t)] = [[0,1],[0,0]] e<sup>At</sup>[y(0),y'(0)] which if A held independent vectors could be diagonalized to Xe<sup>&Lambda;t</sup>X<sup>-1</sup>[y(0),y'(0)] = Xe<sup>&Lambda;t</sup>X<sup>-1</sup>u(0) = Xe<sup>&Lambda;t</sup>c = AX = e<sup>&Lambda;</sup>X = ∂u/∂t.]   

can evaluate e<sup>At</sup> using the definition in terms of Taylor series that is 

e≤sup>At</sup> = I + At + A<sup>2</sup>t<sup>2</sup>/2! + A<sup>3</sup>t<sup>3</sup>/3! + ...    

which stops at A<sup>2</sup> because A<sup>2</sup> = [[0,1],[0,0]] [[0,1],[0,0]] = [[0,0],[0,0]] 

so e<sup>At</sup> = I + At = [[1,0],[0,1]] + [[0,1],[0,0]]t = [[1,t],[0,1]]   

thus, u(t) = [y(t),y'(t)] = [[1,t],[0,1]] [y(0),y'(0)] = [y(0)+y'(0)t],y'(0)] which decouples into  

y(t) = y(0)+y'(0)t and y'(t) = y'(0) where  

y(t) = y(0)+y'(0)t = intercept at time zero + (slope at time zero)(time) which is a flat line with given slope multiplied by t.  [it is y=mx+b or y=b+mt in this case.] 

the factor t tells us that A had only one eigenvector for its two eigenvalues, 0 and 0 and thus is not diagonalizable.  [if both eigenvalues had eigenvectors Algebraic Mutliplicity = Geometric Multiplicity and there would be two t's in the complete solution]
[i guess in some sense then this y(t) = y(0)+y'(0)t is similar to u(t) = linear combination of the eigenvectors weighted by eigenvalues which are exponents in e<sup>(&lambda=0)(t=0)</sup> = 1 that we have seen as complete solution before.

[note for completeness sake:] u(t) is injected into ∂u/∂t = [y,y']' = Au = e<sup>At</sup>[y(0),y'(0)] = [[1,t],[0,1]] [y(0),y'(0)] = [y(0)+y'(0)],y'(0)]

12. 
  a.  sustitute y = e<sup>&lambda;t</sup> into y'' = 6y' - 9y to show that &lambda; = 3,3 is a **repeated root**, which is **trouble**: we need a second solution after e<sup>(&lambda;=3)t</sup>.

the matrix equation is ∂u/∂t = ∂ [y,y'] / ∂t = [[0,1],[-9,6]] [y,y'] = Au [ for which u = e<sup>At</sup> is the only solution.  u = e<sup>&lambda;t</sup> comes from diagonalization. ]

  b. Show that this matrix has only a **single line of eigenvectors** which is **also trouble** 

  c. Show that the second solution to y'' = 6y' - 9y is y = te<sup>3t</sup>

a. y'' = 6y' - 9y --> &lambda;<sup>2</sup>e<sup>&lambda;t</sup> = &lambda;6e<sup>&lambda;t</sup> - 9e<sup>&lambda;t</sup> --> &lambda;<sup>2</sup>e<sup>&lambda;t</sup> - 6&lambda;e<sup>&lambda;t</sup> + 9e<sup>&lambda;t</sup> = (&lambda;<sup>2</sup> - 6&lambda; + 9)e<sup>&lambda;t</sup> = e<sup>&lambda;t</sup>(&lambda; - 3)<sup>2</sup> = 0 --> &lambda;<sub>1</sub> = &lambda;<sub>2</sub> = 3 and so need another solution becuse of repeated eigenvalues because of **double root**.

the matrix representation for y'' = 6y' - 9y is given by ∂u/∂t = ∂ [y(t),y'(t)] / ∂t = [[0,1],[-9,6]] [y(t),y'(t)] = Au(t))
employing the &lambda;s in ( A - &lambda; I ) = 0 leads to eigenvectors X = [[-3,1],[-9,3]] which has [1,3] as the **only eigenvector**.  to show that y = te<sup>3t</sup> is a second eigenvector, evaluate the differential equation for this value of y = te<sup>3t</sup> by computing y, y' and y'' using the product rule:

y = te<sup>3t</sup>  
y' = ∂(te<sup>3t</sup>)/∂t = e<sup>3t</sup> + 3te<sup>3t</sup>  
y'' = ∂<sup>2</sup>(e<sup>3t</sup> + 3te<sup>3t</sup>) / ∂t<sup>2</sup> = 3e<sup>3t</sup> + 3e<sup>3t</sup> + 3•3te<sup>3t</sup> = **6e<sup>3t</sup> + 9te<sup>3t</sup>**
then we are asked to show he second solution to y'' = 6y' -9y is y = te<sup>3t</sup>
substitute in  y'' = 6y' -9y = 6(e<sup>3t</sup> + 3te<sup>3t</sup>) - 9(te<sup>3t</sup>) = 6e<sup>3t</sup> + 18te<sup>3t</sup> - 9te<sup>3t</sup> = **6e<sup>3t</sup> + 9te<sup>3t</sup>**
which is y'' showing how y(t) satisfies this differential equation. 

13.  
a. write 2 functions solving ∂<sup>2</sup>dt<sup>2</sup> = -9y and say which starts with y(0) = 3 and y'(0) = 0 ? 

b. the second order equation y'' = -9y produces a vector equation u' = Au: 

u = [y,y'] and ∂u/∂t = [y',y''] = [[0,1],[-9,0]] [y,y'] = Au   (1 always seems to go in to (1,2) spot so ∂y/∂t = y' = 1 • y' )

find u(t) by using eigenvalues / vectors of A where u(0) = (3,0)

a. generally the cycle is 4:   
y = cos x has y' = -sin x has y'' = -cos x has y''' = sin x has y'''' = cos x 
y = sin x has y' = cos x has y'' = -sin x has y''' = -cos x has y'''' = sin x

y'' = <sup>2</sup>dt<sup>2</sup> = -9y has y = A cos t + B cos t as a general solution, into which I read y = cos 3t and y = sin 3t are solutions to y'' = -9y tsince they give y'' = -9 cos 3t and y'' = -9 sin 3t.  [It might be a question of combining these pure solutions for a complete solution.]

which one satisfies y(0) = 1 and which satisfies y(0) = 0 seems obvious since cos 3•0 = 1 and sin 3•0 = 0.

b. u = [y,y'] and ∂u/∂t = [y',y'']  = Au = [[0,1],[-9,0]] [y,y'] = ∂[y,y']/∂t 

A appears diagonalizable since it's vectors are independent. [careful: not sure who wrote this, but only the eignvectors need to be independent for the matris A to be diagonalizable.]

&lambda;<sup>1</sup> = -3i    
&lambda;<sup>2</sup> = 3i    
&lambda;<sup>1</sup> + &lambda;<sup>2</sup> = 0 = trace (A)    
&lambda;<sup>1</sup>&lambda;<sup>2</sup> = -9 • (i)<sup>2</sup> = -9 • -1 = 9 = det A   
x<sub>1</sub> = (1, 3i) and x<sub>1</sub> = (1, -3i) form the null solution for the A - &lambda;<sup>1</sup>I and A - &lambda;<sup>2</sup>I    

y(0) = 0 and y(0) = 3 mean that u(0) = (0,3)   
by way of c = X<sup>-1</sup>u(0) = (3/2,3/2)

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109439229-7c0e5b80-79fb-11eb-9e6d-3b30aa6a932b.png">


this definitely brings it all together *****

![\begin{align*}
u &= 
\begin{bmatrix}
y\\
y'
\end{bmatrix}\\
\frac{\partial u}{\partial t} &= 
\frac{\partial 
\begin{bmatrix}
y\\
y'
\end{bmatrix}
}{\partial t} = 
\begin{bmatrix}
y'\\
y''
\end{bmatrix}\\
&=Au =
\begin{bmatrix}
0&1\\
-9&0
\end{bmatrix}
\begin{bmatrix}
y\\
y'
\end{bmatrix}\\
&=\frac{\partial u(t)}{\partial t} = 
\frac{\partial 
\begin{bmatrix}
y(t)\\
y'(t)
\end{bmatrix}
}{\partial t} = Au = Au(t)(u(0)) = Ae^{At}u(0) = Xe^{&Lambda;t}X^{-1}u(0) = Xe^{&Lambda;t}c \\
\\
&=Xe^{&Lambda;t}X^{-1}u(0)\\
\\
&=
\begin{bmatrix}
1&1\\
-3i&3i
\end{bmatrix}
\begin{bmatrix}
e^{-3it}&\\
&e^{3it}
\end{bmatrix}
(\frac{1}{6i})
\begin{bmatrix}
3i&-1\\
3i&1
\end{bmatrix}
\begin{bmatrix}
3\\
0
\end{bmatrix} \\ 
&=
\begin{bmatrix}
1&1\\
-3i&3i
\end{bmatrix}
\begin{bmatrix}
e^{-3it}&\\
&e^{3it}
\end{bmatrix}
(-\frac{i}{6})
\begin{bmatrix}
3i&-1\\
3i&1
\end{bmatrix}
\begin{bmatrix}
3\\
0
\end{bmatrix} \\ &=
\begin{bmatrix}
1&1\\
-3i&3i
\end{bmatrix}
\begin{bmatrix}
e^{-3it}&\\
&e^{3it}
\end{bmatrix}
\begin{bmatrix}
\frac{1}{2}&\frac{i}{6}\\
\frac{1}{2}&-\frac{1}{2}
\end{bmatrix}
\begin{bmatrix}
3\\
0
\end{bmatrix} \\ & = Xe^{&Lambda;t}c \\
&=
\begin{bmatrix}
1&1\\
-3i&3i
\end{bmatrix}
\begin{bmatrix}
e^{-3it}&\\
&e^{3it}
\end{bmatrix}
\begin{bmatrix}
\frac{3}{2}\\
\frac{3}{2}
\end{bmatrix}\\
where:&\\
c&=\begin{bmatrix}
\frac{1}{2}&\frac{i}{6}\\
\frac{1}{2}&-\frac{1}{2}
\end{bmatrix}
\begin{bmatrix}
3\\
0
\end{bmatrix}=
\begin{bmatrix}
\frac{3}{2}\\
\frac{3}{2}
\end{bmatrix}\\
thus:&\\
u(t) &= \frac{y(t)}{y'(t)} = X&Lambda;X^{-1}u(0) = X&Lambda;c = 
\begin{bmatrix}
1&1\\
-3i&3i
\end{bmatrix}
\begin{bmatrix}
e^{-3it}&\\
&e^{3it}
\end{bmatrix}
\begin{bmatrix}
\frac{3}{2}\\
\frac{3}{2}
\end{bmatrix}\\
&=c_1x_1&lambda;_1 + c_2x_2&lambda;_2\\
\\
\\
&=\frac{3}{2}
\begin{bmatrix}
1\\
-3i
\end{bmatrix}
e^{-3it}+
\frac{3}{2}
\begin{bmatrix}
1\\
3i
\end{bmatrix}
e^{3it}\\
\\
&=\frac{3}{2}
(\begin{bmatrix}
e^{-3it}\\
-3ie^{-3it}
\end{bmatrix}+
\begin{bmatrix}
e^{3it}\\
3ie^{3it}
\end{bmatrix})
\\
\\
&=\frac{1}{2}
(\begin{bmatrix}
3e^{-3it}\\
-9ie^{-3it}
\end{bmatrix}+
\begin{bmatrix}
3e^{3it}\\
9ie^{3it}
\end{bmatrix})
\\
&=\frac{1}{2}
(\begin{bmatrix}
3(e^{3it}+e^{-3it})\\
9i(e^{3it}-e^{-3it})
\end{bmatrix})\\
\\&=
\begin{bmatrix}
3(\frac{e^{3it}+e^{-3it}}{2})\\
9i(\frac{(e^{3it}-e^{-3it})}{2})
\end{bmatrix}\\
\\
\\&=
\begin{bmatrix}
3(cos3t)\\
9i(isin3t)
\end{bmatrix}\\
\\
\\&=
\begin{bmatrix}
3 cos 3t\\
-9 sin 3t
\end{bmatrix}\\
\\
because&\\
Euler:&\\ \\
e^{i\theta} &= cos \theta + i sin \theta\\
e^{-i\theta} &= cos \theta - i sin \theta\\
e^{i\theta}+e^{-i\theta}&=cos \theta + i sin \theta + cos \theta - i sin \theta\\
&=2cos \theta \\
e^{i\theta}-e^{-i\theta}&=cos \theta + i sin \theta - cos \theta + i sin \theta\\
&=2i sin \theta\\
\frac{e^{i\theta}+e^{-i\theta}}{2}&=cos \theta \\
\frac{e^{i\theta}-e^{-i\theta}}{2}&=i sin \theta\\
\\
\\
\\
\\
u(0) &= 
u(t=0) = \frac{y(t=0)}{y'(t=0)} = X&Lambda;^0X^{-1}u(0) = X(1)X^{-1}u(0) = I*u(0)= X&Lambda;^0c \\
&= 
\begin{bmatrix}
1&1\\
-3i&3i
\end{bmatrix}
\begin{bmatrix}
e^{-3i(t=0}&\\
&e^{3i(t=0)}
\end{bmatrix}
\begin{bmatrix}
\frac{3}{2}\\
\frac{3}{2}
\end{bmatrix}\\
&=\frac{3}{2}
\begin{bmatrix}
1\\
-3i
\end{bmatrix}
e^{-3i(t=0)}+
\frac{3}{2}
\begin{bmatrix}
1\\
3i
\end{bmatrix}
e^{3i((t=0)}\\
&=\frac{3}{2}
(
\begin{bmatrix}
1\\
-3i
\end{bmatrix}
+
\begin{bmatrix}
1\\
3i
\end{bmatrix})\\
&=\frac{3}{2}
\begin{bmatrix}
2\\
0
\end{bmatrix}=
\begin{bmatrix}
3\\
0
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Ay%27%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%26%3D+%0A%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Ay%27%0A%5Cend%7Bbmatrix%7D%0A%7D%7B%5Cpartial+t%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ay%27%5C%5C%0Ay%27%27%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3DAu+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%261%5C%5C%0A-9%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Ay%27%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3D%5Cfrac%7B%5Cpartial+u%28t%29%7D%7B%5Cpartial+t%7D+%3D+%0A%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Ay%28t%29%5C%5C%0Ay%27%28t%29%0A%5Cend%7Bbmatrix%7D%0A%7D%7B%5Cpartial+t%7D+%3D+Au+%3D+Au%28t%29%28u%280%29%29+%3D+Ae%5E%7BAt%7Du%280%29+%3D+Xe%5E%7B%26Lambda%3Bt%7DX%5E%7B-1%7Du%280%29+%3D+Xe%5E%7B%26Lambda%3Bt%7Dc+%5C%5C%0A%5C%5C%0A%26%3DXe%5E%7B%26Lambda%3Bt%7DX%5E%7B-1%7Du%280%29%5C%5C%0A%5C%5C%0A%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A-3i%263i%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B-3it%7D%26%5C%5C%0A%26e%5E%7B3it%7D%0A%5Cend%7Bbmatrix%7D%0A%28%5Cfrac%7B1%7D%7B6i%7D%29%0A%5Cbegin%7Bbmatrix%7D%0A3i%26-1%5C%5C%0A3i%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A3%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D+%5C%5C+%0A%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A-3i%263i%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B-3it%7D%26%5C%5C%0A%26e%5E%7B3it%7D%0A%5Cend%7Bbmatrix%7D%0A%28-%5Cfrac%7Bi%7D%7B6%7D%29%0A%5Cbegin%7Bbmatrix%7D%0A3i%26-1%5C%5C%0A3i%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A3%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D+%5C%5C+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A-3i%263i%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B-3it%7D%26%5C%5C%0A%26e%5E%7B3it%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7Bi%7D%7B6%7D%5C%5C%0A%5Cfrac%7B1%7D%7B2%7D%26-%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A3%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D+%5C%5C+%26+%3D+Xe%5E%7B%26Lambda%3Bt%7Dc+%5C%5C%0A%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A-3i%263i%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B-3it%7D%26%5C%5C%0A%26e%5E%7B3it%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B3%7D%7B2%7D%5C%5C%0A%5Cfrac%7B3%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0Awhere%3A%26%5C%5C%0Ac%26%3D%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7Bi%7D%7B6%7D%5C%5C%0A%5Cfrac%7B1%7D%7B2%7D%26-%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A3%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B3%7D%7B2%7D%5C%5C%0A%5Cfrac%7B3%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0Athus%3A%26%5C%5C%0Au%28t%29+%26%3D+%5Cfrac%7By%28t%29%7D%7By%27%28t%29%7D+%3D+X%26Lambda%3BX%5E%7B-1%7Du%280%29+%3D+X%26Lambda%3Bc+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A-3i%263i%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B-3it%7D%26%5C%5C%0A%26e%5E%7B3it%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B3%7D%7B2%7D%5C%5C%0A%5Cfrac%7B3%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3Dc_1x_1%26lambda%3B_1+%2B+c_2x_2%26lambda%3B_2%5C%5C%0A%5C%5C%0A%5C%5C%0A%26%3D%5Cfrac%7B3%7D%7B2%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-3i%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B-3it%7D%2B%0A%5Cfrac%7B3%7D%7B2%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A3i%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B3it%7D%5C%5C%0A%5C%5C%0A%26%3D%5Cfrac%7B3%7D%7B2%7D%0A%28%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B-3it%7D%5C%5C%0A-3ie%5E%7B-3it%7D%0A%5Cend%7Bbmatrix%7D%2B%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B3it%7D%5C%5C%0A3ie%5E%7B3it%7D%0A%5Cend%7Bbmatrix%7D%29%0A%5C%5C%0A%5C%5C%0A%26%3D%5Cfrac%7B1%7D%7B2%7D%0A%28%5Cbegin%7Bbmatrix%7D%0A3e%5E%7B-3it%7D%5C%5C%0A-9ie%5E%7B-3it%7D%0A%5Cend%7Bbmatrix%7D%2B%0A%5Cbegin%7Bbmatrix%7D%0A3e%5E%7B3it%7D%5C%5C%0A9ie%5E%7B3it%7D%0A%5Cend%7Bbmatrix%7D%29%0A%5C%5C%0A%26%3D%5Cfrac%7B1%7D%7B2%7D%0A%28%5Cbegin%7Bbmatrix%7D%0A3%28e%5E%7B3it%7D%2Be%5E%7B-3it%7D%29%5C%5C%0A9i%28e%5E%7B3it%7D-e%5E%7B-3it%7D%29%0A%5Cend%7Bbmatrix%7D%29%5C%5C%0A%5C%5C%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A3%28%5Cfrac%7Be%5E%7B3it%7D%2Be%5E%7B-3it%7D%7D%7B2%7D%29%5C%5C%0A9i%28%5Cfrac%7B%28e%5E%7B3it%7D-e%5E%7B-3it%7D%29%7D%7B2%7D%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%5C%5C%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A3%28cos3t%29%5C%5C%0A9i%28isin3t%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%5C%5C%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A3+cos+3t%5C%5C%0A-9+sin+3t%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Abecause%26%5C%5C%0AEuler%3A%26%5C%5C+%5C%5C%0Ae%5E%7Bi%5Ctheta%7D+%26%3D+cos+%5Ctheta+%2B+i+sin+%5Ctheta%5C%5C%0Ae%5E%7B-i%5Ctheta%7D+%26%3D+cos+%5Ctheta+-+i+sin+%5Ctheta%5C%5C%0Ae%5E%7Bi%5Ctheta%7D%2Be%5E%7B-i%5Ctheta%7D%26%3Dcos+%5Ctheta+%2B+i+sin+%5Ctheta+%2B+cos+%5Ctheta+-+i+sin+%5Ctheta%5C%5C%0A%26%3D2cos+%5Ctheta+%5C%5C%0Ae%5E%7Bi%5Ctheta%7D-e%5E%7B-i%5Ctheta%7D%26%3Dcos+%5Ctheta+%2B+i+sin+%5Ctheta+-+cos+%5Ctheta+%2B+i+sin+%5Ctheta%5C%5C%0A%26%3D2i+sin+%5Ctheta%5C%5C%0A%5Cfrac%7Be%5E%7Bi%5Ctheta%7D%2Be%5E%7B-i%5Ctheta%7D%7D%7B2%7D%26%3Dcos+%5Ctheta+%5C%5C%0A%5Cfrac%7Be%5E%7Bi%5Ctheta%7D-e%5E%7B-i%5Ctheta%7D%7D%7B2%7D%26%3Di+sin+%5Ctheta%5C%5C%0A%5C%5C%0A%5C%5C%0A%5C%5C%0A%5C%5C%0Au%280%29+%26%3D+%0Au%28t%3D0%29+%3D+%5Cfrac%7By%28t%3D0%29%7D%7By%27%28t%3D0%29%7D+%3D+X%26Lambda%3B%5E0X%5E%7B-1%7Du%280%29+%3D+X%281%29X%5E%7B-1%7Du%280%29+%3D+I%2Au%280%29%3D+X%26Lambda%3B%5E0c+%5C%5C%0A%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A-3i%263i%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B-3i%28t%3D0%7D%26%5C%5C%0A%26e%5E%7B3i%28t%3D0%29%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B3%7D%7B2%7D%5C%5C%0A%5Cfrac%7B3%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3D%5Cfrac%7B3%7D%7B2%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-3i%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B-3i%28t%3D0%29%7D%2B%0A%5Cfrac%7B3%7D%7B2%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A3i%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B3i%28%28t%3D0%29%7D%5C%5C%0A%26%3D%5Cfrac%7B3%7D%7B2%7D%0A%28%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-3i%0A%5Cend%7Bbmatrix%7D%0A%2B%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A3i%0A%5Cend%7Bbmatrix%7D%29%5C%5C%0A%26%3D%5Cfrac%7B3%7D%7B2%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A3%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

<img width="1137" alt="image" src="https://user-images.githubusercontent.com/38410965/109438444-0b197480-79f8-11eb-973d-e06df55dccec.png">


14. ∂u/∂t = Au is solved only by u = e<sup>At</sup>

length sqaured of any vector including our u that is composed of e<sup>At</sup> is
|| u(t) ||<sup>2</sup> = u<sub>1</sub><sup>2</sup> + u<sub>2</sub><sup>2</sup> + u<sub>3 </sub><sup>2</sup>

by the product rule, the derivative of this squared length = ∂|| u(t) ||<sup>2</sup>/∂t = 2uu' = 2u<sub>1</sub>u'<sub>1 </sub> + 2u<sub>2</sub>u'<sub>2</sub> + 2u<sub>3 </sub>u'<sub>3 </sub>

we are given a skew symmetric A: A<sup>T</sup> = -A

∂u/∂t = u' = Au = [[0,c,-b],[-c,0,a],[b,-a,0]] u = [u<sub>1</sub>', u<sub>1</sub>', u<sub>1</sub>']  
where  
u<sub>1</sub>' = Au<sub>1</sub> = cu<sub>2</sub> - bu<sub>3</sub> 
u<sub>2</sub>' = Au<sub>2</sub> = au<sub>3</sub> - cu<sub>1</sub>  
u<sub>3</sub>' = Au<sub>3</sub> = bu<sub>1</sub> - au<sub>2</sub>  

substitute u' = u<sub>1</sub>', u<sub>3</sub>', u<sub>3</sub>' into ∂|| u(t) ||<sup>2</sup>/∂t to see that it is zero.

∂|| u(t) ||<sup>2</sup>/∂t 
= 2u<sub>1</sub>(cu<sub>2</sub> - bu<sub>3</sub>)  
+ 2u<sub>2</sub>(au<sub>3</sub> - cu<sub>1</sub>)  
+ 2u<sub>3</sub>(bu<sub>1</sub> - au<sub>2</sub>)  
= 2cu<sub>1</sub>u<sub>2</sub> - 2bu<sub>1</sub>u<sub>3</sub>    
+ 2au<sub>2</sub>u<sub>3</sub> - 2cu<sub>2</sub>u<sub>1</sub>       
+ 2bu<sub>3</sub>u<sub>1</sub> - 2a<sub>3</sub>u<sub>2</sub>  
= 2cu<sub>1</sub>u<sub>2</sub> - 2cu<sub>2</sub>u<sub>1</sub>    
+ 2au<sub>2</sub>u<sub>3</sub> - 2a<sub>3</sub>u<sub>2</sub>        
+ 2bu<sub>3</sub>u<sub>1</sub> - 2bu<sub>1</sub>u<sub>3</sub>      
= 0   

illustrates that || u(t) ||<sup>2</sup> stays equal to || u(t=0) ||<sup>2</sup> because it's first derivative with respect to time = ∂|| u(t) ||<sup>2</sup>/∂t = 0: ||u|| is a constant when u = e<sup>A</sup> as it is when ∂u/∂t = Au AND when A<sup>T</sup> = -A.

when A is skew symmetric the derivative of u(t) ||<sup>2</sup> is zero.  

when A is skew symmetric Q = e<sup>At</sup> is an orthogonal matrix
Q<sup>T</sup> = e<sup>-At</sup> 
thus Q<sup>T</sup>Q  = I


15. a particular solution to ∂u/∂t = Au - b finds u<sub>p</sub> = A<sup>-1</sup>b when A is invertible.

the usual solutions to ∂u/∂t = Au give u<sub>n</sub> or null solution.  Find the complete solution u = u<sub>p</sub> + u<sub>n</sub>

17. find matrix illustrating these unstable regions of the D T plane
- &lambda;<sub>1</sub> < 0 and &lambda;<sub>2</sub> > 0

D = (&lambda;<sub>1</sub> < 0)(&lambda;<sub>2</sub> > 0) needs to be < 0   
T can be whatever: (&lambda;<sub>1</sub> < 0) + (&lambda;<sub>2</sub> > 0) can be > = < 0

[[1,0],[0-1]] works since it isolates the D as negative and stands in middle of T range.

- &lambda;<sub>1</sub> > 0 and &lambda;<sub>2</sub> > 0

D = (&lambda;<sub>1</sub> < 0)(&lambda;<sub>2</sub> > 0) needs to be > 0   
T = (&lambda;<sub>1</sub> < 0) + (&lambda;<sub>2</sub> > 0) can be > 0

the identity matrix works

- &lambda; = a &pm; i with a > 0

[&lambda;>0 since unstable]

T<sup>2</sup> < 4D imaginary &lambda;s  
T<sup>2</sup> > 4D real &lambda;s  
the real parts of &lambda;<sub>1</sub> and &lambda;<sub>2</sub> are the same and the product of their imaginary = -1.    
since a > 0, 


18. write 5 items of infinite series for e<sup>At</sup> and take their derivative to prove e<sup>At</sup>u<sub>0</sub> solves u' = Au but as part of this see that you have 4 terms of Ae<sup>At</sup> in the end. [infinite series so doesnt matter if fewer terms]

this is good.

∂u/∂t = Au is nothing more than the chain rule since ∂e<sup>At</sup>/∂t = e<sup>At</sup> and ∂At/∂t = A;  the denominator drops out with the product rule since the added quantity of their derivative is zero. Because its the chain rule, (exponent of At)' = exponent -1 and that exponent becomes a factor to At and cancels with the factorial denominator.  A regains its original exponent but loses it when factored out in the end for Au.  AND the intention here is to show that a component drops out.  

![\begin{align*}
u = e^{At} & = I + At + \frac{1}{2}(At)^2 + \frac{1}{6}(At)^3 + \frac{1}{24}(At)^4 ...\\
& = \frac{(At)^0}{0!} + \frac{(At)^1}{1!} + \frac{(At)^2}{2!} + \frac{(At)^3}{3!} + \frac{(At)^4}{4!} ...\\
\frac{\partial u}{\partial t} = \frac{\partial e^{At}}{\partial t} & = (At)'(\frac{(At)^0}{0!})' + (At)'(\frac{(At)^1}{1!})' + (At)'(\frac{(At)^2}{2!})' + (At)'(\frac{(At)^3}{3!})' + (At)'(\frac{(At)^4}{4!})' ...\\
& = A(\frac{(At)^0}{0!})' + A(\frac{(At)^1}{1!}) + A(\frac{(At)^2}{2!})' + A(\frac{(At)^3}{3!})' + A(\frac{(At)^4}{4!})' ...\\
& = A(zero) + A(\frac{1(At)^0}{1!}) + A(\frac{2(At)^1}{2!}) + A(\frac{3(At)^2}{3!}) + A(\frac{4(At)^3}{4!}) ...\\
& = gone + A(I) + A(\frac{At^1}{1!}) + A(\frac{(At)^2}{2!}) + A(\frac{(At)^3}{3!}) ...\\
& = A(I) + A(\frac{At}{1!}) + A(\frac{(At)^2}{2!}) + A(\frac{(At)^3}{3!}) ... \\
& = A + \frac{A^2t}{1!} + \frac{A^3t^2}{2!} + \frac{A^4t^3}{3!} ...\\
& = A + A^2t + \frac{A^3t^2}{2} + \frac{A^4t^3}{6} ...\\
& = A(I + At + \frac{(At)^2}{2} + \frac{(At)^3}{6} ...)\\
& = A(I + At + \frac{1}{2}(At)^2 + \frac{1}{6}(At)^3 ...)\\
& = Au
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au+%3D+e%5E%7BAt%7D+%26+%3D+I+%2B+At+%2B+%5Cfrac%7B1%7D%7B2%7D%28At%29%5E2+%2B+%5Cfrac%7B1%7D%7B6%7D%28At%29%5E3+%2B+%5Cfrac%7B1%7D%7B24%7D%28At%29%5E4+...%5C%5C%0A%26+%3D+%5Cfrac%7B%28At%29%5E0%7D%7B0%21%7D+%2B+%5Cfrac%7B%28At%29%5E1%7D%7B1%21%7D+%2B+%5Cfrac%7B%28At%29%5E2%7D%7B2%21%7D+%2B+%5Cfrac%7B%28At%29%5E3%7D%7B3%21%7D+%2B+%5Cfrac%7B%28At%29%5E4%7D%7B4%21%7D+...%5C%5C%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%3D+%5Cfrac%7B%5Cpartial+e%5E%7BAt%7D%7D%7B%5Cpartial+t%7D+%26+%3D+%28At%29%27%28%5Cfrac%7B%28At%29%5E0%7D%7B0%21%7D%29%27+%2B+%28At%29%27%28%5Cfrac%7B%28At%29%5E1%7D%7B1%21%7D%29%27+%2B+%28At%29%27%28%5Cfrac%7B%28At%29%5E2%7D%7B2%21%7D%29%27+%2B+%28At%29%27%28%5Cfrac%7B%28At%29%5E3%7D%7B3%21%7D%29%27+%2B+%28At%29%27%28%5Cfrac%7B%28At%29%5E4%7D%7B4%21%7D%29%27+...%5C%5C%0A%26+%3D+A%28%5Cfrac%7B%28At%29%5E0%7D%7B0%21%7D%29%27+%2B+A%28%5Cfrac%7B%28At%29%5E1%7D%7B1%21%7D%29+%2B+A%28%5Cfrac%7B%28At%29%5E2%7D%7B2%21%7D%29%27+%2B+A%28%5Cfrac%7B%28At%29%5E3%7D%7B3%21%7D%29%27+%2B+A%28%5Cfrac%7B%28At%29%5E4%7D%7B4%21%7D%29%27+...%5C%5C%0A%26+%3D+A%28zero%29+%2B+A%28%5Cfrac%7B1%28At%29%5E0%7D%7B1%21%7D%29+%2B+A%28%5Cfrac%7B2%28At%29%5E1%7D%7B2%21%7D%29+%2B+A%28%5Cfrac%7B3%28At%29%5E2%7D%7B3%21%7D%29+%2B+A%28%5Cfrac%7B4%28At%29%5E3%7D%7B4%21%7D%29+...%5C%5C%0A%26+%3D+gone+%2B+A%28I%29+%2B+A%28%5Cfrac%7BAt%5E1%7D%7B1%21%7D%29+%2B+A%28%5Cfrac%7B%28At%29%5E2%7D%7B2%21%7D%29+%2B+A%28%5Cfrac%7B%28At%29%5E3%7D%7B3%21%7D%29+...%5C%5C%0A%26+%3D+A%28I%29+%2B+A%28%5Cfrac%7BAt%7D%7B1%21%7D%29+%2B+A%28%5Cfrac%7B%28At%29%5E2%7D%7B2%21%7D%29+%2B+A%28%5Cfrac%7B%28At%29%5E3%7D%7B3%21%7D%29+...+%5C%5C%0A%26+%3D+A+%2B+%5Cfrac%7BA%5E2t%7D%7B1%21%7D+%2B+%5Cfrac%7BA%5E3t%5E2%7D%7B2%21%7D+%2B+%5Cfrac%7BA%5E4t%5E3%7D%7B3%21%7D+...%5C%5C%0A%26+%3D+A+%2B+A%5E2t+%2B+%5Cfrac%7BA%5E3t%5E2%7D%7B2%7D+%2B+%5Cfrac%7BA%5E4t%5E3%7D%7B6%7D+...%5C%5C%0A%26+%3D+A%28I+%2B+At+%2B+%5Cfrac%7B%28At%29%5E2%7D%7B2%7D+%2B+%5Cfrac%7B%28At%29%5E3%7D%7B6%7D+...%29%5C%5C%0A%26+%3D+A%28I+%2B+At+%2B+%5Cfrac%7B1%7D%7B2%7D%28At%29%5E2+%2B+%5Cfrac%7B1%7D%7B6%7D%28At%29%5E3+...%29%5C%5C%0A%26+%3D+Au%0A%5Cend%7Balign%2A%7D)

20. starting from u(0) the solution at time T is e<sup>AT</sup>u(0)   
moving an additional time t to reach a solution e<sup>At</sup>e<sup>AT</sup>u(0)    
which can also be written as e<sup>At+ AT</sup>u(0) = e<sup>A(T+t)</sup>u(0)

21. 

![\begin{align*}
u = e^{At} & = I + At + \frac{1}{2}(At)^2 + \frac{1}{6}(At)^3 + \frac{1}{24}(At)^4 ...\\
& = I + X&Lambda;X^{-1}t + X&Lambda;^2X^{-1}(\frac{t^2}{2})+ X&Lambda;^3X^{-1}(\frac{t^3}{6})\\
& = XX^{-1} + X&Lambda;X^{-1}t + X&Lambda;^2X^{-1}(\frac{t^2}{2})+ X&Lambda;^3X^{-1}(\frac{t^3}{6}) \\
& = X(I + &Lambda;t + &Lambda;^2(\frac{t^2}{2})+ &Lambda;^3(\frac{t^3}{6}))X^{-1}\\
add \, inside \, matrices:&\\
& = 
X( \,
\begin{bmatrix}
1&\\
&1
\end{bmatrix}+
\begin{bmatrix}
&lambda;_1&\\
& &lambda;_2
\end{bmatrix}^1( t) +
\begin{bmatrix}
&lambda;_1&\\
& &lambda;_2
\end{bmatrix}^2 (\frac{t^2}{2}) +
\begin{bmatrix}
&lambda;_1&\\
& &lambda;_2
\end{bmatrix}^3  (\frac{t^3}{6}) +...
) \, X^{-1}\\
& = 
X( \,
\begin{bmatrix}
1&\\
&1
\end{bmatrix}+
\begin{bmatrix}
&lambda;_1t&\\
& &lambda;_2t
\end{bmatrix} +
\begin{bmatrix}
&lambda;_1\frac{t^2}{2}&\\
& &lambda;_2\frac{t^2}{2}
\end{bmatrix}^2 +
\begin{bmatrix}
&lambda;_1 \frac{t^3}{6}&\\
& &lambda;_2 \frac{t^3}{6}
\end{bmatrix}^3 + ...
) \, X^{-1}\\
& = 
X \,
\begin{bmatrix}
1+&lambda;_1t+&lambda;_1\frac{t^2}{2} + &lambda;_1 \frac{t^3}{6} + ...&\\
&1+&lambda;_2t + &lambda;_2\frac{t^2}{2} + &lambda;_2 \frac{t^3}{6} + ...
\end{bmatrix} \,
 X^{-1}\\
& = 
X \,
\begin{bmatrix}
e^{&lambda;_1t}&\\
&e^{&lambda;_2t}
\end{bmatrix} \,
 X^{-1}\\
& = 
X &Lambda;
 X^{-1}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au+%3D+e%5E%7BAt%7D+%26+%3D+I+%2B+At+%2B+%5Cfrac%7B1%7D%7B2%7D%28At%29%5E2+%2B+%5Cfrac%7B1%7D%7B6%7D%28At%29%5E3+%2B+%5Cfrac%7B1%7D%7B24%7D%28At%29%5E4+...%5C%5C%0A%26+%3D+I+%2B+X%26Lambda%3BX%5E%7B-1%7Dt+%2B+X%26Lambda%3B%5E2X%5E%7B-1%7D%28%5Cfrac%7Bt%5E2%7D%7B2%7D%29%2B+X%26Lambda%3B%5E3X%5E%7B-1%7D%28%5Cfrac%7Bt%5E3%7D%7B6%7D%29%5C%5C%0A%26+%3D+XX%5E%7B-1%7D+%2B+X%26Lambda%3BX%5E%7B-1%7Dt+%2B+X%26Lambda%3B%5E2X%5E%7B-1%7D%28%5Cfrac%7Bt%5E2%7D%7B2%7D%29%2B+X%26Lambda%3B%5E3X%5E%7B-1%7D%28%5Cfrac%7Bt%5E3%7D%7B6%7D%29+%5C%5C%0A%26+%3D+X%28I+%2B+%26Lambda%3Bt+%2B+%26Lambda%3B%5E2%28%5Cfrac%7Bt%5E2%7D%7B2%7D%29%2B+%26Lambda%3B%5E3%28%5Cfrac%7Bt%5E3%7D%7B6%7D%29%29X%5E%7B-1%7D%5C%5C%0Aadd+%5C%2C+inside+%5C%2C+matrices%3A%26%5C%5C%0A%26+%3D+%0AX%28+%5C%2C%0A%5Cbegin%7Bbmatrix%7D%0A1%26%5C%5C%0A%261%0A%5Cend%7Bbmatrix%7D%2B%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26+%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%5E1%28+t%29+%2B%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26+%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%5E2+%28%5Cfrac%7Bt%5E2%7D%7B2%7D%29+%2B%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26+%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%5E3++%28%5Cfrac%7Bt%5E3%7D%7B6%7D%29+%2B...%0A%29+%5C%2C+X%5E%7B-1%7D%5C%5C%0A%26+%3D+%0AX%28+%5C%2C%0A%5Cbegin%7Bbmatrix%7D%0A1%26%5C%5C%0A%261%0A%5Cend%7Bbmatrix%7D%2B%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1t%26%5C%5C%0A%26+%26lambda%3B_2t%0A%5Cend%7Bbmatrix%7D+%2B%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%5Cfrac%7Bt%5E2%7D%7B2%7D%26%5C%5C%0A%26+%26lambda%3B_2%5Cfrac%7Bt%5E2%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%5E2+%2B%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1+%5Cfrac%7Bt%5E3%7D%7B6%7D%26%5C%5C%0A%26+%26lambda%3B_2+%5Cfrac%7Bt%5E3%7D%7B6%7D%0A%5Cend%7Bbmatrix%7D%5E3+%2B+...%0A%29+%5C%2C+X%5E%7B-1%7D%5C%5C%0A%26+%3D+%0AX+%5C%2C%0A%5Cbegin%7Bbmatrix%7D%0A1%2B%26lambda%3B_1t%2B%26lambda%3B_1%5Cfrac%7Bt%5E2%7D%7B2%7D+%2B+%26lambda%3B_1+%5Cfrac%7Bt%5E3%7D%7B6%7D+%2B+...%26%5C%5C%0A%261%2B%26lambda%3B_2t+%2B+%26lambda%3B_2%5Cfrac%7Bt%5E2%7D%7B2%7D+%2B+%26lambda%3B_2+%5Cfrac%7Bt%5E3%7D%7B6%7D+%2B+...%0A%5Cend%7Bbmatrix%7D+%5C%2C%0A+X%5E%7B-1%7D%5C%5C%0A%26+%3D+%0AX+%5C%2C%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B%26lambda%3B_1t%7D%26%5C%5C%0A%26e%5E%7B%26lambda%3B_2t%7D%0A%5Cend%7Bbmatrix%7D+%5C%2C%0A+X%5E%7B-1%7D%5C%5C%0A%26+%3D+%0AX+%26Lambda%3B%0A+X%5E%7B-1%7D%0A%5Cend%7Balign%2A%7D)


22. if A<sup>2</sup> = A show that the infinite series produces e<sup>At</sup> = I + (e<sup>r</sup> - I)A.

this is true for [[1,4],[0,0]

e<sup>At</sup>   
= I + At + (At)<sup>2</sup>/2 + (At)<sup>2</sup>/2 + ...  
= I + At + At<sup>2</sup>/2 + At<sup>2</sup>/2 + ...    (because we say if A<sup>2</sup> = A)  
= I + A(e<sup>t</sup> - 1) because ...  

e<sup>t</sup> = 1 + t + t<sup>2</sup>/2 + t<sup>3</sup>/6 + ...
e<sup>t</sup> - 1 = t + t<sup>2</sup>/2 + t<sup>3</sup>/6 + ...

A(e<sup>t</sup> - 1) 
= A(t + t<sup>2</sup>/2 + t<sup>3</sup>/6 + ...)
= At + At<sup>2</sup>/2 + At<sup>3</sup>/6 + ...

I + A(e<sup>t</sup> - 1) 
= I + At + At<sup>2</sup>/2 + At<sup>3</sup>/6 + ...
= e<sup>At</sup>

so for our matrix, e<sup>At</sup> = I + (e<sup>t</sup> -1) A = I + (e<sup>t</sup> -1)[[1,4],[0,0]

26. 2 reasons why e<sup>At</sup> is never singular:

since matrix (e<sup>At</sup>)<sup>-1</sup> = e<sup>-At</sup>, matrix e<sup>At</sup> is never singular.

if Ax = &lambda;x then e<sup>At</sup>x = e<sup>&lambda;t</sup>x and e<sup>&lambda;t</sup> is never = 0

27.  dont make this mistake.  matrix A has a positive eigenvalue and thus blows up as t goes to infnity.  to correct this a scientist switched the rows and found that the eigenvalues were negative et voila stability.  if you look however, it is not the same with different eigenvalues and eigenvectors and thus is a different equation.  

if switch rows in A, must also switch columns.  

3 examples seem like they should be the same   
- the original matrix A: 
∂x/∂t = 0x-4y 
∂y/∂t = -2x +2y
- the matrix with rows switched Ar
∂y/∂t = -2x +2y
∂x/∂t = 0x-4y 
- the matrix with rows and columns switched Arc
∂y/∂t = -2x +2y
∂x/∂t = 0x-4y 

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/109549699-51c0aa80-7a9c-11eb-8dd8-23f9f6890981.png">


the problem is that we switch the rows of A but not of u.  The equations work out with this configuration, but e.g. ∂y is no longer = y' ∂x is = y'!

![\begin{align*}
\frac{\partial x}{\partial t} &= 0x -4y \\
\frac{\partial y}{\partial t} &= -2x+2y \\
\frac{\partial \frac{x}{y}}{\partial t} &= 
\begin{bmatrix}
0&-4\\
-2&2
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}=
\begin{bmatrix}
0x-4y\\
-2x+2y
\end{bmatrix}
\\
\\
\frac{\partial y}{\partial t} &= -2x+2y \\
\frac{\partial x}{\partial t} &= 0x -4y \\
\frac{\partial \frac{y}{x}}{\partial t} &= 
\begin{bmatrix}
-2&2\\
0&-4
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}=
\begin{bmatrix}
-2x+2y\\
0x-4y
\end{bmatrix}
\\
\\
\frac{\partial y}{\partial t} &= 2y-2x \\
\frac{\partial x}{\partial t} &= -4y +0x \\
\frac{\partial \frac{y}{x}}{\partial t} &= 
\begin{bmatrix}
2&-2\\
-4&0
\end{bmatrix}
\begin{bmatrix}
y\\
x
\end{bmatrix}=
\begin{bmatrix}
2y-2x\\
-4y+ 0x
\end{bmatrix}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5Cpartial+x%7D%7B%5Cpartial+t%7D+%26%3D+0x+-4y+%5C%5C%0A%5Cfrac%7B%5Cpartial+y%7D%7B%5Cpartial+t%7D+%26%3D+-2x%2B2y+%5C%5C%0A%5Cfrac%7B%5Cpartial+%5Cfrac%7Bx%7D%7By%7D%7D%7B%5Cpartial+t%7D+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A0%26-4%5C%5C%0A-2%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A0x-4y%5C%5C%0A-2x%2B2y%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%5C%5C%0A%5Cfrac%7B%5Cpartial+y%7D%7B%5Cpartial+t%7D+%26%3D+-2x%2B2y+%5C%5C%0A%5Cfrac%7B%5Cpartial+x%7D%7B%5Cpartial+t%7D+%26%3D+0x+-4y+%5C%5C%0A%5Cfrac%7B%5Cpartial+%5Cfrac%7By%7D%7Bx%7D%7D%7B%5Cpartial+t%7D+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-2%262%5C%5C%0A0%26-4%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A-2x%2B2y%5C%5C%0A0x-4y%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%5C%5C%0A%5Cfrac%7B%5Cpartial+y%7D%7B%5Cpartial+t%7D+%26%3D+2y-2x+%5C%5C%0A%5Cfrac%7B%5Cpartial+x%7D%7B%5Cpartial+t%7D+%26%3D+-4y+%2B0x+%5C%5C%0A%5Cfrac%7B%5Cpartial+%5Cfrac%7By%7D%7Bx%7D%7D%7B%5Cpartial+t%7D+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-2%5C%5C%0A-4%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Ax%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A2y-2x%5C%5C%0A-4y%2B+0x%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D%0A)

6.4 Sym


section 6.4 Symmetric Matrices

https://github.github.com/gfm/

https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

https://github.com/stevedepp/strang/issues/new

https://tex-image-link-generator.herokuapp.com

principles:   
1. a symmetric matrix s has n real eigenvalues &lambda; and n orthogonal eigenvectors q<sub>1</sub>, ... , q<sub>n</sub>   
2. every real symmetric S can be diagonalized [and therefore has n independent columns?]    
S = Q&Lambda;Q<sup>-1</sup> = Q&Lambda;Q<sup>T</sup>   
[ in place of A = X&Lambda;X<sup>-1</sup> ≠ X&Lambda;X<sup>T</sup> ]
3.  the number of positive eigenvalues of S = the number of positive roots.    
4.  antisymmetric matrices A = -A<sup>T</sup> have imaginary &lambda;s and orthogonal complex q's    
5.  section 9.2 explains why the test S = S<sup>T</sup> becomes S = Sbar<sup>T</sup> for complex matrices.   

![\begin{align*}
S&=
\begin{bmatrix}
0&i\\
-i&0
\end{bmatrix} = \bar{S}_T  \longrightarrow &lambda = 1, \, -1\\
A&=\begin{bmatrix}
0&i\\
i&0
\end{bmatrix} = \bar{A}_T  \longrightarrow &lambda = i, \, -i\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%26i%5C%5C%0A-i%260%0A%5Cend%7Bbmatrix%7D+%3D+%5Cbar%7BS%7D_T++%5Clongrightarrow+%26lambda+%3D+1%2C+%5C%2C+-1%5C%5C%0AA%26%3D%5Cbegin%7Bbmatrix%7D%0A0%26i%5C%5C%0Ai%260%0A%5Cend%7Bbmatrix%7D+%3D+%5Cbar%7BA%7D_T++%5Clongrightarrow+%26lambda+%3D+i%2C+%5C%2C+-i%5C%5C%0A%5Cend%7Balign%2A%7D)


Special properties of eigenvalues &lambda; and eigenvectors x when S = S<sup>T</sup>    
Sx = &lambda;x is special when S is symmetric.  

S = X&Lambda;X<sup>-1</sup> = S<sup>T</sup> = (X<sup>-1</sup>)<sup>T</sup>&Lambda;X<sup>T</sup> because S = S<sup>T</sup>   
possibly because X<sup>T</sup>X = I which makes each eigenvector orthogonal to each other when S=S<sup>T</sup>

Facts:
1. symmetric matrix has only real eigenvalues   
2. symmetric matrix eigenvectors can be **chosen** orthonormal  

n orthonormal eigenvectors go into the columns of X   
every symmetric matrix can be diagonalized   
every symmetric matrix eigenvector matrix X becomes orthogonal matrix Q   
orthogonal matrices have Q<sup>-1</sup> = Q<sup>T</sup>

"can be chosen orthonormal" means that they neednt be normal or unit vectors.  
[but will be ortho due to symmetry of their matrix parent]  
when choose unit size for eigenvectors, A = X&Lambda;X<sup>-1</sup> becomes S = Q&Lambda;Q<sup>T</sup> for symmetric matrices.  

Spectral theorem: 
proving symmetric matrices have real &lambda;s and orthonormal [orthogonal] x's      

Every symmetric matrix has the factorization S = Q&Lambda;Q<sup>T</sup> with real eigenvectors in &Lambda; and orthonormal eigenvectors in the columns of Q: S = Q&Lambda;Q<sup>-1</sup> = S = Q&Lambda;Q<sup>T</sup> with Q<sup>-1</sup> = Q<sup>T</sup> diagonalization.

easy to see Q&Lambda;Q<sup>T</sup> symmetric when see (Q&Lambda;Q<sup>T</sup>)<sup>T</sup> = (Q<sup>T</sup>)<sup>T</sup>&Lambda;<sup>T</sup>(Q)<sup>T</sup>, but harder proving that all symmetric matrices have real &lambda;s

"spectral theorem" in mathematics = "principal axis theorem" in geometry/physics    
proof in 3 steps:   
1.  by example showing real &lambda;s in &Lambda; and orthonormal x's in Q   
2.  by proof of these facts [real &lambda;s in &Lambda; and orthonormal x's in Q] when no eigenvalues are repeated   
3. by proof that allows repeated eigenvalues 

1. example proof 

find &lambda;s and x's when S = [[1,2],[2,4]] and S - &lambda;I = [[1-&lambda;,2],[2,4-&lambda;]]

solution: 
the determinant of S-&lambda;I is &lambda;<sup>2</sup> - 5&lambda; with &lambda;s 0 and 5 both real   
- &lambda; = 0 is an eigevalue because S is singular
- &lambda; = 5 because S.trace = 1 + 4 = 5 = sum(&lambda;<sub>1,</sub>), &lambda;<sub>2,</sub> = 0 + 5

[reminds us that symmetric matrices can be singular and all real symmetric matrices are diagonalizable]
[not all symmetric matrices singular of course: &lambda;<sup>2</sup> - &lambda;(a+d) + ad-b<sup>2</sup> = zero reminds us that S is singular only if at least one &lambda; is zero, when ad-b<sup>2</sup> = det S = 0 which solves for &lambda;(&lambda; - (a+d))]

- 2 eigenvectors (2,-1) and (1,2) are orthogonal but not yet orthonormal.  
  - the eigenvector for &lambda;<sub>1,</sub> = 0 is in the null space of S, the eigenvector &lambda;<sub>2,</sub> = 5 is in the column space.   
  - why are the column space and null space perpendicular?  the fundamental theorem says null space and is perpendicular to the row space not column space, but our matrix is symmetric so column space = row space, same!  it's eigenvectors because they form a basis for null and row = column space **must** be perpendicular.  
  - divide these eigenvectors by their length √5 for unit vectors, put the resulting unit eigenvectors into columns of Q and then Q = Q<sup>-1</sup>SQ = &Lambda; and Q<sup>-1</sup> = Q<sup>T</sup>.
  
  ![\begin{align*}
  &Lambda; = Q^{-1}SQ = \frac{1}{\sqrt{5}}
  \begin{bmatrix}
  2&-1\\
  1&2
  \end{bmatrix}
  \begin{bmatrix}
  1&2\\
  2&4
  \end{bmatrix}
  \frac{1}{\sqrt{5}}
  \begin{bmatrix}
  2&1\\
  -1&2
  \end{bmatrix}=
  \begin{bmatrix}
  0&0\\
  0&5
  \end{bmatrix}
  \end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%26Lambda%3B+%3D+Q%5E%7B-1%7DSQ+%3D+%5Cfrac%7B1%7D%7B%5Csqrt%7B5%7D%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%5C%5C%0A1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%262%5C%5C%0A2%264%0A%5Cend%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B5%7D%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%261%5C%5C%0A-1%262%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%260%5C%5C%0A0%265%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/110026771-17a31300-7cff-11eb-9805-b44dba7269e9.png">

For n x n case, the &lambda;s are real when S = S<sup>T</sup> and Sx = &lambda;x   
All the eigenvalues of a **real** symmetric matrix **are real** 

Real Eigenvalues: 
All the eigenvalues of a real symmetric matrix are real.   

[ this is 2.  by **proof** of these facts [**real** &lambda;s in &Lambda; and **orthonormal** x's in Q] when no eigenvalues are repeated ]

Proof:   

Sx = &lambda;x  

- &lambda; might be complex a + ib where a and b are real with complex conjugate a - ib   
- x might be complex as well.   switching the signs of their imaginary parts gives x_bar   
- &lambda;_bar times x_bar is always the conjugate of &lambda; times x.    so can take conjugates of Sx = &lambda;x remembering that S is real

Sx = &lambda;x 
leads to 
Sx_bar = &lambda;_bar x_bar 
transposes to 
x_bar<sup>T</sup>S = x_bar<sup>T</sup>&lambda;_bar

dot product first equation [ Sx = &lambda;x ] with x_bar   
dot product last equation [ x_bar<sup>T</sup>S = x_bar<sup>T</sup>&lambda;_bar ] with x  

x_bar<sup>T</sup> S x = x_bar &lambda; x   
x_bar<sup>T</sup> S x = x_bar<sup>T</sup> &lambda;_bar x

the LHS of both equations is the same and thus the RHS must be the same: (x_bar<sup>T</sup>)(&lambda;)(x) = (x_bar<sup>T</sup>)(&lambda;_bar)(x)

one equation has &lambda; and the other has &lambda;_bar    
both multiply x_bar<sup>T</sup>x which is |x<sub>1</sub>|<sup>2</sup> + |x<sub>2</sub>|<sup>2</sup> + ...  |x<sub>n</sub>|<sup>2</sup> = length squared which is not zero.    
therefore &lambda; must = &lambda;_bar   
[since they are not zero due to length and they are equal and the only difference in their notation is the bar, then the bar and the non-bar variables, &lambda; and &lambda;_bar must be equal.]
and a+ib euqals a-ib.  so b = 0 and thus &lambda; = a = real.

[if x is in complex form, x_bar<sup>T</sup>x = (a-ib)(a+ib) = a<sup>2</sup> - i<sup>2</sup>b<sup>2</sup> = a<sup>2</sup> - ((-1)<sup>1/2</sup>)<sup>2</sup>b<sup>2</sup> = a<sup>2</sup> - (-1)<sup>1</sup>b<sup>2</sup> = a<sup>2</sup> + b<sup>2</sup>]

[squared eigenvalues equal to some negative number are where the complex numbers come from.  there are no squared values in the determination of eigenvectors.  once we determine eigenvalues are real, then eigenvectors must be real because they're solving a real equation:]

the eigenvectors come from solving real equations. (S-&lambda;I)x = 0.  
so, the x's are also real.   
the important fact is that they are perpendicular.

orthogonal eigenvectors:   
eigenvectors of a real symmetric matrix,  
when they correspond to different &lambda;s,   
are always perpendicular.  

proof:  
suppose:  
Sx = &lambda;<sub>1</sub>x   
and 
Sy = &lambda;<sub>2</sub>   
assuming &lambda;<sub>1</sub>x ≠ &lambda;<sub>2</sub>   
take dot product of the 1st equation with y   
take dot product of the 2nd equation with x   

&lambda;<sub>1</sub>xy = Sxy
x<sup>T</sup>Sy = x<sup>T</sup>&lambda;<sub>2</sub>   

Use S<sup>T</sup> = S:
1st &lambda;<sub>1</sub> equation:
(&lambda;<sub>1</sub>x)<sup>T</sup>y = (Sx)<sup>T</sup>y = x<sup>T</sup>S<sup>T</sup>y
2nd &lambda;<sub>2</sub> equation:
x<sup>T</sup>Sy = x<sup>T</sup>&lambda;<sub>2</sub>   

the RHS of 1st and LHS of second are equal because S<sup>T</sup> = S. so, ... the opposite sides LHS of 1st and RHS of 2nd are equal: 
(&lambda;<sub>1</sub>x)<sup>T</sup>y = x<sup>T</sup>&lambda;<sub>2</sub>   
x<sup>T</sup>&lambda;<sub>1</sub><sup>T</sup>y = x<sup>T</sup>&lambda;<sub>2</sub>   
x<sup>T</sup>&lambda;<sub>1</sub>y = x<sup>T</sup>&lambda;<sub>2</sub>   

we assumed no repeating &lambda;s: 
&lambda;<sub>1</sub> ≠ &lambda;<sub>2</sub> 
so the only way that this is true:
x<sup>T</sup>&lambda;<sub>1</sub>y = x<sup>T</sup>&lambda;<sub>2</sub>   
is if x<sup>T</sup>y = 0 
meaning that the eigenvector for &lambda;<sub>1</sub> is perpendicular to the eigenvector for &lambda;<sub>2</sub> 

example 2:

the eigenvectors of 2x2 symmetric matrix have special form:

S = [[a,b],[b,c]] has   
x<sub>1</sub> = [b,&lambda;<sub>1</sub> - a]
x<sub>2</sub> = [&lambda;<sub>2</sub> - c, b]

the point is that the x<sub>1</sub> is perpendicular to x<sub>2</sub>.

x<sub>1</sub><sup>T</sup>x<sub>2</sub> = b(&lambda;<sub>2</sub> - c) + (&lambda;<sub>1</sub>-a)b = b(&lambda;<sub>1</sub> + &lambda;<sub>2</sub> - a - c) = 0   
look inside the parenthesese to see why = 0.   the trace of a matrix = a + b but is also equal to &lambda;<sub>1</sub> + &lambda;<sub>2</sub>.  the difference of those 2 equal quantities is inside the parenthesese so x<sub>1</sub><sup>T</sup>x<sub>2</sub> = 0 and the 2 eigenvectors are perpendicular.  
also:
if S = I then b = &lambda;<sub>1</sub> - a = &lambda;<sub>2</sub> - c = x<sub>1</sub> = x<sub>2</sub> = 0.  &lambda<sub>1</sub> = &lambda<sub>2</sub> = 1 is repeated but then S = I has perpendicular eigenvectors [1,0] and [0,1].   

review: symmetric matrices S has orthogonal eigenvector matrices Q:

columns q<sub>1</sub> and q<sub>2</sub> multiply rows &lambda;<sub>1</sub>q<sub>1</sub><sup>T</sup> and &lambda;<sub>2</sub>q<sub>2</sub><sup>T</sup> to produce S = q<sub>1</sub>&lambda;<sub>1</sub>q<sub>1</sub><sup>T</sup> + q<sub>2</sub>&lambda;<sub>2</sub>q<sub>2</sub><sup>T</sup>

![\begin{align*}
S = Q&Lambda;Q^T = 
\begin{bmatrix}
q_1&q_2
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
q_1\\
q_2
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%3D+Q%26Lambda%3BQ%5ET+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%26q_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%5C%5C%0Aq_2%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

Every symmetric matrix S = Q&Lambda;A<sup>T</sup> = &lambda;<sub>1</sub>q<sub>1</sub>q<sub>1</sub><sup>T</sup> + ... +  &lambda;<sub>n</sub>q<sub>n</sub>q<sub>n</sub><sup>T</sup>

remember the steps to the Spectral Theorem:   
6.2:      
write Ax<sub>i</sub> = &lambda;<sub>i</sub>x<sub>i</sub> in matrix form AX = X&Lambda; or A = X&Lambda;X<sup>-1</sup>   
6.4:   
orthonormal x<sub>i</sub> = q<sub>i</sub> gives X = Q and then S = Q&Lambda;Q<sup>-1</sup> = Q&Lambda;Q<sup>T</sup> which is columns of Q&Lambda; times rows of Q<sup>T</sup> and then summation of the resulting n matrices. 

Direct proof:      

Sq<sub>i</sub> = (&lambda;<sub>1</sub>q<sub>1</sub>q<sub>1</sub><sup>T</sup> + ... + &lambda;<sub>1</sub>q<sub>1</sub><sup>T</sup>)q<sub>i</sub> = &lambda;<sub>i</sub>q<sub>i</sub> 

[since all those q<sub>1</sub>q<sub>1</sub><sup>T</sup> = I]

[seems that it would be the sum of lambdas * q<sub>i</sub>]


**complex eigenvectors of real matrices**

for any real matrix   
Sx = &lambda;x   
gives (is paired with via quadratic solutions)
Sx_bar = &lambda;_bar x_bar

for a symmetric matrix   
&lambda and x   
turn out to be real;   
so those two equations become the same
Sx = &lambda;x   
Sx_bar = &lambda;_bar x_bar

for any non symmetric matrix   
can produce   
&lambda; and x   
that are complex:   
then   
Ax_bar = &lambda;_bar x_bar is true   
but different from Ax = &lambda; x   
we get 
another complex eigenvalue &lambda;_bar   
a new eigenvector which is x  

for real matrices,   
complex &lamnda;s and x's come in conjugate pairs    
&lambda; = a + ib   
&lambda;_bar = a - ib  
if Ax = &lambda;x   
then
Ax_bar = &lambda;_bar x_bar    

example

A = [[cos&theta;, -sin&theta;],[sin&theta;, cos&theta;]] 
has
&lambda;<sub>1</sub> = cos&theta; + isin&theta;
&lambda;<sub>2</sub> = cos&theta; - isin&theta;
conjugates to each other   
labeled &lambda; and &lambda;_bar   
the eigenvectors must be x and x_bar because A is real
[and need to cancel those nasty imaginary bits]

![\begin{align*}
A &= 
\begin{bmatrix}
cos&theta;&-sin&theta;\\
sin&theta;&cos&theta;
\end{bmatrix}\\
has:\\
&lambda;_1 &= cos&theta;+isin&theta;\\
&lambda;_2 &= cos&theta;-isin&theta;\\
\\
Ax &= 
\begin{bmatrix}
cos&theta;&-sin&theta;\\
sin&theta;&cos&theta;
\end{bmatrix}
\begin{bmatrix}
1\\
-i
\end{bmatrix}=
&lambda;x =
(cos&theta; + isin&theta;)
\begin{bmatrix}
1\\
-i
\end{bmatrix} =
\begin{bmatrix}
cos&theta; + isin&theta;\\
sin&theta; -icos&theta;
\end{bmatrix}
\\
A\bar{x} &= 
\begin{bmatrix}
cos&theta;&-sin&theta;\\
sin&theta;&cos&theta;
\end{bmatrix}
\begin{bmatrix}
1\\
i
\end{bmatrix}=
\bar{&lambda;}\bar{x} =
(cos&theta; - isin&theta;)
\begin{bmatrix}
1\\
i
\end{bmatrix} =
\begin{bmatrix}
cos&theta; - isin&theta;\\
sin&theta; +icos&theta;
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Acos%26theta%3B%26-sin%26theta%3B%5C%5C%0Asin%26theta%3B%26cos%26theta%3B%0A%5Cend%7Bbmatrix%7D%5C%5C%0Ahas%3A%5C%5C%0A%26lambda%3B_1+%26%3D+cos%26theta%3B%2Bisin%26theta%3B%5C%5C%0A%26lambda%3B_2+%26%3D+cos%26theta%3B-isin%26theta%3B%5C%5C%0A%5C%5C%0AAx+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Acos%26theta%3B%26-sin%26theta%3B%5C%5C%0Asin%26theta%3B%26cos%26theta%3B%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-i%0A%5Cend%7Bbmatrix%7D%3D%0A%26lambda%3Bx+%3D%0A%28cos%26theta%3B+%2B+isin%26theta%3B%29%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-i%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0Acos%26theta%3B+%2B+isin%26theta%3B%5C%5C%0Asin%26theta%3B+-icos%26theta%3B%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0AA%5Cbar%7Bx%7D+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Acos%26theta%3B%26-sin%26theta%3B%5C%5C%0Asin%26theta%3B%26cos%26theta%3B%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0Ai%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbar%7B%26lambda%3B%7D%5Cbar%7Bx%7D+%3D%0A%28cos%26theta%3B+-+isin%26theta%3B%29%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0Ai%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0Acos%26theta%3B+-+isin%26theta%3B%5C%5C%0Asin%26theta%3B+%2Bicos%26theta%3B%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

eigenvectors (1,-i) and (1,i) are complex conjugates because A is real.  

eigenvalue absolute value [magnitude?] is |&lambda;| = 1 because cos<sup>2</sup>&theta; + sin<sup>2</sup>&theta; = 1  

eigenvalue absolute value [magnitude?] is |&lambda;| = 1 holds for eigenvalues of every Q orthogonal matrix    

complex numbers are unavoidable even for real matrices.  

**eigenvalues vs pivots**

elimination --> pivots   
det(A-&lambda;I) = 0 --> eigenvalues

product of pivots = product of eigenvalues = determinant of A    

d<sub>1</sub>, ..., d<sub>n</sub>    
&lambda;<sub>1</sub>, ..., &lambda;<sub>n</sub> 

d<sub>i</sub> ≠ &lambda;<sub>i</sub>    
but   
for **symmetric matrices**, the pivots and eigenvalues have the same signs:   
the number of positive eigenvalues equals the number of positive pivots for S = S<sup>T</sup>

S will have all positive eigenvalues &lambda;<sub>i</sub> > 0 IFF all pivots are positive.  
return to this when discussing positive definite matrices.   

example:

S = [[1,3],[3,1]] has pivots 1 and -8 and eigenvalues 4 and -2   

proof that for S=S<sup>T</sup> there are the same number of positive eigenvalues as pivots:

S = LU = LDL<sup>T</sup> 

if move L's off diagonal to zero then L becomes I and the eigenvalues of IDI = become 1 and -8    
as this occurs eigenvalues from 4,-2 to 1,-8 the eigenvalues never cross zero where they become singular.   

as  move L toward I by moving the off diagonal entries to zero, the pivots are not changing and not zero.  the eigenvalues of LDL<sup>T</sup> change to the eigenvalues of  IDI<sup>T</sup> =  the pivots of both.  Since the eigenvalues cannot cross zero as they move toward the pivots, their signs cannot change. 

**all symmetric matrices are diagonalizable**

when no eigenvalues of A are repeated  
all eigenvalues are sure to be independent.  

a repeated eigenvalue may produce a shortage of eigenvectors.   
this never happens for symmetric matrices  
there are always enough eigenvectors to diagonalize S = S<sup>T</sup>   

6.2 remember:  
there is no connection between invertibility and diagonalizability:  
invertibility is concerned with eigenvalues: a single &lambda; = 0 means determinant = 0     
diagonalizability is concerned with sufficient or insufficient numbers of eigenvectors    
any matrix with NO repeated eigenvalues can be diagonalized.  
6.4 remember:  diagonalizable even if singular/not invertible
S = [[1,2],[2,4]] is singular with dependent columns and determinant = 0, but has &lambda;s = 0, 5 and 2 eigenvectors (2,-1) and (1,2) which are not only different eigenvectors but different eigenvectors because they come from different eigenvalues. "any matrix that has no repeated eigenvalues can be diagonalized because its eigenvectors are independent." and "theres a proof for when λ eigenvalues are distinct, eigenvectors x are independent."

no repeat &lambda;s --> independent eigenvectors --> X<sup>-1</sup> exists --> diagonlizable

returning to "there are always enough eigenvectors to diagonalize S = S<sup>T</sup>". 

proof-ish:
S with repeated eigenvaleus   
change S slightly by a diagonal matrix = diag(c<sub>1</sub>, ... , c<sub>n</sub>).   
if c very small then symmetric matrix will have no repeated eigenvalues.   
then S has a full set of orthonormal eigenvectors.   
as c --> 0, the eigenvectors --> n orthonormal eigenvectors of the original S   
even if some of the eigenvalues of S are repeated.  

a different proof:   
useful factorization of square matrices A   
symmetric or not   
quickly produces   
S = Q&Lambda;Q<sup>T</sup>  
with full set of real orthonormal eigenvectors  
WHEN S is any realy SYMMETRIC matrix.

Schur's theorem:  

**Every square A factors into QTQ<sup>-1</sup>   
where T is upper triangular   
where Q_bar<sup>T</sup> = Q<sup>-1</sup>     
if A has real eigenvalues, 
then Q and T can be chosen as real: Q<sup>T</sup>Q = I**
[no bar in that last Q<sup>T</sup>!]

when S is symmetric, 
T is diagonal (T = &Lambda;)  
and  S = Q&Lambda;Q<sup>T</sup>    

we know   
every symmetric S  
has real eigenvalues   
Schur's S allows repeated eigenvalues.  

Schur's S = QTQ<sup>-1</sup>
means that T = Q<sup>T</sup>SQ
and the transpose is also Q<sup>T</sup>SQ.
the triangular T is symmetric when S = S<sup>T</sup>   
then T must be diagonal and T = &Lambda; [seems repetitive]

this proves S = Q&Lambda;Q<sup>-1</sup>.  
The symmetric S has n orthonormal eigenvectors Q

7.2 shows eigenvalues &lambda; can be described one at a time  
the largest &lambda; is maximum of x<sup>T</sup>Sx / x<sup>T</sup>.  
then &lambda;<sub>2</sub> = second largest is again the same maximum if we only allow vectors x that are perpendicular to the 1st eigenvector.  the 3rd eigenvalue &lambda;<sub>3</sub> comes by requiring x<sub>T</sub>q<sub>1</sub> = 0 and x<sub>T</sub>q<sub>2</sub> = 0.  chapter 7 covers this because one-at-a-time succeeds for singular values of any matrix A.  singular values come from A<sup>T</sup>A and AA<sup>T</sup>.

review:
1. every symmetric matrix S has real eigenvalues and perpendicular eigenvectors  
2. diagonalization becomes S = Q&Lambda;Q<sup>T</sup> with an orthonormal eigenvector matrix Q  
3. all symmetric matrices are diagonalizable even with repeated eigenvalues    
4. the signs of eigenvalues match the signs of pivots when S + S<sup>T</sup>
5. every square matrix can be 'triangularlized' by A = QTQ<sup>-1</sup>
if A = S then T = &Lambda;

worked examples:
A. what matrix A has eigenvalues &lambda; =1,-1 and eigenvectors x<sub>1</sub>eigenvectors x<sub>1</sub> = (-sin&theta;, cos&theta;) ? which property can be predicted in advance?

A = A<sup>T</sup>  
A<sup>2</sup> = I  
det A = -1   
pivots are + and -
A<sup>-1</sup> = A   

all can be predicted:   
- with real eigenvalues 1 and -1 and orthonormal x<sub>1</sub> and x<sub>2</sub> the matrix A = Q&Lambda;Q<sup>T</sup> must be symmetric.
- the eigenvalues 1 and -1 indicate:
  - A<sup>2</sup> = I since &lambda;<sup>2</sup> = 1
  - A<sup>-1</sup> = A also since &lambda;<sup>2</sup> for both = 1
  - det A = -1
- 2 pivots must be positive and negative like eigenvalues since A is symmetric
- the matrix will be a reflection.  
  - vectors in the directoin of x<sub>1</sub> = (cos&theta;,sin&theta;) will be unchanged by A since &lambda;=1  
  - vectors in the perpendicular direction of (-sin&theta;,cos&theta;) are reversed.  
- the reflection A = Q&Lambda;Q<sup>T</sup> is across the "&theta;" line.  Write c for cos&theta; and s for sin&theta;:

notice that x = (1,0) goes to Ax = (cos2&theta, sin2&theta;) on the 2&theta; line [unchd] and (cos2&theta, sin2&theta;) goes back across the &theta; line to x = (1,0)

\begin{align*}
A=
\begin{bmatrix}
cos&theta;-&sin&theta;\\
sin&theta;&cos&theta;
\end{bmatrix}
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}
\begin{bmatrix}
cos&theta;-&sin&theta;\\
-sin&theta;&cos&theta;
\end{bmatrix}=
\begin{bmatrix}
cos^2&theta;-sin^2&theta;&2cos&theta;sin&theta;\\
2cos&theta;sin&theta;&sin^2&theta;-cos^2&theta;
\end{bmatrix}=
\begin{bmatrix}
cos&theta;&sin&theta;\\
sin&theta;&-cos&theta;
\end{bmatrix} 
\end{align*}

B. find eigenvalues and eigenvectors (discrete sines and cosines) of A<sub>3</sub> and B<sub>4</sub>.

The 1-2-1 pattern in both matrices is a 'second difference' like 'second derivative'.  
Ax = &lambda;x and Bx = &lambda;x are like ∂<sup>2</sup>x/∂t<sup>2</sup> = &lambda;x    
this has eigenvectors = x = sin kt and x = cos kt that are the bases for Fourier Series.

A<sub>n</sub> and B<sub>n</sub> lead to "discrete sines" and "discrete cosines" that are bases for Discrete Fourier Transform.  The DFT is absolutely central to all areas of digital singal processing.  The favorite choice for JPEG in image processing has been B<sub>8</sub> of size n=8.

A<sub>3</sub> below eigenvector matrix X gives the "Discrete SIne Transform" and the eigenvectors fall onto sine curves.

the eigenvectors are orthogonal as proved in this section for all symmetric matrices.  

all the eigenvalues are real and negative which means "negative definite" so that e<sup>At</sup> decays to zero --> stable. 

the starting u(0) = (0, 2√2, 0) is x<sub>3</sub> - x<sub>2</sub> and so the solution is u(t) = e<sup>&lambda;<sub>3</sub>t</sup>x<sub>3</sub> + e<sup>&lambda;<sub>2</sub>t</sup>x<sub>2</sub>

The eigenvalues of B<sub>4</sub> are 2-√2 and 2 and 2+√2 and zero which is the same as A<sub>3</sub> with the addition of the zero.  Trace remains 6 but determinant = 0.  Eigenvector matrix gives the 4-point "Discrete Cosine Transform".  All eigenvectors of B<sub>4</sub> fall on the consine curves.  These eigenvectors match cosines at the half-way points &pi;/8, 3&pi;/8, 5&pi;/8, 7&pi;/8


![\begin{align*}
A_3 &= 
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix}\\
det(A-&lambda;I) &=
\begin{bmatrix}
2-&lambda;&-1&0\\
-1&2-&lambda;&-1\\
0&-1&2-&lambda;
\end{bmatrix} \\ 
&= (-2-&lambda;)[(-2-&lambda;)^2 - 1] -1(-2-&lambda;) \\
&= (-2-&lambda;)[(-2-&lambda;)^2 - 2] \\
&= (-2-&lambda;)[(&lambda;^2 +4&lambda; + 2] \\
&lambda;_1 = -2 \longrightarrow (A + 2I) &= 
\begin{bmatrix}
0&-1&0\\
-1&0&-1\\
0&-1&0
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix} =
\begin{bmatrix}
0\\0\\0
\end{bmatrix}
\longrightarrow x_1 = 
\begin{bmatrix}
1\\0\\-1
\end{bmatrix}
\\
&lambda;_2 = -2-\sqrt{2}  \longrightarrow (A + (2+\sqrt{2})I)& = 
\begin{bmatrix}
\sqrt{2}&-1&0\\
-1&\sqrt{2}&-1\\
0&-1&\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix} =
\begin{bmatrix}
0\\0\\0
\end{bmatrix}
\longrightarrow x_2 = 
\begin{bmatrix}
1\\ \sqrt{2}\\1
\end{bmatrix}\\
&lambda;_3 = -2+\sqrt{2} \longrightarrow (A + (-2-\sqrt{2})I) &= 
\begin{bmatrix}
-\sqrt{2}&-1&0\\
-1&-\sqrt{2}&-1\\
0&-1&-\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix} =
\begin{bmatrix}
0\\0\\0
\end{bmatrix}
\longrightarrow x_3 = 
\begin{bmatrix}
1\\-\sqrt{2}\\1
\end{bmatrix}\\
sines &=
\begin{bmatrix}
1&\sqrt{2}&1\\
\sqrt{2}&0&-\sqrt{2}\\
1&-\sqrt{2}&1
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA_3+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D%5C%5C%0Adet%28A-%26lambda%3BI%29+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A2-%26lambda%3B%26-1%260%5C%5C%0A-1%262-%26lambda%3B%26-1%5C%5C%0A0%26-1%262-%26lambda%3B%0A%5Cend%7Bbmatrix%7D+%5C%5C+%0A%26%3D+%28-2-%26lambda%3B%29%5B%28-2-%26lambda%3B%29%5E2+-+1%5D+-1%28-2-%26lambda%3B%29+%5C%5C%0A%26%3D+%28-2-%26lambda%3B%29%5B%28-2-%26lambda%3B%29%5E2+-+2%5D+%5C%5C%0A%26%3D+%28-2-%26lambda%3B%29%5B%28%26lambda%3B%5E2+%2B4%26lambda%3B+%2B+2%5D+%5C%5C%0A%26lambda%3B_1+%3D+-2+%5Clongrightarrow+%28A+%2B+2I%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A0%26-1%260%5C%5C%0A-1%260%26-1%5C%5C%0A0%26-1%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C0%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+x_1+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C0%5C%5C-1%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%26lambda%3B_2+%3D+-2-%5Csqrt%7B2%7D++%5Clongrightarrow+%28A+%2B+%282%2B%5Csqrt%7B2%7D%29I%29%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%26-1%260%5C%5C%0A-1%26%5Csqrt%7B2%7D%26-1%5C%5C%0A0%26-1%26%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C0%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+x_2+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C+%5Csqrt%7B2%7D%5C%5C1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26lambda%3B_3+%3D+-2%2B%5Csqrt%7B2%7D+%5Clongrightarrow+%28A+%2B+%28-2-%5Csqrt%7B2%7D%29I%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-%5Csqrt%7B2%7D%26-1%260%5C%5C%0A-1%26-%5Csqrt%7B2%7D%26-1%5C%5C%0A0%26-1%26-%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C0%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+x_3+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C-%5Csqrt%7B2%7D%5C%5C1%0A%5Cend%7Bbmatrix%7D%5C%5C%0Asines+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%26%5Csqrt%7B2%7D%261%5C%5C%0A%5Csqrt%7B2%7D%260%26-%5Csqrt%7B2%7D%5C%5C%0A1%26-%5Csqrt%7B2%7D%261%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/110194155-fdebf380-7e04-11eb-9a38-2408360c18cd.png">

Lessons from problem set:

1.  For a matrix that factors into ASB, B must = A<sup>T</sup> = A<sup>-1</sup> for the matrix to be symmetric. 

2. For ASB where S = S<sup>-1</sup>, ASB is "similar" to S (has same eigenvalues) when B = A<sup>-1</sup>. [Simply means that ASB is diagonalizable; remember the eigenvectors in X need to be independent to obtain X<sup>-1</sup>.]

For ASB to be symmetric, B = A<sup>T</sup>     
For ASB to be **similar** and **symmetric** B = A<sup>T</sup> = A<sup>-1</sup>

3. to write A as a sum of a symmetric matrix S and skew symmetric matrix N:

A = S + N = 0.5 (A + A<sup>T</sup>) + 0.5 (A - A<sup>T</sup>)

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/110214481-b56b1f00-7e72-11eb-9c11-08e9bdf24c65.png">

4. if C symmetric, prove A<sup>T</sup>CA is also symmetric by transposing it:

(A<sup>T</sup>CA)<sup>T</sup> = A<sup>T</sup>C<sup>T</sup>(A<sup>T</sup>)<sup>T</sup> = A<sup>T</sup>CA and thus A<sup>T</sup>CA symmetric because (A<sup>T</sup>CA)<sup>T</sup> = A<sup>T</sup>CA 

this is true even if A is 6x3 matrix:  
A<sup>T</sup>CA = [3x6][6x6][6x3] 

7. Since A = A<sup>T</sup>, the eigenvalues must be real and the eigenvectors will be orthogonal (as shown below). 

Find eigenvalues by expanding the determinant of (A - &lambda;I) and finding the roots of the characteristic polynomial: &lambda;(&lambda;<sup>2</sup> - 9) = 0      
For each eigenvalue, the eigenvector is given by the null space of (A - &lambda;<sub>i</sub>I).  Each (A - &lambda;<sub>i</sub>I) has a null space given by the span of the eigenvector.  

The eigenvectors for &lambda;<sub>2</sub> = 0 are given by the null space of (A - 0 • I) or the span of x<sub>2</sub> = (2,2,-1) which is orthogonal to the eigenvectors for &lambda;<sub>1</sub> and &lambda;<sub>3</sub>.

To obtain an orthogonal matrix for eigenvectors, normalize x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> to q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub> which makes Q<sup>-1</sup> = Q<sup>T</sup>

![\begin{align*}
A = A^T &= 
\begin{bmatrix}
1&0&2\\
0&-1&-2\\
2&-2&0
\end{bmatrix}\\
det(A-&lambda;I) &=
\begin{bmatrix}
1-&lambda;&0&2\\
0&-1-&lambda;&-2\\
2&-2&0-&lambda;
\end{bmatrix} \\ 
&= [1-&lambda;] [(-1-&lambda;)(-&lambda;)-(-2)(-2)] + [2][0-(2(-1-&lambda;))] \\
&= [1-&lambda;] [&lambda;+&lambda;^2-4] + [2][2-2&lambda;] \\
&= [&lambda;+&lambda;^2-4+ -&lambda;^2-&lambda;^3+4&lambda;] + [4-4&lambda;] \\
&= -&lambda;^3+9&lambda;\\
&= -(&lambda;^3-9&lambda;)\\
&= -&lambda;(&lambda;^2-9)\\
\\
&lambda;_1 = -3 \longrightarrow (A + 3I) &= 
\begin{bmatrix}
4&0&2\\
0&2&-2\\
2&-2&3
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix} =
\begin{bmatrix}
0\\0\\0
\end{bmatrix}
\longrightarrow x_1 = 
\begin{bmatrix}
1\\-2\\-2
\end{bmatrix}
\\
&lambda;_2 = 0  \longrightarrow (A -0I)& = 
\begin{bmatrix}
1&0&2\\
0&-1&-2\\
2&-2&0
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix} =
\begin{bmatrix}
0\\0\\0
\end{bmatrix}
\longrightarrow x_2 = 
\begin{bmatrix}
2\\ 2\\-1
\end{bmatrix}\\
&lambda;_3 = 3 \longrightarrow (A -3I) &= 
\begin{bmatrix}
-2&0&2\\
0&-4&-2\\
2&-2&-3
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix} =
\begin{bmatrix}
0\\0\\0
\end{bmatrix}
\longrightarrow x_3 = 
\begin{bmatrix}
2\\-1\\2
\end{bmatrix}\\
\\
A = A^T = 
\begin{bmatrix}
1&0&2\\
0&-1&-2\\
2&-2&0
\end{bmatrix} &= X&Lambda;X^{-1}=
\begin{bmatrix}
1&2&2\\
-2&2&-1\\
-2&-1&2
\end{bmatrix}
\begin{bmatrix}
-3&&\\
&0&\\
&&3
\end{bmatrix}
\frac{1}{9}
\begin{bmatrix}
1&-2&-2\\
2&2&-1\\
2&-1&02
\end{bmatrix}
\\
A = A^T = 
\begin{bmatrix}
1&0&2\\
0&-1&-2\\
2&-2&0
\end{bmatrix} &= Q&Lambda;Q^{-1}=
\frac{1}{3}
\begin{bmatrix}
1&2&2\\
-2&2&-1\\
-2&-1&2
\end{bmatrix}
\begin{bmatrix}
-3&&\\
&0&\\
&&3
\end{bmatrix}
\frac{1}{3}
\begin{bmatrix}
1&-2&-2\\
2&2&-1\\
2&-1&02
\end{bmatrix}=Q&Lambda;Q^T\\
\\
&= q_1q_1^T&lambda;_1 +q_2 q_2^T&lambda;_2 + q_3q_3^T&lambda;_3\\
\\
&= \frac{x_1x_1^T&lambda;_1}{|x_1|} + \frac{x_2x_2^T&lambda;_2}{|x_2|} + \frac{x_3x_3^T&lambda;_3}{|x_2|}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%3D+A%5ET+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%262%5C%5C%0A0%26-1%26-2%5C%5C%0A2%26-2%260%0A%5Cend%7Bbmatrix%7D%5C%5C%0Adet%28A-%26lambda%3BI%29+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1-%26lambda%3B%260%262%5C%5C%0A0%26-1-%26lambda%3B%26-2%5C%5C%0A2%26-2%260-%26lambda%3B%0A%5Cend%7Bbmatrix%7D+%5C%5C+%0A%26%3D+%5B1-%26lambda%3B%5D+%5B%28-1-%26lambda%3B%29%28-%26lambda%3B%29-%28-2%29%28-2%29%5D+%2B+%5B2%5D%5B0-%282%28-1-%26lambda%3B%29%29%5D+%5C%5C%0A%26%3D+%5B1-%26lambda%3B%5D+%5B%26lambda%3B%2B%26lambda%3B%5E2-4%5D+%2B+%5B2%5D%5B2-2%26lambda%3B%5D+%5C%5C%0A%26%3D+%5B%26lambda%3B%2B%26lambda%3B%5E2-4%2B+-%26lambda%3B%5E2-%26lambda%3B%5E3%2B4%26lambda%3B%5D+%2B+%5B4-4%26lambda%3B%5D+%5C%5C%0A%26%3D+-%26lambda%3B%5E3%2B9%26lambda%3B%5C%5C%0A%26%3D+-%28%26lambda%3B%5E3-9%26lambda%3B%29%5C%5C%0A%26%3D+-%26lambda%3B%28%26lambda%3B%5E2-9%29%5C%5C%0A%5C%5C%0A%26lambda%3B_1+%3D+-3+%5Clongrightarrow+%28A+%2B+3I%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A4%260%262%5C%5C%0A0%262%26-2%5C%5C%0A2%26-2%263%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C0%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+x_1+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C-2%5C%5C-2%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%26lambda%3B_2+%3D+0++%5Clongrightarrow+%28A+-0I%29%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%262%5C%5C%0A0%26-1%26-2%5C%5C%0A2%26-2%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C0%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+x_2+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%5C%5C+2%5C%5C-1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26lambda%3B_3+%3D+3+%5Clongrightarrow+%28A+-3I%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-2%260%262%5C%5C%0A0%26-4%26-2%5C%5C%0A2%26-2%26-3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C0%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+x_3+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%5C%5C-1%5C%5C2%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0AA+%3D+A%5ET+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%262%5C%5C%0A0%26-1%26-2%5C%5C%0A2%26-2%260%0A%5Cend%7Bbmatrix%7D+%26%3D+X%26Lambda%3BX%5E%7B-1%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%262%262%5C%5C%0A-2%262%26-1%5C%5C%0A-2%26-1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A-3%26%26%5C%5C%0A%260%26%5C%5C%0A%26%263%0A%5Cend%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B9%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-2%26-2%5C%5C%0A2%262%26-1%5C%5C%0A2%26-1%2602%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0AA+%3D+A%5ET+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%262%5C%5C%0A0%26-1%26-2%5C%5C%0A2%26-2%260%0A%5Cend%7Bbmatrix%7D+%26%3D+Q%26Lambda%3BQ%5E%7B-1%7D%3D%0A%5Cfrac%7B1%7D%7B3%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%262%262%5C%5C%0A-2%262%26-1%5C%5C%0A-2%26-1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A-3%26%26%5C%5C%0A%260%26%5C%5C%0A%26%263%0A%5Cend%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B3%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-2%26-2%5C%5C%0A2%262%26-1%5C%5C%0A2%26-1%2602%0A%5Cend%7Bbmatrix%7D%3DQ%26Lambda%3BQ%5ET%5C%5C%0A%5C%5C%0A%26%3D+q_1q_1%5ET%26lambda%3B_1+%2Bq_2+q_2%5ET%26lambda%3B_2+%2B+q_3q_3%5ET%26lambda%3B_3%5C%5C%0A%5C%5C%0A%26%3D+%5Cfrac%7Bx_1x_1%5ET%26lambda%3B_1%7D%7B%7Cx_1%7C%7D+%2B+%5Cfrac%7Bx_2x_2%5ET%26lambda%3B_2%7D%7B%7Cx_2%7C%7D+%2B+%5Cfrac%7Bx_3x_3%5ET%26lambda%3B_3%7D%7B%7Cx_2%7C%7D%0A%5Cend%7Balign%2A%7D)


<img width="662" alt="image" src="https://user-images.githubusercontent.com/38410965/110219152-89a86300-7e8b-11eb-9064-edb4d1a2e0da.png">


8.  to provide all orthogonal matrices that diagonalize a matrix A  
- normalize the eigenvectors 
- place a factor next to each eigenvector to represent that all orthogonal matrices that diagonalize A are found in the span of A's eigenvector matrix.  these factors are different from the c values computed with u(0).  

9. to find a symmetric matrix [[1,b].[b,1]] that has only negative eigenvalues, reduce to find the pivots and solve for b where all pivots are < zero.  symmetric matrices have same number of positive eigenvalues and positive pivots. 


10. if A<sup>3</sup> = 0 then the eigenvalues of A must be zero. 

11. if &lambda; = a + ib is an eigenvalue of a real matrix A, then its conjugate &lambda;_bar = a - ib is also an eigenvalue.  and so for a 3x3 matrix, there must be at least one real eigenvalue. 

always the trace = &lambda; + &lambda; is real.  

the characteristic equation of a 3x3 matrix is a third order polynomial. as such it can hae at most 2 complex roots (that must be complex conjugates) to be a real matrix


projection review:

a is a vector recipient of b's projection:

b shines onto a   
shortest distance is via e that is perpendicular to a   
so b - e arrives at xhat(a) = the endpoint that is at a percentage xhat of a that is closest to b:  
b - e = xhat(a)   
b - xhat(a) = e
[keep in mind e extends from 0, 0 in this last equation]    
a<sup>T</sup> • e = a<sup>T</sup>(b - xhat(a)) = 0 because perpendicular    
a<sup>T</sup>b = a<sup>T</sup>( xhat(a)) = xhat(a<sup>T</sup>a)    
xhat = (a<sup>T</sup>b) / (a<sup>T</sup>a) = a ratio or percentage number    
p = xhat(a) = [(a<sup>T</sup>b) / (a<sup>T</sup>a)]a    
p = Pb where P is a matrix and b is a vector    
p    
= [(a<sup>T</sup>b) / (a<sup>T</sup>a)]a = xhat(a) = a(xhat)   
= [(aa<sup>T</sup>) / (a<sup>T</sup>a)]b = Pb    
P = [(aa<sup>T</sup>) / (a<sup>T</sup>a)]   

Note:   
switching from p = xhat percentage of a to a matrix projection of b, note that a is switching sides in the numerator as:    
- either xhat(a) = a(xhat) when xhat is a percent of vector a    
- or when computing P by placing itself on the LHS of a<sup>T</sup>.    
The way to resolve whether a is dot product with a<sup>T</sup> by being on its RHS or a matrix by a being on a<sup>T</sup>'s LHS is that a is a vector being acted on by xhat or a vector forming a matrix.


A is a matrix surface recipient of b's projection:

A is a matrix representing a surface   
b shines onto that surface   
the closest point from b to A, is at point Axhat on A,   
where b - Axhat is perpendicular to A:   
A<sup>T</sup>(b - Axhat) = zero vector = 0      
A<sup>T</sup>b = A<sup>T</sup>Axhat    
xhat =  (A<sup>T</sup>A)<sup>-1</sup>(A<sup>T</sup>b)
p = Axhat = A(A<sup>T</sup>A)<sup>-1</sup>(A<sup>T</sup>b)
p = Pb = A(A<sup>T</sup>A)<sup>-1</sup>(A<sup>T</sup>)b
P = A(A<sup>T</sup>A)<sup>-1</sup>(A<sup>T</sup>)

A is a matrix surface recipient of b's projection but A is symmetric and diagonalizable to Q&Lambda;Q<sup>T</sup> or Q&Lambda;Q<sup>-1</sup>

page 236   
orthogonal matrices are excellent for computations - numbers never grow too large when lengths are fixed. stable computer odes use Q as much as possible. for projections onto subspaces all formulas involve A<sup>T</sup>A.  The entries of A<sup>T</sup>A are the dot products of a<sub>i</sub><sup>T</sup>a<sub>i</sub> of the basis vectors a<sub>i</sub>, ... , a<sub>n</sub>.  suppose the basis vectors are actually orthonormal.  the a's become q's. then A<sup>T</sup>A simplifies to Q<sup>T</sup>Q = I.  Improvments in x_hat and p and P computations.  Instead of A<sup>T</sup>A there is Q<sup>T</sup>Q but that too is replaced with a blank.   

A<sup>T</sup>(b - Axhat) = zero vector = 0        
Q<sup>T</sup>(b - Qxhat) = zero vector = 0      

A<sup>T</sup>b = A<sup>T</sup>Axhat    
Q<sup>T</sup>b = Q<sup>T</sup>Qxhat    

A<sup>T</sup>Axhat = A<sup>T</sup>b    
Q<sup>T</sup>Qxhat = Q<sup>T</sup>b    

xhat =  (A<sup>T</sup>A)<sup>-1</sup>(A<sup>T</sup>b)    
xhat =  (Q<sup>T</sup>Q)<sup>-1</sup>(Q<sup>T</sup>b)    
xhat =  (I)(Q<sup>T</sup>b)    
xhat =  Q<sup>T</sup>b    

p = Axhat = A(A<sup>T</sup>A)<sup>-1</sup>(A<sup>T</sup>b)    
p = Qxhat = Q(Q<sup>T</sup>Q)<sup>-1</sup>(Q<sup>T</sup>b)    
p = Qxhat = Q(I)(Q<sup>T</sup>b)    
p = Qxhat = QQ<sup>T</sup>b    
p = Qxhat = Qxhat    

p = Pb = A(A<sup>T</sup>A)<sup>-1</sup>(A<sup>T</sup>)b    
p = Pb = Q(Q<sup>T</sup>Q)<sup>-1</sup>(Q<sup>T</sup>)b    
p = Pb = Q(I)(Q<sup>T</sup>)b    
if Q square: p = Pb = Q(I)(Q<sup>T</sup>)b = QQ<sup>T</sup>b = Ib = b   

P = A(A<sup>T</sup>A)<sup>-1</sup>(A<sup>T</sup>)    
P = Q(Q<sup>T</sup>Q)<sup>-1</sup>(Q<sup>T</sup>)    
P = QQ<sup>T</sup>    
if Q sqaure: P = QQ<sup>T</sup> = I   
 
no matrices to invert which is the point of an orthonormal basis.  the best xhat = Q<sup>T</sup>b just has  dot products of q<sub>1</sub>, ... , q<sub>n</sub> with b.  these are one dimensional projections!  the "coupling matrix" or "correlation matrix" A<sup>T</sup>A is now Q<sup>T</sup>Q = I.  
**there is no coupling**   Wgeb A us Q with orthonormal columns, here is p = Qxhat = QQ<sup>T</sup>b:

![\begin{align*}
p = 
\begin{bmatrix}
q_1&...&q_n
\end{bmatrix}
\begin{bmatrix}
q_1^Tb\\
...\\
q_n^Tb
\end{bmatrix}=
q_1(q_1^Tb) + ... + q_n(q_n^Tb)
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ap+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%26...%26q_n%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%5ETb%5C%5C%0A...%5C%5C%0Aq_n%5ETb%0A%5Cend%7Bbmatrix%7D%3D%0Aq_1%28q_1%5ETb%29+%2B+...+%2B+q_n%28q_n%5ETb%29%0A%5Cend%7Balign%2A%7D)

important case:   
when Q is square and m = n, the subspace is the whole space.
then Q<sup>T</sup> = Q<sup>-1</sup> and xhat = Q<sup>T</sup>b is the same as x = Q<sup>-1</sup>b.  The solution is exact! The projection of b onto the whole space is b itself (no e)  In this case p = b and P = QQ<sup>T</sup> = I.  

when p = b the formula assembles b out of its  1-dimensional projections.   
if q<sub>1</sub>, ..., q<sub>n</sub> is an orthonormal basis for the whole space then Q is square.  Every b = QQ<sup>T<sup>b is the sum of its components along the q's:

b = q<sub>1</sub>(q<sub>1</sub><sup>T</sup>b) + ... + q<sub>n</sub>(q<sub>n</sub><sup>T</sup>b)

transforms:   
QQ<sup>T</sup> = I is the foundation of Fourier series and all great transforms of applied mathematics.  They break vectors b or functions f(x)  into perpendicular pieces.  they by adding the pieces in the above equation together, teh inverse transform puts b and f(x) back together. 

example: 

the columns of tis orthogonal Q are orthonormal vectors q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub>

the separate projections of b = (0,0,1) onto q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub> are p<sub>1</sub>, p<sub>2</sub>, p<sub>3</sub>

the sum of the first two is the projection of b onto the the plane of q<sub>1</sub> and q<sub>2</sub>.   

the sum of all three is the projection of b onto the whole space = q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub> which is p<sub>1</sub> + p<sub>2</sub> + p<sub>3</sub> = b itself. 

this leads to gram-schmidt processes.

![\begin{align*}
m = n & = 3 \\ 
Q &= \frac{1}{3}
\begin{bmatrix}
-1&2&2\\
2&-1&2\\
2&2&-1
\end{bmatrix}\\
\\
I& = Q^TQ = QQ^T\\
\\
b& = 
\begin{bmatrix}
0\\0\\1
\end{bmatrix}\\
\\
q_1(q_1^Tb) &= q_1(q_1^T 
\begin{bmatrix} 
0\\0\\1 
\end{bmatrix} ) = 
\frac{2}{3}q_1\\
q_2(q_2^Tb) &= q_2(q_2^T
\begin{bmatrix} 
0\\0\\1 
\end{bmatrix} ) = 
\frac{2}{3}q_2\\
q_3(q_3^Tb) &= q_3(q_3^T 
\begin{bmatrix} 
0\\0\\1 
\end{bmatrix} ) = 
\frac{1}{3}q_3\\
q_1(q_1^Tb) + ... + q_n(q_n^Tb) \\
\\
b & = p_1+p_2+p+3 \\
&= \frac{2}{3}q_1 +\frac{2}{3}q_2 +\frac{1}{3}q_3 \\
&= \frac{2}{3}(\frac{1}{3} \begin{bmatrix} -1\\2\\2 \end{bmatrix} )
+\frac{2}{3}(\frac{1}{3} \begin{bmatrix} 2\\-1\\2 \end{bmatrix} )
+\frac{1}{3}(\frac{1}{3} \begin{bmatrix} 2\\2\\-1 \end{bmatrix} ) \\
&= \frac{1}{9}
\begin{bmatrix}
-2+4-2\\
4-2-2\\
4+4+1
\end{bmatrix} \\
& = 
\begin{bmatrix} 
0\\0\\1 
\end{bmatrix}  
= b
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Am+%3D+n+%26+%3D+3+%5C%5C+%0AQ+%26%3D+%5Cfrac%7B1%7D%7B3%7D%0A%5Cbegin%7Bbmatrix%7D%0A-1%262%262%5C%5C%0A2%26-1%262%5C%5C%0A2%262%26-1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0AI%26+%3D+Q%5ETQ+%3D+QQ%5ET%5C%5C%0A%5C%5C%0Ab%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Aq_1%28q_1%5ETb%29+%26%3D+q_1%28q_1%5ET+%0A%5Cbegin%7Bbmatrix%7D+%0A0%5C%5C0%5C%5C1+%0A%5Cend%7Bbmatrix%7D+%29+%3D+%0A%5Cfrac%7B2%7D%7B3%7Dq_1%5C%5C%0Aq_2%28q_2%5ETb%29+%26%3D+q_2%28q_2%5ET%0A%5Cbegin%7Bbmatrix%7D+%0A0%5C%5C0%5C%5C1+%0A%5Cend%7Bbmatrix%7D+%29+%3D+%0A%5Cfrac%7B2%7D%7B3%7Dq_2%5C%5C%0Aq_3%28q_3%5ETb%29+%26%3D+q_3%28q_3%5ET+%0A%5Cbegin%7Bbmatrix%7D+%0A0%5C%5C0%5C%5C1+%0A%5Cend%7Bbmatrix%7D+%29+%3D+%0A%5Cfrac%7B1%7D%7B3%7Dq_3%5C%5C%0Aq_1%28q_1%5ETb%29+%2B+...+%2B+q_n%28q_n%5ETb%29+%5C%5C%0A%5C%5C%0Ab+%26+%3D+p_1%2Bp_2%2Bp%2B3+%5C%5C%0A%26%3D+%5Cfrac%7B2%7D%7B3%7Dq_1+%2B%5Cfrac%7B2%7D%7B3%7Dq_2+%2B%5Cfrac%7B1%7D%7B3%7Dq_3+%5C%5C%0A%26%3D+%5Cfrac%7B2%7D%7B3%7D%28%5Cfrac%7B1%7D%7B3%7D+%5Cbegin%7Bbmatrix%7D+-1%5C%5C2%5C%5C2+%5Cend%7Bbmatrix%7D+%29%0A%2B%5Cfrac%7B2%7D%7B3%7D%28%5Cfrac%7B1%7D%7B3%7D+%5Cbegin%7Bbmatrix%7D+2%5C%5C-1%5C%5C2+%5Cend%7Bbmatrix%7D+%29%0A%2B%5Cfrac%7B1%7D%7B3%7D%28%5Cfrac%7B1%7D%7B3%7D+%5Cbegin%7Bbmatrix%7D+2%5C%5C2%5C%5C-1+%5Cend%7Bbmatrix%7D+%29+%5C%5C%0A%26%3D+%5Cfrac%7B1%7D%7B9%7D%0A%5Cbegin%7Bbmatrix%7D%0A-2%2B4-2%5C%5C%0A4-2-2%5C%5C%0A4%2B4%2B1%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%26+%3D+%0A%5Cbegin%7Bbmatrix%7D+%0A0%5C%5C0%5C%5C1+%0A%5Cend%7Bbmatrix%7D++%0A%3D+b%0A%5Cend%7Balign%2A%7D)

14.  every 2x2 symmetric matrix is &lambda;<sub>1</sub>x<sub>1</sub>x<sub>1</sub><sup>T</sup> + &lambda;<sub>2</sub>x<sub>2</sub>x<sub>2</sub><sup>T</sup> = &lambda;<sub>1</sub>P<sub>1</sub> + &lambda;<sub>2</sub>P<sub>2</sub>   
Explain P<sub>1</sub> + P<sub>2</sub> = x<sub>1</sub>x<sub>1</sub><sup>T</sup> + x<sub>2</sub>x<sub>2</sub><sup>T</sup> = I from columns times rows of PQ.  Why is P<sub>1</sub> P<sub>2</sub> = 0?

becuase A = S = S<sup>T</sup>, 
{x<sub>1</sub>, x<sub>2</sub>} is a Q matrix so P<sub>1</sub> + P<sub>2</sub> = x<sub>1</sub>x<sub>1</sub><sup>T</sup> + x<sub>2</sub>x<sub>2</sub><sup>T</sup> = I   
because ||x<sub>1</sub>|| = ||x<sub>2</sub>|| = 1 and x<sub>1</sub><sup>T</sup>x<sub>2</sub> = 0  


P<sub>1</sub>P<sub>2</sub> = 0 
- because P<sub>1</sub>P<sub>2</sub> = x<sub>1</sub>x<sub>1</sub><sup>T</sup> x<sub>2</sub>x<sub>2</sub><sup>T</sup> = 0   
- also because P<sub>1</sub> + P<sub>2</sub> = I and then   
P<sub>1</sub> = I - P<sub>2</sub> or P<sub>2</sub> = I - P<sub>1</sub>   
so P<sub>1</sub>P<sub>2</sub> = P<sub>1</sub>(I - P<sub>1</sub>) = P<sub>1</sub> - P<sub>2</sub><sup>2</sup> = P<sub>1</sub> - P<sub>2</sub> = 0

every 2x2 symmetric marix system can be written as A = &lambda;<sub>1</sub>x<sub>1</sub>x<sub>1</sub><sup>T</sup> + &lambda;<sub>2</sub>x<sub>2</sub>x<sub>2</sub><sup>T</sup> = &lambda;<sub>1</sub>P<sub>1</sub> + &lambda;<sub>2</sub>P<sub>2</sub>
where P<sub>1</sub> and P<sub>2</sub> are projection matrices 
if x<sub>1</sub> and x<sub>2</sub> are orthogonal to one another and unit length then the projection matrices sum = I and product = zero.

S = Q&Lambda;Q<sup>T</sup> = &lambda;<sub>1</sub>q<sub>1</sub>q<sub>1</sub><sup>T</sup> + &lambda;<sub>2</sub>q<sub>2</sub>q<sub>2</sub><sup>T</sup>

P is derived:   
Axhat = b when Ax ≠ b   
Axhat is projection of b on to A  
Axhat + e = b   
solving for xhat:  
Axhat = b --> A<sup>T</sup>Axhat = A<sup>T</sup>b --> xhat = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b --> p = Axhat = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b = **P** b = **(A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>)** b where P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>

then, finding orthogonal basis vectors for A in q's: A<sup>T</sup>A becomes Q<sup>T</sup>Q = I   
thus:   
xhat = Q<sup>T</sup>b   
p = Qxhat   
P = QQ<sup>T</sup>  
p = Pb   

if Q is square then Q<sup>T</sup> = Q<sup>-1</sup> maps all space:  
p = Qxhat   
p = Pb   
p = QQ<sup>T</sup>b = Ib = b
p = q<sub>1</sub>q<sub>1</sub><sup>T</sup>b + q<sub>n</sub>q<sub>n</sub><sup>T</sup>b

interesting putting that together with S = Q&Lambda;Q<sup>T</sup> = q<sub>1</sub>q<sub>1</sub><sup>T</sup>&lambda;<sub>n</sub> + q<sub>n</sub>q<sub>n</sub><sup>T</sup>&lambda;<sub>n</sub>

where b is replaced by a series of &lambda;<sub>i</sub> matched to each orthogonal axis q<sub>i</sub>


15. the eigenvalues of A = -A<sup>T</sup> are imaginary.  verify by means of characteristic equation 

![\begin{align*}
det A - &lambda;I & = det (-A)^T - &lambda;I \\ &= det 
\begin{bmatrix} 0&b\\-b&0\end{bmatrix} \\ &= det 
\begin{bmatrix} 0&-b\\b&0\end{bmatrix} \\ & =
&lambda;^2 + b^2 = 0 \longrightarrow &lambda; = \pm bi
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Adet+A+-+%26lambda%3BI+%26+%3D+det+%28-A%29%5ET+-+%26lambda%3BI+%5C%5C+%26%3D+det+%0A%5Cbegin%7Bbmatrix%7D+0%26b%5C%5C-b%260%5Cend%7Bbmatrix%7D+%5C%5C+%26%3D+det+%0A%5Cbegin%7Bbmatrix%7D+0%26-b%5C%5Cb%260%5Cend%7Bbmatrix%7D+%5C%5C+%26+%3D%0A%26lambda%3B%5E2+%2B+b%5E2+%3D+0+%5Clongrightarrow+%26lambda%3B+%3D+%5Cpm+bi%0A%5Cend%7Balign%2A%7D)

if need to make a 4x4 example can use these block matrices which are skew symmetric:

![\begin{align*}
A = -A^T &= 
\begin{bmatrix} 0&b\\-b&0\end{bmatrix} \\ 
\\
BM &= 
\begin{bmatrix} 0&A\\A&0\end{bmatrix} \\ & =
\begin{bmatrix} A&0\\0&A\end{bmatrix} 
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%3D+-A%5ET+%26%3D+%0A%5Cbegin%7Bbmatrix%7D+0%26b%5C%5C-b%260%5Cend%7Bbmatrix%7D+%5C%5C+%0A%5C%5C%0ABM+%26%3D+%0A%5Cbegin%7Bbmatrix%7D+0%26A%5C%5CA%260%5Cend%7Bbmatrix%7D+%5C%5C+%26+%3D%0A%5Cbegin%7Bbmatrix%7D+A%260%5C%5C0%26A%5Cend%7Bbmatrix%7D+%0A%5Cend%7Balign%2A%7D)

![\begin{align*}
A = -A^T &= 
\begin{bmatrix} 0&b\\-b&0\end{bmatrix} \\ 
\\
BM_1 &= 
\begin{bmatrix} 0&A\\A&0\end{bmatrix} \\
BM_2 &= 
\begin{bmatrix} A&0\\0&A\end{bmatrix} \\
|BM_1| & = det 
\begin{bmatrix} 
-&lambda;&b&0&0\\
-b&-&lambda;&0&0\\
0&0&-&lambda;&b\\
0&0&-b&-&lambda;\\
\end{bmatrix} \\ & = 
(-&lambda;)(-&lambda;)[(-&lambda;)(-&lambda;) - (b)(-b)] -b(-b)[(-&lambda;)(-&lambda;) - (b)(-b)] \\ &= 
&lambda;^2[&lambda;^2 + b^2] +b^2[&lambda;^2+b^2] \\ &=
&lambda;^4 + 2&lambda;^2b^2 + b^4 \\ &=
(&lambda;^2 + b^2)^2 = 0 \longrightarrow &lambda;^2 + b^2 = 0 \longrightarrow &lambda;^2 = -b^2 \longrightarrow &lambda; = \pm ib
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%3D+-A%5ET+%26%3D+%0A%5Cbegin%7Bbmatrix%7D+0%26b%5C%5C-b%260%5Cend%7Bbmatrix%7D+%5C%5C+%0A%5C%5C%0ABM_1+%26%3D+%0A%5Cbegin%7Bbmatrix%7D+0%26A%5C%5CA%260%5Cend%7Bbmatrix%7D+%5C%5C%0ABM_2+%26%3D+%0A%5Cbegin%7Bbmatrix%7D+A%260%5C%5C0%26A%5Cend%7Bbmatrix%7D+%5C%5C%0A%7CBM_1%7C+%26+%3D+det+%0A%5Cbegin%7Bbmatrix%7D+%0A-%26lambda%3B%26b%260%260%5C%5C%0A-b%26-%26lambda%3B%260%260%5C%5C%0A0%260%26-%26lambda%3B%26b%5C%5C%0A0%260%26-b%26-%26lambda%3B%5C%5C%0A%5Cend%7Bbmatrix%7D+%5C%5C+%26+%3D+%0A%28-%26lambda%3B%29%28-%26lambda%3B%29%5B%28-%26lambda%3B%29%28-%26lambda%3B%29+-+%28b%29%28-b%29%5D+-b%28-b%29%5B%28-%26lambda%3B%29%28-%26lambda%3B%29+-+%28b%29%28-b%29%5D+%5C%5C+%26%3D+%0A%26lambda%3B%5E2%5B%26lambda%3B%5E2+%2B+b%5E2%5D+%2Bb%5E2%5B%26lambda%3B%5E2%2Bb%5E2%5D+%5C%5C+%26%3D%0A%26lambda%3B%5E4+%2B+2%26lambda%3B%5E2b%5E2+%2B+b%5E4+%5C%5C+%26%3D%0A%28%26lambda%3B%5E2+%2B+b%5E2%29%5E2+%3D+0+%5Clongrightarrow+%26lambda%3B%5E2+%2B+b%5E2+%3D+0+%5Clongrightarrow+%26lambda%3B%5E2+%3D+-b%5E2+%5Clongrightarrow+%26lambda%3B+%3D+%5Cpm+ib%0A%5Cend%7Balign%2A%7D)


<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/110273307-50aae400-7f9a-11eb-803e-4cb2b1861eca.png">


16. M is anti symmetric and also orthogonal.  All its eigenvalues are pure imaginary: |&lambda;<sub>i</sub>| = 1.  For every x, ||Mx|| = ||&lambda;x|| = ||x||.  Find all four eigenvalues for trace of M.  

those are i, i, -i, -i

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/110280099-3ed03d80-7fa8-11eb-9762-93439bd598f2.png">

https://github.com/stevedepp/strang/blob/master/ch6/README2.md

https://github.com/stevedepp/strang/issues/new

https://tex-image-link-generator.herokuapp.com


17.  A<sup>T</sup> = A is not such a special property for complex matrices.  The good property is Abar<sup>T</sup> = A which relates conjugate complex matrices.  Then all &lambda;s are real and eigenvalues are orthogonal.  

![\begin{align*}
A&=
\begin{bmatrix}i&1\\1&i\end{bmatrix}\\
\\
det A-&lambda;I &= det \begin{bmatrix}i-&lambda;&1\\1&i-&lambda;\end{bmatrix}=0\\
&=&lambda;^2+1-1=&lambda;^2=0 \longrightarrow &lambda; = 0,0\\
\\
(A-&lambda;I)x &= \begin{bmatrix}i-&lambda;&1\\1&i-&lambda;\end{bmatrix}x = 0 \\
&=
\begin{bmatrix}i&1\\1&i\end{bmatrix}x \longrightarrow x = \begin{bmatrix}i\\1\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA%26%3D%0A%5Cbegin%7Bbmatrix%7Di%261%5C%5C1%26i%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Adet+A-%26lambda%3BI+%26%3D+det+%5Cbegin%7Bbmatrix%7Di-%26lambda%3B%261%5C%5C1%26i-%26lambda%3B%5Cend%7Bbmatrix%7D%3D0%5C%5C%0A%26%3D%26lambda%3B%5E2%2B1-1%3D%26lambda%3B%5E2%3D0+%5Clongrightarrow+%26lambda%3B+%3D+0%2C0%5C%5C%0A%5C%5C%0A%28A-%26lambda%3BI%29x+%26%3D+%5Cbegin%7Bbmatrix%7Di-%26lambda%3B%261%5C%5C1%26i-%26lambda%3B%5Cend%7Bbmatrix%7Dx+%3D+0+%5C%5C%0A%26%3D%0A%5Cbegin%7Bbmatrix%7Di%261%5C%5C1%26i%5Cend%7Bbmatrix%7Dx+%5Clongrightarrow+x+%3D+%5Cbegin%7Bbmatrix%7Di%5C%5C1%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

18. even if A is rectangular, the block matrix is symmetric.

Az = &lambda;y  
A<sup>T</sup>y = &lambda;z

multiply both sides of 1st equation by A<sup>T</sup> to reveal that &lambda;<sup>2</sup> is an eigenvalue of A<sup>T</sup>A.  (This algebra shown below the python code below.)

Thus if A = I then &pm; 1 is an eigenvalue of A and two of &pm; 1 are 4 eigenvalues of S: 1-1+1-1 = 0 = trace<sub>S</sub> and det S = 0 • 0 - (I • I) = -I<sup>2</sup> should match the product of the eigenvalues which is +1 not -1, but this says det S = 1 so it concurs with logic of det S = product of eigenvalues +1, -1, +1, -1.

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/110359280-4c6adf00-800b-11eb-8fab-834fa582ee45.png">

19.  if A = (1,1) then eigenvalues are zero, and &pm; √2   
and inciidentally (not shown) eigenvectors are (1,-1,0), (1,1,√2), (1,1,-√2)


![\begin{align*}
S &=
\begin{bmatrix}
0&A\\
A^T&0
\end{bmatrix} \\
\\
Sx & = 
\begin{bmatrix}
0&A\\
A^T&0
\end{bmatrix} 
\begin{bmatrix}
y\\
z
\end{bmatrix} = &lambda; 
\begin{bmatrix}
y\\
z
\end{bmatrix} = &lambda;x 
\\
\longrightarrow &
 Az = &lambda;y \\
& A^Ty = &lambda;z\\
\\
&A^T(Az = &lambda;y) \\
&A^TAz = &lambda;A^Ty \\
&A^TAz = &lambda;^2z \\
\longrightarrow & &lambda;_{A^TA} = &lambda;^2 = \pm &lambda;\\
\\
A&=
\begin{bmatrix}
1\\
1
\end{bmatrix} \\
S = &
\begin{bmatrix}
&&1\\
&&1\\
1&1&
\end{bmatrix} = 
\begin{bmatrix}
0&0&1\\
0&0&1\\
1&1&0
\end{bmatrix}\\
\\
det (S - &lambda;I) &= 
det (\begin{bmatrix}
-&lambda;&0&1\\
0&-&lambda;&1\\
1&1&- &lambda;&
\end{bmatrix}) \\
&= -&lambda;(&lambda;^2-1) + 1*(0-(1*-&lambda;)) = -&lambda;(&lambda;^2-2)=0 \\
& \longrightarrow &lambda; = 0,  +\sqrt{2}, -\sqrt{2}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%26A%5C%5C%0AA%5ET%260%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%5C%5C%0ASx+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A0%26A%5C%5C%0AA%5ET%260%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D+%3D+%26lambda%3B+%0A%5Cbegin%7Bbmatrix%7D%0Ay%5C%5C%0Az%0A%5Cend%7Bbmatrix%7D+%3D+%26lambda%3Bx+%0A%5C%5C%0A%5Clongrightarrow+%26%0A+Az+%3D+%26lambda%3By+%5C%5C%0A%26+A%5ETy+%3D+%26lambda%3Bz%5C%5C%0A%5C%5C%0A%26A%5ET%28Az+%3D+%26lambda%3By%29+%5C%5C%0A%26A%5ETAz+%3D+%26lambda%3BA%5ETy+%5C%5C%0A%26A%5ETAz+%3D+%26lambda%3B%5E2z+%5C%5C%0A%5Clongrightarrow+%26+%26lambda%3B_%7BA%5ETA%7D+%3D+%26lambda%3B%5E2+%3D+%5Cpm+%26lambda%3B%5C%5C%0A%5C%5C%0AA%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D+%5C%5C%0AS+%3D+%26%0A%5Cbegin%7Bbmatrix%7D%0A%26%261%5C%5C%0A%26%261%5C%5C%0A1%261%26%0A%5Cend%7Bbmatrix%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A0%260%261%5C%5C%0A0%260%261%5C%5C%0A1%261%260%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Adet+%28S+-+%26lambda%3BI%29+%26%3D+%0Adet+%28%5Cbegin%7Bbmatrix%7D%0A-%26lambda%3B%260%261%5C%5C%0A0%26-%26lambda%3B%261%5C%5C%0A1%261%26-+%26lambda%3B%26%0A%5Cend%7Bbmatrix%7D%29+%5C%5C%0A%26%3D+-%26lambda%3B%28%26lambda%3B%5E2-1%29+%2B+1%2A%280-%281%2A-%26lambda%3B%29%29+%3D+-%26lambda%3B%28%26lambda%3B%5E2-2%29%3D0+%5C%5C%0A%26+%5Clongrightarrow+%26lambda%3B+%3D+0%2C++%2B%5Csqrt%7B2%7D%2C+-%5Csqrt%7B2%7D%0A%5Cend%7Balign%2A%7D)



20.  Another proof that eigenvectors are perpendicular when S = S<sup>T</sup> in 2 steps:   
1. suppose Sx = &lambda;x and Sy = 0y and &lambda; ≠ 0   
then y is in the null space [presumably because 0y = 0]   
and x is in the column space   
why are these subspaces orthogonal?

y is in the null space of S and x in the column space of S which is the row space of S<sup>T</sup>.  
the null space and row space are perpendicualar.   
so y<sup>T</sup>x = 0
[answer to me doesnt make sense since the question states &lambda; ≠ 0 and so is y an eigenvector to begin with if it is just paired with zero but zero is not an eigenvalue?]

if Sy = &beta;y and &beta; is an eigenvalue, apply that argument to  S - &beta;I.  One eigenvalue of S-&beta;I moves to zero. the eigenvectors x,y stay the same and so they are perpendicular.  

if Sx = &lambda;x and Sy = &beta;y then shift S by &beta;I to have zero eigenvalue that matches step 1.  y is known null and By = Sy; so Sy - &beta;yIy = (S-&beta;I)y = 0.  (S-&betal=;I)x = (&lambda-&beta;)x and (S-&beta;I)y = 0 and again x perpendicular to y.  

22.
S is Hermatian where S_bar<sup>T</sup> = S  
its eigenvalues are -4 and 6   

![\begin{align*}
S &= 
\begin{bmatrix}
1&3+4i\\
3-4i&1
\end{bmatrix}\\
\overline{S} &= 
\begin{bmatrix}
1&3-4i\\
3+4i&1
\end{bmatrix}\\
\overline{S}^T &= 
\begin{bmatrix}
1&3+4i\\
3-4i&1
\end{bmatrix}\\
\\
det S &= (&lambda;+4)(&lambda;-6) = 0\\
\\
(S-&lambda;I)x &= \begin{bmatrix}
1-&lambda;&3+4i\\
3-4i&1-&lambda;
\end{bmatrix}x\\
&= \begin{bmatrix}
-5&3+4i\\
3-4i&-5
\end{bmatrix}x_1\\ 
&= \begin{bmatrix}
-5&3+4i\\
3-4i&-5
\end{bmatrix}x_2
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%263%2B4i%5C%5C%0A3-4i%261%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Coverline%7BS%7D+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%263-4i%5C%5C%0A3%2B4i%261%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Coverline%7BS%7D%5ET+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%263%2B4i%5C%5C%0A3-4i%261%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Adet+S+%26%3D+%28%26lambda%3B%2B4%29%28%26lambda%3B-6%29+%3D+0%5C%5C%0A%5C%5C%0A%28S-%26lambda%3BI%29x+%26%3D+%5Cbegin%7Bbmatrix%7D%0A1-%26lambda%3B%263%2B4i%5C%5C%0A3-4i%261-%26lambda%3B%0A%5Cend%7Bbmatrix%7Dx%5C%5C%0A%26%3D+%5Cbegin%7Bbmatrix%7D%0A-5%263%2B4i%5C%5C%0A3-4i%26-5%0A%5Cend%7Bbmatrix%7Dx_1%5C%5C+%0A%26%3D+%5Cbegin%7Bbmatrix%7D%0A-5%263%2B4i%5C%5C%0A3-4i%26-5%0A%5Cend%7Bbmatrix%7Dx_2%0A%5Cend%7Balign%2A%7D)

Adjust equations to prove that &lambda; always real when Hermatian.

Sx = &lambda;x -->      
S_bar x_bar = &lambda;_bar x_bar  -->   
x_bar<sup>T</sup>S_bar<sup>T</sup>  = x_bar<sup>T</sup>&lambda;_bar  

since S_bar<sup>T</sup> = S     
x_bar<sup>T</sup>S  = x_bar<sup>T</sup>&lambda;_bar    

multiply both sides by x   
x_bar<sup>T</sup>Sx  = x_bar<sup>T</sup>&lambda;_bar x  

notice that the Sx on the LHS = &lambda;x from the first equation above; so, ....  
x_bar<sup>T</sup>&lambda;x  = x_bar<sup>T</sup>&lambda;_bar x  

thus &lambda; = &lambda;_bar

![\begin{align*}
Sx & = &lambda;x \longrightarrow \overline{S}\overline{x} = \overline{&lambda;}\overline{x} \longrightarrow \overline{x}^T\overline{S}^T = \overline{x}^T\overline{&lambda;}\\
\\
\overline{S}^T & = S \longrightarrow \overline{x}^TS = \overline{x}^T\overline{&lambda;}
\\
\overline{x}^TSx &= \overline{x}^T\overline{&lambda;}x
\\
\overline{x}^T&lambda;x &= \overline{x}^T\overline{&lambda;}x\\
\\
&lambda; &= \overline{&lambda;}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0ASx+%26+%3D+%26lambda%3Bx+%5Clongrightarrow+%5Coverline%7BS%7D%5Coverline%7Bx%7D+%3D+%5Coverline%7B%26lambda%3B%7D%5Coverline%7Bx%7D+%5Clongrightarrow+%5Coverline%7Bx%7D%5ET%5Coverline%7BS%7D%5ET+%3D+%5Coverline%7Bx%7D%5ET%5Coverline%7B%26lambda%3B%7D%5C%5C%0A%5C%5C%0A%5Coverline%7BS%7D%5ET+%26+%3D+S+%5Clongrightarrow+%5Coverline%7Bx%7D%5ETS+%3D+%5Coverline%7Bx%7D%5ET%5Coverline%7B%26lambda%3B%7D%0A%5C%5C%0A%5Coverline%7Bx%7D%5ETSx+%26%3D+%5Coverline%7Bx%7D%5ET%5Coverline%7B%26lambda%3B%7Dx%0A%5C%5C%0A%5Coverline%7Bx%7D%5ET%26lambda%3Bx+%26%3D+%5Coverline%7Bx%7D%5ET%5Coverline%7B%26lambda%3B%7Dx%5C%5C%0A%5C%5C%0A%26lambda%3B+%26%3D+%5Coverline%7B%26lambda%3B%7D%0A%5Cend%7Balign%2A%7D)

23.

F
a matrix with real eigenvalues and n real eigenvectors is symmetric
e.g. A = [[1,2],[0,1]]

T
a matrix with real eigenvalues and n orthogonal eigenvectors is symmetric    
because dot product in off diagonal = - and lengths in diagonals.
A<sup>T</sup> = Q&Lambda;Q<sup>T</sup> 


T 
the inverse of ann invertible symmetric matrix is symmetric   
because faxtors and cofactors are same on both sides of diagonal.  
S<sup>-1</sup> = Q&Lambda;Q<sup>T</sup>


24. if AA<sup>T</sup> = A<sup>T</sup>    
then A and A<sup>T</sup> share the same eigenvectors    
A and A<sup>T</sup> share the same eigenvalues.  

Whats wrong with this conclusion:  A and A<sup>T</sup> must have the same X and &Lambda

A and A<sup>T</sup> have same &lambda;s and there's no ordering the &lambda;s,
but the order of the x's change for each &lambda; as switch from A to A<supT</sup>.  
Shown below, A and A<sup>T</sup> have &lambda;<sub>1</sub> = i and &lambda;<sub>2</sub> = -i,
but for &lambda;<sub>1</sub> = i, A has x<sub>1</sub> = (1,i) while A<sup>T</sup> has x<sub>1</sub> = (1,-i) .

![\begin{align*}
A =& 
\begin{bmatrix}
0&1\\
-1&0
\end{bmatrix} \\
A^T =&
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix} \\
\\
det(A-&lambda;I)=det(A^T-&lambda;I) =& &lambda;^2 + 1 = 0 \\
\longrightarrow & &lambda;_1 = i \\
& &lambda;_2 = -i\\
\\
(A-&lambda;_1I)x_1  =& 
\begin{bmatrix}
-i&1\\
-1&-i
\end{bmatrix}x_1 \longrightarrow x_1 = 
\begin{bmatrix} 
1\\
i 
\end{bmatrix} \\
(A^T-&lambda;_1I)x_1  =& 
\begin{bmatrix}
-i&-1\\
1&-i
\end{bmatrix}x_1 \longrightarrow x_1 = 
\begin{bmatrix} 
1\\ 
-i 
\end{bmatrix}\\
\\
(A-&lambda;_2I)x_2  =& 
\begin{bmatrix}
i&1\\
-1&i
\end{bmatrix}x_2 \longrightarrow x_2 = 
\begin{bmatrix} 
1\\
-i 
\end{bmatrix} \\
(A^T-&lambda;_2I)x_2  =& 
\begin{bmatrix}
i&-1\\
1&i
\end{bmatrix} x_2 \longrightarrow x_2 = 
\begin{bmatrix} 
1\\
-i 
\end{bmatrix}\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A0%261%5C%5C%0A-1%260%0A%5Cend%7Bbmatrix%7D+%5C%5C%0AA%5ET+%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A0%26-1%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%5C%5C%0Adet%28A-%26lambda%3BI%29%3Ddet%28A%5ET-%26lambda%3BI%29+%3D%26+%26lambda%3B%5E2+%2B+1+%3D+0+%5C%5C%0A%5Clongrightarrow+%26+%26lambda%3B_1+%3D+i+%5C%5C%0A%26+%26lambda%3B_2+%3D+-i%5C%5C%0A%5C%5C%0A%28A-%26lambda%3B_1I%29x_1++%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A-i%261%5C%5C%0A-1%26-i%0A%5Cend%7Bbmatrix%7Dx_1+%5Clongrightarrow+x_1+%3D+%0A%5Cbegin%7Bbmatrix%7D+%0A1%5C%5C%0Ai+%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%28A%5ET-%26lambda%3B_1I%29x_1++%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A-i%26-1%5C%5C%0A1%26-i%0A%5Cend%7Bbmatrix%7Dx_1+%5Clongrightarrow+x_1+%3D+%0A%5Cbegin%7Bbmatrix%7D+%0A1%5C%5C+%0A-i+%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%28A-%26lambda%3B_2I%29x_2++%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ai%261%5C%5C%0A-1%26i%0A%5Cend%7Bbmatrix%7Dx_2+%5Clongrightarrow+x_2+%3D+%0A%5Cbegin%7Bbmatrix%7D+%0A1%5C%5C%0A-i+%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%28A%5ET-%26lambda%3B_2I%29x_2++%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ai%26-1%5C%5C%0A1%26i%0A%5Cend%7Bbmatrix%7D+x_2+%5Clongrightarrow+x_2+%3D+%0A%5Cbegin%7Bbmatrix%7D+%0A1%5C%5C%0A-i+%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cend%7Balign%2A%7D)


26. what number b in A = [[2,b],[1,0]] makes A = Q&Lambda;Q<sup>T</sup> possible? makes diagonalization impossible, makes A singular ?

1 makes Q&Lambda;Q<sup>T</sup> possible because symmetry makes possible orthogonal diagonalization.    
-1 makes diagonalization impossible since (&lambda; -1)<sup>2</sup> has repeated eigenvalues with insufficient eigenvector and thus the eigenvector matrix wont have independent vectors.

0 makes A singular. 

27. find all 2x2 matrices that are orthogonal and symmetric. which 2 numbers can be eigenvalues of these 2 matrices ?   

orthogonal and symmetric matrices require |&lambda;| = 1 and &lambda; real.  So &lambda; = &pm; 1.  

1st matrix:   
so S 
= &pm; I 
or 
2nd matrix:  
S 
= Q&Lambda;Q<sup>T</sup>  
= [[cos &theta;, -sin &theta;], [sin &theta;, cos &theta;]] [[1,0],[0,-1]] [[cos &theta;, sin &theta;],[-sin &theta;, cos &theta;]] 
= [[cos 2&theta;, sin 2&theta;],[sin 2&theta;, -cos 2&theta;]]

28. A is nearly symmetric but eigenvectors are far from orthogonal.

whats the angle between them ?

eigenvectors (1,0) and (1,1) give 45 degrees even thought the A<sup>T</sup> is very close to A.  

The point is that eigenvectors are blunt instrument. 

![\begin{align*}
A &=
\begin{bmatrix}
1&10^{-15}\\
0&1+10^{-15}
\end{bmatrix} \\
\\
det(A-&lambda;I) &=
\begin{bmatrix}
1-&lambda;&10^{-15}\\
0&1+10^{-15} - &lambda;
\end{bmatrix}  =  (1-&lambda;)(1+10^{-15} - &lambda;) - 0*10^{-15} \longrightarrow &lambda; =1,1+10^{-15} \\
\\
(A-&lambda;_1I)x_1  &= 
\begin{bmatrix}
1-1&10^{-15}\\
0&1+10^{-15}-1
\end{bmatrix}x_1 = 
\begin{bmatrix}
0&10^{-15}\\
0&10^{-15}
\end{bmatrix}x_1 
\longrightarrow x_1 = 
\begin{bmatrix} 
1\\ 
0 
\end{bmatrix}\\
\\
\\
(A-&lambda;_2I)x_2  &= 
\begin{bmatrix}
1-(1+10^{-15})&10^{-15}\\
0&1+10^{-15}-(1+10^{-15})
\end{bmatrix}x_2 = 
\begin{bmatrix}
-10^{-15}&10^{-15}\\
0&0
\end{bmatrix}x_2 
\longrightarrow x_2 = 
\begin{bmatrix} 
1\\ 
1 
\end{bmatrix}\\
\\
cos &theta; &= \frac{v^Tw}{||v|| \, ||w||} \\
&theta; &= acos (\frac{v^Tw}{||v|| \, ||w||})  \\
&= acos (\frac{
\begin{bmatrix} 1& 0 
\end{bmatrix}
\begin{bmatrix} 1\\ 1 
\end{bmatrix}}
{\sqrt{1^2+0^2} \,\sqrt{1^2+1^2}}) \\
& = acos \frac{1}{1*\sqrt{2}} \\
& = acos \frac{1}{\sqrt{2}} \\
& = \pi \frac{45^\circ}{180^\circ}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%2610%5E%7B-15%7D%5C%5C%0A0%261%2B10%5E%7B-15%7D%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%5C%5C%0Adet%28A-%26lambda%3BI%29+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1-%26lambda%3B%2610%5E%7B-15%7D%5C%5C%0A0%261%2B10%5E%7B-15%7D+-+%26lambda%3B%0A%5Cend%7Bbmatrix%7D++%3D++%281-%26lambda%3B%29%281%2B10%5E%7B-15%7D+-+%26lambda%3B%29+-+0%2A10%5E%7B-15%7D+%5Clongrightarrow+%26lambda%3B+%3D1%2C1%2B10%5E%7B-15%7D+%5C%5C%0A%5C%5C%0A%28A-%26lambda%3B_1I%29x_1++%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1-1%2610%5E%7B-15%7D%5C%5C%0A0%261%2B10%5E%7B-15%7D-1%0A%5Cend%7Bbmatrix%7Dx_1+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A0%2610%5E%7B-15%7D%5C%5C%0A0%2610%5E%7B-15%7D%0A%5Cend%7Bbmatrix%7Dx_1+%0A%5Clongrightarrow+x_1+%3D+%0A%5Cbegin%7Bbmatrix%7D+%0A1%5C%5C+%0A0+%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%5C%5C%0A%28A-%26lambda%3B_2I%29x_2++%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1-%281%2B10%5E%7B-15%7D%29%2610%5E%7B-15%7D%5C%5C%0A0%261%2B10%5E%7B-15%7D-%281%2B10%5E%7B-15%7D%29%0A%5Cend%7Bbmatrix%7Dx_2+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-10%5E%7B-15%7D%2610%5E%7B-15%7D%5C%5C%0A0%260%0A%5Cend%7Bbmatrix%7Dx_2+%0A%5Clongrightarrow+x_2+%3D+%0A%5Cbegin%7Bbmatrix%7D+%0A1%5C%5C+%0A1+%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Acos+%26theta%3B+%26%3D+%5Cfrac%7Bv%5ETw%7D%7B%7C%7Cv%7C%7C+%5C%2C+%7C%7Cw%7C%7C%7D+%5C%5C%0A%26theta%3B+%26%3D+acos+%28%5Cfrac%7Bv%5ETw%7D%7B%7C%7Cv%7C%7C+%5C%2C+%7C%7Cw%7C%7C%7D%29++%5C%5C%0A%26%3D+acos+%28%5Cfrac%7B%0A%5Cbegin%7Bbmatrix%7D+1%26+0+%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D+1%5C%5C+1+%0A%5Cend%7Bbmatrix%7D%7D%0A%7B%5Csqrt%7B1%5E2%2B0%5E2%7D+%5C%2C%5Csqrt%7B1%5E2%2B1%5E2%7D%7D%29+%5C%5C%0A%26+%3D+acos+%5Cfrac%7B1%7D%7B1%2A%5Csqrt%7B2%7D%7D+%5C%5C%0A%26+%3D+acos+%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D+%5C%5C%0A%26+%3D+%5Cpi+%5Cfrac%7B45%5E%5Ccirc%7D%7B180%5E%5Ccirc%7D%0A%5Cend%7Balign%2A%7D)


30.  for complex matrices, S<sup>T</sup> = S the produces real eigenvalues must change to Sbar<sup>T</sup> = S.  From det (S - &lambda;I) = 0 find the eigenvalues of the 2x2 Hermitian matrix S = [[4, 2+i], [2-i, 0]] = S_bar<sup>T</sup>  

det S - &lambda;I = -&lambda;(4-&lambda;) - (2+i)(2-i) = &lambda;<sup>2</sup> - 4&lambda; - 5 = (&lambda;-5)(&lambda;+1) --> &lambda; = 5, -1

this solution proves that &lambda;s are real when S_bar<sup>T</sup> = S.

31.  Normal matrices have N_bar<sup>T</sup>N = NN_bar<sup>T</sup>.  
[normal allows transpose to commute]  Normal includes symmetric, skew symmetric and orthogonal (with real |&lambda;, imaginary |&lambda; and |&lambda;|=1).  Other normal matrices can have only complex eigenvalues.  Key point is normal matrices have n orthonormal eigenvectors.  THose vectors x<sub>i</sub> probably will have complex components.  In that complex case, orthogonality means x_bar<sub>i</sub><sup>T</sup>x<sub>i</sub> = 0 [imaginary cancel to -1].  Inner produces (dots) x<sup>T</sup>y become x_bar<sup>T</sup>y.

The test for n orthonormal columns in Q becomes Q_bar<sup>T</sup>Q = I instead of Q<sup>T</sup>Q = I

N has n orthonormal eigenvectors (N = Q&Lambda;Q_bar<sup>T</sup>) if and only if N is normal.  

a. start from N = Q&Lambda;Q_bar<sup>T</sup> with Q_bar<sup>T</sup>Q = I.  Show N_bar<sup>T</sup>N = NN_bar<sup>T</sup>.  N is normal.  

b. Now start from N_bar<sup>T</sup>N = NN_bar<sup>T</sup>.   Schur found A = QTQ_bar<sup>T</sup> for every matrix A with a triangular T.  For normal matrices A = N we must show (3 steps) that this triangular matrix T will be diagonal and then T = &Lambda.

1. Put N = QTQ_bar<sup>T</sup> into N_bar<sup>T</sup>N = NN_bar<sup>T</sup> to find T_bar<sup>T</sup>T = TT_bar<sup>T</sup>

N = Q&Lambda;Q_bar<sup>T</sup> with Q_bar<sup>T</sup>Q = I   
A = Q&lambda;Q_bar<sup>T</sup> times A<sup>T</sup> = Q&Lambda;_bar<sup>T</sup>Q_bar<sup>T</sup> = A_bar<sup>T</sup>A because Q = Q_bar<sup>T</sup> and &Lambda;&Lambda;_bar<sup>T</sup> = &Lambda;_bar<sup>T</sup>&Lambda;

Diagonal!

![\begin{align*}
\overline{A}^T ( Q&Lambda; \overline{Q}^T ) = Q \overline{&Lambda;}^T \overline{Q}^T ( Q&Lambda; \overline{Q}^T ) = Q \overline{&Lambda;}^T I &Lambda; \overline{Q}^T
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Coverline%7BA%7D%5ET+%28+Q%26Lambda%3B+%5Coverline%7BQ%7D%5ET+%29+%3D+Q+%5Coverline%7B%26Lambda%3B%7D%5ET+%5Coverline%7BQ%7D%5ET+%28+Q%26Lambda%3B+%5Coverline%7BQ%7D%5ET+%29+%3D+Q+%5Coverline%7B%26Lambda%3B%7D%5ET+I+%26Lambda%3B+%5Coverline%7BQ%7D%5ET%0A%5Cend%7Balign%2A%7D)

2. suppose T = [[a,b],[0,d]] has T_bar<sup>T</sup>T = TT_bar<sup>T</sup> prove that b = 0

4. extend step 2 to size n.  Any normal triangular T must be diagonal. 


