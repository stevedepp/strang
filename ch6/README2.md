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
\end{bmatrix}x_1 \longrightarrow x_1 = \begin{bmatrix} 1\\i \end{bmatrix}\\
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
\end{bmatrix}x_2 \longrightarrow x_2 = \begin{bmatrix} 1\\-i \end{bmatrix}\\
(A^T-&lambda;_2I)x_2  =& 
\begin{bmatrix}
i&-1\\
1&i
\end{bmatrix}x_2 \longrightarrow x_2 = 
\begin{bmatrix} 
1\\ 
i 
\end{bmatrix}\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A0%261%5C%5C%0A-1%260%0A%5Cend%7Bbmatrix%7D+%5C%5C%0AA%5ET+%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A0%26-1%5C%5C%0A1%260%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%5C%5C%0Adet%28A-%26lambda%3BI%29%3Ddet%28A%5ET-%26lambda%3BI%29+%3D%26+%26lambda%3B%5E2+%2B+1+%3D+0+%5C%5C%0A%5Clongrightarrow+%26+%26lambda%3B_1+%3D+i+%5C%5C%0A%26+%26lambda%3B_2+%3D+-i%5C%5C%0A%5C%5C%0A%28A-%26lambda%3B_1I%29x_1++%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A-i%261%5C%5C%0A-1%26-i%0A%5Cend%7Bbmatrix%7Dx_1+%5Clongrightarrow+x_1+%3D+%5Cbegin%7Bbmatrix%7D+1%5C%5Ci+%5Cend%7Bbmatrix%7D%5C%5C%0A%28A%5ET-%26lambda%3B_1I%29x_1++%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A-i%26-1%5C%5C%0A1%26-i%0A%5Cend%7Bbmatrix%7Dx_1+%5Clongrightarrow+x_1+%3D+%0A%5Cbegin%7Bbmatrix%7D+%0A1%5C%5C+%0A-i+%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0A%28A-%26lambda%3B_2I%29x_2++%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ai%261%5C%5C%0A-1%26i%0A%5Cend%7Bbmatrix%7Dx_2+%5Clongrightarrow+x_2+%3D+%5Cbegin%7Bbmatrix%7D+1%5C%5C-i+%5Cend%7Bbmatrix%7D%5C%5C%0A%28A%5ET-%26lambda%3B_2I%29x_2++%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ai%26-1%5C%5C%0A1%26i%0A%5Cend%7Bbmatrix%7Dx_2+%5Clongrightarrow+x_2+%3D+%0A%5Cbegin%7Bbmatrix%7D+%0A1%5C%5C+%0Ai+%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5Cend%7Balign%2A%7D)
