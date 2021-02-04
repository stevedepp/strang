
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

