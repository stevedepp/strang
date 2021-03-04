section 6.4 Symmetric Matrices

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

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/110010805-b1ad9000-7cec-11eb-90c5-d306840a84f8.png">

2.  by **proof** of these facts [**real** &lambda;s in &Lambda; and **orthonormal** x's in Q] when no eigenvalues are repeated 

For n x n case, the &lambda;s are real when S = S<sup>T</sup> and Sx = &lambda;x   
All the eigenvalues of a **real** symmetric matrix **are real** 

Proof:   

Sx = &lambda;x  

&lambda; might be complex a + ib where a and b are real with complex conjugate a - ib   
x might be complex as well.   switching the signs of their imaginary parts gives 
x(U+0305)
