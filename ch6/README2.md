section 6.4 Symmetric Matrices

https://github.com/stevedepp/strang/issues/new

https://tex-image-link-generator.herokuapp.com

principles:   
1. a symmetric matrix s has n real eigenvalues &lambda; and n orthogonal eigenvectors q<sub>1</sub>, ... , q<sub>n</sub>   
2. every real symmetric S can be diagonalized [and therefore has n independent columns?]    
S = Q&Lambda;Q<sup>-1</sup> = Q&Lambda;Q<sup>T</sup>   
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
