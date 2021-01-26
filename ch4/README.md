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


