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


Start with 3d space, R<sup>3</sup>. Then imagine a plane through (0,0,0). That plane is a vector space itself.  Add 2 vectors in the plane.  Their sum is in the plane (closed to addition).  Multiply by a scalar and still in the plane (closed multiplication). A plane in R<sup>3</sup> looks like R<sup>2</sup> but its not in R<sup>2</sup> space.  The vectors in the vector space of the plane have 3 components and so belong to R<sup>3</sup>.  The plane is a vector space inside of R<sup>3</sup>.  Most fundamental Linear Algebra idea: The plane through 0,0.0 is a subspace of the full vector space R<sup>3</sup>.  Definition: A subspace of a vector space is a set of vectors (including zero) that satisfies two requirements: if v and w vectors in the subspace and c is any scalar, then:  
1. v+w is in the subspace  
2. cv is in the subspace 

np.array( [ [a, d], [b, e], [c, f] ] )

These mean the set of vectors is closed under addition v+w and multiplication cv and dw.  Can subtract because -w is in the subspace and its addition with v enables v-w in the subspace too. All linear combinations stay in the subspace.  Those are 4 of the rules of subspace (add, mulitply, negative, add negative).  Every subspace contains zero vector.  The plane in R<sup>3</sup> MUST GO THROUGH (0.0.0): choose c = 0 and the cv = 0.0.0.  Planes that fail this test, dont go through the origin and arent subspaces. Line through the origin (0,0,0) are also subspaces. R<sup>3</sup> is another subspace. Z is a subspace (0,0,0).

SUBSPACE INVERTIBILITY SOLVABILITY  

topic / requirement / question         
subspace / Ax / does it meet 8 rules ?
invertibility / A and A<sup>-1</sup> / can it be inverted ?
solvability / Ax = b and x = A<sup>-1</sup>b / is b in the column space ?

my conclusions:  
if not a subspace then cannot use x to linear combine.  
if not invertible then cannot solve for any b or a unique b even if A is a subspace.   
if not solvable for b, b may not be in A's column space, even if a subspace and invertible.

can be solvable but not invertible and singular because over spacified m>n which leads to cannot fill its R<sup>m</sup>.  Can only fill a plane subspace in R<sup>3</sup> defined by A with m>m times all x's.  It is solvable for only b's in its column space.  Ax=0 is solveable but only for x = 0 vector.

If the matrix is invertible, then it is solvable for all b in its column space, not for limited b (e.g. a plane in R<sup>3</sup>) in its vector space.  If invertible, its subspace is all R<sup>n</sup>

