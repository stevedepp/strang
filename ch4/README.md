ch4

[yellow notes start with "this chapter is a bitch" and it is!]

section 4.1  
orthogonality of the 4 subspaces  

principles

orthogonal vectors have v<sup>T</sup>w = 0.
then ||v||<sup>2</sup> + ||w||<sup>2</sup> = ||v+w||<sup>2</sup> = ||v-w||<sup>2</sup>

v<sup>T</sup>v = v•v = ||v||<sup>2</sup> = v<sub>1</sub><sup>2</sup> + v<sub>2</sub><sup>2</sup> + v<sub>3</sub><sup>2</sup>

subspaces V and W are orthogonal when v<sup>T</sup>w = 0 for every v in V and every w in W.

the row space of A with dimension r columns is orthogonal to the null space of of A with dimension n-r columns.  
the column space of A with dimension m rows is orthogonal to the left null space of A with m-r dimension columns.

one pair of dimensions adds to r + (n-r) = n and the other pair of dimensions add to r + (m-r) = m

row space and bull space are orthogonal complements: every x in R<sup>n</sup> splits into x<sub>r</sub> + x<sub>null</sub>. 

suppose a space S has dimension d. then every basis for S consists of d vectors.

if d vectors in S are independent, they span S.  if d vectors span S, they are independent. 

2 vectors are orthogonal when their dot product = 0 = v • w = v<sup>T</sup>w

now do the same with orthogonal subspaces, orthogonal bases, othogonal matrices.

orthogonal vectors 

v<sup>T</sup>w = ||v||<sup>2</sup> + ||w||<sup>2</sup> = ||v+w||<sup>2</sup> = length<sup>2</sup> = (v+w)•(v+w) = (v+w)<sup>T</sup>(v+w) 

because length = ||v|| = (v•v)<sup>0.5</sup> = (v<sup>T</sup>v)<sup>0.5</sup>

and when v<sup>T</sup>w = 0 that product falls out of ||v+w||<sup>2</sup> to leave ||v||<sup>2</sup> + ||w||<sup>2</sup> as shown here:

(v+w)<sup>T</sup>(v+w) = v<sup>T</sup>v + w<sup>T</sup>v + v<sup>T</sup>w + w<sup>T</sup>w = v<sup>T</sup>v + zero + zero + w<sup>T</sup>w = v•v + w•w = ((v•v)<sup>0.5</sup>)<sup>2</sup> + ((w•w)<sup>0.5</sup>)<sup>2</sup> = length<sub>v</sub><sup>2</sup> + length<sub>w</sub><sup>2</sup> = ||v||<sup>2</sup> + ||w||<sup>2</sup> = (v<sub>1</sub>, v<sub>2</sub>, v<sub>3</sub>).T x (v<sub>1</sub>, v<sub>2</sub>, v<sub>3</sub>) + (w<sub>1</sub>, w<sub>2</sub>, w<sub>3</sub>).T x (w<sub>1</sub>, w<sub>2</sub>, w<sub>3</sub>)

4 subspaces are what a matrix does.  
Ax can be seen as:  
only numbers  
combination of column vectors  
4 subspaces  

row space of A is perpendicular to null space of A  
every row r of A is perpendicular to every n-r solution to Ax=0  
column space of A is perpendicular to null space of A<sup>T</sup>  
when b is outside the column space of A  
when we want to solve Ax = b but canot  
then this null space of A<sup>T</sup> is important.  
null space of A<sup>T</sup> contains the error = b - Ax in least squares.

Part 1 of fundamental theorem gives subspace dimensions, r for row and column spaces and n-r and m-r for the two null spaces.   

Now show row space C(A<sup>T</sup>) and null space N(A) are orthogonal subspaces inside of R<sup>n</sup>  


Definition   
2 subspaces V and W of vector space R are orthogonal if every vector v in V is perpendicular to every vector w in W.  
v<sup>T</sup>w = 0 for all v in V and all w in W  

example: 2d floor of room is subspace V in R<sup>3</sup>.  the 1d line where 2 walls meet is a subspace W.  Those 2 subspaces are orthogonal: the 2d infinite floor and 1d line at the corner of walls are orthogonal subspaces.   Every vector up the meeting line of the walls is perpendicular to every vector in the floor.  [the line between walls might be r and the floor might be n-r in R<sup>n</sup> with n = 3]

example: 2 walls look perpendicular and are, but the 2 subspaces are not orthogonal since not every vector in one wall is perpendicular to every other vector in the other wall.  Best example of this vector is the one that is the line where the walls meet.  That vector or meeting line is in both V and W.  If that line is in each space V wall and W wall then it must be perpendicular to itself and it isnt. 

Also in that second example, the 2 planes that make up the 2 walls are both dimension 2 = 2 + 2 in R<sup>3</sup> and so cannot be orthogonal subspaces.  When a vector is in 2 orthogonal subspaces, its product must be zero: v<sup>T</sup>w = 0 and the only way a vector in 2 different orthogonal subspaces can be zero is if it is the zero vector.  

Orthogonality is impossible when dim V<sup>subspace</sup> + dim W<sup>subspace</sup> > R<sup>space</sup>

Side lesson  
if there are surplus columns n-r, then those surplus columns are combinations of the pivot columns.  pivot columns form the basis for column space.  setting n-r free columns coefficients = 1 in each of n-r special solutions and the other n-r-1 free columns to zero shows how each free column is a combination of the pivot columns, ie forces us to find the pivot column coefficients that offset the one n-r free column with a 1 coefficient. do this n-r times and get n-r free solutions which supplement the one particular solution that combines the basis columns of col space.  

special solutions combine one free column and all column space basis columns and result in coefficients that are a basis for null space.

since each special solution vector has one 1 in it, the combination of special solutions or null space basis vectors is independent since it forms an I formation in the free columns.  

each special solution combines the r pivot columns to equal one of the n-r free columns but since the signs are reversed on pivot columns, the special solution / null space basis vectors are (-r<sub>1</sub>, r<sub>2</sub>, <sub>3</sub>, f<sub>1</sup>, f<sub>2</sub>) where only one of the free is 1 nd some combo of the pivot columns is chosen to make Z.

Every vector in x in the null space is perpendicular to every row vector in A because Ax = 0.  The null space N(A) and the row space C(A<sup>T</sup>) are orthogonal subspaces of and in R<sup>n</sup>.  

Each row is perpendicular to x in null space.  Thus x is perpendicular to every combination of rows which is the whole row space C(A<sup>T</sup>)

2nd proof of orthogonality uses matrix shorthand.  The vectors in row space are combinations A<sup>T</sup>y of the rows.  [C(A<sup>T</sup>] = A<sup>T</sup>y for all y.]  Take the dot product of A<sup>T</sup>y with any x in null space.  These vectors are perpendicular and so the dot product is zero. 

x<sup>T</sup>(A<sup>T</sup>y) = (Ax)<sup>T</sup>y = 0<sup>T</sup>y = Z

Now for column space:  

column space of A and null space of A<sup>T</sup> are always orthogonal subspaces.

every vector y in the null space of A<sup>T</sup> is perpendicular to every column of A. 

the left null space N(A<sup>T</sup>) and columns space C(A) are orthogonal in R<sub>m</sub>

Orthogonal components  
the fundamental sub spaces are more than just orthogonal in pairs.  their dimensions are right.  2 lines could be perpendicular in R<sup>3</sup>, but those line could not be the row space and null space of a 3x3 matrix.  The lines have dimensions 1 and 1 and add to 2 but the correct dimensions in a 3x3 matrix must add to 3, either dim 2 plane and dim 1 line or dim 1 line and dim 2 plane or dim 3 object and dim zero null space. Those pairs are not only orthogonal but they are also orthogonal complements. 

definition: orthogonal complement of a subspace V contains every vector that is perpendicular to V.  This subspace is denoted by V with a perpendicular superscript and pronounced "v perp".  so the null space is the orthogonal complement of the row space.  

reverse also true : if v is orthogonal to the null space, then it must already be in the row space.  otherwise [think <--this is the wrong word] we could add this v as this extra row to the matrix without changing the null space.  the row space wuold grow by 1 which breaks law of r + (n-r) = n.  We conclude that the null space complements N(A) perp is exactly the row space C(A<sup>T</sup>)

Fundamental Theorem of LA part 2  
N(A) is the orthogonal complement of the row space C(A<sup>T</sup>) in R<sup>n</sup>  
N(A<sup>T</sup>) is the orthogonal complement of the column space C(A) in R<sup>m</sup>  

part 1 gave dimensions of subspaces.  
part 2 gives 90 degree angles between subspaces.  
the point of complements is that every x can be split into a row space component x<sub>r</sub>and a null space component x<sub>n</sub>.

When A multiplies x = x<sub>r</sub> + x<sub>n</sub> = Ax = Ax<sub>r</sub> + Ax<sub>n</sub> ...

... the null space component goes to zero Ax<sub>n</sub> = 0 and the row space component goes to the column space Ax<sub>r</sub> = Ax.

can do the same with A<sup>T</sup>y

there is an r x r invertible matrix inside A if throw out the 2 null spaces.  From the row space to the column space, A is invertible.  The pseudo inverse will invert that part of A in section 7.4.

Every matrix of rank r contains an r x r invertible matrix.  

in a 3 x 5 with a r = 2, the other 11 zeros are the null spaces.


<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/105800565-05e28900-5f65-11eb-867f-f2d36e55f7aa.png">

In a 3 x 5 with r = 2 the invertible matrix is found in the pivot columns and rows.  

every matrix can be diagonalized by selecting the right bases for for R<sup>n</sup> and R<sup>m</sup>   

A row of A cannot be in the null space except zero vector. The only vector in 2 orthogonal subspaces is the zero vector.

row space dimension is not equal to the number of rows but equal to the number of pivots in each row, how many components of rows pass information.  Null space is how many components do not transfer information.  

Combining Bases from Subspaces

independence and spanning:

basis is linearly independent vectors that span the space.

independent and span are properties

normally check both properties.

when the count is right, only one property is needed: one implies the other

any n independent vectors in R<sup>n</sup> must span R<sup>n</sup>; so they are a basis.

any n vectors that span R<sup>n</sup> must be independent; so they are a basis.

when vectors go into columns of n x n square matrix A facts are:

if the n columns are independent then they span R<sup>n</sup>: Ax=b is solvable

if the columns span R<sup>n</sup> then they are independent: Ax=b has only one solution.

uniqueness and existence properties imply one another:

if there are no free variables the solution exists and is unique; there must be n pivot columns and back substitution solves Ax=b 

if Ax=b can be solved for every b (i.e. if a solutions exist) then elimination produced no zeros, there are n pivots and no free variables, the null space contains only x = 0 and solutions are unique.

review
V and W subspaces are orthogonal if every v in V is orthogonal to every w in W

V and W are orthogonal complements if W contains all vectors perpendicular to V.  Inside R<sup>n</sup> the dimensions of complements V and W add to n

the null space N(A) and row space C(A<sup>T</sup>) are orthogonal complements with dimensions (n-r) + r = n  
the left null space N(A<sup>T</sup>) and column space C(A) are orthogonal complements with dimensions (m-r) + r = m.

any n independent vectors in R<sup>n</sup> span R<sup>n</sup>.  Any n spanning vectors are independent. 

generalizing the 2 walls meeting.  a p-dimensional subspace of R<sup>n</sup> and a q-dimensional subspace of R<sup>n</sup> share at least a line if p+q > n.  The p+q basis vectors of V and W cannot be independent; so some comnbinaion of the basis vectors of V is also a combination of the basis vectors of W. 

These spaces A and B cannot be orthogonal. A has dimension p = 2 and B has dimensions q = 2 so AB has dimensions p+q unless they share a dimension as revealed by sharing column space at the vector [5,6,5] = Ax = Bxhat.  So p+q > n.  We know p+q>n because p+q=4 and rref shows n = 3 and because they share a soluition. in column space.

