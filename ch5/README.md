
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


