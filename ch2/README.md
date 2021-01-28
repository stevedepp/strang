chapter 2 matrices

column picture = vector equation = vector space

row picture = dot product = cartesian space

when b vector = zero then one comb x of vectors can be zero.

difficult to see row picture when more than 3d in vector space because then youre talking about more than 3 planes in cartesian space.

EA = U
A = LU

the rank of A after elimination gives dimension of Ax = 0 solutions = null set

to know Ax = b has only x as a solution, must know that A is invertible, A's columns are independent, and the determinant is not zero.  I think these are the same requirement.

exch()  
exchange matrix = exch(n)  
 0  1  
 1  0  

90 rotation matrix  
 0   1  
-1   0  

rotate180(n)  
180 rotation matrix  
 0 -1  
-1  0  

permute(listy)  
permutation matrix  
multiply from the L  
puts row 2 in row 1  
puts row 1 in row 3  
puts row 3 in row 2  
0 1 0  
0 0 1  
1 0 0  
multiply from R  
puts col 3 in col 1  
puts col 1 in col 2  
puts col 2 in col 3  

`rotating degrees`   
`def rotate(d):`  
`       r = d * math.pi / 180`  
`   x = math.cos(r)`  
`   y = math.sin(r)`  
`   return np.array([[x, -y], [y, x]])`  
<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/104539534-bfe40780-55eb-11eb-9eaf-90fef0d49954.png">


matrix represents in row view the equations for 3 planes, all 3 of which slope:

 2  4 -2  2  
 4  8 -4  4  
 4  9 -3  8  
 
finding U and L. 
i = row  
j = column  

i,j is first elimination  
j,j is first pivot  
l is multiplier  =  i,j / j,j  
the matrix is * 1.0 so that it is no longer integer matrix whose components cannot subtract floats.  

[i should provide more comments in code]  
[U is correct; L is not]  

end up with 3 planes, 2 of which slope and 3rd is 4z = 8 is horizontal to xy cartesian plane.  

U x = c = [2,4,8].T  

A x = b = [2,8,10].T  

so x solves both U and A for expected c and b respectively.

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/104740710-4137b900-5716-11eb-8ce9-46cda9aa5b14.png">


<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/104787181-eb3a3400-575c-11eb-8ca5-108d08b6904a.png">



P is permutation matrix that starts as identity matrix and as need row changes in A, P adapts by making changes in I. So, if A needs row 2 and 3 switched then P for this task is I with rows 2 and 3 switched.

E contains the compounded effects of each multiplier, l or -l.  To express the compounded effects of each, use a new matrix E<sub>21</sub> to eliminte item (2,1) in row 2 column 1 to zero then E<sub>31</sub> to eliminate the item below that, E<sub>32</sub> to eliminte the item to the right of that.  In a 3x3 matrix, E<sub>32</sub> E<sub>31</sub> E<sub>21</sub> A = U.  

If item 21 contains a zero, then a row exchange is afforded by P<sub>32</sub> which swaps rows 3 and 2 and then E<sub>21</sub> can be applied: E<sub>32</sub> E<sub>31</sub> E<sub>21</sub> P<sub>32</sub> A = U


The magic is in the E A = U, L U = A and E L = I  

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/104829444-f31fd400-5841-11eb-998b-90227281811d.png">


Section 2.4 

4 ways to multiply matrices

Row picture: Dot product of A rows B columns --> 1 matrix

a<sub>1,:</sub><sup>T</sup>b<sub>:,1</sub> ... a<sub>m,:</sub><sup>T</sup>b<sub>n,p</sub>

Column picture: matrix A x columns of B --> each AB column is an average of A columns weighted by row of a B column 

A [ b<sub>1</sub> ... b<sub>p</sub>] = [Ab<sub>1</sub> ... Ab<sub>p</sub>]


Columns of A in outer product with Rows of B and then n matrices are summed


Laws of matrix operations:

Addition:

commutative: A + B = B + A  

distributive: c ( A + B ) = cA + cB  

associative: A + ( B + C ) = ( A + B ) + C

Mulitplication:

commutative: A B != B A  

but all square matrices commute with I: A I = I A

distributive from LHS: A ( B + C ) = AB + AC 

distributive from RHS: ( A + B ) C  = AC + BC

associative: A (BC) = (AB) C

Exponents:

A<sup>p</sup> = AAA...A (p factors)

A<sup>p</sup>A<sup>q</sup> = A<sup>p+q</sup>

(A<sup>p</sup>)<sup>q</sup> = A<sup>p</sup><sup>q</sup>

A<sup>0</sup> = I


