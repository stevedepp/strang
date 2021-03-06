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

if keep only part of the plane or line, e.g. the positive part of line or only the part of the plane in quadrant 1, then requirements for subspace dont hold. I think this limits the usefulness of linear algebra since cannot move parts around. For example, if only x,y vectors with positive components then only 1/4 of plane and cannot multiply by c<0.

An example of M space is U which combined or multiplied by another U is still a U.  D's are another example.

The good RHS of Ax=b is the column space.  

If A is not invertible, the the system is solveable but for some b and not other b in R<sup>m</sup>
[though to me it seems that e.g. if m>n overspecification as in our plane specified in a 3x2 matrix of R<sup>m=3</sup>, then the solution is to reduce rows specification and reduce space from R<sup>m</sup> to R<sup>n</sup>] 

Column space is all the linear combinations of the columns of A that produce the column space of A and is a vector space made up column vectors.

A 3x2 matrix A in combinations may pass through (0,0,0) but not necessarily.

There is only one non zero vector v in S.  The subspace SS is the line through v.  Always SS is the smallest subspace containing S.  This is a fundamental way to create subspaces.  The columns span the column space.  The subspace is the span of S containing all combinations of vectors of S. The subspace SS contains all combinations of the vectors of S.   

Interesting problems:

If A is any 5x5 invertible matrix then its column space is in R<sup>5</sup>.   [Dont think necessarily, it is all of R<sup>5</sup>].  The equation Ax=b is always solvable by x=A<sup>-1</sup>b so every b is in the column space of that invertible matrix. 

If the 9x12 system Ax=b is solvable for every b, then C(A) is in R<sup>9</sup>.

Some notes on 3.1 and 3.2

R<sup>n</sup> is all column vectors with n components

Ax and AB are linear combinations of n vectors.

Vector space R<sup>n</sup> consists of all column vectors v with n [real] components.

8 conditions required of every vector space.

M = all 2 dimensional real matrices.  
F = all real functions.  
Z = the space that consists of only a zero vector.  Smallest possible vector space.  Not R<sup>0</sup> which means compents.  Z has vectors.  It has exactly 1 vector = zero vector.  
C<sup>n</sup> = the n dimnensional space of complex numbers with vectors of n components.  
R<sup>n</sup> = same but real  

Subspace is only part of vector spaces R C M F.  "Inside vector space" means that the result stays in the space when a linear combination are performed. 

"Invertible" is about A only.  
"Solvable" if and only if b in column spac of A, i.e. if b is a combination of the columns of A.  
If A is invertible, then Ax=b is solvable for all b in R<sup>n</sup>. ******


3.2 Null space

[  
some combination of the columns Ax will = 0.  
if invertible, then the only combination will be x = 0.  
if m>n then a minimum of m-n non-zero column values will get Ax to zero.
two ways to look at this.  there are n unknowns in cartesian space and only m equations and so cannot solve for a point. or in vector space, there are m-n excess vectors in R<sup>m</sup> space that must be dependent or combinations of other vectors.  So e.g. if 2x3 matrix ...  
]

For invertible matrices x = is only solution to Ax=0. For non invertible matrices, there are non-zero solutions that belong to null space of A in R<sup>n</sup>.  These null space solution vectors have n components.

example A = np.array( [ [1, 2], [3, 6] ] ) we have 1 line x<sub>1</sub> + 2x<sub>2</sub> = 0.  Choose one point on that line and all other points are mulitple of this.  It is also the combination of the column vectors: 2 of vector a<sub>1</sub> plus 1 of vector a<sub>2</sub> = 0.  So (-2,1) solves Ax = 0 and the null space of A contains all multiples of np.array([-2,1])

example 2 is x + 2y + 3z with A = np.array( [ 1, 2, 3 ] ) where Ax = 0 is a plane x, y, z and so all vectors that solve Ax=b whatever b it is will lie on the plane x + 2y + 3z = 0 which is the plane that is perpendicular to vector np.array( [ 1, 2, 3 ] )

