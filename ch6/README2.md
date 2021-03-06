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