The big point is that they are not orthogonal subspaces, which requries the vectors of AB to be independent and perpendicular.  They are not indpendent because there is a null soluion ABx = 0.  THis is same as floor V and wall W are not orthogonal subspaces because they share a non-zero vector along the line that they meet.  No plane V and W in R<sup>3</sup> can be orthogonal.  Ax = Bxhat means [AB](x,xhat).T = 0.Three homogenous equations always have a non zero solution 2 planes intersecting in R<sup>3</sup> must share a line.

<img width="745" alt="image" src="https://user-images.githubusercontent.com/38410965/105848394-e5d6b800-5fac-11eb-83dc-06de95636ad6.png">

If A is invertible, then column 1 of A<sup>-1</sup> is orthogonal to rows 2 and 3 of A as evidenced by the zeros in I(2,1) and I(3,1)


section 4.2  Projections

principles

the projection of a vector b onto the line a is the closes point p = a(a<sup>T</sup>b/a<sup>T</sup>a)

the error e = b - p is the perpendicular to a: right triangle bpe has ||p||<sup>2</sup> + ||e||<sup>2</sup> = ||b||<sup>2</sup>

the projection of b on to subspace S is the closest  vector p in S.  b-p is orthogonal to S.  [kind of like e]

A<sup>T</sup>A is invertible (and symmetric) only if A has independent columns: N(A<sup>T</sup>A) = N(A) [same as problem 4.1 #8]

the projection of b onto the column space of A is the vector p = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b

The projection matrix on to C(A) is ... 

P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>  

p = Pb

P<sup>2</sup> = P = P<sup>T</sup>

Projection matrices are symmetrix matrices with P<sup>2</sup> = P where the projection of b is Pb.

A projection onto a line comes from a rank one matrix and projection onto a plane comes from a rank 2 matrix.  Projection matrices match the rank of the destination subspace (line or plane in this case).

goal is to find the part p in each subspace and to find the projection matrix P that produces that part p = Pb.

every subspace of R<sup>m</sup> has its own m x m projection matrix. to compute P, obtain a description of the subspace upon which b is projected.  the best description of a subspace is a basis.  put the basis vectors into the columns of A and project b oto the column space of A.  

start with a projection onto a line.

a line through origin in direction of a = (a<sub>1</sub>, ... , a<sub>m</sub>).  
along the line find point p closest to b = (b<sub>1</sub>, ... , b<sub>m</sub>).  
the key to projection is orthogonality.  
the line from b to p is perpendicular to a.  it is e = b - p.  
[ in diagrams it is shown as a dotted line dropping from b to a, but since e = b - p, it is actually the line dropping from b - p to origin or said more correctly in my view, the vector from origin to b - p.  in this sense it might be easier to say you go out on b and then subtract e error to get to p along a.  b - p = e but more visually pleasing is b - e = p]
[ reality might be b and model might be x<sub>hat</sub> model that finds p along a a la x<sub>hat</sub>a and error from reality to model is b - p =  b - x<sub>hat</sub>a]

computing x<sub>hat</sub> gives us vector p. then from formular p = Pb, we read off the projection matrix P.  

error e is perpendicular to a.  this helps to determine x<sub>hat</sub>.  that b - x<sub>hat</sub>a = e is perpendicular to a means that the dot product of (b-x<sub>hat</sub>a) to a is zero.  

e =  b - p  = b - x<sub>hat</sub>a --> finding p

a • e = a • ( b - x<sub>hat</sub>a ) = 0 = a • b - x<sub>hat</sub>a • a = 0

thus x<sub>hat</sub> = (a • b) / (a • a) =  a<sup>T</sup>b / <sup>T</sup>a 

use the transpose formula rather than dot product formula since it leads to how matrices will be multiplied.

the projection of b onto th eline through a is  the vector p

p = x<sub>hat</sub>a

p = ( a<sup>T</sup>b / <sup>T</sup>a ) a

2 special cases:

if b = a then x<sub>hat</sub> = 1 : the projection of b = a onto a is a projection of a onto itself: Pa = a = ( a<sup>T</sup>a / <sup>T</sup>a ) a = 1a

if b is perpendicular to a then a<sup>T</sup>b = a • b = 0 and then ( a<sup>T</sup>b / <sup>T</sup>a ) a = 0 times a = p = 0

example: 

project b = (1,1,1) onto a = (1,2,2) to find p = x<sub>hat</sub>a  

solution: the number x<sub>hat</sub> is the ratio of a<sup>T</sup>b = 5 to a<sup>T</sup>a = 9

so the projection is p = x<sub>hat</sub>a = ( a<sup>T</sup>b / a<sup>T</sup>a ) a = (5/9) a

error vector = distance from b to p on a is e = b - p 

where e is perpendicular to a and since p is on a perpendicular to p too.

<img width="745" alt="image" src="https://user-images.githubusercontent.com/38410965/105938147-f9be0080-6024-11eb-9335-10ab9863a936.png">

cos theta of the angle b to a is = b • a / ||b|| ||a||

the vector b is split into 2 parts (similar to splitting any vector into its 2 axes).  There is a component along the line a which is p.  b' perpendicular part is e.  those 2 sides have length ||p|| = ||b|| cos theta = x and ||e|| = ||b|| sin theta = y.

so p = a<sup>T</sup>b / a<sup>T</sup>a has length = ||p|| = ( ||a|| ||b|| cos theta / ||a||<sup>2</sup> ) ||a|| = ||b|| cos theta after cancelling the ||a|| components of that formula. 

dot products are simpler than cos theta and ||b|| 

projection matrix is outer product / inner product

p = a x<sub>hat</sub> = a ( a<sup>T</sup>b / a<sup>T</sup>a ) = P b where P = aa<sup>T</sup> / a<sup>T</sup>a 

P is projection matrix with m x m but here its rank is one since it is a single column times a single row in the numerator outer product.  

the diagonal of P add to 1 because you are displacing 100% of b's weight onto the basis of a via P

finally, the matrix I - P should be a projection because it produces the other side of e near origin.  (I - P) b = b - p = e in left null space


<img width="745" alt="image" src="https://user-images.githubusercontent.com/38410965/105942950-3fcb9200-602e-11eb-96df-33ff85614270.png">


Next move from projecting onto a line to projecting onto an n-dimensional subspace of R<sup>m</sup> 

Projecting onto a subspace.

start with n vectors a<sub>a</sub>, ... , a<sub>n</sub> in R<sup>m</sup> [don't make mistake to think a<sub>j</sub> are components. they are n vector columns in R<sup>m</sup> space.]

assume these n a's are linearly independent (as they need be in a basis)

problem is: find combination [combinations if not independent] p = x.hat<sub>1</sub>a<sub>1</sub> + , ... , x.hat<sub>n</sub>a<sub>n</sub> closests to a given vector b  

projecting each [?] b in R<sub>m</sub> onto the subspace spanned by the a's
"[?]" may refer to an object b composed of many b's on RHS projected onto surface A with many a's on LHS ?

[application: what if value is p of object b shown onto perception a but we allow b to change and cast different projections over n infinitely brief times b<sub>1</sub>, ... , b<sub>n</sub> onto distinctly different minds that can only act at distinctly and infinitely brief time slots a<sub>1</sub>, ... , a<sub>n</sub> to create projections p<sub>1</sub>, ... , p<sub>n</sub>.  a's collect to A perceptions over landscape of minds.  b's collect to object B geography of true value over time.   p's collect to an X time-series weighted collection of a's.   key question: Can n times be dimensioned in the same R<sup>m</sup> space as n minds if allow x weights to have independent columns?
p = xa.  we dont care about b or a really.  we only want the true value b to cast its shadow on many minds a and reveal p price projection. but then we are left with m dimensional p price in n dimensional time / mind segments. ....]


[back to reality.  we have each b that may mean he wants to project B object onto A space]

with n = 1 one vector a<sub>1</sub>, this projects b onto a line.  this line is the column space of A matrix which has only one column.  in general the matrix A has n columns a<sub>1</sub>, ... , a<sub>n</sub> 

the combinations in R<sup>m</sup> are the vectors Ax in column space. 

looking for the particular comnbination p = Ax.hat = the projection that is closest to b.  the 'hat' over x.hat indicates the best choice x.hat to give the closest vector p in the column space:

x.hat = a<sup>T</sup>b/a<sup>T</sup>a when n = 1

for n > 1, the best x.hat = the vector x.hat = (x.hat<sub>1</sub>, ... , .x.hat<sub>n</sub>) derived here:

compute projections onto n-dimensional subspaces in 3 steps.  
1. find the vector x.hat  
2. find the projection p = Ax.hat
3. find the projection matrix P:  p = Pb  

[if b shines onto A in R<sup>m</sup> space then e must also be in R<sup>m</sup> space and can be just one vector. but what if b is an object?]

the dotted line from b to nearest point Ax.hat in subspace.  b - Ax.hat is perpendicular to subspace.  the error b - Ax makes a right angle with all the vectors a<sub>1</sub>, ... , a<sub>n</sub> in the base.  the n right angles give the equation for x.hat.  

a<sub>1</sub><sup>T<sup> (b - Ax.hat) = 0  
...
a<sub>n</sub><sup>T<sup> (b - Ax.hat) = 0

[such that the a<sub>1</sub><sup>T<sup>, ... , a<sub>n</sub><sup>T<sup> are A<sup>T</sup> that has n rows and m columns and A.T is multiplying the error vector b - Ax.hat which has m rows because both A and e are in R<sup>m</sup>.  this product = 0 because A and e are both m dimensional in m-dimensional space and are perpendicular. i believe these are orthogonal complements.] 

the matrix with these rows a<sub>i</sub><sup>T</sup> is A<sup>T<sup>.

the n equations are exactly A<sup>T</sup>( b - Ax.hat ) = 0

rewritten as  

A<sup>T</sup>b - A<sup>T</sup>Ax.hat = 0

rewritten as 

A<sup>T</sup>Ax.hat = A<sup>T</sup>b

which is equation for x.hat and its coefficient matrix A<sup>T</sup>A.

now find x.hat and p and P.

x.hat is n x 1

A<sup>T</sup>A is symmetric and nxn and invertible if the a's are independent.  

the solution is x.hat = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b 

the projection of b onto the subspace is p

p is m x 1  

p = Ax.hat = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b  

the next formula picks out the P from the above formula in order to arrive at p = Pb

p = Pb = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup> times b  

so P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>

comparing column space line a (below) with column space surface A (above))

for n = 1 / n > 1  

x.hat = a<sup>T</sup>b / a<sup>T</sup>a   
x.hat = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b 

p = x.hat * a = a<sup>T</sup>b/a<sup>T</sup>a * a  
p = Ax.hat = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b  

P = aa<sup>T</sup> / a<sup>T</sup>a     
P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>

LA gives us the normal equation.  

1. subspace is the column space of A  
2. error vector b - Ax.hat is perpendicular to the column space of A  
3. b - Ax.hat is in the null space of A<sup>T</sup>   
[is it an orthogonal complement?  i think yes since we defined the subspaces row and null space as orthogonal complements.]
hence: A<sup>T</sup>(b-Ax,hat) = 0 = A<sup>T</sup> • e = 0  the left null space of A contains the error vectors e = b - Ax.hat.  The vector b is being split into projection p which is in A's column space and the error e = b - p which is not in A's column space but orthogonal to it's row space.  projection produces a right triangle with sides p e and b. 

https://docs.sympy.org/latest/modules/matrices/matrices.html

example:


<img width="656" alt="image" src="https://user-images.githubusercontent.com/38410965/106049865-a09dad80-60b4-11eb-9532-7ff9a05c8ed6.png">

then applying that to a function:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106050711-7a2c4200-60b5-11eb-9861-20d6ce3338ac.png">

here's the function:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106050829-a1830f00-60b5-11eb-95de-dcff2b179d17.png">

then, checking relationships: 

vector space A is perpendicular to the error e, or more technically, e is the left null space to A, or e is the null space of A transpose.

the projection of b on to a = p = Pb

the projection p is perpendicular to the error e

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106051788-e5c2df00-60b6-11eb-8415-e0beccc093eb.png">


Problems that involve rectangular matrices almost always employ A<sup>T</sup>A.  When A has independent columns, A<sup>T<sup>A is invertible. It's worth proving it.

A<sup>T</sup>A is invertible if and only if A has linearly independent columns.

Prove A<sup>T</sup>A has same null space as A.

When columns of A are linearly independent, it's null space contains only the zero vector.  A<sup>T</sup>A has same null space and is invertible.

Let A be any matrix.  If x is in the null space of A, then Ax = 0.  Multiplying by A<sup>T</sup> gives A<sup>T</sup>Ax also = 0 since A<sup>T</sup> is merely multiplying 0 = Ax.  So x is also in the null space of A<sup>T</sup>A.

Now start with null space of A<sup>T</sup>A.  From A<sup>T</sup>Ax = 0 we prove Ax = 0.  We cannot multiply by (A<sup>T</sup>)<sup>-1</sup> because generally n > m for A<sup>T</sup> and so the inverse doesnt exist.  

so we multiply by x<sup>T</sup>

(x<sup>T</sup>)A<sup>T</sup>A = 0 = (Ax)<sup>T</sup>(Ax) = 0 = ||Ax||<sup>2</sup> = 0

we have shown that if A<sup>T</sup>Ax = 0 then Ax has length = 0.  Therefore Ax = 0. Every vector in x in one null space is in the other null space.  


if A<sup>T</sup>A has dependent columns then so does A   

if A<sup>T</sup>A has independent columns then so does A


interesting problems

2. b = np.array([cos theta, sin theta]) and a = np.array([1,0]) compute p 

p = ( a<sup>T</sup>b / a<sup>T</sup> ) a = np.array([ cos theta, 0 ]) which makes sense since cos theta is in the x position in the vector and shines down onto the vector a that lies on the x axis at (1,0)

4. compute the projection matrix for problem 2. only need a for this. not b. 

when P is multiplied by b = (cos theta, sin theta) it will only pick up the cos theta and thus shines onto (1,0) on the x axis.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106062065-44428a00-60c4-11eb-9d98-1ee5df0715dd.png">


5. cmopute the projection matrices onto the lines a<sub>1</sub> = (-1,2,2) and a<sub>2</sub> = (2,2,-1) and multiply their projection matrices and explain why their product P<sub>1</sub> P<sub>2</sub> is what it is. 

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106061025-d77ac000-60c2-11eb-8f84-9c5459c843d0.png">

6. project b = (1,0,0) onto a<sub>1</sub> = (-1,2,2), a<sub>2</sub> = (2,2,-1), a<sub>3</sub> = (2,-1,2) and sump the 3 projections p<sub>1</sub>, p<sub>2</sub>, p<sub>3</sub>

notice that dot product combinations for a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub> reveal they are perpendicular and that p<sub>1</sub> + p<sub>2</sub> + p<sub>3</sub> = b and that all the projection matrices = identity.  this is principal components moving the axes from traditional x, y, z to a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub> and by shining b onto those producing p<sub>1</sub>, p<sub>2</sub>, p<sub>3</sub> that are the coordinates of b onto these new 3 dimensional axes.  Thus the projection matrices sum to identity in this new 3 dimensional space.  if you mutliply the sum of (P<sub>1</sub> + P<sub>2</sub> + P<sub>3</sub> ) times b you get b's coordinates inthis new 3d system.  "we can add projections onto orthogonal vectors a<sub>1</sub>, a2</sub>, a3</sub> to get the projection matrix onto the larger space. "

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/106063382-19f1cc00-60c6-11eb-900e-3dd865e739be.png">


8. project b = (1,1) onto the lines through a<sub>1</sub> = (1,0) and a<sub>2</sub> = (1,2) and add p<sub>1</sub> + p<sub>2</sub>. these do not add to b because the a's are not orthogonal.  

9. projections of b onto the plan containing a<sub>1</sub> = (1,0) and a<sub>2</sub> = (1,2) will sum to equal b.

since A is invertible P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup> separates into AA<sup>-1</sup>(A<sup>T</sup>)<sup>-1</sup>A<sup>T</sup> = I which is the projection matrix onto the vector space of R<sup>2</sup>

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106065649-94701b00-60c9-11eb-9bc1-78cc82dd421b.png">


11. project b into the column space of A by solving for e and show e perpendicular to A.

here is not obvious that b is already lying in the plane or subspace of the plane of A, but computing e = 0 shows that. also showing that b is in the column space of a is that Ax=b despite A having m>n finds a solution, as revealed when computing the rref of the augmented Ab. note the last row of Ab.rref has zeros across. 

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106066606-1ca2f000-60cb-11eb-8d93-4a27f0fa3e22.png">

16. what linear combination of (1,2,-1) and (1,0,1) is closest to (2,1,1).  

This one is easy.  Put the first two vectors into A and find the the third's projection onto it.   
Even easier is that the first two are orthogonal to one another and so A<sup>T</sup>A = some multiple of I   
One cannot take them out of their parentheses, but they are invertible.    
e = 0 so b is in A's column space.  
Here again we see that Ab is solvable which means that b is in As column space.  

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106067966-b5d30600-60cd-11eb-81ce-61aaecff6849.png">


17. P<sup>2</sup> = P then (I - P)<sup>2</sup> = (I - P).  When P projects into the column space of A, (I-P) projects into the left null space of A.  

(I-P)<sup>2</sup> = (I-P)(I-P) = I<sup>2</sup> - PI - IP - P<sup>2</sup> = I - 2P + (P<sup>2</sup>=P) = I - P

e = b - p = b - Pb = b (I - P) so e is the projection of b using (I - P) projection matrix. geometrically, b shines onto a plane that is perpendicular to A columns.  A's columns are perpendicular to A's left null space: C(A) N(A<sup>T</sup>) = zero vector.  So e is b's projection into A's left null space.

18. for example, if P is the 3 x 3 projection matrix onto the line through (1,1,1) then I - P is the projection matrix onto the plane perpendicular to (1,1,1).  

Do not even need to solve for this. The plane perpendicular to (1,1,1) is x + y + z = 0.  
From the question, P projects b onto (1,1,1).  (I - P)b would be the projection of b into the space perpendicular to (1,1,1) because using that projection matrix on b = (I-P)b = b - p = e and we know e is perpendicular to (1,1,1) .

20. similarly, to find the projection matrix P onto some plane x - y - 2z = 0, first write down a vector e that is perpendicular to the plane e.g. e = (3,1,1) and computer Q = ee<sup>T</sup> / e<sup>T</sup>e which is just treating like a as a line to be shone upon. 


P<sup>2</sup> = P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup> A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup> = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>

PPb = Pb becaue Pb is already in the column space of A and it's projection would of course be in the column space of A.

if A is square and invertible then P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup> = AA<sup>-1</sup>(A<sup>T</sup>)<sup>-1</sup>A<sup>T</sup> = I and thus P = I which means that column space of A is not a line or a plane or something limited.  Column space of A is all of R<sup>n</sup> and so b is in the column space of R<sup>n</sup> and p = Pb = Ib = b and e = b - p = 0.

The null space of A<sup>T</sup> is orthogonal to the column space C(A). So if A<sup>T</sup>b = 0 then the projection of b onto the C(A) should be p = 0 since b is in the left null space of a = null space of A<sup>T</sup>, b is in the orthogonal complement of A<sup>T</sup> = N(A<sup>T</sup>.


section 4.3 least squares approx

m points cartesian plane represented by 2 vectors t = (0,1,2) along the x axis and b = (0,0,6) along the y axis 

seeking C intercept and D slope for a line fitted nearest to these points to minimize error e

C scales fixed 1 and D scales variable t resulting in a line p that is nearest to b.

C + Dt = b

C + D (t=0) = (b=6)
C + D (t=1) = (b=0)
C + D (t=2) = (b=0)

C and D are independent vectors at this point.

finding x.hat, p and P

compute square matrix A<sup>T</sup>A

compute x.hat = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b

compute Ax.hat = p

compute b - p = error

from p = Pb = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b,  
compute P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>  

confirm e perpendicular to p and A   
or more informative e as left null space to A or null space and orthogonal complement to A<sup>T</sup>  

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/106185327-ae186d80-6170-11eb-9b3c-4d52e5c91db6.png">

when e = 0, Ax = b  
when e > 0, Ax.hat = p ≠ b

principles:

solving A<sup>T</sup>Ax.hat = A<sup>T</sup>b gives the projection p = Ax.hat of b onto the column space of A.

when Ax = b has no solutions, x.hat is the least squares solution: || b - Ax ||<sup>2</sup> is minimized. (b - Ax = b - p = e)

(recall ||a - b|| = ((a - b)<sup>2</sup>)<sup>0.5</sup>) = a<sup>2</sup> - ab cos theta - ba cos theta - b<sup>2</sup> but cos theta = 0 when a - b = b - Ax = e in this case is right angled.)

setting partial derivatives of E = || b - Ax || to zero, ∂E / ∂x<sub>i</sub> = 0, also produces A<sup>T</sup>Ax.hat = A<sup>T</sup>b  

to fit points (t<sub>i</sub>, b<sub>i</sub>), ... , (t<sub>m</sub>, b<sub>m</sub>) by a straight line, A is equipped with 2 columns (1, ... , 1) and (t<sub>1</sub>, ... , t<sub>m</sub>)  

in that case A<sup>T</sup>A is the 2 x 2 matrix 

https://tex-image-link-generator.herokuapp.com

![\begin{bmatrix}
m&\sum_{}^{} t_i\\
\sum_{}^{} t_i&\sum_{}^{} t_i^2
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Am%26%5Csum_%7B%7D%5E%7B%7D+t_i%5C%5C%0A%5Csum_%7B%7D%5E%7B%7D+t_i%26%5Csum_%7B%7D%5E%7B%7D+t_i%5E2%0A%5Cend%7Bbmatrix%7D)

and A<sup>T</sup>b is the vector  

![\begin{bmatrix}
\sum_{}^{} b_i\\
\sum_{}^{} t_i b_i
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A%5Csum_%7B%7D%5E%7B%7D+b_i%5C%5C%0A%5Csum_%7B%7D%5E%7B%7D+t_i+b_i%0A%5Cend%7Bbmatrix%7D)

Ax = b has no solutions because m > n i.e. A is overspecified i.e. the n columns span a small slice of m dimensional space that may not include b.  

Ax + e = b

when e is as small as possible via x.hat it is a least squares solution.

previous section sought p

this section seeks x.hat

Minimizing error:

x.hat is found by geometry such that error e meets the column space A at a right angle and by algebra such that A<sup>T</sup>Ax.hat = A<sup>T</sup>b and by calculus which via first derivative = 0 gives minimum of the function for x.hat = || Ax - b ||<sup>2</sup>.

calculus is the only unexplored interpretation of x.hat

[not sure the reason for this]

|| Ax - b ||<sup>2</sup> = || Ax - p ||<sup>2</sup> + || e ||<sup>2</sup>

as reduce Ax - p to zero by employing x = x.hat you are left with only squared error.

with C = 5 and D = 3 the error from B to p is (1,2,1) = (e<sub>1</sub>), e<sub>2</sub>, e<sub>3</sub>)