[The reason that the solution to x + 2y + 3z has a plane of solutions for whatever b is selected is that it is under specified. If there were 2 other equations in cartesian space; i.e. vector space was R<sup>3</sup> not R<sup>1</sup>, then 2 of the 3 components of x and 2 of the 3 column vectors would not be useless.  So we can choose 2 solutions. One sets one of the free variables to 1 and the other to 0 and solves for the 1st variable.  s<sub>1</sub> = np.array( [ -2, 1, 0] ). The other sets teh second of the free variables to 1 and the first of free variables to 0 and solves for the 1st variable again.  s<sub>2</sub> = np.array( [ -3, 0, 1] )  Both lie in the plane x + 2y + 3z = 0 and form a basis for the null space.  So whatever solution you arrive at for a selected b: x + 2y + 3z = b = 5 can be solved with (0, 1, 1) if you add either of the null space vectors to it, the solution stands (0,1,1) + either or both (-2,1,0) + (-3,0,1) then the solution Ax=5 still holds since those 2 null space basis vectors into x + 2y + 3z yield no change to b.

How to find null space.  Arbitrarily we assume the first column vector contains the pivot.  So we assume the first component of x is not free.  Then choose 1 for one of the free variables, 0 for the other free variables and solve for the x associated with the pivot. 

pvots and rank

max pivots = m that determine vector space

max variables = n that determines object and its solution

dimension in null space = at least n - m and maybe more if m > r  

free variables = n - m or more really = max variables n - max pivots r < m  
so dimension of null space > n - m if pivots < m

rank = number of pivots with max = number of rows m

pivots = max m rows  
= not in zero rows  
= not in identical columns or rows

null space = n - r = number of free variables = number of special solutions

if n=r then invertible because null space = 0

special solutions show how free columns are combinations of pivot columns.

null space arrived via elimination.  just set Ux = 0 and solve for x.

if overspecified m > n but n = r then null space is also Z.  This is because extra rows do not expand x dimensions beyond r since x dimensions are set by n not m.

null spaces does not change as move from A to U to R = reduced row echelon form where 1s are on diagonal and zeros are above and below. rref simply makes easier to see the pivot and free variables.   

Example:

A = np.array( [ [ 1, 2, 2, 4 ], [ 3, 8, 6, 16 ] ] )

U = np.array( [ [ 1, 2, 2, 4 ], [ 0, 2, 0, 4 ] ] )

R = np.array( [ [ 1, 0, 2, 0 ], [ 0, 1, 0, 2 ] ] )

m = 2, n = 4, r = 2, s = 2 = free solutions = null space dimension

set x components for one free variable to 1 and pivot to that free variable's coefficent negative value.  then do the other free variables in the same way. 

rank of matrix = number of pivots

Null space ia subspace of R<sup>n</sup>  

(0,0,0) is not mentioned as a null solution because the zero vector is always in every subspace (its a requirement to be a subspace.)

An invertible matrix has no free variables.TF  An invertible square matrix has no free variables.  Wonder why put square in the answer since I dont think you can invert a rectangular matrix. Seems invertible and square are redundant.  

https://en.wikipedia.org/wiki/Invertible_matrix
Answer: A square matrix that is not invertible is called singular or degenerate. A square matrix is singular if and only if its determinant is zero. ... Non-square matrices (m-by-n matrices for which m ≠ n) do not have an inverse. However, in some cases such a matrix may have a left inverse or right inverse.   If A is m-by-n and the rank of A is equal to n (n ≤ m), then A has a left inverse, an n-by-m matrix B such that BA = I<sub>n</sub>. If A has rank m (m ≤ n), then it has a right inverse, an n-by-m matrix B such that AB = I<sub>m</sub>.

A good way to see null solutions and what they provide in terms of solutions to a series of equations. The plan x - 3y -z = 12 is parallel to [the plane] x - 3y - z = 0.  One particular p solution on this plane is found (12, 0, 0).  All points on the plane have form combining the one particular solution and 2 special solutions: (x,y,z) = p1(1,0,0) + s1(3,1,0) + s2(1,0,1).

if A is an m x n matric with r = 1 then its columns are multipls of one column and its rows are multples of one row. C(A) is a line in R<sup>m</sup>.  The null space matrix N has a shape of a [hyper]plane in R<sup>n</sup>.  The null space matrix is n x (n-1) with n-1 special solutions whcih makes sense since there are n-1 free variables when r = 1 (1 pivot) =.  Null space is all x --> Ax=0. The column space of A<sup>T</sup> is a line. 

Elimination: the big picture

To eliminate at vector level and subspace level when A --> R start wth 1st pivot and move L-->R column at a time T-->B row at a time, answering 2 questions

1. Is this column a combination of previous columns?  If column contains a pivot then the answer is no.  Pivot columns are independent of previous columns.  If col 4 has no pivot it is a combination of columns 123.

2. Is this row a combination of previous rows?  If the row contains a pivot then the answer is no.  Pivot rows are independent of previous rows.  If rows 3 ends up with no pivot it is a zero row ans is moved to the bottom of R.

THen thats A --> U via T-->B.  Next B-->T takes us U-->R.

U tells us which columns are combinations of earlier columns (pivots missing).  Then R tells us what those combinations are: tells us the special solutions to Ax=0.  R reveals the 'basis' for 3 fundamental spaces.  

Column space of A = choose the pivot columns of A as basis.

Row space of A - choose the non-zero rows of R as basis.

The null space of A - choose special solutions to Rx = 0 (and same as Ax = 0)

When A is square and invertible R = I. and E = A<sup>-1</sup>.

We learn most important number from elimination: Rank.

Rank counts pivot columns and pivot rows.  Then n-r count free columns and special solutions.  Reducing AI to RE tells you even more about A in EA=R.  E keeps a record of eliminations A-->R.

section 3.3

Principles

1. the complete solution to Ax=b

x 
= (one particular solution x<sub>p</sub>)  
+ (any x<sub>n</sub> in null space as special solution)

2. elimination on [Ab] leads to [Rd] then Ax=b is equivalent to Rx=d

3. Ax=b and Rx=d are solvable only when all zeros rows of R have zeros rows in d.

4. when Rx=d is solvable one very particular solution x<sub>p</sub> has all free variables equal to zero.

5. A has full column rank r=n when its nullspace N(A) = zero vector: no free variables.

6. A has full row rank r=m when its column space C(A) is R<sup>m</sup>: Ax=b is always solvable.

7. the 4 cases are / the augmented [ R ] matrix is

r=m=n so that A is invertible   [ I ]  
r=m<n so that every Ax=b is solvable (with infinite solutions?)  [ I F ]   
r=n<m where Ax=b has one or zero solutions  
[ I  ]   
[ 0 ]  
r<m and r<n where zero or infinite solutions are possible.  
[ I F ]
[ 0 0 ]   

Last section solved Ax=0  
Elimination converted Ax=0 --> Rx=0  
Free variables given 0 or 1 special values  
Pivot variables found via back substitution  
RHS was easy - always zero no matter what we did to LHS
The solution x was in the null space of A

Now treat b ≠ 0.  Ax=b reduces to Rx=d and look for 0=0 in that reduction.  Generally if a row of Rx=d ends up 0=0, then one or more b's are a combination of the other b's: b<sub>1</sub> +  b<sub>2</sub> = b<sub>3</sub>  

Review

1. the rank r is th number of pivots

2. the matrix R has m-r zero rows  

3. Ax=b is solvable if and only if the last m-r rows / equations reduce to 0=0

4. One particular solution x<sub>p</sub>  has all free variables = 0

5. the pivot variables are determined after the free variables are chosen

6. full column rank r = n means no free variables: one or no solution

7. full row rank r=m meanns solution if m=n or infinite if m<n


Using sympy to find particular and 2 special solutions and show the left null space

Every column of A above is perpendicular to y = np.array([2,1,-1]) which means that if you combine 2 of row 1 with 1 of row 2 with -1 of row 3 you get zeros.  This is the left null space of A.  A<sup>T</sup> y = np.array([0,0,0,0,0]])

