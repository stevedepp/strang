ch4

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

p = x.hat*a = a<sup>T</sup>b/a<sup>T</sup>a * a  
p = Ax.hat = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b  

P = aa<sup>T</sup> / a<sup>T</sup>a     
P = A(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>


