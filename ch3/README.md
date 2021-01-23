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


Using sympy


<img width="864" alt="image" src="https://user-images.githubusercontent.com/38410965/105608588-cdc72480-5d71-11eb-8d62-a262ee6bbdc2.png">
