chapter 3


3.1  Principles

1. The standard n-dimensional space R<sup>n</sup> contains all real column vectors with n components

2. If v and w are in a vector space S, every combination cv+dw must be in S [must means that S is not a vector space if those combinations are not in S].  This is closed in addition and scalar multiplication.

3. The vectors in S can be matrices or functions of x.    The one point space z consists of x = 0.

4. A subspace of R<sup>n</sup> is a vector space inside of R<sup>n</sup> e.g. the line y = 3x inside R<sup>2</sup>.

5. The column space of A contains all combinations of the columns of A: a subspace of R<sup>m</sup>.

6. The column space contains all the vectors Ax:  Ax = b is solvable when b is in the column space of A = C(A).

space R<sup>n</sup> contains all column vectors with n components.

R<sup>1</sup> is a line: each vector has one component

R<sup>2</sup> is a plane: each vector has two components

R<sup>3</sup> is 3 dimensional space

R is for real numbers.

Vectors whose n components are in complex numbers are in C<sup>n</sup>

np.array( [ [ 1+i ], [1 - i ] ] ) is in C<sup>2</sup>

Two essential vector operations occur inside vector space: add vectors and mulitply them by scalar c.

"inside vector space" means the result stays in the space.

8 rules for vector spaces.  Must be able to do these things and remain in the space for it to be defined as vector space.

1. add vectors v+w=w+v
2. x + (y+z) = (x + y) + z
3. there is a UNIQUE zero vector inside the subsoace 0+v=v
4. for every x there is a -x for which x + (-x) = 0
5. 1 times x = x
6. c<sub>1</sub>c<sub>2</sub>x = c<sub>1</sub>(c<sub>2</sub>x)
7. (c<sub>1</sub>+c<sub>2</sub>)x = c<sub>1</sub>x+c<sub>2</sub>x
8. mutliply by scalar c(v+w) = cv+cw


R<sup>n</sup> space = all column vectors v with n components  
C<sup>n</sup> space = all vectors whose n components are complex  
M = vector space of all real 2x2 matrices  
F = vector space of all real functions  
Z = vector space that consists of zero vectors only  
F is infinite but P<sup>n</sup> would be all polynomials of degree n a<sub>0</sub> +a<sub>1</sub>x + ... +a<sub>n</sub>x<sup>n</sup>  


Z is smallest possible vector space and contains only one vector = zero.  No space can do without zero vector.  Each space has its own zero vector = zero matrix, zero function, zero vector.

In our terms, b is the object with n dimensions in the space with R<sup>m</sup> dimensions
