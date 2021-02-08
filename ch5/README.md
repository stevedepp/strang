
determinant of A:

det A = [ [a,b], [c,d] ] = ab - bc

singular matrix A has zero determinant:

det A = [ [a,xa], [c,xc] ] = 0

row exchanges in A reverse det A sign

PA = [ [0,1], [1,0] ]  [ [a,b], [c,d] ] = [ [c,d], [a,b] ] has det PA = bc - ad = - det A

the determinant is linear in row 1 by itself:

det [ [xa + yA,xb + yB], [c,d] ] = xad - xbc + yAd - yBc = x(ad - bc) + y(Ad - Bc)

elimination gives det EA = U = product of the pivots 

EA = [ [a,b], [0,d-(c/a)b] ]

det EA = a ( d - (c/a)b ) = product of pivots = det A = ad - bc

generally the above hold for matrix A that is n x n 

det singular = 0

det reverse sign each time rows are exchanged

det is linear in row 1 by itself

det is product of pivots

Always, whether n x n or not, det BA = det B times det A and det A.T = det A

Intro to properties of determinants:

determinant of square matrix is single number

determinant contains a lot of information
- is matrix invertible
- determinant of A<sup>-1</sup> = 1 / (det A)
- determinant --> a formula for every cell in A<sup>-1</sup>
- determinants find inverse matrices, pivots, and solutions to A<sup>-1<sup>b
- elimination is faster than determinant formulas for finding the above information.

A<sup>-1</sup> = 1/(ad-bc) [ [d,-b], [-c,a] ]

A<sup>-1</sup>A = 1/(ad-bc) [ [d,-b], [-c,a] ] [ [a,b], [c,d] ] = 1/(ad-bc) [ [ad-bc, bd-bd], [ac-ac, ad-bc] ] = I

singular matrix has ad-bc = 0 and so
- 1/(ad-bc) = 1/0 = undefined
- ad = bc --> a/c = b/d so rows have same ratio = dependent or a/c = b/d so columns have same ratio = dependent.  dependent columns or rows always lead to det A = 0. it means the rows are parallel. 

the determinant can be found 3 ways:
- multiply the n pivots "pivot formula"
- add up n! terms "big formula"
- combine n smaller determinants "cofactor formula"

all three ways involve sign switches: rule is for an n x n matric, determinant changes when rows or columns are exchanged.

det I = | I | = 1   
det P = | P |  1 or -1 since half the Ps involve switching I with even number of exchanges and half require an odd number of exchanges.   
det I = 1  
det [ [0,1], [1,0] ] = -1 because it switched rows or columns once.

linearity doesnt mean det (A + B ) = det A + det B:  for example   
det ( I + I ) ≠ 1 + 1 = 2
det ( I + I ) = det [ [2,0], [0,2] ] = 4  
so deta n * I = 2<sup>n</sup> * det I 

properties define determinants   

determinants have 3 properties = rules 1 2 3  
can compute the determinant of any square matrix A  

properties 1-3 produce properties 4-10

2 x 2 matrices for examples but make application general:

properties of the determinant

with rules  1 2 3 can compute determinant of any square matrix A

show for 2 x 2 and explan for n x n

terminology 

det A = | A |

every rule for rows applies to columns just by transposing A which we prove in rule 10 = A<sup>T</sup>

1. the determinant of the n x n identity matrix is 1

any n

this matches with volume of a unit cube = 1

2. the determinant changes sign when 2 rows (or columns) are exchanged

det [ [c,d], [a,b] ] = -det [ [a,b], [c,d] ]  = bc - ad

det P = 1 or -1 for any even or odd number of row/column switches that start from I

3. the determinant is a linear function of each row separately: all other rows fixed.

if 2 matrices 1st rows are added, determinants are added.   

this rule applies only when other rows are not changed.  

(a) multiplication: multiply only row 1 by any number t causes det to be multiplied by t

det [ [ta,tb], [c,d] ] = t • det [ [a,b], [c,d] ]

(b) addition: add row 1 of A to row 1 of A' causes the determinants of A and A' to be added

det [ [a+a',b+b'], [c,d] ] = det [ [a,b], [c,d] ] + det [ [a',b'], [c,d] ]

notice c and d are common to both A and A'

these three rules apply when A is n x n and one 

det A = det [ [4,8,8], [0,1,1], [0,0,1] ] = 4 • det [ [1,2,2], [0,1,1], [0,0,1] ]

combining multiplication and addition can be linear combination in one row:

x • det [ [a,b], [c,d] ] + y • [ [A,B], [c,d] ]   
= det [ [xa+yA,xb+yB], [c,d] ]   
= d(xa+yA) - c(xb+yB)   
= x(ad-bc) + y(Ad - Bc) <-- same as 1st row of this equation sequence  

det A = det [ [4,8,8], [0,1,1], [0,0,1] ] = det [ [4,0,0], [0,1,1], [0,0,1] ] + det [ [0,8,8], [0,1,1], [0,0,1] ]

only one row (1st) changes in each of these 2 linear combinations, multiplication above and addition below.

det t • [ [a,b], [c,d] ] = det [ [ta,tb], [tc,td] ] = ta•td - tb•tc = t<sup>2</sup>(ad-bc) = t<sup>2</sup>det [ [a,b], [c,d] ]

so generally det t • A = t<sup>2</sup> • det A

this is like area and volume.

expand a rectangles sides by factor of 3 from 2x3=6 to 6x9=54 and the area increases by a factor of 3<sup>2</sup>=9 from 6 to 54.  

expand a cube's sides by factor of 4 from 2x3x4=24 to 8x12x16=1536 and the volume increases by a factor of 4<sup>3</sup>=64 from 24 to 1536: (orginal volume) * factor<sup>dimensions</sup> = (new volume)

determinants = volumes and areas

rules 4-10 make determinants easier to work with. 

4. if 2 rows of A are equal, det A = 0

proof: exchange 2 rows and det A doesnt change. the only number with D = -D is D = 0

2 equal rows is flat in that dimension.

matrix with 2 equal rows has no inverse.

possible to have singular matrix with D = 0 without equal rows.

5. subtracting a multiple of one row from another row leaves D unchanged

t times row 1 subtracted from row 2:  
det [ [a,b], [c-t•a, d-t•b] ] 
= det ( [ [a,b], [c,d] ] - t • [ [a,b], [a,b] ] )  <-- rule 3 linearity splits 2 parts and acts on only one (bottom) row  
= det [ [a,b], [c,d] ] - zero <-- rule 4 says duplicate rows have zero determinant