from :  
C + D (t=0) = (b=6)
C + D (t=1) = (b=0)
C + D (t=2) = (b=0)

we get:  
E = || Ax = b ||<sup>2</sup> =
( C + D (t=0) = (b=6) )<sup>2</sup>
( C + D (t=1) = (b=0) )<sup>2</sup>
( C + D (t=2) - (b=0) )<sup>2</sup>

with 2 unknowns, there are 2 partial derivatives.    
the chain rule multiplies the derivative of the square by the derivative of its contents

∂E / ∂C treats D as a constant and the derivative of the C = 1 in each case:

∂E / ∂C
= 2 ( C + D • 0 - 6 )<sup>1</sup> • 1
+ 2 ( C + D • 1 - 0 )<sup>1</sup> • 1
+ 2 ( C + D • 2 - 0 )<sup>1</sup> • 1
= 0

∂E / ∂D treats C as a constant and the derivative of the t<sub>i</sub>D = 0, 1, and 2 respectively:

∂E / ∂D
= 2 ( C + D • 0 - 6 )<sup>1</sup> • 0
+ 2 ( C + D • 1 - 0 )<sup>1</sup> • 1
+ 2 ( C + D • 2 - 0 )<sup>1</sup> • 2
= 0

the C factors are 1,1,1  
the D factors are 0,1,2   
obviously appear in A  
and when algebra reduces ∂E / ∂C and ∂E / ∂D equations,   
it sums these factors  
which are squared because the first derivative chain rule places the factor outside the parentheses too 
so the C factors end up as 1<sup>2</sup>, 1<sup>2</sup>, 1<sup>2</sup> and the D factors end up as 0<sup>2</sup> in the ∂E / ∂C, 1<sup>2</sup>, 2<sup>2</sup> = 5 in the ∂E / ∂D