<img width="864" alt="image" src="https://user-images.githubusercontent.com/38410965/105609683-e555db80-5d78-11eb-879f-31e39e4986ea.png">

if not provided with the b, and want to know what b's are valid, then set solve Ab to Rd and the d will be a linear combination of the b's.  This linear combination will show you the surface of solutions possible in terms of b1 b2 b3 etc.

b combinations in the row filled with all zeros show the combinations of rows that are valid for solution. shows the conditions for b's to fit into column space. 

full column rank when r = n  
full row rank when r = m  

section 3.4

principles

The independent columns of A: the only solution to Ax = 0 is x = 0 and null space = Z.  

Independent vectors: Th eonly zero combination c<sub>1</sub>v<sub>1</sub> + c<sub>k</sub>v<sub>k</sub> = 0 has all c's = 0.

A matrix with m<n has dependent columns.  At least n-m free variables / special solutions

The vectors v<sub>1</sub> ... v<sub>k</sub> span the space S if S = all comninations of the v's.

The vectors v<sub>1</sub> ... v<sub>k</sub> are a basis for S if they are independent and they span S.

The dimension of a space S is the number of vectors in every basis for S.

If A is 4x4 and invertible then its columns are a basis for R<sup>4</sup>. The dimension of R<sup>4</sup> is 4.