linear combinations leave determinant unchanged as eliminate from A to U

det A = +/- det U depending on row exchanges.

6. a matrix of row of zeros has a det of zero

proof: add another row in the matrix to the zero row (rule 5) and the determinant is still zero (rule 5) because there are now duplicate rows (rule 4)

proof: multiply zero row by t=2 causes det A to be multiplied by t=2 (rule 3)but the matrix is the same adn so det A must also be unchanged.  Only 0 has this feature: t • matrix --> determinant unchanged.

7.  det of triangular A = product of diagonal components for L or U

proof: if U or L eliminate to a diagonal matrix by subtraction of one row multiple from another --> det unchanged (rule 5). then factor A's diagonal elements from a<sub>jj</sub> to 1  (rule 3) --> a<sub>jj</sub> (det I) = det A a<sub>jj</sub> = a<sub>jj</sub> • 1 ()rule 1)

if a<sub>jj</sub> = 0 then det A = 0 since a<sub>jj</sub>= 0 is in the product of diagonals, by rule 6 because that row will be all zeros,  and A is singular

8.  if A is singular then det A = 0; if A is invertible then det A ≠ 0

proof: elimination A to U produces zero row --> singular and det zero (rule 6) and if non-zero pivots then det is non zero (rule 7)

9. the determinant of AB is det A times det B: | A | • | B | = | AB |

det [ [a,b], [c,d] ] • det  [ [p,q], [r,s] ] = det [ [ap+br, aq+bs], [cp+dr, cq+ds] ] 
= (ad-bc) ( ps-qr) = (ap+br)(cq+ds) - (aq+bs)(cp+dr)

when matrix B = A<sup>-1</sup>:
|AB| = |AA<sup>-1</sup>| = | I | = |A| |A<sup>-1</sup>| = 1 thus rule 9 implies that |A<sup>-1</sup>| = 1 / |A|

proof for n x n matrices: det A = det AB / det B. if A has all 3 properties of rules 1, 2 and 3 then det A has to be the determinant of A adn so |AB| / |B| = |A|.  How to check if A has properties 1,2, and 3?

property 1 says determinant of I is 1. thus if A = I then ratio det A = det IB / det B = |B| / |B| = 1

property 2 says sign reversal on row exchanges: when two rows of A are swapped, then the same two rows of AB are swapped.  thus, |AB| changes sign and so does ratio of |AB| / |B| 

property 3 says linearity : t multiplies row 1 of A then it also multiplies row 1 of AB and t multiplies the det AB.  So the ratio |AB| / |B| is multiplied by t.  linearity also says that if you add row 1 of A to row 1 of A' (where other rows are same) then row one of AB adds to row 1 of A'B. after dividing by |B| the ratios add as desired. 

|AB| / |B| has same 3 properties as define |A|.  therefore |AB| / |B| = |A| and this proves the produce rule |AB| = |A| |B|
The case of |B| = 0 and dividing by zero is easily resolved because |AB| is singular when B is singular.  then |AB| = |A||B| = |A|•zero.

10.  the transpose of A<sup>T</sup> has the same determinant as A

| A<sup>T</sup> | = | A |

det [ [a,b], [c,d] ] = det [ [a,c], [b,d] ] = ad - bc

the equation | A<sup>T</sup> | = | A | becomes 0 = 0 for singular matrix transposes

det PA = LU = det (PA)<sup>T</sup> = det (LU)<sup>T</sup> = | A<sup>T</sup>P<sup>T</sup> | = | U<sup>T</sup>L<sup>T</sup> |

proof: by rule 9, |AB| = |A| |B| and then |L| = |L<sup>T</sup>| = 1 because L has 1s on diagonal.  |U| = |U<sup>T</sup>| because triangular matrice tranposes have same diagonal.

the proof disintegrates here but essentially PA = LU where L = 1 and P = 1

P<sup>T</sup>P = I so |P| |P<sup>T</sup>| = 1 by rule 9 and so |P| and |P<sup>T</sup>| are both -1 or 1.  [??]

this leaves det A = det A<sup>T</sup> ??

by rule 10, every rule for rows applies to columns just by transposing A.
- determinant changes sign when columns exchanged
- zero column or 2 equal columns makes determinant zero
- column multiplied by t then the determinant is multiplied by t
- determinant is a linear function of each column separately

review:

the determinant is defined by det I = 1, sign reversal, and linearity in each row (column)

after elimination, det A is +/- product of pivots

determinant is zero exactly when A is not invertible

2 remarkable properties are:
 
 det AB = det A det B
 
 det A<sup>T</sup> = det A



Unrelated from problem 7: Pythagorian Trig Identities are easily understood if think of H = hypotenuse length H = radius of circle as the vector length whose x = cos and y = sin.  Opposite O is opposite of an angle.  O = y = sin if radius is unit.  A = cos theta = x if H is unit radius: 
- sin theta = O / H = just a means of scaling the y component to the length of the hypotenuse.  if H = 1 then just read off the y
- cos theta = A / H
- O = H sin theta
- A = H cos theta
- H<sup>2</sup> = O<sup>2</sup> + A<sup>2</sup>
- H<sup>2</sup> = (H sin theta)<sup>2</sup> + (H cos theta)<sup>2</sup>
- H<sup>2</sup> = H<sup>2</sup>(sin<sup>2</sup>theta) + H<sup>2</sup>(cos<sup>2</sup>theta)
- 1 = sin<sup>2</sup>theta + cos<sup>2</sup>theta


orthogonal matrix 

orthonormal vectors have unit length and are orthogonal to one another.   
a matrix with orthonormal columns is assigned the special letter Q.  
Q easy to work with because Q<sup>T</sup>Q = I   
Q is not required to be square.   
when Q square, Q<sup>T</sup>Q = QQ<sup>T</sup> = I means that QT=Q-1
Q that is square
called orthogonal matrix not orthonormal matrix
inverse from LHS and RHS too rows of square Q are orthonormal too inverse is transpose

every orthogonal matrix Q [where Q<sup>T</sup>Q = QQ<sup>T</sup> = I] has determinant 1 or -1 because | Q<sup>T</sup>Q = I | = | Q<sup>T</sup> | | Q | = | Q |<sup>2</sup> = 1 and so det Q is either -/+ 1 

Q<sup>n</sup> stays orthogonal and so its determinanet doesnt blow up as n --> ∞