∂E / ∂C = 3C + 3D = 6

∂E / ∂D = 3C + 5D = 0

producing the matrix same as A<sup>T</sup>A

![\begin{bmatrix}
3&3\\
3&5
\end{bmatrix}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A3%263%5C%5C%0A3%265%0A%5Cend%7Bbmatrix%7D%0A)


the calculus equation same as normal equation from linear algebra.

partial derivatives of || Ax - b ||<sup>2</sup> are zero when A<sup>T</sup>Ax = A<sup>T</sup>b

previously when n > m there were many, infinite, solutions to Ax = b and so x = x<sub>r</sub> + x<sub>n</sub> split.  

here with m > n, there are no solutions to Ax = b.  Instead of splitting x, the problem splits b into p and e.  Instead of solving Ax = b which is impossible, solve Ax.hat = p and know e perpendicular to p gets us to b. 

The null space of A<sup>T</sup> = N(A<sup>T</sup>) is very small.  With independent columns, the only solution is Ax = 0 is x = 0. Then A<sup>T</sup>A is invertible.  

The equation A<sup>T</sup>Ax.hat = A<sup>T</sup>b fully determines the best vector x.hat. The error has A<sup>T</sup>e = 0.  All vectors in C(A) have dot product with e = zero.  They are orthogonal complements: left null and column spaces.

A's vectors assumed independent and so A<sup>T</sup>A is invertible.

A's vectors when orthogonal turn A<sup>T</sup>A into a diagonal matrix that is easier to solve since the orthogonal vectors' zero dot products appear in the off diagonals.  

It is easier to solve A<sup>T</sup>Ax.hat = A<sup>T</sup>b:

3C + 8D = np.array([ 7, 6 ]) --> C = 7/3 and D = 6/8

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/106217161-a671bc80-61a2-11eb-8d7e-ca67a7fb3e16.png">

so helpful are orthogonal columns that it is worth recentering t by subtracting t.bar = (t<sub>1</sub>, ... , t<sub>m</sub>) / m

for example t = (1,3,5) subtracts t.bar = 3 to give the same solution as above. 

(Similar to Gram-Schmift in next section.)

Dependent columns:

Independent columns in A provide an invertible A<sup>T</sup>A.
Dependent columns in A disable inversion and so rather than solving for the full matrix A<sup>T</sup>A, solve via the single column which is repeated.

Here A has 2 measurements of b = 1 and 3 at the same time = 1 so A = np.array([[1,1],[1,1]]) and b = np.array([3,1])

As before a straight line cannot go through both points (1,3) and (1,1).  Projecting b = (3,1) onto the column space of A yields infinite solutions because A has null space ≠ 0 = (-1,1).

Ax = b

Ax.hat = p where p = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b 

x.hat = x_p = (C, D) = (2,0) will solve but of course so will x_p + s • x_n = (2,0) + 1• (-1,1) e.g. (1,3) or (3,1) 

1 = a1 = 1st column of A  
t = a2 = 2nd column of A  
C = x1 = intercept  
D = x2 = slope  
b = y  
p = projection of b on A  

C • 1 + D • t ≠ b  

no x = (C, D) --> (t,b) = (1,1) and (1,3):  
observations:  
C • 1 + D • t = b   
C • 1 + D • 1 = 1  
C • 1 + D • 1 = 3  
but x.hat = x_p = (C, D) = (2,0) --> (t,b) = (2,2) and (2,2) that minimize error to 1 (flat line from 2 intercept)  
2 • 1 + 0 • 2 = 2 = p1  
2 • 1 + 0 • 2 = 2 = p2  
[b = (1,3)] - [p = (2,2)] = [e = (-1,1)]  
or with s = 1, x.hat = x_c = x_p + 1 • x_n = (C, D) = (2-1=1,0+1=1) --> (t,b) = p = (2,2) that has same error.  
1 • 1 + 1 • 1 = 2 = p1  
1 • 1 + 1 • 1 = 2 = p2  
b - p = e = (-1,1)  
or with s = -1, x.hat = x_p - 1 • x_n = (C, D) = (2--1=3,0-+1=-1) --> (t,b) = p = (2,2) that has same error.  
3 • 1 - 1 • 1 = 2 = p1  
3 • 1 - 1 • 1 = 2 = p2  
b - p = e = (-1,1)  

as shown here:  
<img width="522" alt="image" src="https://user-images.githubusercontent.com/38410965/106343414-40a13580-6273-11eb-8fbc-d2ddeabf5384.png">


section 7.4 pseudo inverse of A chooses the shortest solution to Ax.hat = p, aka x<sup>+</sup> = (1,1) which is the particular solution in the row space of A, i.e. x<sub>p</sub> shown above, and x<sup>+</sup> has length √2 which is better than x.hat = (2,0) and (0,2) which have length = 2.  Arbitrarily can choose the bull space component of the x<sup>+</sup> solution to be zero [by setting s = 0 i guess].

fit a parabola

C + Dt + Et<sup>2</sup> = b  

where b might be height of ball at time t  

c.hat ( C, D, E ) 

C + D t<sub>1</sub> + E t<sub>m</sub><sup>2</sup> = b<sub>1</sub>
...
C + D t<sub>m</sub> + E t<sub>m</sub><sup>2</sup> = b<sub>m</sub>

Ax = b with a m x n or m x 3 matrix.

3 normal equations are captured in A<sup>T</sup>A = A<sup>T</sup>b

column space of A has dimension 3 = number of basis vectors.  

the projection of b is p = Ax.hat combinig 3 columns using coefficients C, D, E

error e at each data point is e<sub>i</sub> = b<sub>i</sub> - C - Dt<sub>i</sub> - Et<sub>i</sub><sup>2</sup>

the total squared error is E = e<sub>i</sub><sup>2</sup> + ... + e<sub>m</sub><sup>2</sup>

total squared error can be minimized via calculus by taking partial derivative of E with respect to C, D, E which will be zero when x = x.hat = (C, D, E) that solves the 3 x 3 system of equations when m = 3: A<sup>T</sup>Ax.hat = A<sup>T</sup>b.  

section 10.5 does more with least squares: Fourier seires approximate function rather than vectors.

example: 

C + Dt + Et<sup>2</sup> = b to push us to 3 different heights b = (6,0,0) when t = (0,1,2):

C + D•0 + E•0<sup>2</sup> = 6  
C + D•1 + E•1<sup>2</sup> = 0  
C + D•2 + E•2<sup>2</sup> = 0  

x = x.hat = (6,-9, 3) so b = p = (6,0,0)

6 + -9•0 + 3•0<sup>2</sup> = 6  
6 + -9•1 + 3•1<sup>2</sup> = 0  
6 + -9•2 + 3•2<sup>2</sup> = 0

gives an exact fit because A is invertible, essentially because A is square already.  Wont always be invertible, even though we insist on indpendence, but certainly helps that m = n.

A is square.

A echelon form is the identity matrix  

Ax = b --> x = A<sup>-1</sup>b = (6,-9,3)  --> Ax = (6,0,0)

e = b - p = 0

P = identity matrix because A column space is all of R<sup>3</sup> and so Pb which is projecting b onto A is projecting b into R<sup>3</sup>.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106346408-f1640080-6284-11eb-8d4b-32dd2b351a32.png">

A has 3 columns that span the whole space of R<sup>3</sup>.  The projection matrix is the identity matrix.  The projection of b is b.  The error is zero.  We dont need A<sup>T</sup>Ax.hat = A<sup>2</sup>b because inversion solves Ax = b directly.  

(t<sub>4</sub>, b<sub>4</sub>) may or may not be on the parabola.  if on the parabola, solve directly.  if not on the parabola then solve via A<sup>T</sup>Ax.hat = A<sup>T</sup>b.  The error will not be at the last point even though first 3 points are on this parabola.  The errors will be averaged out over all points. .  The 4th point makes m > n --> least squares need.

review:  

the least squares solution x.hat minimizes:

|| Ax - b ||<sup>2</sup> = x<sup>T</sup>A<sup>T</sup>Ax - 2x<sup>T</sup>A<sup>T</sup>b + b<sup>T</sup>b

which is E = the sum of squares of the errors in the m equations m > n.

the best x.hat comes from the normal equations A<sup>T</sup>Ax.hat = A<sup>T</sup>b 

To fit m points by a line b = C + Dt the normal equations give C and D

the heights of the best fit line are p = (p<sub>1</sub>, ... , p<sub>m</sub>) 

the vertical distances to the b data points are the errors e = (e<sub>1</sub>, ... , e<sub>m</sub>)

A key equation is A<sup>T</sup>e = 0 for orthogonality.

if fit m points by a combination of n < m functions, the m equations Ax = b are generally unsolvable.  The n equations A<sup>T</sup>Ax.hat = A<sup>T</sup>b give the least squares solution = combination with the smallest MSE.

good problems:

1  with b = 0,8,8,20 at t = 0,1,3, 4 solve normal equation A<sup>T</sup>Ax = A<sup>T</sup>b for xhat, P, heights p and minimum error E = ∑ e.  Find 4 equations Ca1 + Da2 = p ≠ b 

compute the normal equation

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106361087-00c96500-62ea-11eb-8f26-0092fa4b7bf2.png">

using new function "doc_ls"

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106361097-0b83fa00-62ea-11eb-9145-46bf4def0f99.png">

compute the partials ∂C / ∂e and ∂D / ∂E for the grouped 4 equations and reduce to the normal equation.

E = (1•C + 0•D - 0)<sup>2</sup> + (1•C + 1•D - 8)<sup>2</sup> + (1•C + 3•D - 8)<sup>2</sup> + (1•C + 4•D - 20)<sup>2</sup>  

∂C/∂E   
= 2•(1•C + 0•D - 0)<sup>2</sup>•1 + 2•(1•C + 1•D - 8)<sup>2</sup>•1 + 2•(1•C + 3•D - 8)<sup>2</sup>•1 + 2•(1•C + 4•D - 20)<sup>2</sup>•1  
= 4C + 8D = 36 = C + 2D = 9

∂D/∂E   
= 2•(1•C + 0•D - 0)<sup>2</sup>•0 + 2•(1•C + 1•D - 8)<sup>2</sup>•1 + 2•(1•C + 3•D - 8)<sup>2</sup>•3 + 2•(1•C + 4•D - 20)<sup>2</sup>•4
= 8C + 26D = 112