Independent vectors ... no extra vectors

Spanning a space ... enough vectors to produce the rest

Basis for a space ... not too many or too few

Dimension of a space ... the number of vectors in a basis

Linear independence  
The columns of  are linearly independent when the only solution to Ax = 0 is x = 0.  No other combination of the columns gives this zero vector Z.  
If you can go out on one vector and get back to the zero vector(s), orgin, via another vector, then your path out is some combination of your path home.  If you can do that without the zero vector, the members of your collection of vectors is not independent.   

Correct: A sequence of vectors is linearly independent.  
OK: The vectors (i.e. without sequence) are independent.
Wrong: The matrix is independent.  

In RR<sup>2</sup> any 3 or more vectors are dependent.  

Columns of a matrix are dependent exactly when there is a non-zero vector in the null space.  

Any vector and the zero vector are dependent since any non zero vector times the zero vector is zero vector.  

Dependent columns imply dependent rows if m=n.

Full column rank means the columns are independent.  

In a dependent sequence of vectors or in a matrix containing dependent vectors, we do not one way or one vector that causes dependence.

Span

The column space is all combinations of the columns is spanned by the columns.  A set of vectors (columns) spans a space if their linear combination fills the space.  

The columsn of a matrix span its columns space.  They might be dependent.  For example np.array([1,1]) and np.array([-1,-1]) are surely dependent, but they span a line in RR<sup>2</sup>.  


Row space = the subspace of RR<sup>n</sup> spanned by the rows.  
Columns span column space  
Row space is the combination of rows.  
The row space of A = C(A<sup>T</sup>) = column space of A<sup>T</sup>  

The rows are vectors in R<sup>n</sup> or would be in R<sup>n</sup> if they are written as column vectors which happens when the matrix is transposed to e.g. A<sup>T</sup>


Example: A = np.array( [ [ 1, 4 ], [ 2, 7 ], [ 3, 5 ] ] ) and A<sup>T</sup> = np.array( [ [ 1, 2, 3 ], [ 4, 7, 5 ] ] )
The column space of A is the plane (2d) in R<sup>3</sup> space that is spanned by the columns of A.  The row space is all of R<sup>2</sup> that is spanned by the three rows of A.  The rows are oin R<sup>n</sup> spanning the row space.  The columns are in R<sup>m</sup> spanning the column space. 

2 vectors cannot span all of R<sup>3</sup> even if theyre independent.  
4 vectors cannot be independent in R<sup>3</sup> even if they span all of R<sup>3</sup>.

We want enough vectors to span space but not more thna enough becuse we waqnt the vectors to be independent.

A basis for a vector space is a sequence of vectors with 2 properties: the basis vectors are linearly independent and they span the space.  This combination of properties is fundamental to LA.

Every vector v in the space is a combination of the basis vectors becaaue they span the space.  The combination of basis vectors that produces vector v is unique because basis vectors v<sub>1</sub> ... v<sub>n</sub> are independent.

There is one and only one way to write v as a combination of basis vectors.

Columns of I produce the standard basis for any R<sup>n</sup>.

The columns of ANY and EVERY invertible n x n matrix give a basis for R<sup>n</sup>.

R<sup>n</sup> has infinity many different bases.

The pivot columns (rows) of A (A<sup>T</sup>) are a basis for the column (row) space.