if entries in every row of A add to zero then Ax = 0.  obvious since null space = (1,1, ... , 1,1)  and so it is singular and by rule 8 it has det A = 0 

if entries in every row of A add to 1 then (A-I)x = 0 and similarly, the null space indicates singular and so det A = 0, but it doesnt mean det (A-I) = 0 since all rows are having 1s added to them.

prove every orthgonal matrix Q<sup>T</sup> has a determinant 1 or -1

Q<sup>T</sup>Q = I --> | Q<sup>T</sup> | | Q | = Q<sup>2</sup> = I --> | Q | = +/- 1

skew symmetric matrix: A = -A<sup>T</sup>

odd dimensioned skew symmetrix matrices determinants = 0 because det (K<sup>T</sup>) = det (-K) = -1<sup>n</sup> det(K) because to pull the -1 out you need to raise it to the dimension of the matrix.

if you do one row add to another row the determinant doesnt change but if you do two row operations at the same time then the determinant changes.  

det [ [a,b], [c,d] ] = ad - bc

det [ [a-c,b-d], [c,d] ] = (a-c)d - (b-d)c = ad - cd - bc + dc = ad - bc

det [ [a-c,b-d], [c-a,d-b] ] = (a-c)(d-b) - (b-d)(c-a) = ad - cd - ab + cb - bc + dc -da  + ba ≠ ad - bc

rules 5 and 3 produce rule 2

falsities:

the determinant of A is always the product of its pivots.  Nope.  you forget that row exchanges cause -1 factors

the determinant of A -B equals det A - det B.  Nope.  determinants are additive in one row only.  example: A = 2I and B = I have A - B = I but determinant = [ 2<sup>n<sup> for A = 2I ] minus [ 1 for B = I ]

truths

det AB = det A det B