For elimination, we use E which it is important to remember is doing the same operation on both sides of each equation in the matrices it operates on. So is not changing the relationship between the variables x, y, z, etc...

So for block operations, as long as the individual underlying matrices can operate on each other in terms of sizes, then the multiplication is valid. Then we can also say that block elimination is valid and expose Schuler's constant D - CA<sup>-1</sup>B as in this example matrix:

A B  
0 Schulers constant


section 2.5  


algorithm to test invertibility is elimination: A must have n non-zero pivots

algebra to test invertibility is determinant: det A must not = zero

equation to test invertibility is Ax = 0 only for x = 0

if A and B are invertible, then so is AB

(AB)<sup>-1</sup> = B<sup>-1</sup>A<sup>-1</sup>

Gauss-Jordan eliminates AI to IA<sup>-1</sup>

There are 14 conditions for A to be invertible:

Invertible [Singular]

1. A is invertible [singular].

2. Columns are independent [dependent].

3. Rows are independent [dependent].

4. Determinant is non-zero [zero].

5. Ax = 0 has only 1 solution: x=0 [infinite solutions].

6. Ax = b has one solution [no solution / infinite solutions].

7. A has n non-zero pivots [r < n pivots].

8. A has full rank r = n [rank r < n].

9. Reduced row echelon form is R = Identity. [R has at least one zero row.]

10. Column space is all of R<sub>n</sub>. [Column space dimension r < n.]

11. Row space is all of R<sub>n</sub> [Row space dimension r < n.]

12. All eigenvalues are non-zero. [Zero is an eigenvalue of A.]

13. A<sup>T</sup>A is symmetric positive definite. [A<sup>T</sup>A is only semidefinite.] 

14. A has n positive singular values. [A has r < n singular values.]


Six things about A's inverse A<sup>-1</sup>: Whatever A does to x, A<sup>-1</sup> undoes it. 

1. Inverse exists only if elimination reveals n pivots.  Elimination solves Ax = b without using the matrix A<sup>-1</sup>.

2. A cannot have 2 different inverses: if BA = I and AC = I, then B = C.  To prove this, must know that A<sup>-1</sup>A = I = AA<sup>-1</sup>: if A is square then its inverse can take it to I whether on RHS or LHS.

B(AC) = (BA)C thus B(I) = IC and thus B=C

3. If A is invertible, then the one and only soution to Ax = b is x = A<sup>-1</sup>b:

(Ax =b)A<sup>-1</sup> = x = A<sup>-1</sup>Ax = A<sup>-1</sup>b

4. If there is a non-zero vector x that Ax = 0, then A cannot have an inverse. This is trye because no matrix A<sup>-1</sup> can bring b = 0 back to x:

Ax = b = 0 and if there is an x that makes this true, then there cannot be an A<sup>-1</sup> that multiplies b = 0 to equal x.  That is, A<sup>-1</sup>Ax = A<sup>-1</sup>b = A<sup>-1</sup>0 = x is not possible when x is non-zero.

5. A 2x2 matric is invertible only when ad-bc = 0

np.array( [[a,b],[c,d]] )<sup>-1</sup> = 1/(ad-bc) * np.array( [[d,-b],[c,a]] )

Since (ad-bc) is determinant of A and appears in denominator, it cannot be zero.