A and R share the same row space but not necessarily the same column space.
[think this is because A is modified via elimination which doesnt change the relative weighting of row components but does change the relative weighting of column components.

Find the basis for the space that matrix vectors span by elimination to Rd.
The pivots of A columns are a basis for its column space.  The pivot rows of A are a basis for its row space as are the rows of R.

Dimension of a space is the number of vectors in every basis.

Good example of how dimension of a sole vector is one in R<sup>3</sup> while its null space dimension is 2 and they add to the space's dimension 3.
The line through np.array( [1,5,2] ) has dimension one.  It is a subspace with this one vector in its basis.  Perpendicular to v = (1,5,2) is the plan x + 5y + 2z = 0.  This plane has dimension of 2.  To prove that, find a basis in vectors (5,1,0) and (-2,0,1) to solve the equation.  

Special solutions always give the dimension for the null space of a matrix, such as the matrix A above np.array( [ 1, 5, 2] ). 

Never say the rank of a space or the dimension of  basis or the basis of a matrix.  Dimension of the column space.  The rank of a matrix.  These are correct. 

Defined dimension of a space is the number of vectors in every basis.  v = np.array( [ 1, 5, 2 ] ) has dim 1 and 1x<sub>1</sub> + 5x<sub>2</sub> + 2x<sub>3</sub> = 0 has dim 2.

Matrix spaces for the space of M

Vector space M contains all 2x2 matrices. Its dimension is 4:

A<sub>1</sub> = np.array( [ [ 1, 0], [0, 0] ] )  
A<sub>2</sub> = np.array( [ [ 0, 1], [0, 0] ] )  
A<sub>3</sub> = np.array( [ [ 0, 0], [0, 1] ] )  
A<sub>4</sub> = np.array( [ [ 0, 0], [1, 0] ] )  

A linear combinations of these 4 can create any 2x2 matrix and so it spans the space.
Only a linear combination where all c's are zero creates the zero matrix. So the matrices are linearly independent. 

c<sub>1</sub>A<sub>1</sub> + c<sub>2</sub>A<sub>2</sub> + c<sub>3</sub>A<sub>3</sub> + <sub>4</sub>A<sub>4</sub>

c<sub>1</sub>A<sub>1</sub> + c<sub>2</sub>A<sub>2</sub> + c<sub>3</sub>A<sub>3</sub> are a basis for all upper triangular matrices which as subspace has dimension 3

c<sub>1</sub>A<sub>1</sub> + c<sub>3</sub>A<sub>3</sub> are a basis for all diagonal matrices which as subspace has dimension 2

c<sub>1</sub>A<sub>1</sub> + c<sub>2</sub>A<sub>2</sub> and c<sub>3</sub>A<sub>3</sub> + <sub>4</sub>A<sub>4</sub> are a basis for all symmetric matrices who dimension is 2 or 4?

The space of al n x n matrices has a basis in single non-zero entries matrices.  There are n<sup>2</sup> positions for that entry; so there are n<sup>2</sup> basis matrices.

The dimension for the whole n x n matric space is n<sup>2</sup>.  The dimension for the subspace of upper triangular matrices is 0.5*n<sup>2</sup> + 0.5*n

Function spaces

d<sup>2</sup>y/dx<sup>2</sup> = y'' = 0 is solved by any linear function y = cx + d  

d<sup>2</sup>y/dx<sup>2</sup> = y'' = -y is solved by any combination of y = c*sinx + d*cosx  

d<sup>2</sup>y/dx<sup>2</sup> = y'' = y is solved by any combination of y = c*e<sup>x</sup> + d*e<sup>-x</sup>  

d<sup>2</sup>y/dx<sup>2</sup> = y'' = 2 doesnt form a subspace:  
a particular solution is y(x) = x<sup>2</sup>.  A complete solution is however y(x) = x<sup>2</sup> + cx + d since all those functions satisfy y'' = 2.  Notice that the particular function + any function c*x+d [is column space +] null space.  A linear differential equation is like a linear matrix equation except it is solved by calculus instead of linear algebra. 

The space Z that contains only the zero vector has dimension zero.  The empty set containing no vectors is a basis for Z.  We can never let the zero vector into a basis because then linear independence is lost. 

Example
v<sub>1</sub> =  (1,2,0) and v<sub>2</sub> = (2,3,0)   
Are they linearly independent? v<sub>1</sub> and v<sub>2</sub> are linearly independent: the only combination to give Z is 0*v<sub>1</sub> + 0*v<sub>2</sub> as shown by moving from A = np.array( [ [ 1, 2 ] , [ 2, 3 ], [0, 0] ] ) to R = np.array( [ [ 1, 0 ], [ 0, 1 ], [ 0, 0 ] ] )

Are v<sub>1</sub> and v<sub>2</sub> a basis for any space?  Yes they are a bsis for the space they span.

Which space V for they span?  The space V contains all vectors (x,y,0).  It is the xy plane in R<sup>3</sup>.

What is the dimension of V?  The dimension of V is 2 since the basis contains 2 vectors.

Which matrices A have V as their column space?  This matrix V is the column space of any 3 x n matrix of rank 2 if every column is a combination of v<sub>1</sub> and v<sub>2</sub>.

Which matrices have V as their null space.  This V is null space of any m x 3 matrix B of rank 1 if every row is a mulitple of (0,0,1).  In particular, take B = np.transpose(np.array( [ 0, 0, 1] ) ).  Then Bv<sub>1</sub> = Bv<sub>2</sub> = 0

Describe all vectors v<sub>3</sub> that complete a basis v<sub>1</sub>, v<sub>2</sub>,v<sub>3</sub> for R<sup>3</sup>.  Any 3rd vector v<sub>3</sub> = (a.b,c) will complete a bsis for R<sup>3</sup> provided c is not = 0 [ because any vector would --> R = I ]

Change of basis matrix B is 

np.transpose(np.arrray([v<sub>1</sub>,v<sub>2</sub>,v<sub>3</sub>])) = np.transpose(np.arrray([w<sub>1</sub>,w<sub>2</sub>,w<sub>3</sub>])) B

where V is 1 x 3 and W is 1 x 3 and B is 3 x 3

Independent v's come from independent w's when B is invertible and if these vectors v and w are in R<sup>3</sup> then they are not only independent, but they are a basis for R<sup>3</sup>.  [We obtain an R<sup>n</sup>] basis of v's from basis of w's when the change of basis matrix B is invertible.

This is true v = Aw or v = wB.  If A or B are invertible then if w is a basis for R<sup>3</sup> then so is v. 

A square triangular matrix has indpendent columns when its diagonal has no zeros.

TF if zero vector is in the row space, the rows are dependent.  F if only zero in the null space then independent. Zero vector is always in the row space. 

v+w and v-w are combinations of v and w.  wirte v and w as combinations of v+w and v-w.

v = 0.5 (v+w) + .5 (v-w)

w = 0.5 (v+w) - .5 (v-w)

the 2 pairs of vectors v+w and v-w span the space because they can be combined to make the same things.  They are a basis when they are independent. 

The columns of every invertible n x n matrix give a basis for R<sup>n</sup> because all columns will be indpendent.

By definition a matrix is commutative with its inverse on multiplication: A<sup>-1</sup>A = AA<sup>-1</sup>= I   
A and A<sup>-1</sup> must be square.  

If the columns of A are vectors from R<sup>m</sup> and linearly independent, then:  
the rank of A is r = n since n independent columns have rank r = n  
If they are a basis for R<sup>m</sup> then the columns span R<sup>m</sup> and rank m = n.  [If n>m then cannot be a basis for R<sup>m</sup> since too many for a basis.]
The rank counts the number of independent columns. 


As shown earlier a basis for the plane x-2y+3z=0 in R<sup>3</sup> are the vectors of special solutions.

A basis gives exactly one solution for every b. Because a basis contains independent b's.  


Example: Find all functions that satisfy y' = 0  
y(x) = constant c  
Choose a particular function that satisfies y' = 3  
y(x) = 3x 
Find all functions that satisfy y' = 3
y(x) = 3x + c = x<sub>p</sub> + x<sub>n</sub>  


Suppose y<sub>1</sub>(x), y<sub>2</sub>(x), y<sub>3</sub>(x) are 3 different functions of x. The vector space they span could have dimension 1, 2 or 3.  Show examples of vectors for each dimension.

function  y<sub>1</sub> , y<sub>2</sub> , y<sub>3</sub>  
dim = 1: x  2x  3x
dim=2:  x  2x  x<sup>2</sup>
dim=3:  x x<sup>2</sup>  x<sup>3</sup>   

so e.g. 2x, 2x, x<sup>2</sup> is 2 dim because its null space contains 1 dimension (1,-1,0)

Find a basis for space of polynomials with degree 3:  y = 1, y=x, y=x<sup>2</sup>, y=x<sup>3</sup>


Suppose A is a 5x4 matric with rank 4. Show how Ax=b no solution when the 5x5 augmented matrix [A b] is invertible.  Answer is that if [A b] is the 5x5 identity matrix then the last row is 4 zeros and 1 one which is unsolvable since LHS not = RHS. "If the 5x5 [A b] is invertible then b is not a combination of the columns of A and so Ax=b cannot be solved" [since x is the factor that combines As columns to make b].

section 3.5

cheat sheet  
subspaces of vector spaces are C(A) and N(A<sup>T</sup>) for R<sup>m</sup> and N(A) and C(A<sup>T</sup>) for  R<sup>n</sup>  
rank of matrix = number of pivots = r  
dimensions of sub spaces = number of basis vectors = r for = C(A) and C(A<sup>T</sup>), n-r for N(A) and m-r for N(A<sup>T</sup>)   
bases vectors for spaces = pivots = independences  
basis vectors span the sub spaces and vector spaces

Principles

1. the column space C(A) and row space C(A<sup>T</sup>) both have dimension r = the rank of A

2. the null space N(A) has dimension n-r  
the left null space N(A<sup>T</sup>) has dimension m-r  

3. Elimination produces bases for the row space and null space of A.  The bases for these two spaces of A are the the same as for R.

4. Elimination often changes the column space and left null space so that bases for A, C(A) and N(A<sup>T</sup>), are not the same as for R.  Dimensions dont change from A to R. 

5. Rank one matrices A = u•v<sup>T</sup> = column times row: C(A) has basis u and C(A<sup>T</sup>) has basis in v.

Main theorem connects rank with dimension. Rank of matrix = number of pivots.  Dimension of subspace = number of vectors in basis.  We count pivots or we count basis vectors. 

The rank of A reveals the dimensions of all for fundamental subspaces:

1. row space = C(A<sup>T</sup>) = subspace of R<sup>n</sup>

2. column space = C(A) = subspace of R<sup>m</sup>

3. null space = N(A) = subspace of R<sup>n</sup>

4. left null space = N(A<sup>T</sup>) = subspace of R<sup>m</sup>

2 subspaces come from A and 2 from A<sup>T</sup>

column space is an R<sup>m</sup> subspace = combination of r of n columns of A

null space is an R<sup>n</sup> subspace = combination of n-r of n columns of A 

row space is an R<sup>n</sup> subspace = combination of r of m rows of A

left null space is an R<sup>m</sup> subspace = combination of m-r of m rows of .

Any of the above subspaces of R<sup>m</sup> change as elimination moves from A to R because multipliers and add subtraction change the ratio of rows fonud in columns.

Row space contains all combinations of all rows of A. Row space of A is column space of A<sup>T</sup>

Null space solves Ax = 0  
Left null space solves A<sup>T</sup>y = 0 and is the null space of A<sup>T</sup>  
y<sup>T</sup>A = 0<sup>T</sup> represents the same mathematics as A<sup>T</sup>y = 0  


Part 1 of Fundamental Theorem  
row space and column space have same dimension r
r is rank of matrix  
null space and left null space make up the full n and m left over after r is counted  

Part 2 of Fundamental Theorem
row space combines the essential rows of A but only r of m add new information  
row space is dimensioned by the essential columns of A = r of n  
the non zero rows of R form a basis and are linearly independent  
column space combines essential columns of A = r of n  
column space is dimensioned by the essential rows of m  
the pivot columns form a basis and are linearly independent  
null space combines the free columns of A = n-r of n  
null space is dimensioned by the free columns of A = n-r of n  
the special solutions form a basis for null space and are linearly independent  
left null space combinese the free rows of A = m-r of m  
left null space is dimensioned by the free rows of A = m-r of m  

Find 4 subspaces by eliminating/reducing to R echelon form and finding a basis for each subspace.

A has same dimension r as R  
A has same basis as R  
Same because every row of A is a combination of the rows of R  
Same because every row of R is a combination of the rows of A  
Elimination changes rows but not row spaces

Rank theorem: the number of independent columns = the number of independent rows.  
A and R do not have the same column space.   
The columns of R often end in zeros.
The columns of A dont often end in zeros.
C(A) not = C(R)  
but the same combination of the columns are zero. So N(A) = N(R)?
Dependent columns in A are dependent columns in R.  Independent in A are independent in R.  


Rank 2 matrices = Rank 1 + Rank 1

A    
1 0 3    
1 1 7    
4 2 20    

C  
1 0 0  
1 1 0  
4 2 1  

R  
1 0 3   
0 1 4   
0 0 0     

A = CR  

R = rref(A)  Some elimination matrix E simplifies A to EA = R.  Then the inverse matrix C = E<sup>-1</sup> converts R back to A = CR.  

<img width="864" alt="image" src="https://user-images.githubusercontent.com/38410965/105750107-48c74100-5f12-11eb-8caf-75055208920c.png">

Row space of R clearly has 2 bsais vectors v<sub>1</sub><sup>T</sup> = [1 0 3] and v<sub>2</sub><sup>T</sup> = [0 1 4]. So the **same** row space of A has this basis and row rank is 2.  Multiplying C times R says that row 3 of A = 
A =  4v<sub>1</sub><sup>T</sup> + 2v<sub>2</sub><sup>T = [4 2 1]  
Now look at columns.  Pivot columns of R are clearly (1,0,0) and (0,1,0).  [Free to combine those columns Rx=0 would solution would be s1=(-3,-4,1).]  Pivot columns of A are also in columns 1 and 2,  u<sub>1</sub> = (1,1,4) and u<sub>2</sub> = (0,1,2). Notice that C has those same columns.  That is guaranteed to happen since C first 2 columns are multiplying [being weighted by in columnar matrix multiplication] the first 2 columns of R that are always an identity matrix.  R pivot columns wont change the same columns of C when making same first two columns of A. 
Those pivot columns in A and C are both always u<sub>1</sub> and u<sub>2</sub> [when viewing an A=CR decomposition/factoring].  

When you put letters v and u in for columns and rows, you see rank 2 = rank 1 + rank 1.

Matric A (rank 2) =   
A =   
[u<sub>1</sub> u<sub>2</sub> u<sub>3</sub>]   
times   
[v<sub>1</sub><sup>T</sup>  
 v<sub>2</sub><sup>T</sup>  
 zero row]  
= u<sub>1</sub>v<sub>1</sub><sup>T</sup> + u<sub>2</sub>v<sub>2</sub><sup>T</sup>  
= rank 1 + rank 1  

So multiplying matrices using columns x rows.  u<sub>2</sub> drops out when that column is multiplied by the zero row.  [In column x row matrix multiplication c1 x r1 + c2 x r2 + c3 x r3 remember is most useful form.]

Every rank r matrix is the sum of r rank one matrices.  Pivot columns of A times non-zero rows of R.  The (0,0,0) row of $ disappears.  The pivot columns u<sub>1</sub> and u<sub>2</sub> are a basis for the column space of A.  {not R}


Interesting problems:

If the row space = column space then A<sup>T</sup> = A.  False. A can be invertible and unsymmetric even if C( A<sup>T</sup>) = C(A). Pick any invertible matrix m x m then the row and column spaces are the entire of Rm.  But many invertible matrices exist such that A not = At.

Construct A = uv<sup>T</sup> + wz<sup>T</sup> whose C(A) has basis in (1,2,4) and (2,2,1) and R(A) = C(A<sup>T<?sup>) has basis in (1,0) and (1,1).  Write A as 3x2 times 2x2.

u and w span the column space of A  
v and z span the row space of A   

<img width="864" alt="image" src="https://user-images.githubusercontent.com/38410965/105745866-bec8a980-5f0c-11eb-8239-0c9d668db8eb.png">


How do you know from these shapes that A cannot be invertible?  The rank of a 3x2 times a 2x3 cannot be be larger than the rank of either factor.  So rank <=2 and the resulting 3x3 matrix is non invertible with rank <=2.


