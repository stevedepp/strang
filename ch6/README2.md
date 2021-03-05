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