normal equation via calculus:   
1C + 2D = 9   
8C + 26D = 112   

5. Find height C of best horizontal line to fit b = 0,8,8,20 at times t = 0,1,3,4.  Thus, only looking for flat line only intercept C is relevant and D irrelevant.  Set A = only the a1 component that is relevant to intercept and solve for p.  Show the normal equation.  This is projecting the vector b = (0,8,8,20) onto the line A = (1,1,1,1) to get p = (9,9,9,9) because xhat = 9 and notice that p is still perpendicular to e

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106361925-ff9a3700-62ed-11eb-9e09-de48cf6b9635.png">

Find the closest line through the origin, i.e. with a zero intercept, and thus C and a1 irrelevant:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106362020-86e7aa80-62ee-11eb-8e73-15d8f9dfeb9c.png">

now use a degree 2 polynomial to solve for best parabola:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106362348-48eb8600-62f0-11eb-8f67-1f10d63001b5.png">

now fit a 4th degree, cube, to the 4 points.  as the matrix becomes square, we get a solution with zero error:

"Vandermort gives exact interpolation by a cubic at 0,1,3,4"
<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106362430-bf888380-62f0-11eb-92f0-57bf864417be.png">

the average of the 4 times t = 0,1,3,4 = 2 and 4 actual heights b = 0,8,8,20 = 9
verify that the best line goes through the center point t.bar, b.bar = 2,9  
explain why C + D•t.bar = b.bar comes from the first equation where C = 1 and D = 4:
C + D t.bar = b.bar ... 1 + 4 • 2 = 9

The reason is that the first equation has C•m + D•∑t<sub>i</sub> = ∑b<sub>i</sub>  
when divided by m, it shows that the best line goes through b.bar at time t.bar 


12. project b = (b<sub>1</sub>, ... , b<sub>m</sub>) onto the line through a = (1, ... , 1) by solving m equations ax = b in 1 unknown by least squares. 

solve a<sup>T</sup>ax = a<sup>T</sup>b to show that x.hat is the mean or average of the b's.  remember C = 1, .. ,1

a = (1, ... , 1) has a<sup>T</sup>a = m = ∑ (1, ... , 1) and a<sup>T</sup>b = ∑ (b<sub>1</sub>, ... , b<sub>m</sub>)

so a<sup>T</sup>b / a<sup>T</sup>a = (b<sub>1</sub> + ... + b<sub>m</sub>) / m = average of b's

this was alluded to in the matrices formulas earlier in this section of chapter.

Find e = b - ax.hat and variance of b || e ||<sup>2</sup> and standard deviation of b = || e || 

|| e ||<sup>2</sup> =  (b<sub>1</sub> - weighted_mean)<sup>2</sup> + ... + (b<sub>m</sub> = weighted_mean)<sup>2</sup> = 

|| e || = standard deviation