The test of pivots, (test #1 of 14 above) is usally decided before teh determinant appears.

6. A diagonal matrics as an inverse provided no diagonal entries are zero.

if A = np.diag([d<sub>1</sub>, ..., d<sub>n</sub>])  
then A<sup>-1</sup> = np.diag([1/d<sub>1</sub>, ..., 1/d<sub>n</sub>])

So no d can = 0 since d appears in demoninator of diagonal values of A's inverse.

Notes:

Even if A and B are invertible, difficult to say if A+B is invertible.

Inverses come out of parentheses in reverse order because:

ABC(ABC)<sup>-1</sup>=ABCC<sup>-1</sup>B<sup>-1</sup>A<sup>-1</sup> = I

Which finds a good example in the E<sub>ij</sub> elimination matrices and their inverses E<sub>ij</sub><sup>-1</sup>: MIght have: 

E<sub>22</sub>E<sub>31</sub>E<sub>21</sub>A = U
but apply inverses:
E<sub>21</sub>E<sub>31</sub>E<sub>22</sub>U = A

Diagonally dominant

|a<sub>ii</sub>| > SUM<sub>i≠j</sub>|a<sub>ij</sub>|


A is diagonally dominant. B is not diagonally dominant but is invertible.  C is singular.

![A = \begin{bmatrix}
3&1&1\\
1&3&1 \\
1&1&3
\end{bmatrix}
,B = \begin{bmatrix}
2&1&1\\
1&2&1 \\
1&1&3
\end{bmatrix}
,   C = \begin{bmatrix}
1&1&1\\
1&1&1 \\
1&1&3
\end{bmatrix}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+A+%3D+%5Cbegin%7Bbmatrix%7D%0A3%261%261%5C%5C%0A1%263%261+%5C%5C%0A1%261%263%0A%5Cend%7Bbmatrix%7D%0A%2CB+%3D+%5Cbegin%7Bbmatrix%7D%0A2%261%261%5C%5C%0A1%262%261+%5C%5C%0A1%261%263%0A%5Cend%7Bbmatrix%7D%0A%2C+++C+%3D+%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A1%261%261+%5C%5C%0A1%261%263%0A%5Cend%7Bbmatrix%7D%0A)

Reasoning. Because we are testing the diagonal elements of A, we are testing the weight applied to every x in Ax=0.  So if for every row of A there is an a that is greater than the sum of all other a's then it is impossible for all x components to mulitply all a components and arrive at zero vector b.

SUM<sub>j≠i</sub> |a<sub>ij</sub>x<sub>j</sub>| ≤ SUM<sub>j≠i</sub> |a<sub>ij</sub>| • |x<sub>j</sub>| < |a<sub>jj</sub>| • |x<sub>j</sub>|


Difference matrix:  

![\begin{bmatrix}
1&0&0\\
-1&1&0\\
1&-1&0\\
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-1%261%260%5C%5C%0A1%26-1%260%5C%5C%0A%5Cend%7Bbmatrix%7D)

Sum matrix (is difference matrix inverted)

![\begin{bmatrix}
1&0&0\\
1&1&0\\
1&1&0\\
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A1%261%260%5C%5C%0A1%261%260%5C%5C%0A%5Cend%7Bbmatrix%7D)



Pascal triangle: add each entry on left give entry below. Entries on left are binomial coefficients.

![\begin{bmatrix}
1&0&0&0\\
1&1&0&0\\
1&2&1&0\\
1&3&3&1\\
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A1%260%260%260%5C%5C%0A1%261%260%260%5C%5C%0A1%262%261%260%5C%5C%0A1%263%263%261%5C%5C%0A%5Cend%7Bbmatrix%7D)


Adjacency matrix for network that has one 1-step connection between 1-1,1-2 and 2-1, 1-3 and 3-1, 2-3 and 3-2, 3-4 and 4-3 and 4-4 but no connections between any other pairs.  if you take square of this matrix, you get the number of 2-step connections between the nodes.

![\begin{bmatrix}
0&1&1&0\\
1&0&1&1\\
1&1&0&1\\
0&1&1&0\\
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A0%261%261%260%5C%5C%0A1%260%261%261%5C%5C%0A1%261%260%261%5C%5C%0A0%261%261%260%5C%5C%0A%5Cend%7Bbmatrix%7D)


Note from problem 8b
np.array([  
[a,b,a+b],  
[c,d,c+d],  
[e,f,e+f]  
])

for this matrix there is a solution but not a unique one because it is singluar.  the vector (a,c,e) can be added to vector (b,d,f) so that when vector (a+b,c+d,e+f) is subtracted you get the zero vector (0,0,0). In other words Ax = b = 0 for vector x = (1,1,-1) or visually, can go out the first column vector then extend via the second column vector and return to zero via the third column vector. 

Some interesting algebra from problem 9:  if B = PA then some exchange of rows makes B and A equal.  When inverting, we find that some exchange of columns makes their inversions equal.  B<subp-1</sup> = P<subp-1</sup>A<subp-1</sup>


problem 12
if C = AB invertible, and A and B are square, then A is invertible. Formula for A<sup>-1</sup> is found  
C = AB  
A<sup>-1</sup>C = A<sup>-1</sup>AB  
C is square since A and B are square and so C<sup>-1</sup> can multiply on either side  
A<sup>-1</sup>CC<sup>-1</sup>=A<sup>-1</sup>ABC<sup>-1</sup>  
A<sup>-1</sup> = BC<sup>-1</sup>  

problem 13
if M = ABC is invertible, then A, B, and C are invertible (?). Find formla for B<sup>-1</sup> involving M<sup>-1</sup>, A, C  
M<sup>-1</sup> = C<sup>-1</sup>B<sup>-1</sup>A<sup>-1</sup>  
but heres the answer  
M = ABC  
MC<sup>-1</sup>B<sup>-1</sup> = ABCC<sup>-1</sup>B<sup>-1</sup>  
MC<sup>-1</sup>B<sup>-1</sup> = A  
B<sup>-1</sup> = CM<sup>-1</sup>A

problem 14  
If add row 1 to row 2 of A to equal B, then how find B<sup>-1</sup> from A<sup>-1</sup>?  

B = np.array([[1,0],[1,1]])A = PA  
B<sup>-1</sup> = (PA)<sup>-1</sup>  
B<sup>-1</sup> = A<sup>-1</sup>P<sup>-1</sup>

problem 15  
Prove that if a matrix has a column of zeros then it cannot have an inverse.  
If has a column of zeros then it cannot generate a pivot not = 0.  
If A has column of zeros then so does BA and thus if B = A<sup>-1</sup>. then BA = I = np.eye() is impossible.  np.eye is identity matrix with a one in all columns.  

problem 18  
if B is inverse of A<sup>2</sup> then show that AB is the inverse of A:  
A<sup>2</sup>B = I  
AAB = I  
A<sup>-1</sup>AAB = A<sup>-1</sup>  
IAB = AB = A<sup>-1</sup>  

problem 28  
if A has row of zeros then AB does too.  So AB cannot = I.  So B cannot = A<sup>-1</sup>


section 2.6

diagonal x upper = upper  

upper x diagonal = upper

diagonal x lower = lower

lower x diagonal = lower



Section 2.7

Transpose  

(Ax)<sup>T</sup> = x<sup>T</sup>A<sup>T</sup>

(AB)<sup>T</sup> = B<sup>T</sup>A<sup>T</sup>

(A<sup>-1</sup>)<sup>T</sup> = (A<sup>T</sup>)<sup>-1</sup>

x•y = x<sup>T</sup>y  

(Ax)<sup>T</sup>y = x<sup>T</sup>A<sup>T</sup>y = x•A<sup>T</sup>y because x• is same as x<sup>T</sup>

the product of A<sup>T</sup>A is always symmetric but not always invertible.

Orthogonal matrix has Q<sup>T</sup> = Q<sup>-1</sup>

there are n! different orderings of Permutation matrix rows.

P<sup>T</sup> = P<sup>-1</sup>

(A + B)<sup>T</sup> = A<sup>T</sup> + B<sup>T</sup>

(A<sup>-1</sup>)<sup>T</sup> = (A<sup>T</sup>)<sup>-1</sup>

[A<sup>-1</sup>B<sup>-1</sup> = (AB)<sup>-1</sup>][AB] = I

Ax combines columns of A

(Ax)<sup>T</sup> combines rows of A<sup>T</sup> because x<sup>T</sup> appears on LHS

(A<sup>-1</sup>A) = I  

A<sup>T</sup>(A<sup>-1</sup>)<sup>T</sup> = I  

A<sup>T</sup> is invertible when A is invertible

when a 3x3 LHS multiplies a 3x3 RHS, each cell is   
a weighted average of LHS columns based on a single RHS of weights  
a weighted average of RHS rows bsaed on a single row of LHS weights  
the sum of 3 matrices = 3 outside products of 1st col LHS ª 1st row RHS, 2nd col LHS • 2nd row RHS, etc   


meaning of inner and outer product.  when T is inside, x<sup>T</sup>x, it is inside product and when T is outside, xx<sup>T</sup>, it is outer product.

A<sup>T</sup> is often characterized a flipping the matrix across its diagonal but it is mathematically the matrix that makes these 2 inner products equal:  
(Ax)<sup>T</sup>y = x<sup>T</sup>(A<sup>T</sup>y)


Symmetric matrix; A<sup>T</sup> = A  = S = most important matrices  

The inverse of a symmetric matrix is also symmetric  

The transpose of a symmetric matrix inverse is the same matrix of course.

S<sup>-1</sup> = (S<sup>-1</sup>)<sup>T</sup> = (S<sup>T</sup>)<sup>-1</sup> = S<sup>-1</sup>  

Implies that when S is invertible (ie when A is symmetric and invertible) S<sup>-1</sup> is symmetric

<img width="864" alt="image" src="https://user-images.githubusercontent.com/38410965/105074375-410d2580-5a56-11eb-948c-0ed9f976ee34.png">



A<sup>T</sup>A and AA<sup>T</sup> and LDL<sup>T</sup> are all symmetric.  
Can produce S square symmetric matrix from any matrix and its transpose.   

Every (i,j) = (j,i) cell of A<sup>T</sup>A or AA<sup>T</sup> because    
(i,j) in AA<sup>T</sup> = a product of A's ith row and A<sup>T</sup>'s jth column which is A's jth row  
(j,i) in AA<sup>T</sup> = a product of A's jth row and A<sup>T</sup>'s ith column which is A's ith row  
These are the same combinations each time.   

AA<sup>T</sup>(i,j) = A[i,:] • A<sup>T</sup>[:,j] = A[i,:] • A[j,:]  

AA<sup>T</sup>(j,i) = A[j,:] • A<sup>T</sup>[:,i] = A[j,:] • A[i,:]  

AA<sup>T</sup> is symmetric but not necessarily = A<sup>T</sup>A which is also symmetric

When A is S then factoring A into LDU actually factors it into LDL<sup>-1</sup>, but cannot see this in LU, must be LDU.  
Notice (LDL<sup>T</sup>)<sup>T</sup> = (L<sup>T</sup>)<sup>T</sup>D<sup>T</sup>L<sup>T</sup> = LDL<sup>T</sup>  

Importantly, the multiplications are fewer too since you only need L not U

Of the n! permutation matrices, the single row exchanges are their own inverses, and are their transposes too  
since PP<sup>-1</sup> = P<sup>-1</sup>P = I  
then PP<sup>T</sup> = P<sup>T</sup>P = I  

In elmination, if P is done before E then PA = LU but must put A's rows in right order for each E<sub>ij</sub> elmination steps.   
If P is inserted between E<sub>ij</sub> elmination steps then A = LPU   
PA = LU is used in computing   
A = LPU is more elegant   
P = I when A=LU requires no exchanges  


The transpose of A<sub>-1</sub> is the inverse of A<sub>T</sub>:  (A<sub>-1</sub>)<sub>T</sub> = (A<sub>T</sub>)<sub>-1</sub>  

whatever confusion there might be from earlier section: (Ax)<sub>T</sub>y = x<sub>T</sub>(A<sub>T</sub>y)  

When A is summetric S then its LDU factorization is symmetric S = LDL<sub>T</sub>   

A permutation matric has a 1 in each row and column and P<sub>T</sub> = P<sub>-1</sub>  

There are n! permutation matrices, half even and half odd.  Even refers to an even number of off diagonal 1s.   

If A is invertible, then a permutation matrix will reorder its rows for PA = LU

A<sup>T</sup>A is invertible if A has independent columns.

If A and B are symmetric, then  

their AB product is symmetric.  <-- A=np.array([[a,b],[b,c]) and B=np.array([[d,e],[e,f]]) contradict this.
their sum and difference are symmetric A + B and A - B
A B A is symmetric
(A + B)(A+B) is not symmetric

Skew symmetric is -A = A<sup>T</sup>

The transpose of a block matrix transposes the blocks' insides as well. np.array([[A,B],[B,C]])

x•y = Px•Py because youre moving x's and y's in the same ways.

(Px)<sup>T</sup>Py = x•y because = x<sup>T</sup>P<sup>T</sup>Py and P<sup>T</sup>P = I  


A<sup>T</sup>A can have no negative number in the diagonal because all squares.   
A.shape = (3,2) ... A = np.array([[a,d],[b,e],[c,f]])  
np.diag(A<sup>T</sup>A) = array(a<sup>2</sup>)+b<sup>2</sup>+c<sup>2</sup>, d<sup>2</sup>+e<sup>2</sup>+f<sup>2</sup>)
The 2 diagonal cells of A<sup>T</sup>A each contain the sqaures of one of A's 2 columns. A(1,1) contains square of 1st column and A(2,2) contains square of 2nd column.  The off diagonals contain the dot products of the two columns and are the same = symmetric.



P on LHS uses its row elements to reorder rows  
P on RHS uses its column elements to reorder columns 

PSP<sup>T</sup>  
P ruins symmetry
P<sup>T</sup> recovers symmetry  
but since P works rows and P<sup>T</sup> works columns the new matrix will not be the same as the old matrix  


LDL<sup>T</sup> factorization  

<img width="864" alt="image" src="https://user-images.githubusercontent.com/38410965/105108832-230ce880-5a89-11eb-9c0e-c136c082073b.png">


https://tex-image-link-generator.herokuapp.com

\begin{align*}
\sum_{}^{} t_i^2 \\
\mathbf{y})
\end{align*}


![\begin{bmatrix}
1&2&3\\
A&B&C
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bpmatrix%7D%0A1%262%263%5C%5C%0AA%26B%26C%0A%5Cend%7Bpmatrix%7D)



![\begin{bmatrix}
1&2&3\\
A&B&C
\end{bmatrix}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A1%262%263%5C%5C%0AA%26B%26C%0A%5Cend%7Bbmatrix%7D)


![\begin
\end](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bbmatrix%7D%0A1%262%263%5C%5C%0AA%26B%26C%0A%5Cend%7Bbmatrix%7D)