whats wrng with the proof that a projection matrix has det P = `1 ?

P = A<sup>T</sup>(A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup> so det P = (|A| / |A<sup>T</sup>A|) • |A| = 1

the problem is that A is rectangular and so det (A<sup>T</sup>A) ≠ (det A<sup>T</sup>)(det A).  Those determinants are not defined. in fact if A is tall and thin (m>n) then det (A<sup>T</sup>A) adds up to |det B\<sup>2</sup> where B's are all the nxn submatrices of A.  ???haah 

section 5.2

2x2 matrix has det = ad - bc which has 2! terms with +/- signs  
nxn matrix has det A which has n! terms with +/- signs.

for determinant formulas each row appears once in every row and every column appear once in every term.  for example, in a 3x3, two of the n! = 3! = 6 terms are a<sub>12</sub>a<sub>23</sub>a<sub>31</sub> and -a<sub>13</sub>a<sub>22</sub>a<sub>31</sub>.  row 1, 2, 3 appear in each term and column 1, 2, 3 appear in each term but only once each row and column in each term.  using rows 1, 2, 3 as done in both terms requires no row exchanges.  using columns 2, 3, 1 as in the 1st term requires two column exchanges 1 swapped with 2 making 2, 1, 3 and then 1 swapped with 3 making 2, 3, 1.  an even number of column swaps, 2 in 1st term, leads to -1<sup>2</sup> = +1 factor on that first term of the determinant.  using columns 3, 2, 1 in the 2nd term requires one or an odd number of column exchanges from 1, 2, 3 to 3, 2, 1 and so the factor on that term of the determinant is -1<sup>1<sup> = -1.

the six terms include a<sub>11</sub>a<sub>22</sub>a<sub>33</sub> - a<sub>11</sub>a<sub>23</sub>a<sub>32</sub> = a<sub>11</sub>(a<sub>22</sub>a<sub>33</sub> - a<sub>23</sub>a<sub>32</sub>) where a<sub>11</sub> is multiplying the cofactor C<sub>11</sub> = a<sub>22</sub>a<sub>33</sub> - a<sub>23</sub>a<sub>32</sub>.

always det A = a<sub>11</sub>C<sub>11</sub> + a<sub>12</sub>Ca<sub>12</sub> + a<sub>1n</sub>C<sub>1n</sub>.  cofactors are determinants of size n-1

computer finds determinant from pivots via elimination.

here uses 2 formulas:   
big formula uses all n! permutations  
cofactor formula uses determinants of size n-1

use this as example.

A = 
[
[ 2, -1, 0, 0],
[-1, 2, -1, 0],
[0, -1, 2, -1],
[0, 0, -1, 2]
]

1. pivots are 2 • 3/2 • 4/3 • 5/4 from elimination to LU; all numerators and denominators cancel --> det A = 5

L = 
[
[1,0,0,0],
[-1/2,1,0,0],
[0,-2/3,1,0],
[0,0,0,-3/4,1]
]

U =
[
[2,-1,0,0],
[0,3/2,-1,0],
[0,0,4/3,-1],
[0,0,0,5/4]
]

2. big formual has n! = 4! terms of which only 5 are non-zero.

det A = 16 - 4 - 4 -4 + 1 = 5

the 16 comes from 2 • 2 • 2 • 2 on the diagonal selecting one of each column and row only once = a<sub>11</sub> • a<sub>22</sub> • a<sub>33</sub> • a<sub>44</sub>.  when you know where -4 and +1 come from you know the big formula.

3. 2, -1, 0, 0 in 1st row multiply their cofactors 4, 3, 2, 1 from the other rows giving 2 • 4 - 1 • 3 + 0 • 2 + 0 • 1 = 5.  

The cofactors are are 3x3 determinants. Every term in a determinant uses each row and column once. 

pivot formula

elimination -> PA = LU = LDU

det P det A = det L det U = det L det D det U = (1) • (d<sub>1</sub>, • ... • , d<sub>n</sub>) • (1)

det A = +/- d<sub>1</sub> • ... • d<sub>n</sub>

example:

[
[0,0,1],
[0,2,3],
[4,5,6]
]

requires 1 row exchange ( 1 <--> 3 ) via P

det A = -1 • 4 • 2 • 1 = 8

example:

-1 2 -1 tridiagonal matrix --> factors to U with -1 off diagonal and 2 • 3/2 • 4/3 • ... • n+1/n on the diagonal. 

so det A = n+1 since all the numerators and denominators of the diagonal fractions cancel except the last which is n+1

important rule: for all matrices without row exchanges, the 1st pivot depends only on the top left entry which never changes in elimination.  thus the determinant of that submatrix, the top left corner cell, is A<sub>k</sub> where k = 1 is the subscript of how far through the diagononal from 1 to n the determinant calculation has progressed.

elimination deals witg the matrix A<sub>k</sub> in the UL corner.  A<sub>k</sub> = L<sub>k</sub>U<sub>k</sub>. 

dividing one determinant A<sub>k</sub> by the previous determinant A<sub>k-1</sub> cancels everything except the latest pivot d<sub>k</sub>

thus, each pivot is a ratio of the determinants of sub matrices A<sub>k</sub>/A<sub>k-1</sub>

so one can obtain the pivots from determinants: 

the kth pivot is d<sub>k</sub> = (d<sub>1</sub>•d<sub>2</sub>• ... •d<sub>k</sub>)/(d<sub>1</sub>•d<sub>2</sub>• ... •d<sub>k-1</sub>) = det Asub>k</sub>/det Asub>k-1</sub>

the math is easy: 

(d<sub>1</sub>•d<sub>2</sub>• ... •d<sub>k</sub>)/(d<sub>1</sub>•d<sub>2</sub>• ... •d<sub>k</sub>) = (d<sub>1</sub>•d<sub>2</sub>• ... •d<sub>k</sub>)/(d<sub>1</sub>•d<sub>2</sub>• ... •d<sub>k</sub>)

now divide LHS by by (d<sub>1</sub>•d<sub>2</sub>• ... •d<sub>k</sub>)/(d<sub>1</sub>•d<sub>2</sub>• ... •d<sub>k-1</sub>) and all but d<sub>k</sub>) cancel on LHS and you have the ratio shown above which equals det A<sub>k</sub> / det A<sub>k-1</sub>

do not need row exchanges when all UL matrices have det A ≠ 0

the big formula:

pivots concentrate a lot of information into one number.  included in that information is the determinant, but it is difficult to connect the determinant to the original a<sub>ij</sub>.  rules 1-3 provide clues to connect to original data: linearity, sign reversal, det I = 1 help derive a single explicit formula for determinants, directly from a<sub>ij</sub>.

the big formula has n! terms: for n=11, there are 40 million terms. 

half of terms have minus signs e.g. -bc while 50% have positive e.g. ac.

each term has one entry from each column and row.  if the order of the terms' subscripts are different from 123...n, then a +/- 1 comes into play. permutations tell us the sign.  for n=4, there are 24 ways, n!, to choose entruy from each row and column.  down the diagonal the column order is 111 2222 3333 4444 called the 'identity permutation'.

deriving the big formula break each row into 2 simpler rows:

A =
[
[a,b],
[c,d]
]

all the following math occurs inside of determinant brackets |A| that arent shown. 

[a,b] = [a,0] + [0,b]  
[c,d] = [c,0] + [0,d]  

apply linearity to arrive at 2<sup>2</sup> = 4 combinations that boil down to 2! = 2

break up the first row first:
[
[a,b],
[c,d]
]
= [
[a,0],
[c,d]
]
+ [
[0,b],
[c,d]
]

then the complete set is shown after breaking the second row:
[
[a,b],
[c,d]
]
= [
[a,0],
[c,0]
]
+ [
[a,0],
[0,d]
]
+ [
[0,b],
[c,0]
]
+ [
[0,b],
[0,d]
]

any with only zeros in columns have zero determinants

[
[0,b],
[0,d]
]
and
[
[a,0],
[c,0]
]

leaves 2! determinants to compute

[
[a,b],
[c,d]
]
= [
[a,0],
[0,d]
]
+ [
[0,b],
[c,0]
]

strang uses P to put the factors into identity form to show the alternating -1 factor
because there is no determinant calculation for the off diagonals; only a rule for the diagonals.

splitting led to permutation matrices whose determinants give a +1 or -1 factor
det (
[
[a,b],
[c,d]
]
)
= det (
[
[1,0],
[0,1]
]
[
[a,0],
[0,d]
]
)
+
det (
[
[0,1],
[1,0]
]
[
[0,b],
[c,0]
]
)
= +1 • det (
[
[a,0],
[0,d]
]
)
+ 
-1 • det (
[
[b,0],
[0,d]
]
)

in 3 dimensioned matrix there are 3<sup>3</sup> simpler matrices that boil down to 3! nonzero determinants. zero determinants are where each column or row is used MORE than once in a simplified matrix:

det [
[a<sub>11</sub>,0,0]
[a<sub>21</sub>,0,0]
[0,a<sub>12</sub>,0,0]
] = 0

of the 6 permutations of 1,2,3 there is one identity permutation and 5 where P ≠ I.

123, 231, 312, 132, 213, 321 are the six where the first 3 are even and the last 3 are odd.  odd permutations require an odd number of column or row swaps and have determinant of P = -1

as you choose column permutation, rows are automatically chosen since you choose a column for a row, e.g. row 1, and then no other columns are chosen for that row.  then you move to the next row.

the determinant is the sum of these simple determinants that are a product of P<sup>+</sup> or P<sup>-</sup> that reorders the simple matrix with one entry in each row in a different column into a diagonal matrix which can then have its determinant determined by rule 7 about U matrices.


when A is U, only one of the n! products can be non-zero, and that is from the diagonal.  all other column orderings pick at least one entry below the diagonal which is zero.

determinants by cofactors

the big formula's n! terms satisfy rules 1,2,3 then all other properties 4-10 follow.  the result is the simple matrices separating row items one at a time until n! terms.  one can separate each row into n-1 sets:

n = 3 
det A = 
a<sub>11</sub>(a<sub>22</sub>a<sub>33</sub> - a<sub>23</sub>a<sub>32</sub>) +
a<sub>12</sub>(a<sub>23</sub>a<sub>31</sub> - a<sub>21</sub>a<sub>33</sub>) +
a<sub>13</sub>(a<sub>21</sub>a<sub>32</sub> - a<sub>22</sub>a<sub>31</sub>) 

quantities in paranethese are cofactors which are 2x2 determinants from 2nd and 3rd row.

lower rows contribute these cofactors C<sub>11</sub>, C<sub>12</sub>, C<sub>13</sub> 

using linearity, can split A into 6 permutations that group into three 2x2 cofactors one for each of the 3 components of the first row.

watch signs:  
the 2x2 that goes with a<sub>11</sub> is positive, but the 2x2 that goes with a<sub>12</sub>.

systematically, cofactors are C<sub>ij</sub> = (-1)<sup>i+j</sup> det M<sub>ij</sub> where for the first row, all i's are 1.  So for the determinant calculation

det A = ∑ i =1, j from 1 to n of a<sub>ij</sub>C<sub>ij</sub> 

= a<sub>ij</sub> (-1)<sup>i+j</sup> det M<sub>ij</sub>

recursively, move from cofactors with determinants of order n -1 to n-2 to 1

key properties are 1-3 : linearity, sign reversal and I =1

since det A = det A<sup>T</sup> cofactors can be formed for columns instead of rows.

cofactors are useful when matrices have many zeros

hessenberg matrix is a triangular matrix with one extra diagonal whose determinant follows the rule of |H<sub>4</sub>| = |H<sub>3</sub>| + |H<sub>2</sub>| or generally |H<sub>n</sub>| = |H<sub>n-1</sub>| + |H<sub>n-2</sub>| 

the cofactor C<sub>11</sub> for H<sub>4</sub> is the determinant |H<sub>3</sub>| 

since there is an additional diagonal ontop the triangular matrix L, need another cofactor C<sub>12</sub> for cell a<sub>12</sub> but of course it is factored by -1<sup>1+2</sup>  = -1.  

C<sub>11</sub> is H3 and C<sub>12</sub> is H2

so | H<sub>4</sub> | =  2 • | H<sub>3</sub> | - 1 • | H<sub>3</sub> | + 1 • | H<sub>2</sub> |

| H<sub>n</sub> | = 2, 3, 5, 8 for n = 1, 2, 3, 4 and so follows Fibonacci | H<sub>n</sub> | = F<sub>n+2</sub>


question  
if A is 10x10 all ones how does the big formula give det A = 0  
all products in big formula are 1 since all elements of matrix are 1.  half require even (1) and half require odd (-1) permutations which sum to 0 and of course an all 1s matrix has det A = 0 anyway. 

for n = 2 and 3 the product of all n! permutation matrices is odd.  for n > 3 the product of all permutation matrices is even. 

a 3x3 matrix of only 1s and -1s can have 4 as its largest determinant because the determinant formula for 3x3 has 3! = 6 terms all + or - 1.  

can group the cofactor results into matrix C and the source matrix A and AC<sup>T</sup> = (det A)I because a<sub>ij</sub> is multiplied with C<sub>ij</sub> and the products are summed. since C = C<sup>T</sup> can use AC<sup>T</sup> or C<sup>T</sup>A.


section 5.3 

cramers rule, inverses and volumes

principles:

A<sup>-1</sup> = C<sup>T / </sup>det A  
then (A<sup>-1</sup>)<sub>ij</sub> = cofactor C<sub>-ij</sub> divided by det A  

cramers rule computes x = A<sup>-1</sup>b from x<sub>j</sub> = det(A with column j changed to b) / det A

area of parallelogram = | ad - bc | if the four corners are (0,0), (a,b), (c,d) and (a+c, b+d)

volumn of box = | det A | if the rows of A (or columns of A) give the sides of the box.  

the cross product of w = u x v is =  
| i   j   k  |   
| u<sub>1</sub> u<sub>2</sub> u<sub>3</sub> |   
| v<sub>1</sub> v<sub>2</sub> v<sub>3</sub> |

v x u = =(u x v)    
w<sub>1</sub>, w<sub>2</sub>, w<sub>3</sub> are cofactors of row 1  
w<sup>T</sup>u and w<sup>T</sup>v = 0

detail:

this section :  
- solves Ax = b.   
- finds A<sup>-1</sup> by algebra not elimination.    
- all formulas divide by det A.  
- each entry in A<sup>-1</sup> and A<sup>-1</sup>b is a determinant divided by the determinant of A.  

this formula is very complex to construct and for a 3x3 A multiplying a 3x3 X to get a 3x3 I so that X ends up being A<sup>-1</sup> there is a lot of substitution and subscripts.  I dont think it's possible to put it here with out a lot of work and not sure there is a benefit to knowing the construction of the algebra you end up with.

key idea 

using artificially constructed x or X and artificially constructed b or B to find x or A<sup>-1</sup>:

one example is Ax = b  
another is AX = I to find A<sup>-1</sup>  
which is more interesting  
and he goes on to do that for a 3x3  

the four 2x2's have x vector and y vector component unknowns on the LHS solving for 0s and 1s on the b side RHS.  The a, b, c, and d on LHS and RHS are merely numbers that we can plug into the formula to verify. 

the x<sub>j</sub>'s of X are solving for the (1,0) of B which is I identity since X is A's inverse = A<sup>-1</sup>.  

the x<sub>j</sub>'s and y<sub>j</sub>'s are put in an identity matrix so that their determinant solves to just one of the 4 X components.  So they are inserted into an identity matrix that gives only 1s on the diagonal and zeros everywhere else (i.e. lower or upper triangular) that solves to a determinant of x<sub>1</sub>, or x<sub>2</sub>. or y<sub>1</sub> or y<sub>2</sub>.

The objective of this set up is to have determinant of X on LHS get to x<sub>j</sub> and y<sub>j</sub> and our correct b on the RHS.  The x<sub>j</sub>'s should go to a b = (1,0) of I on the RHS and the y<sub>j</sub>'s should go to (0,1) of I on the RHS.  To get to the x<sub>1</sub> that yields (1,0) on the RHS, need to have x<sub>1</sub> in a lower triangular matrix so det of that X = x<sub>1</sub>; to have x<sub>1</sub> in a lower triangular the x<sub>j</sub>'s need to be on the LHS of X and the (1,0) thus are on the LHS of the B.  To get x<sub>2</sub> that yields (1,0) on the RHS, need to have x<sub>2</sub> in an upper triangular matrix so det of that X = x<sub>2</sub>; to have x<sub>2</sub> in a upper triangular, the x<sub>j</sub>'s need to be on the RHS of X and the (1,0) thus are on the RHS of the B.

![\begin{bmatrix}
A
\end{bmatrix}
= \begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
\begin{bmatrix}
x_1&0\\
x_2&1
\end{bmatrix}
=\begin{bmatrix}
ax_1 + bx_2&b\\
cx_1 + dx_2&d
\end{bmatrix} 
=\begin{bmatrix}
1&b\\
0&d
\end{bmatrix}-take-the-determinant->|A| (x_1) = |B_1|
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0AA%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0Ac%26d%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%260%5C%5C%0Ax_2%261%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0Aax_1+%2B+bx_2%26b%5C%5C%0Acx_1+%2B+dx_2%26d%0A%5Cend%7Bbmatrix%7D+%0A%3D%5Cbegin%7Bbmatrix%7D%0A1%26b%5C%5C%0A0%26d%0A%5Cend%7Bbmatrix%7D-take-the-determinant-%3E%7CA%7C+%28x_1%29+%3D+%7CB_1%7C%0A)


![\begin{bmatrix}
A
\end{bmatrix}
= \begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
\begin{bmatrix}
1&x_1\\
0&x_2
\end{bmatrix}
=\begin{bmatrix}
a&ax_1 + bx_2\\
c&cx_1 + dx_2
\end{bmatrix} 
=\begin{bmatrix}
a&1\\
c&0
\end{bmatrix}-take-the-determinant->|A| (x_2) = |B_2|](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0AA%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0Ac%26d%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26x_1%5C%5C%0A0%26x_2%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0Aa%26ax_1+%2B+bx_2%5C%5C%0Ac%26cx_1+%2B+dx_2%0A%5Cend%7Bbmatrix%7D+%0A%3D%5Cbegin%7Bbmatrix%7D%0Aa%261%5C%5C%0Ac%260%0A%5Cend%7Bbmatrix%7D-take-the-determinant-%3E%7CA%7C+%28x_2%29+%3D+%7CB_2%7C)

the y<sub>j</sub>'s of X are solving for the (0,1) of B which is I identity since X is A's inverse = A<sup>-1</sup>.  

The objective of this set up is to have determinant of X on LHS get to x<sub>j</sub> and y<sub>j</sub> and our correct b on the RHS.  The x<sub>j</sub>'s should go to a b = (1,0) of I on the RHS and the y<sub>j</sub>'s should go to (0,1) of I on the RHS.  To get to the y<sub>1</sub> that yields (0,1) on the RHS, need to have y<sub>1</sub> in a lower triangular matrix so det of that X = y<sub>1</sub>; to have y<sub>1</sub> in a lower triangular the y<sub>j</sub>'s need to be on the LHS of X and the (0,1) thus are on the LHS of the B.  To get y<sub>2</sub> that yields (0,1) on the RHS, need to have y<sub>2</sub> in an upper triangular matrix so det of that X = y<sub>2</sub>; to have y<sub>2</sub> in a upper triangular, the y<sub>j</sub>'s need to be on the RHS of X and the (0,1) thus are on the RHS of the B.

![\begin{bmatrix}
A
\end{bmatrix}
= \begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
\begin{bmatrix}
y_1&0\\
y_2&1
\end{bmatrix}
=\begin{bmatrix}
ay_1 + by_2&b\\
cy_1 + dy_2&d
\end{bmatrix} 
=\begin{bmatrix}
0&b\\
1&d
\end{bmatrix}-take-the-determinant->|A| (y_1) = |B_3|
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0AA%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0Ac%26d%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ay_1%260%5C%5C%0Ay_2%261%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0Aay_1+%2B+by_2%26b%5C%5C%0Acy_1+%2B+dy_2%26d%0A%5Cend%7Bbmatrix%7D+%0A%3D%5Cbegin%7Bbmatrix%7D%0A0%26b%5C%5C%0A1%26d%0A%5Cend%7Bbmatrix%7D-take-the-determinant-%3E%7CA%7C+%28y_1%29+%3D+%7CB_3%7C%0A)

![\begin{bmatrix}
A
\end{bmatrix}
= \begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
\begin{bmatrix}
1&y_1\\
0&y_2
\end{bmatrix}
=\begin{bmatrix}
a&ay_1 + by_2\\
c&cy_1 + dy_2
\end{bmatrix} 
=\begin{bmatrix}
a&0\\
c&1
\end{bmatrix}-take-the-determinant->|A| (y_2) = |B_4|
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0AA%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0Ac%26d%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26y_1%5C%5C%0A0%26y_2%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0Aa%26ay_1+%2B+by_2%5C%5C%0Ac%26cy_1+%2B+dy_2%0A%5Cend%7Bbmatrix%7D+%0A%3D%5Cbegin%7Bbmatrix%7D%0Aa%260%5C%5C%0Ac%261%0A%5Cend%7Bbmatrix%7D-take-the-determinant-%3E%7CA%7C+%28y_2%29+%3D+%7CB_4%7C%0A)

this explodes in complications of subscripts when go to 3x3. To see that go to yellow notes. 

for this one, 

x<sub>1</sub> = |B<sub>1</sub>| / |A| = (factor = 1<sup>1+1</sup>) • (cofactor = d) / (ad-bc) 

x<sub>2</sub> = |B<sub>2</sub>| / |A| = (factor = 1<sup>1+2</sup>) • (cofactor = c) / (ad-bc) 

y<sub>1</sub> = |B<sub>3</sub>| / |A| = (factor = 1<sup>2+1</sup>) • (cofactor = b) / (ad-bc) 

y<sub>2</sub> = |B<sub>4</sub>| / |A| = (factor = 1<sup>2+2</sup>) • (cofactor = a) / (ad-bc) 

A<sup>-1</sup> = 
[
[d,-b],
[-c,a]
]

\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
x_11&0&0\\
x_21&1&0\\
x_31&0&1\\
\end{bmatrix}
= \begin{bmatrix}
a_11x_11+a_12x_21+a_13x_31=1&a_12&a_13\\
a_21x_11+a_22x_21+a_23x_31=0&a_22&a_23\\
a_31x_11+a_32x_21+a_33x_31=0&a_32&a_33\\
\end{bmatrix}
= B_11



so for 3 dimensions:  

X is A<sup>-1</sup>  
b =  a column of I which we will label b<sub>1</sub> for 1st column of I

B is the result of AX; notice that subscripts of B matrices are reversed of the X matrix because the 1 in the B matrices (that comes from their I column) is what directs the labeling of the B matrix subscripts because that 1 in each B is the factor and the remainder of the B is the cofactor for computing the determinant of B.  These will be same subscripts used for cofactor C<sub>ji</sub> and it's embedded matrix M<sub>ji</sub>. 

for 1st column of X = X<sub>1</sub> = A<sup>-1</sup> on LHS that will eventually bring 1st column of I = (1,0,0) on RHS:  

this gets you the first row of X<sub>1</sub> = X<sub>11</sub>:   
[ A<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ][ X<sub>1</sub> I<sub>2</sub> I<sub>3</sub> ] = [ I<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ] = B<sub>11</sub>

this gets you the second row of X<sub>1</sub> = X<sub>21</sub>:   
[ A<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ][ I<sub>1</sub> X<sub>1</sub> I<sub>3</sub> ] = [ A<sub>1</sub> I<sub>1</sub> A<sub>3</sub> ] = B<sub>12</sub>

this gets you the third row of X<sub>1</sub> = X<sub>31</sub>:   
[ A<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ][ I<sub>1</sub> I<sub>2</sub> X<sub>1</sub> ] = [ A<sub>1</sub> A<sub>2</sub> I<sub>1</sub> ] = B<sub>13</sub>

for 2nd column of X = X<sub>2</sub> = A<sup>-1</sup> on LHS that will eventually bring 2nd column of I = (0,1,0) on RHS:  

this gets you the first row of X<sub>2</sub> = X<sub>12</sub>:   
[ A<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ][ X<sub>2</sub> I<sub>2</sub> I<sub>3</sub> ] = [ I<sub>2</sub> A<sub>2</sub> A<sub>3</sub> ] = B<sub>21</sub>

this gets you the second row of X<sub>2</sub> = X<sub>22</sub>:   
[ A<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ][ I<sub>1</sub> X<sub>2</sub> I<sub>3</sub> ] = [ A<sub>1</sub> I<sub>2</sub> A<sub>3</sub> ] = B<sub>22</sub>

this gets you the third row of X<sub>2</sub> = X<sub>32</sub>:   
[ A<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ][ I<sub>1</sub> I<sub>2</sub> X<sub>2</sub> ] = [ A<sub>1</sub> A<sub>2</sub> I<sub>2</sub> ] = B<sub>23</sub>

for 3rd column of X = X<sub>3</sub> = A<sup>-1</sup> on LHS that will eventually bring 3rd column of I = (0,0,1) on RHS:  

this gets you the first row of X<sub>3</sub> = X<sub>13</sub>:   
[ A<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ][ X<sub>3</sub> I<sub>2</sub> I<sub>3</sub> ] = [ I<sub>3</sub> A<sub>2</sub> A<sub>3</sub> ] = B<sub>31</sub>

this gets you the second row of X<sub>3</sub> = X<sub>23</sub>:   
[ A<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ][ I<sub>1</sub> X<sub>3</sub> I<sub>3</sub> ] = [ A<sub>1</sub> I<sub>3</sub> A<sub>3</sub> ] = B<sub>32</sub>

this gets you the third row of X<sub>3</sub> = X<sub>33</sub>:   
[ A<sub>1</sub> A<sub>2</sub> A<sub>3</sub> ][ I<sub>1</sub> I<sub>2</sub> X<sub>3</sub> ] = [ A<sub>1</sub> A<sub>2</sub> I<sub>3</sub> ] = B<sub>33</sub>




![\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
x_11&0&0\\
x_21&1&0\\
x_31&0&1\\
\end{bmatrix}
= \begin{bmatrix}
a_11x_11+a_12x_21+a_13x_31=1&a_12&a_13\\
a_21x_11+a_22x_21+a_23x_31=0&a_22&a_23\\
a_31x_11+a_32x_21+a_33x_31=0&a_32&a_33\\
\end{bmatrix}
= B_11](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_13%5C%5C%0Aa_21%26a_22%26a_23%5C%5C%0Aa_31%26a_32%26a_33%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_11%260%260%5C%5C%0Ax_21%261%260%5C%5C%0Ax_31%260%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa_11x_11%2Ba_12x_21%2Ba_13x_31%3D1%26a_12%26a_13%5C%5C%0Aa_21x_11%2Ba_22x_21%2Ba_23x_31%3D0%26a_22%26a_23%5C%5C%0Aa_31x_11%2Ba_32x_21%2Ba_33x_31%3D0%26a_32%26a_33%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+B_11)


![\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
1&x_11&0\\
0&x_21&0\\
0&x_31&1\\
\end{bmatrix}
= \begin{bmatrix}
a_11&a_11x_11+a_12x_21+a_13x_31=1&a_13\\
a_21&a_21x_11+a_22x_21+a_23x_31=0&a_23\\
a_31&a_31x_11+a_32x_21+a_33x_31=0&a_33\\
\end{bmatrix}
= B_12](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_13%5C%5C%0Aa_21%26a_22%26a_23%5C%5C%0Aa_31%26a_32%26a_33%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26x_11%260%5C%5C%0A0%26x_21%260%5C%5C%0A0%26x_31%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_11x_11%2Ba_12x_21%2Ba_13x_31%3D1%26a_13%5C%5C%0Aa_21%26a_21x_11%2Ba_22x_21%2Ba_23x_31%3D0%26a_23%5C%5C%0Aa_31%26a_31x_11%2Ba_32x_21%2Ba_33x_31%3D0%26a_33%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+B_12)

![\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
1&0&x_11\\
0&1&x_21\\
0&0&x_31\\
\end{bmatrix}
= \begin{bmatrix}
a_11&a_12&a_11x_11+a_12x_21+a_13x_31=1\\
a_21&a_22&a_21x_11+a_22x_21+a_23x_31=0\\
a_31&a_32&a_31x_11+a_32x_21+a_33x_31=0\\
\end{bmatrix}
= B_13](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_13%5C%5C%0Aa_21%26a_22%26a_23%5C%5C%0Aa_31%26a_32%26a_33%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%26x_11%5C%5C%0A0%261%26x_21%5C%5C%0A0%260%26x_31%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_11x_11%2Ba_12x_21%2Ba_13x_31%3D1%5C%5C%0Aa_21%26a_22%26a_21x_11%2Ba_22x_21%2Ba_23x_31%3D0%5C%5C%0Aa_31%26a_32%26a_31x_11%2Ba_32x_21%2Ba_33x_31%3D0%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+B_13)

![\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
x_12&0&0\\
x_22&1&0\\
x_32&0&1\\
\end{bmatrix}
= \begin{bmatrix}
a_11x_12+a_12x_22+a_13x_32=0&a_12&a_13\\
a_21x_12+a_22x_22+a_23x_32=1&a_22&a_23\\
a_31x_12+a_32x_22+a_33x_32=0&a_32&a_33\\
\end{bmatrix}
= B_21](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_13%5C%5C%0Aa_21%26a_22%26a_23%5C%5C%0Aa_31%26a_32%26a_33%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_12%260%260%5C%5C%0Ax_22%261%260%5C%5C%0Ax_32%260%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa_11x_12%2Ba_12x_22%2Ba_13x_32%3D0%26a_12%26a_13%5C%5C%0Aa_21x_12%2Ba_22x_22%2Ba_23x_32%3D1%26a_22%26a_23%5C%5C%0Aa_31x_12%2Ba_32x_22%2Ba_33x_32%3D0%26a_32%26a_33%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+B_21)

![\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
1&x_12&0\\
0&x_22&0\\
0&x_32&1\\
\end{bmatrix}
= \begin{bmatrix}
a_11&a_11x_12+a_12x_22+a_13x_32=0&a_13\\
a_21&a_21x_12+a_22x_22+a_23x_32=0&a_23\\
a_31&a_31x_12+a_32x_22+a_33x_32=1&a_33\\
\end{bmatrix}
= B_22
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_13%5C%5C%0Aa_21%26a_22%26a_23%5C%5C%0Aa_31%26a_32%26a_33%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26x_12%260%5C%5C%0A0%26x_22%260%5C%5C%0A0%26x_32%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_11x_12%2Ba_12x_22%2Ba_13x_32%3D0%26a_13%5C%5C%0Aa_21%26a_21x_12%2Ba_22x_22%2Ba_23x_32%3D1%26a_23%5C%5C%0Aa_31%26a_31x_12%2Ba_32x_22%2Ba_33x_32%3D0%26a_33%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+B_22%0A)

![\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
1&0&x_12\\
0&1&x_22\\
0&0&x_32\\
\end{bmatrix}
= \begin{bmatrix}
a_11&a_12&a_11x_12+a_12x_22+a_13x_32=0\\
a_21&a_22&a_21x_12+a_22x_22+a_23x_32=0\\
a_31&a_32&a_31x_12+a_32x_22+a_33x_32=1\\
\end{bmatrix}
= B_23](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_13%5C%5C%0Aa_21%26a_22%26a_23%5C%5C%0Aa_31%26a_32%26a_33%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%26x_12%5C%5C%0A0%261%26x_22%5C%5C%0A0%260%26x_32%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_11x_12%2Ba_12x_22%2Ba_13x_32%3D0%5C%5C%0Aa_21%26a_22%26a_21x_12%2Ba_22x_22%2Ba_23x_32%3D1%5C%5C%0Aa_31%26a_32%26a_31x_12%2Ba_32x_22%2Ba_33x_32%3D0%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+B_23)

![\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
x_13&0&0\\
x_23&1&0\\
x_33&0&1\\
\end{bmatrix}
= \begin{bmatrix}
a_11x_13+a_12x_23+a_13x_33=0&a_12&a_13\\
a_21x_13+a_22x_23+a_23x_33=0&a_22&a_23\\
a_31x_13+a_32x_23+a_33x_33=1&a_32&a_33\\
\end{bmatrix}
= B_31
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_13%5C%5C%0Aa_21%26a_22%26a_23%5C%5C%0Aa_31%26a_32%26a_33%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_13%260%260%5C%5C%0Ax_23%261%260%5C%5C%0Ax_33%260%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa_11x_13%2Ba_12x_23%2Ba_13x_33%3D0%26a_12%26a_13%5C%5C%0Aa_21x_13%2Ba_22x_23%2Ba_23x_33%3D0%26a_22%26a_23%5C%5C%0Aa_31x_13%2Ba_32x_23%2Ba_33x_33%3D1%26a_32%26a_33%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+B_31%0A)

![\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
1&x_13&0\\
0&x_23&0\\
0&x_33&1\\
\end{bmatrix}
= \begin{bmatrix}
a_11&a_11x_13+a_12x_23+a_13x_33=0&a_13\\
a_21&a_21x_13+a_22x_23+a_23x_33=0&a_23\\
a_31&a_31x_13+a_32x_23+a_33x_33=1&a_33\\
\end{bmatrix}
= B_32](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_13%5C%5C%0Aa_21%26a_22%26a_23%5C%5C%0Aa_31%26a_32%26a_33%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26x_13%260%5C%5C%0A0%26x_23%260%5C%5C%0A0%26x_33%261%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_11x_13%2Ba_12x_23%2Ba_13x_33%3D0%26a_13%5C%5C%0Aa_21%26a_21x_13%2Ba_22x_23%2Ba_23x_33%3D0%26a_23%5C%5C%0Aa_31%26a_31x_13%2Ba_32x_23%2Ba_33x_33%3D1%26a_33%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+B_32)

![\begin{bmatrix}
a_11&a_12&a_13\\
a_21&a_22&a_23\\
a_31&a_32&a_33
\end{bmatrix}
\begin{bmatrix}
1&0&x_13\\
0&1&x_23\\
0&0&x_33\\
\end{bmatrix}
= \begin{bmatrix}
a_11&a_12&a_11x_13+a_12x_23+a_13x_33=0\\
a_21&a_22&a_21x_13+a_22x_23+a_23x_33=0\\
a_31&a_32&a_31x_13+a_32x_23+a_33x_33=1\\
\end{bmatrix}
= B_33
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_13%5C%5C%0Aa_21%26a_22%26a_23%5C%5C%0Aa_31%26a_32%26a_33%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%26x_13%5C%5C%0A0%261%26x_23%5C%5C%0A0%260%26x_33%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+%5Cbegin%7Bbmatrix%7D%0Aa_11%26a_12%26a_11x_13%2Ba_12x_23%2Ba_13x_33%3D0%5C%5C%0Aa_21%26a_22%26a_21x_13%2Ba_22x_23%2Ba_23x_33%3D0%5C%5C%0Aa_31%26a_32%26a_31x_13%2Ba_32x_23%2Ba_33x_33%3D1%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%3D+B_33%0A)

![\begin{equation}
   \begin{vmatrix} 
   a_{11} & a_{12} & a_{13}  \\
   a_{21} & a_{22} & a_{23}  \\
   a_{31} & a_{32} & a_{33}  \\
   \end{vmatrix} 
\end{equation}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bequation%7D%0A+++%5Cbegin%7Bvmatrix%7D+%0A+++a_%7B11%7D+%26+a_%7B12%7D+%26+a_%7B13%7D++%5C%5C%0A+++a_%7B21%7D+%26+a_%7B22%7D+%26+a_%7B23%7D++%5C%5C%0A+++a_%7B31%7D+%26+a_%7B32%7D+%26+a_%7B33%7D++%5C%5C%0A+++%5Cend%7Bvmatrix%7D+%0A%5Cend%7Bequation%7D)