13. first assumption behind least squares Ax = b noise e with mean zero. multiply the error vector e = b - Ax by (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup> to get (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b - (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>x = x.hat - x on the RHS.  The estimation errors x.hat - x average to zero.  The estimation x.hat is unbiased. this tells us when the components of Ax - b add to zero, so do the components of x.hat - x.  so x unbiased estimator.   Ax-b = y.hat and y departing from zero when x.hat and x do so. "

14. the m errors e<sub>i</sub> are independent with variance sigma squared so the average of (b-Ax)<sup>T</sup> is sigma<sup>2</sup> • I.   multiply on LHS by (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup> and on RHS by A(A<sup>T</sup>A)<sup>-1</sup> to show that the average matrix (x.hat - x)(x.hat - x)<sup>T</sup> is sigma<sup>2</sup>(A<sup>T</sup>A)<sup>-1</sup>.  This covariance matrix W in section 10.2.

might help: ee<sup>T</sup> = || e ||<sup>2</sup> = (b - Ax)(b-Ax)<sup>T</sup>

the matrix (x.hat - x)(x.hat - x)<sup>T</sup> is (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>(b-Ax)(b-Ax)<sup>T</sup>A(A<sup>T</sup>A)<sup>-1</sup> when the average of (b-Ax)(b-Ax)<sup>T</sup> = sigma<sup>2</sup> • I
the average of (x.hat - x)(x.hat - x)<sup>T</sup> will be the output covariance matrix (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>sigma<sup>2</sup>A(A<sup>T</sup>A)<sup>-1</sup> which simplifies to sigma<sup>2</sup>(A<sup>T</sup>A)<sup>-1</sup> that gives the average of the squared output errors x.hat - x.  

15.  when A has a column of four 1s, problem 14 gives the expected error (x.hat - x) as sigma (A<sup>T</sup>A(<sup>-1</sup>) = sigma<sup>2</sup>/4 

ny taking m measurements, the variance drops from sigma<sup>2</sup> to sigma<sup>2</sup>/m

this leads to the monte carlo method in section 12


section 4.4 

principles

columns q<sub>1</sub>, ... , q<sub>n</sub> are orthnormal if q<sub>i</sub><sup>T</sup>q<sub>j</sub> = 0 for i ≠ j and = 1 for i = j.  then Q<sup>T</sup>Q = I

if Q is also square then QQ<sup>T</sup> = I and Q<sup>T</sup> = Q<sup>-1</sup>.  Q is then an orthonormal matrix

the least squares solution to Qx = b is x.hat = Q<sup>T</sup>b. Projection of b: p = QQ<sup>T</sup>b = Pb

the Gram-Schmidt process takes independent a<sub>i</sub> to orthonormal q<sub>i</sub>.  start with  q<sub>1</sub> = a<sub>1</sub> / || a<sub>1</sub> ||

q<sub>i</sub> is = (a<sub>i</sub> - projection p<sub>i</sub>) / || a<sub>i</sub> - p<sub>i</sub> || 

projection p<sub>i</sub> = (a<sub>i</sub><sup>T</sup>q<sub>1</sub>) q<sub>1</sub> + ... + (a<sub>i</sub><sup>T</sup>q<sub>i-1</sub>) q<sub>i-1</sub>

each a<sub>i</sub> will be a combination of q<sub>1</sub> to q<sub>i</sub> then A = QR: orthogonal Q and triangular R.

detail:

orthogonality good because A<sup>T</sup> is diagonal.

gram-schmidt chooses combinations of A's original basis vectors to produce right angles of orthonormal basis vectors in a new matrix Q

basis   
independent vectors  
span a space  
meet at any angle except zero and 180 degrees (identical)

cannot make independent vectors from dependent vectors
can make orthogonal vectors from independent vectors

vectors q<sub>1</sub>, ... , q<sub>n</sub> are orthogonal when dot product q<sub>i</sub> • q<sub>j</sub> are zero: q<sub>i</sub><sub>T</sub>q<sub>j</sub>   i ≠ j

normal when lenght || q || = 1 = unit vectors.

orthogonal unit vectors = orthonormal.

vectors q<sub>1</sub>, ... , q<sub>n</sub> are orthonormal are an orthonormal basis if 

q<sub>i</sub><sup>T</sup>q<sub>j</sub> = 0 when i ≠ j orthogonal vectors  
q<sub>i</sub><sup>T</sup>q<sub>i</sub> = 1 when i = j unit vectors || q || = 1  

A matrix with orthonormal columns is assigned the special letter Q.

Q easy to work with because Q<sup>T</sup>Q = I    

Q matrices have columns that are orthonormal. 

Q is not required to be square.

when Q square, Q<sup>T</sup>Q = I means that Q<sup>T</sup>=Q<sup>-1</sup>

Q that is square   
called orthogonal matrix not orthonormal matrix   
inverse from LHS and RHS too 
rows of square Q are orthonormal too
inverse is transpose

any matrix with orthonormal columns uses the letter Q

rotation, permutation, reflection are orthogonal matrices

independent vs orthogonal
rectangular vs square
any length vs unit length


some utility functions:

deg2rad - converts degrees from 1,0 to units of pi   
rad2deg  - converts units of pi to deg  
length_xy - takes x and y coordinates  
length - takes any dim vector   
make_unit - converts vector to unit vector   
degrees_shift_xy - moves a point in x,y to a point degrees away from that. from_point and to_point keep non unit length  
degrees_shift - takes any number of vectors in R<sup>2</sup> and shifts them degrees  
v2angle - converts a R<sup>2</sup> vector to an angle vs x-axis
angle2v - converts any angle from x-axis to a unit vector.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106376359-a4eef280-6362-11eb-9afc-419e1b5e605b.png">

example of rotation:

Q rotates every vector in the plane by angle theta

the columns of Q are orthogonal: (cos&theta;, sin&theta;) • (-sin&theta;, cos&theta;) = -cos&theta; sin&theta; + sin&theta; cos&theta; = cos&theta; sin&theta; - cos&theta; sin&theta; = 0

the columns of Q are unit vectors: sin<sup>2</sup>&theta; + cos<sup>2</sup>&theta; = = x<sup>2</sup> + y <sup>2</sup> = 1 as long as q<sub>1</sub> orthogonal to q<sub>2</sub>.

I = Q<sup>T</sup>Q = Q<sup>-1</sup>Q and because Q is square QQ<sup>-1</sup>

logically since   
Q<sup>-1</sup>Q = QQ<sup>-1</sup> =   
Q rotates vectors through &theta; and Q<sup>-1</sup> rotates vectors back through -&theta; 

[i think every rotation matrix is an orthogonal matrix]

![\begin{bmatrix}
cos\theta&-sin\theta\\
sin\theta&cos\theta
\end{bmatrix}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Acos%5Ctheta%26-sin%5Ctheta%5C%5C%0Asin%5Ctheta%26cos%5Ctheta%0A%5Cend%7Bbmatrix%7D%0A)

the above Q matrix effect is shown here:  


<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106393690-9cc89e80-63c6-11eb-8511-81e077ac33c6.png">

and implemented in degrees_shift:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106393706-b2d65f00-63c6-11eb-9c53-082013491229.png">

example of permutation  

change the order of rows when used on the LHS and of columns when used on the RHS.  

since one and only one 1 is in every column    
all columns are unit vectors and orthogonal to each other  

the inverse of a permutation is its transpose  Q<sup>-1</sup> = Q<sup>T</sup>

every permutation matrix is an orthogonal matrix

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106394687-d059f780-63cb-11eb-8654-d48dec8a3fbf.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106394704-e7004e80-63cb-11eb-8218-7d3da20b539d.png">

reflection matrix

1. take any unit vector u   
2. set Q = I - 2uu<sup>T</sup>   
3. Q is symmetric and orthogonal and Q<sup>2</sup> = I  
because reflecting twice through a mirror brings back the original like (-1)<sup>2</sup> = 1,
reflection matrix squared Q<sup>T</sup>Q is the identity matrix = (I - 2uu<sup>T</sup>)<sup>2</sup> = I - 4uu<sup>T</sup> +4uu<sup>T</sup>uu<sup>T</sup> because u<sup>T</sup>u = 1


unit vector: u<sup>T</sup>u = 1  

u = (u1, u2)

uu<sup>T</sup> =   

![\begin{bmatrix}
u_1*u_1&u_1*u_2\\
u_2*u_1&u_2*u_2
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Au_1%2Au_1%26u_1%2Au_2%5C%5C%0Au_2%2Au_1%26u_2%2Au_2%0A%5Cend%7Bbmatrix%7D)

Since diagonal elements of uu<sup>T</sup> contain u<sub>1</sub><sup>2</sup> and u<sub>2</sub><sup>2</sup> respectively  
then they sum to 1   
u<sub>1</sub><sup>2</sup> + u<sub>2</sub><sup>2</sup> = 1   
because as unit vector u,   
( u<sub>1</sub><sup>2</sup> + u<sub>2</sub><sup>2</sup> )<sup>0.5</sup> = 1  
then (( u<sub>1</sub><sup>2</sup> + u<sub>2</sub><sup>2</sup> )<sup>0.5</sup>)<sup>2</sup> = 1<sup>2</sup>  
then u<sub>1</sub><sup>2</sup> + u<sub>2</sub><sup>2</sup> = 1  

Since Q = I - 2uu<sup>T</sup>  
this means for diagonals   
np.diag(Q) = 1 - 2 • u<sub>1</sub><sup>2</sup>,  1 - 2 • u<sub>2</sub><sup>2</sup>

set
a = u<sub>1</sub><sup>2</sup>
b = u<sub>2</sub><sup>2</sup>
b = 1 - a

if Q = I - 2uu<sup>T</sup>  
then 
np.diag(Q) 
= 1 - 2a, 1 - 2b 
= 1 - 2a, 1 - 2 (1 - a) 
= 1 - 2a, 1 - 2 + 2a 
= 1 - 2a, -1 + 2a
= -(2a - 1), 2a - 1
= -(2(u<sub>1</sub><sup>2</sup>) - 1), 2(u<sub>1</sub><sup>2</sup>) - 1

so the diagonal components are same but opposite signed number

off diagonals are identical.

example: v<sub>1</sub> = sp.Matrix([-10,10]) reduces to unit vector u<sub>1</sub> = sp.Matrix( [ -1/√2, 1 / √2 ] ) which is orthogonal and unit: u<sub>1</sub><sup>T</sup>u<sub>1</sub> = 1.  v<sub>1</sub> points from lower right origin to upper left on 45 degree line and that is the direction of reflection. 

Q causes a reflection to -u<sub>1</sub> ie across a vector from LL to UR.

Q = sp.Matrix([ [ 0, 1 ], [ 1, 0 ] ]) which when applied to v<sub>2</sub> = sp.Matrix( [3,3] ) yeilds no change because v<sub>2</sub> lies on the same vector as u<sub>1</sub> across which vectors are reflected.  

v<sub>3</sub> = sp.Matrix( [1,0] ) flips across u<sub>1</sub> in direction of u<sub>1</sub> to sp,Matrix( [0,1] ).


<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106507283-d1a52600-6498-11eb-970a-1ef9cc375491.png">

example: v<sub>1</sub> = sp.Matrix([10,10]) reduces to unit vector u<sub>1</sub> = sp.Matrix( [ 1/√2, 1 / √2 ] ) which is orthogonal and unit: u<sub>1</sub><sup>T</sup>u<sub>1</sub> = 1.  v<sub>1</sub> points from LL origin to UR on 45 degree line. 

Q causes a reflection to -u<sub>1</sub> ie across a vector from LR to UL.

Q = sp.Matrix([ [ 0, 1 ], [ 1, 0 ] ]) which when applied to v<sub>2</sub> = sp.Matrix( [3,3] ) yeilds a flip across the line throught -u<sub>1</sub> that runs LR to UL to sp.Matrix( [-3, -3 ] )

v<sub>3</sub> = sp.Matrix( [1,0] ) flips across the same -u<sub>1</sub> in direction to sp,Matrix( [-1, 0] ).

<img width="638" alt="image" src="https://user-images.githubusercontent.com/38410965/106508038-e0400d00-6499-11eb-902f-d92d724cca4d.png">

Not entirely sure of the reflection workings.

With reflections lengths do not change || Qx<sup>2</sup> || = || x<sup>2</sup> || because  
(Qx)<sup>T</sup>(Qx) = x<sup>T</sup>Q<sup>T</sup>Qx = x<sup>T</sup>Ix = x<sup>T</sup>s

if Q has orthonormal columns Q<sup>T</sup>Q = I

Q also preserves dot products between 2 different vectors, x and y: (Qx)<sup>T</sup>Qy = x<sup>T</sup>Q<sup>T</sup>Qy = x<sup>T</sup>y

Projections with orthonormal bases 

Orthonormal matrices simplify computations; numbers do not grow large when lengths of vectors are fixed.  Stable computer codes use Qs as much as possible. 

Projections onto subspaces, e.g., use A<sup>T</sup>A where this A<sup>T</sup>A matrix entries are dot products of a<sub>i</sub><sup>T</sup>a<sub>j</sub> of the basis vectors a<sub>1</sub>, ... , a<sub>n</sub> from A

if basis vectors are orthonormal A<sup>T</sup>A simplifies to Q<sup>T</sup>Q and x.hat, p and P formulas improve. Instead of Q<sup>T</sup>Q or its equivalent I, the formula has a blank:

A<sup>T</sup>Ax.hat = A<sup>T</sup>b --> Q<sup>T</sup>Qx.hat = Q<sup>T</sup>b --> Ix.hat = Q<sup>T</sup>b --> x.hat = Q<sup>T</sup>b

p = Ax.hat = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b --> p = Qx.hat = Q(Q<sup>T</sup>Q)<sup>-1</sup>Q<sup>T</sup>b = QQ<sup>T</sup>b or can just replace x.hat with the formula from paragraph above Q<sup>T</sup>b in the formula p = Qx.hat --> QQ<sup>T</sup>b

P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup> = Q(Q<sup>T</sup>Q)<sup>-1</sup>Q<sup>T</sup> = Q ( I ) Q<sup>T</sup> = QQ<sup>T</sup> which also provides a formula for p = Pb = QQ<sup>T</sup>b

least squares solution of Qx = b is x.hat = Q<sup>T</sup>b.

the projection matrix is QQ<sup>T</sup> = P

the projection is p = Qx.hat = QQ<sup>T</sup>b

no matrices are inverted because of orthonormal basis.  

best x.hat = Q<sup>T</sup>b just has dot products of q<sub>1</sub>, ... , q<sub>n</sub> with b --> 1 dimensional (one basis vector) projections. 

the 'coupling matrix' or 'correlation matrix' A<sup>T</sup>A is not Q<sup>T</sup>Q = I.   
there is no coupling.  

projection onto q's:  
p 
= QQ<sup>T</sup>b
= [q<sub>1</sub>, ... , q<sub>n</sub>] 
• 
[
[q<sub>1</sub><sup>T</sup>b]
[...]
[q<sub>n</sub><sup>T</sup>b]
]
= q<sub>1</sub>(q<sub>1</sub><sup>T</sup>b) + ... + q<sub>n</sub>(q<sub>n</sub><sup>T</sup>b)

[
There are a few ways to look at this mathematics:  
1. we've learned that 2 matrices multiplied can be viewed as the sum of matrices formed by the outside products between 1st column x 1st row + 2nd column x 2nd row + ... + nth column x nth row and so QQ<sup>T</sup> is just that q<sub>1</sub>(q<sub>1</sub><sup>T</sup>) + q<sub>2</sub>(q<sub>2</sub><sup>T</sup>) + ... + q<sub>n</sub>(q<sub>n</sub><sup>T</sup> and QQ<sup>T</sup>b is a square matrix whose columns are weighted by the row components of b: 

QQ<sup>T</sup>  
= (q<sub>1</sub>(q<sub>1</sub><sup>T</sup>) + q<sub>2</sub>(q<sub>2</sub><sup>T</sup>) + ... + q<sub>n</sub>(q<sub>n</sub><sup>T</sup>)b

= q<sub>1</sub>(q<sub>1</sub><sup>T</sup>b) + q<sub>2</sub>(q<sub>2</sub><sup>T</sup>b) + ... + q<sub>n</sub>(q<sub>n</sub><sup>T</sup>b)

2. each q<sub>j</sub><sup>T</sup>b is a inner product that weights q in q<sub>j</sub>(q<sub>j</sub><sup>T</sup>b)

3. b shines onto a to form p  
p is some percentage x.hat of a  
a and p are perpendicular to error e = b - p: a • e = 0   
so, a • ( b - p ) = a • ( b - x.hat a ) = a • b - a • x.hat • a = 0   
a • x.hat • a = a • b   
x.hat • a<sup>T</sup>a = a<sup>T</sup>b    
x.hat = a<sup>T</sup>b / a<sup>T</sup>a   
since p = P b = a x.hat = a ( a<sup>T</sup>b ) / ( a<sup>T</sup>a )   
P = aa<sup>T</sup> / a<sup>T</sup>a   
if P = Q because it has orthonormal vectors, then, P = aa<sup>T</sup> / a<sup>T</sup>a = qq<sup>T</sup> / q<sup>T</sup>q where the denominator is the length of the unit vector 1 and the numerator is a single dimension of many q's in Q that are added together to make Q.  p = Pb = qq<sup>T</sup>b as shown in our formula,   

when Q is square m = n the space is whole sapce and Q<sup>T</sup> = Q<sup>-1</sup> and x.hat = Q<sup>T</sup>b is same as x = Q<sup>-1</sup>b: solution is exact not projection. 

the projection of b onto whole space Q is b itself and p = b and P = QQ<sup>T</sup> = I.

if Q not square then p ≠ b.

when projecting onto whole space, when p = b the formular assembles b from 1 dimensional projections.

if q<sub>1</sub>, ... , q<sub>n</sub> is an orthonormal basis for the whole space then Q is square.

[logic appears to go both ways: square --> whole space basis and whole space basis --> square]

every b = QQ<sup>T</sup>b is the sum of its components along the q's:

b = q<sub>1</sub>(q<sub>1</sub><sup>T</sup>b) + ... + q<sub>n</sub>(q<sub>n</sub><sup>T</sup>b)

transforms QQ<sup>T</sup> = I is the foundation of Fourier series and all great transforms of applied mathematics.  transforms break b or functions f(x) into perpendicular pieces.  

inverse transforms add the pieces to put b and f(x) back together.

example

Q is shown as 1/3 scaling a 3x3 matrix.

Q<sup>T</sup>Q = QQ<sup>T</sup> = I

sum of projections of b on Q is shown as sum of projections of b on each of Qs columnar vectors.  b is pulled out and distributed to each of the q<sub>j</sub>q<sub>j</sub><sup>T</sup> that are summed up to produce p = b.

each of the q<sub>j</sub><sup>T</sup>b values are shown before they are then multiplied by q<sub>j</sub>

q<sub>j</sub>q<sub>j</sub><sup>T</sup>  
separate projections of b = sp.Matrix([0,0,1]) on to q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub> are p<sub>1</sub>, p<sub>2</sub>, p<sub>3</sub>

because QQ<sup>T</sup>b decomposes into sum of outside products q<sub>j</sub>(q<sub>j</sub><sup>T</sup>b), the individual projections of b onto q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub> sum to the single projection of b onto Q.

separate q<sub>j</sub>q<sub>j</sub><sup>T</sup>b are 2/3 q<sub>1</sub>, 2/3 q<sub>2</sub>, -1/3q<sub>3</sub> 

the individual q<sub>j</sub>q</sub>j</sub></sup>T</sup> are summed to produce I as QQ<sup>T</sup> would as well.

<img width="522" alt="image" src="https://user-images.githubusercontent.com/38410965/106540483-07183680-64ce-11eb-96e0-b9beb31e4f11.png">

gram schmidt process

orthogonal is good.   
projections always involve A<sup>T</sup>A and when columns are orthonormal that becomes Q<sup>T</sup>Q which makes inverses unnecessary.  

gram schmidt uncouples the one dimensional projections into n separate dot products q<sub>j</sub>q<sub>j</sub><sup>T<sup>b 

for all this to be true, all vectors in A need to be orthogonal and unit = orthonormal. gram-schmidt does that: makes A's columns orthonormal vectors.

in our example, start with three vectors that are independent: a, b, c and construct three orthogonal vectors A, B, C and then at end divide by || A ||, || B ||, || C || to make them unit and orthonormal. 

1. begin choosing A = a.  
the first direction is accepted as it comes.

2. B is chosen perpendicular to A
by starting with b   
from b subtract b's projection p on A because b - p = e is perpendicular to A  
and we are looking for something perpendicular to A.    Here's how it goes again:   

B = b - p = e  
p = Ax.hat = some combination of A's column vectors each weighted by x.hat elements.    
substitute Ax.hat in for p   
B = b - Ax.hat = e  
to solve for and then remove x.hat, use the fact that e is perpendicular to A and since B = e, B is perpendicular to A   
multiply B = b - Ax.hat by A<sup>T</sup> and set to zero:   
A<sup>T</sup>B = 0 = A<sup>T</sup>(b - Ax.hat) = A<sup>T</sup>b - AA<sup>T</sup>   
use the RHS to solve for x.hat:  
0 = A<sup>T</sup>b - A<sup>T</sup>Ax.hat  
A<sup>T</sup>b = A<sup>T</sup>Ax.hat   
( A<sup>T</sup>b ) / ( A<sup>T</sup> )A = x.hat    
return to B = b - Ax.hat and replace x.hat with ( A<sup>T</sup>b ) / ( A<sup>T</sup> )A:     
B = b - A( A<sup>T</sup>b ) / ( A<sup>T</sup> )A

B = b - (A<sup>T</sup>b)A / (A<sup>T<sup>A) 

[ in the end remember B = e on LHS and b - p is on the RHS ]

[ a and b can be any angle. ] 
A and B are now orthogonal.

multiply B = b - (A<sup>T</sup>b)A / (A<sup>T</sup>A) by A<sup>T</sup> to verify A and B orthogonal:   
A<sup>T</sup>B = A<sup>T</sup>b - A<sup>T</sup>(A<sup>T</sup>b)A / (A<sup>T</sup>A)   
cancel A<sup>T</sup> and A separately in numerator and denominator of the 2nd term on the RHS   
the equality on RHS with zero confirms that the LHS is orthogonal:    
A<sup>T</sup>B = A<sup>T</sup>b - A<sup>T</sup>(A<sup>T</sup>b) / (A<sup>T</sup>A) 
A<sup>T</sup>B = A<sup>T</sup>b - (A<sup>T</sup>b)  

third dimension starts with c.   
c is not likely perpendicular to A and B.   

c is a vector.   
c is not likely in perpendicular to A or B.   
c is not likely in A or B 
c can project onto A and B which together are perpendicular axes  of a plane
heres c formula:  
C = c - e<sub>A</sub> - e<sub>B</sub>  
C = c - A<sup>T</sup>cA / A<sup>T</sup>A - B<sup>T</sup>cB / B<sup>T</sup>B  

[try to derive here:actually no need because its simply C<sub>A</sub> = c - p<sub>A</sub>] and then C = C<sub>A</sub> - p<sub>B</sub>
C = c - p = e   
p = ABx.hat     
C and c - p and c - ABx.hat and e are equal and are perpendicular to AB  
multiply AB by c - ABx.hat and set = 0 to solve for x.hat  
(AB)<sup>T</sup>(c - ABx.hat) = 0  
(AB)<sup>T</sup>c = (AB)<sup>T</sup>ABx.hat)  
(AB)<sup>T</sup>c / (AB)<sup>T</sup>AB = x.hat  
return to C = c - ABx.hat and substitute in x.hat   
C = c - AB((AB)<sup>T</sup>c / (AB)<sup>T</sup>AB)  

if had 4th vector for R<sup>4</sup>, subtract d's 3 projections onto A, B and C to get D.  This is Gram-Schmidt.

Then divide A by || A ||, B by || B ||, and C by || C || to obtain unit vectors, q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub>

example of gram schmidt

independent, non-orthogonal vectors a, b, c:

a = sp.Matrix( [ 1, -1, 0 ] )  
b = sp.Matrix ( [ 2, 0, -2 ] )
c = sp.Matrix ( [ 3, -3, 3 ] )

independence seen via inversion or reduction, non-orthogonality via dot products.

A = a

B 
= p - p 
= b - ((A<sup>T</sup>b) / (A<sup>T</sup>A)) A =  b - 2/3 A 
= sp.Matrix([1,1,2])   
A<sup>T</sup>A = 2 ; A<sup>T</sup>b = 2  
Subtract from b, it's projection p along A  
confirm A<sup>T</sup>B = 0 as engineered  
B is left null space of A

C 
= c - p  
= c - ((A<sup>T</sup>c) / (A<sup>T</sup>A))A - ((B<sup>T</sup>c) / (B<sup>T</sup>B))B   
= c - (6/2)A + (6/6)B   
= sp.Matrix([1,1,1])  
confirm that C is perpendicular to A and B: A<sup>T</sup>C = 0 and B<sup>T</sup>C = 0  

[is p in the column space of AB?  how confirm?  if the rref of AB has zeros at bottom then yes?]

convert A, B, C to unit vectors:
|| A || = √2, || B || = √6, || C || = √3  
divide by those lengths for orthonormal bases:  
q<sub>1</sub> = (1/√2) sp.Matrix( [1,-1,0] )  
q<sub>2</sub> = (1/√2) sp.Matrix( [1,1,-2] )  
q<sub>3</sub> = (1/√2) sp.Matrix( [1,1,1] )  

A ,B, C usually contain fractions.   
Usually always q's contain square roots.  


<img width="522" alt="image" src="https://user-images.githubusercontent.com/38410965/106632509-d37bf180-654b-11eb-9451-e710925f9507.png">


<img width="700" alt="image" src="https://user-images.githubusercontent.com/38410965/106632509-d37bf180-654b-11eb-9451-e710925f9507.png">


matrix A gave us a, b, c which are converted to matrix Q whose columns are q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub>.   how are these related?

a, b, c are combinations of the q's and the q's are combinations of a, b, c   
a third matric R connects A and A.

the first step:

q<sub>1</sub> = a / || a ||

with no other vectors involved.

the second step combines A with b:

B = b - ((A<sup>T</sup>b) / (A<sup>T</sup>A)) A  
q<sub>2</sub> = B / || B ||

with C and q<sub>3</sub> uninvolves.

C = c - ((A<sup>T</sup>c) / (A<sup>T</sup>A))A - ((B<sup>T</sup>c) / (B<sup>T</sup>B))B    
q<sub>3</sub> = C / || C ||

the uninvolvement of later vectors is THE key point of gram-schmidt:  
- the vectors a and A and q<sub>1</sub> are all along a single line.  
- the vectors a, b and A, B and q<sub>1</sub>, q<sub>2</sub> are all in the same plane  
- the vectors a, b, c, and A, B, C are q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub> are in one subspace

At every step a<sub>1</sub>, ... , a<sub>k</sub> are combinations of q<sub>1</sub>, ... , q<sub>k</sub>.  Later q's are not involved.  [not involved seems to imply trianglar R much like L?]  So the connecting matrix R is triangular:  A = QR  

[ a b c ] = [ q<sub>1</sub> q<sub>2</sub> q<sub>3</sub> ] R

where R is:  

![\begin{bmatrix}
q_1^Ta&q_1^Tb&q_1^Tc\\
&q_2^Tb&q_2^Tc\\
&&q_3^Tc
\end{bmatrix}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aq_1%5ETa%26q_1%5ETb%26q_1%5ETc%5C%5C%0A%26q_2%5ETb%26q_2%5ETc%5C%5C%0A%26%26q_3%5ETc%0A%5Cend%7Bbmatrix%7D%0A)

A = QR  
R = Q<sup>T</sup>A  

example continued

[book labels original matrix A. I label it X since there is a vector A]

X has a, b and c in its columns  
Q has q<sub>1</sub>, q<sub>2</sub> and q<sub>3</sub> in its columns  
Q has q<sub>1</sub><sup>T</sup>, q<sub>2</sub><sup>T</sup> and q<sub>3</sub><sup>T</sup> in its rows

R is triangular from rows q<sub>1</sub><sup>T</sup>, q<sub>2</sub><sup>T</sup>, q<sub>3</sub><sup>T</sup> of Q.T multiplying columns a, b and c of X.

R has square roots but has empties where   
B's unit vector q<sub>2</sub> is designed perpendicular to a in R21
C's unit vector q<sub>3</sub> is designed perpendicular to a in R31 and b in R32:  

R = Q<sup>T</sup>X    
r21 = q<sub>2</sub><sup>T</sup>a = 0 because q<sub>2</sub> is unit B = b - p = e which is perpendicular to a (p here is b's projection onto a)   
r31 = q<sub>3</sub><sup>T</sup>a = 0 because q<sub>3</sub> is unit C = c - p = e which is perpendicular to b (p here is c's projection onto a)  
r32 = q<sub>3</sub><sup>T</sup>b = 0 because q<sub>3</sub> is unit C = c - p = e which is perpendicular to b (p here is c's projection onto b)   

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/106656740-18fae780-6569-11eb-8cc5-8fcea00f66fe.png">

thus the point of gram-schmidt is that:  
q<sub>1</sub> is only a  
q<sub>2</sub> is only a and b
q<sub>3</sub> is a, b and c


gram-schmidt   
from independent vectors a<sub>1</sub>, ... , a<sub>n</sub> construct orthonormal vectors q<sub>1</sub>,  ... , q<sub>n</sub>: the matrices A and Q with these columns satisfy A = QR then R = Q<sup>T</sup> which is upper triangular because the later q's are orthogonal to the earlier q's.

the i,j entry of R = Q<sup>T</sup>A is the row i of Q<sup>T</sup> (= q<sub>j</sub> vector of Q) times the column j of A.

the lengths of A, B, C are √2, √6 and √3 on the diagonal of R.  

the columns of Q are orthonormal  

both LR and QR are fundamental to linear algebra

Any m x n matrix A with indpendent columns can be factored into QR.  

the m x n matrix Q has orthonormal columns and the square matrix R is upper triangular with a positive diagonal (lengths)

usefulness for least squares:  
A<sup>T</sup>A = (QR)<sup>T</sup>QR = R<sup>T</sup>Q<sup>T</sup>QR = R<sup>T</sup>R   
so, the least squares equation A<sup>T</sup>Ax.hat = A<sup>T</sup>b simplifies to:   
R<sup>T</sup>Rx.hat = R<sup>T</sup>Q<sup>T</sup>b  
[ because R<sup>T</sup>R = A<sup>T</sup>A and (QR)<sup>T</sup> = A<sup>T</sup>]
and then to  
Rx.hat = Q<sup>T</sup>b   
and then to
x.hat = R<sup>-1</sup>Q<sup>T</sup>b  

so instead of solving Ax = b, which is impossible, solve Rx.hat = Q<sup>T</sup>b by back substitution.  

the cost is m x n<sup>2</sup> multiplications in the gram-schmidt process to construct orthonormal R and the triangular R with A = QR.

r<sub>i,j</sub> = ∑ i=1 to m of q<sub>i,k</sub>v<sub>i,j</sub>  
and  
v<sub>i,j</sub> = v<sub>i,j</sub> - q<sub>i,k</sub>r<sub>k,j</sub>  
and  
r<sub>j,j</sub> = ( ∑ i = 1 to m of v<sub>i,j</sub><sup>2</sup> )<sup>1/2</sup>  
and   
q<sub>i,j</sub> = v<sub>i,j</sub> / r<sub>j,j</sub>

starting from a, b, c = a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub> this code constructs q<sub>1</sub>, then B, q<sub>2</sub> then C q<sub>3</sub>:

q<sub>1</sub> = a<sub>1</sub> / || a<sub>1</sub> ||

B = a<sub>2</sub> - (q<sub>1</sub><sup>T</sup>a<sub>2</sub>)q<sub>1</sub>

q<sub>2</sub> = B / || B ||

C' = a<sub>3</sub> - (q<sub>1</sub><sup>T</sup>a<sub>3</sub>)q<sub>1</sub>

C = C' - (q<sub>2</sub><sup>T</sup>C')q<sub>2</sub>  

q<sub>3</sub> = C / || C ||

code for QR decomp and sympy function - same!

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106694858-6e55e980-65a7-11eb-9e8e-54c464c96114.png">


<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/106694779-3fd80e80-65a7-11eb-84b6-87218da336bc.png">

Householder reflections are a better way than this code by acting on A to produce the upper triangular R, one column at a time int eh same way that elimination produces upper triangular U in LU.

The reflection matrices I - 2uu<sup>T</sup> come in chapter 11 on numerical linear algebra.  A tridiagonal simplifies even more to 2 x 2 notations, always to A = QR. 

Review:

if orthonormal vectors q<sub>1</sub>, ... , q<sub>n</sub> are the columns of Q then q<sub>i</sub><sup>T</sup>q<sub>j</sub> = 0 and q<sub>j</sub><sup>T</sup>q<sub>j</sub> = 1 translate into the matrix multiplication Q<sup>T</sup>Q = I

if Q is square (an orthonormal matrix) then Q<sup>T</sup> = Q<sup>-1</sup>: transpose = inverse

the length of Qx = the length of x since all || Qx || = || x ||

the projection onto the column space of Q spanned by the q's is P = QQ<sup>T</sup>
[Q<sup>T</sup>Q = I but not QQ<sup>T</sup>]

if Q is square then P = QQ<sup>T</sup> = I and every b = q<sub>1</sub>(q<sub>1</sub><sup>T</sup>b), ... , q<sub>n</sub>(q<sub>n</sub><sup>T</sup>b)

gram-schmidt produces orthonormal vectors q<sub>1</sub>q<sub>2</sub>q<sub>3</sub> from independent a, b, c. In matrix form this is factorization A = QR = (orthogonal Q)(triangular R)

examples:

Hadamard matrix ... add 2 columns that are orthogonal

![\begin{bmatrix}
1&1&x&x\\
1&-1&x&x\\
1&1&x&x\\
1&-1&x&x
\end{bmatrix}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A1%261%26x%26x%5C%5C%0A1%26-1%26x%26x%5C%5C%0A1%261%26x%26x%5C%5C%0A1%26-1%26x%26x%0A%5Cend%7Bbmatrix%7D%0A)

this is orthogonal

![\begin{bmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{bmatrix}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A1%261%261%261%5C%5C%0A1%26-1%261%26-1%5C%5C%0A1%261%26-1%26-1%5C%5C%0A1%26-1%26-1%261%0A%5Cend%7Bbmatrix%7D%0A)

this H<sub>4</sub> can be built from H<sub>2</sub>'s in the same way that the below H<sub>8</sub> is built from H<sub>4</sub>'s

![\begin{bmatrix}
H_2&H_2\\
H_2&-H_2
\end{bmatrix}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0AH2%26H2%5C%5C%0AH2%26-H2%0A%5Cend%7Bbmatrix%7D%0A)

what's the product of this H<sub>8</sub><sup>T</sup>H<sub>8</sub>

![\begin{bmatrix}
H_4&H_4\\
H_4&-H_4
\end{bmatrix}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0AH4%26H4%5C%5C%0AH4%26-H4%0A%5Cend%7Bbmatrix%7D%0A)

making H<sub>8</sub> orthonormal?

![\begin{bmatrix}
H_4&H_4\\
H_4&-H_4
\end{bmatrix}^T
\begin{bmatrix}
H_4&H_4\\
H_4&-H_4
\end{bmatrix}
=\begin{bmatrix}
H_4^T&H_4^T\\
H_4^T&-H_4^T
\end{bmatrix}
\begin{bmatrix}
H_4&H_4\\
H_4&-H_4
\end{bmatrix}
=\begin{bmatrix}
8I&0\\
0&8I
\end{bmatrix}
;\begin{bmatrix}
Q_8
\end{bmatrix}
=\begin{bmatrix}
\frac{H_8}{\sqrt8}
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0AH_4%26H_4%5C%5C%0AH_4%26-H_4%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cbegin%7Bbmatrix%7D%0AH_4%26H_4%5C%5C%0AH_4%26-H_4%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0AH_4%5ET%26H_4%5ET%5C%5C%0AH_4%5ET%26-H_4%5ET%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AH_4%26H_4%5C%5C%0AH_4%26-H_4%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A8I%260%5C%5C%0A0%268I%0A%5Cend%7Bbmatrix%7D%0A%3B%5Cbegin%7Bbmatrix%7D%0AQ_8%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7BH_8%7D%7B%5Csqrt8%7D%0A%5Cend%7Bbmatrix%7D)

key point of orhogonal columns is that A<sup>T</sup> is diagonal and easy to invert. 

if the projection of b = (6,0,0,0,2) onto the 1st column of H<sub>4</sub> is p<sub>1</sub> = (2,2,2,2) and onto 2nd column is p<sub>2</sub> = (1,-1,1,-1) then the projection of b onto the 2 dimensional space spanned by the 1st two columns is p<sub>12</sub> = the sum of the first two projections.  this is true because the first two columns are orthogonal to one another. 

independent if determinant is not zero

orthogonal if dot product is zero

orthogonal and therefore independent

lenght 1 and orthogonal and thus orthonormal

Q<sup>T</sup>Q = I only assured from left because only columns are orthonormal.

3 orthogonal column length 4: A<sup>T</sup>A = 16 * I

3 orthogonal columns lenghts 3, 4, 5: A<sup>T</sup>A = sp.diagonal( [9, 16, 25 ] ) 

any Q with n > m has QQ<sup>T</sup> ≠ I

QQ<sup>T</sup> = I only for sqaure Q

nonzero orthogonal vectors are independent.

these two orthogonal vectors are not linearly independent (1,0) and (0,0)

zero is orthogonal with every vector and not independent with any.

any two orthogonal matrices, Q's, multiplied produce an orthogonal matrix:  
proving only need to show that their produce is I.  any two matrices whose product is I are orthogonal; so if 2 orthogonal matrices are multiplied, you can prove that their product is orthogonal by multiplying the product by itself and finding I:  
(Q<sub>1</sub>Q<sub>2</sub>)<sup>T</sup>Q<sub>1</sub>Q<sub>2</sub> = Q<sub>2</sub><sup>T</sup>Q<sub>1</sub><sup>T</sup>Q<sub>1</sub>Q<sub>2</sub> = Q<sub>2</sub><sup>T</sup>Q<sub>2</sub> = I

when gram-schmidt gives Q with orthonormal columns, Q<sup>T</sup>Qx.hat = Q<sup>T</sup>b becomes x.bar = Q<sup>T</sup>b.  theres no cost to solving the normal equation. 

if q<sub>1</sub> and q<sub>2</sub> are orthonormal vectors in R<sup>5</sup> then p = (q<sub>1</sub><sup>T</sup>b)q<sub>1</sub> + (q<sub>2</sub><sup>T</sup>b)q<sub>2</sub> is closest to b.  e = b - p is orthogonal to q<sub>1</sub> and q<sub>2</sub>

Ax = b has no solution. Ax.hat = p has a solution and p is closest to b.  
begin with Ax.hat = b   
multiply by A<sup>T</sup> on both sides:  
A<sup>T</sup>Ax.hat = A<sup>T</sup>b   
multiply both sides by (A<sup>T</sup>A)<sup>-1</sup>  
(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>Ax.hat = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>  
Ix.hat = x.hat = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b  
p = Ax.hat = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b  
p = Pb = Ax.hat = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b  
so P = Ax.hat = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>   

when A is Q, i.e. when A's columns are orthonormal, then repeating
p = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b  
then substituting Q for A  
p = Q(Q<sup>T</sup>Q)<sup>-1</sup>Q<sup>T</sup>b  
then substituting I for Q<sup>T</sup>Q  
p = Q(I)<sup>-1</sup>Q<sup>T</sup>b = QQ<sup>T</sup>b  
p 
= [ q<sub>1</sub> q<sub>2</sub> q<sub>3</sub>]
@ 
[
[q<sub>1</sub><sup>T</sup>] 
[q<sub>2</sub><sup>T</sup>] 
[q<sub>3</sub><sup>T</sup>]
]
b
= [ q<sub>1</sub> q<sub>2</sub> q<sub>3</sub>]
@ 
[
[q<sub>1</sub><sup>T</sup>b] 
[q<sub>2</sub><sup>T</sup>b] 
[q<sub>3</sub><sup>T</sup>b]
]

since q<sub>j</sub><sup>T</sup>b is a dot product it is a scaler and becomes a 3 component vector shown in the second part of last equation that is then multiplied by a square matrix Q.  the following though shows the scalars q<sub>j</sub><sup>T</sup>b on the LHS of columns of Q because of columns multiplication.  q<sub>j</sub><sup>T</sup>b is weighting each of the j columns of Q.

p = q<sub>1</sub><sup>T</sup>b(q<sub>1</sub>) + q<sub>2</sub><sup>T</sup>b(q<sub>2</sub>) + q<sub>3</sub><sup>T</sup>b(q<sub>3</sub>))

example of that last point and shows that two orthogonal vectors whose Q<sup>T</sup>Q is I does not have QQ<sup>T</sup> = I:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106788835-7ea9ab00-661f-11eb-9d52-6471890432cb.png">

if a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub> are a basis for R<sup>3</sup> any vector b can be written as b = x<sub>1</sub>a<sub>1</sub> + x<sub>2</sub>a<sub>2</sub> + x<sub>3</sub>a<sub>3</sub> <--- this is simply columnar multiplication Ax=b.  Now if a's are orthonormal, then x<sub>1</sub> = a<sub>1</sub><sup>T</sup>b because when you substitute in x<sub>1</sub>a<sub>1</sub> + x<sub>2</sub>a<sub>2</sub> + x<sub>3</sub>a<sub>3</sub> for b, you have x<sub>1</sub> = a<sub>1</sub><sup>T</sup>(x<sub>1</sub>a<sub>1</sub> + x<sub>2</sub>a<sub>2</sub> + x<sub>3</sub>a<sub>3</sub>).  since a<sub>1</sub>a<sub>2</sub> = a<sub>1</sub>a<sub>3</sub> = 0 that reduces to x<sub>1</sub>(a<sub>1</sub><sup>T</sup>a<sub>1</sub>) and since  a<sub>1</sub><sup>T</sup>a<sub>1</sub> = || a || = 1, that original a<sub>1</sub><sup>T</sup>b reduces to x<sub>1</sub>. 

what multiple of a = (1,1) should be subtracted from b = (4,0) to make the result B orthogonal to a?

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/106791421-e281a300-6622-11eb-833f-8eca6c29cabb.png">

16 what multiple of a = (4,5,2,2) is closest to b = (1,2,0,0). find the orthonormal vectors q<sub>1</sub> and q<sub>2</sub> in the plane of a and b.

q<sub>1</sub> = a / length(a) = a / sqrt( a<sup>T</sup>a )

= B 
= b - x.hat * a  
= b - ( a<sup>T</sup>b / a<sup>T</sup>a ) a

q<sub>2</sub> 
= b - (q<sub>1</sub><sup>T</sup>b)(q<sub>1</sub>)
= b - (a<sub>1</sub><sup>T</sup>b)(a<sub>1</sub>)((a<sub>1</sub><sup>T</sup>a)<sup>0.5</sup>)<sup>2</sup>
= b - (x.hat) a / length

[not sure why B = b - p and then q = B / || B || doesnt divide b by length]
[it is becuse this math is only about p not B.  B here just coincidentally has length 1]

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/106800034-f7176880-662d-11eb-84f5-465515a3cf5f.png">

confirming above calculations:

also shows that A<sup>T</sup>A = (QR)<sup>T</sup>QR = R<sup>T</sup>R

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/106804615-a0149200-6633-11eb-963e-3d4b64eb360c.png">


