section 6.5 positive definite matrices

1. symmetric S: all eigenvalues > 0 &longleftrightarrow; all pivots > 0 &longleftrightarrow; all upper left determinants > 0    
2. the matrix S is then positive definite:    tests are ...
- the energy test is x<sup>T</sup>Sx > 0 for all vectors ≠ 0.     
- another positive definitiveness test is S = A<sup>T</sup>A with independent columns in A  
3. positive semidefinite S allows: 
- &lambda; = 0    
- pivots = 0   
- determinant ≠ 0    
- energy x<sup>T</sup>Sx = 0  
4. the equation x<sup>T</sup>Sx = 1 gives an ellipse in R<sup>n</sup> when S is symmetric positive definite.

this section is about symmetric matrices with positive eigenvalues.

all &lambda;s > 0 is special and at the center of many applications.  

positive definite names symmetric matrices with all positive eigenvalues  

testing all &lambda;s requires too much computation.  

2 goals of this section:   
1. find quick tests on symmetric matrices that guarantee positive eigenvalues.    
2. explain applications of positive definitiveness.  


**every eigenvalue is postive because the matrix is symmetric:**

when does [ [a,b], [b,c] ] have &lambda;<sub>1</sub> > 0 and &lambda;<sub>2</sub> > 0 ?

only when a > 0 and ac - b<sup>2</sup> = |S| > 0

why?   
we know b<sup>2</sup> always > 0

a > 0   
ac - b<sup>2</sup> > 0 ––> ac > b<sup>2</sup> > 0 ––> c > 0 too because a > 0

rememeber:
det A = ac - b<sup>2</sup>
trace<sub>A</sup> = a + c

![\begin{align*}
A &=
\begin{bmatrix}
a&b\\
b&c
\end{bmatrix}\\
\\
det(A) &= ac - b^2 > 0
\\
A-&lambda;I &=
\begin{bmatrix}
a-&lambda;&b\\
b&c-&lambda;
\end{bmatrix} \\
\\
det(A-&lambda;I) &= &lambda;^2-a&lambda;-c&lambda; + ac - b^2\\
&= 1&lambda;^2-(a+c)&lambda; + (ac - b^2)\\
&= 1&lambda;^2-trace_A&lambda; + |A|\\
\\
&lambda;s &= \frac{(a+c) \pm \sqrt{(-(a+c))^2 - 4(ac-b^2)}}{2}\\
&= \frac{trace_A \pm \sqrt{(-trace_A)^2 - 4(det(A))}}{2}\\
\\
& (a+c)^2 - 4(ac-b^2)  > 0  \longrightarrow &lambda;_1, &lambda;_2 &isinv; \mathbb{R} \\
& trace_A^2 - 4(det(A))  > 0  \longrightarrow &lambda;_1, &lambda;_2 &isinv; \mathbb{R}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0Ab%26c%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Adet%28A%29+%26%3D+ac+-+b%5E2+%3E+0%0A%5C%5C%0AA-%26lambda%3BI+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Aa-%26lambda%3B%26b%5C%5C%0Ab%26c-%26lambda%3B%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%5C%5C%0Adet%28A-%26lambda%3BI%29+%26%3D+%26lambda%3B%5E2-a%26lambda%3B-c%26lambda%3B+%2B+ac+-+b%5E2%5C%5C%0A%26%3D+1%26lambda%3B%5E2-%28a%2Bc%29%26lambda%3B+%2B+%28ac+-+b%5E2%29%5C%5C%0A%26%3D+1%26lambda%3B%5E2-trace_A%26lambda%3B+%2B+%7CA%7C%5C%5C%0A%5C%5C%0A%26lambda%3Bs+%26%3D+%5Cfrac%7B%28a%2Bc%29+%5Cpm+%5Csqrt%7B%28-%28a%2Bc%29%29%5E2+-+4%28ac-b%5E2%29%7D%7D%7B2%7D%5C%5C%0A%26%3D+%5Cfrac%7Btrace_A+%5Cpm+%5Csqrt%7B%28-trace_A%29%5E2+-+4%28det%28A%29%29%7D%7D%7B2%7D%5C%5C%0A%5C%5C%0A%26+%28a%2Bc%29%5E2+-+4%28ac-b%5E2%29++%3E+0++%5Clongrightarrow+%26lambda%3B_1%2C+%26lambda%3B_2+%26isinv%3B+%5Cmathbb%7BR%7D+%5C%5C%0A%26+trace_A%5E2+-+4%28det%28A%29%29++%3E+0++%5Clongrightarrow+%26lambda%3B_1%2C+%26lambda%3B_2+%26isinv%3B+%5Cmathbb%7BR%7D%0A%5Cend%7Balign%2A%7D%0A)

examples


![\begin{align*}
S_1 & = 
\begin{bmatrix}
1&2\\
2&1
\end{bmatrix}\\
S_2 & = 
\begin{bmatrix}
1&-2\\
-2&6
\end{bmatrix} \\
S_3 & = 
\begin{bmatrix}
-1&2\\
2&-6
\end{bmatrix} = -S_2
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS_1+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%262%5C%5C%0A2%261%0A%5Cend%7Bbmatrix%7D%5C%5C%0AS_2+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%26-2%5C%5C%0A-2%266%0A%5Cend%7Bbmatrix%7D+%5C%5C%0AS_3+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-1%262%5C%5C%0A2%26-6%0A%5Cend%7Bbmatrix%7D+%3D+-S_2%0A%5Cend%7Balign%2A%7D%0A)


S<sub>1</sub> &lambda;s = 3,-1 ––> S<sub>1</sub> not positive definite    
more quickly identified by |S<sub>1</sub>| = 1-4 = -3 even though a = 1 > 0.  remember:   &lambda;<sub>1</sub>&lambda;<sub>2</sub> = |S<sub>1</sub>| 
&lambda;<sub>1</sub>+&lambda;<sub>2</sub> = trace<sub>S</sub>  

S<sub>2</sub> has a and |S<sub>1</sub>| > 0 so is positive defnite

S<sub>3</sub> = -S<sub>2</sub> and so has both &lambda;s < 0   
the 2 positive eigenvalues for S<sub>2</sub> are negative for S<sub>3</sub>  

above use 2x2 tests, a > 0 and |S| > 0, to determine &lambda;s > 0  
reverse the logic:  
use the &lambda;s >0  to say that the 2x2 tests above are passed: a and |S| > 0
- the product of &lambda;<sub>1</sub>&lambda;<sub>2</sub> = ac - b<sup>2</sup> = |S| > 0 so 2nd test passed, and ac > 0 ––> a and c have same sign.
- the sum of &lambda;<sub>1</sub> + &lambda;<sub>2</sub> > 0 combined with having the same sign means that a and c > 0.

thus :

a > 0, |S| >0 &longleftrightarrow; &lambda;<sub>1</sub> > 0, &lambda;<sub>2</sub> > 0 

**n>2 matrices**

the above tests, use det(a) = a and det(S) = ac - b<sup>2</sup>   
when S is nxn, n>2, det(S) > 0 is the 3rd test which requires positive pivots.  

test:  

the eigenvalues of S are positive  
if and only if  
the pivots of S are positive

for 2x2 matrix:  
a > 0  
(ac - b<sup>2</sup>)/a > 0 

a > 0 is required for all 3 tests:  
1. a > 0
2. ac - b<sup>2</sup> = det(S) > 0
3. all pivots > 0

obvious for a > 0 test.   
need a > 0 for det (S) test because then know c > 0 ––> ac > 0 ––> ac - b<sup>2<sup> > 0.   
a is a pivot since it is unchanged in reduction/elimination/traingularization that reveal pivots.

second pivot:  
(ac - b<sup>2</sup>)/a > 0 

![\begin{align*}
\begin{bmatrix}
a&b\\
b&c
\end{bmatrix} = 
\begin{bmatrix}
a&b\\
b - \frac{b}{a}a&c - \frac{b}{a}b
\end{bmatrix} =
\begin{bmatrix}
a&b\\
0&c - \frac{b}{a}b
\end{bmatrix} 
\longrightarrow pivot_2 = c - \frac{b^2}a \longrightarrow = \frac{ac - b^2}{a}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0Ab%26c%0A%5Cend%7Bbmatrix%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0Ab+-+%5Cfrac%7Bb%7D%7Ba%7Da%26c+-+%5Cfrac%7Bb%7D%7Ba%7Db%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0A0%26c+-+%5Cfrac%7Bb%7D%7Ba%7Db%0A%5Cend%7Bbmatrix%7D+%0A%5Clongrightarrow+pivot_2+%3D+c+-+%5Cfrac%7Bb%5E2%7Da+%5Clongrightarrow+%3D+%5Cfrac%7Bac+-+b%5E2%7D%7Ba%7D%0A%5Cend%7Balign%2A%7D%0A)

this connects   
linear algebra concepts: positive eigenvalues &longleftrightarrow; positive pivots
- each pivto is a ratio of upper level determinants: the 2nd pivot is a ratio of determinant = ac - b<sup>2</sup> and determinant = a
- the pivots give a quicker computation to test for &lambda;s > 0 than actually computing &lambda;s


example:

S - I will be positive semidefinite because S - I will have eigenvalues 1,1,4 - 1,1,1 = 0,0,3 since I has &lambda;s 1,1,1

S - 2I will be indefinite because S - 2I will have eigenvalues 1,1,4 - 2,2,2 = -1,-1,2.  

![\begin{align*}
S &=
\begin{bmatrix}
2&1&1\\
1&2&1\\
1&1&2
\end{bmatrix} \\
&lambda;s &= 1, 1, 4\\
determinants & = 2, 3, 4\\
pivots & = 2, \frac{3}{2}, \frac{4}{3} 
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%261%261%5C%5C%0A1%262%261%5C%5C%0A1%261%262%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%26lambda%3Bs+%26%3D+1%2C+1%2C+4%5C%5C%0Adeterminants+%26+%3D+2%2C+3%2C+4%5C%5C%0Apivots+%26+%3D+2%2C+%5Cfrac%7B3%7D%7B2%7D%2C+%5Cfrac%7B4%7D%7B3%7D+%0A%5Cend%7Balign%2A%7D%0A)


Energy:  a different way to look at symmetric matrices with &lambda;s > 0

**energy based definition**

from   
Sx = &lambda;x  
multiply by x<sup>T</sup> to get   
x<sup>T</sup>Sx = &lambda;x<sup>T</sup>x   
[when positive definite]   
RHS is positive number &lambda; time positive number x<sup>T</sup>x   
so LHS is positive for any eigenvector.   

the new idea is that   
x<sup>T</sup>Sx   
is positive for all non-zero vectors x   
not just eigenvectors   

[once Sx = &lambda;x is known from well derived &lambda; and x, and all &lambda;s > 0   
then Sx = &lambda;x works for any x when &lambda; > 0:    
z<sup>T</sup>Sz = &lambda;z<sup>T</sup>z   
z not an eigenvector   
always z<sup>T</sup>Sz > 0 
when &lambda;s > 0 and always z<sup>T</sup>z = || z ||<sup>2</sup> = length(z) > 0]

x<sup>T</sup>Sx    
is the energy of the system   
for many applications  
(sometimes x<sup>T</sup>Sx / 2 )

the positive energy requirement gives another definition of positive defnite matrix    

Definition:  S is positive definite if x<sup>T</sup>Sx > 0 for every non-zero vector x.

2x2 example:


![\begin{align*}
x^TSx &=
\begin{bmatrix}
x&y
\end{bmatrix} 
\begin{bmatrix}
a&b\\
b&c
\end{bmatrix} 
\begin{bmatrix}
x\\
y
\end{bmatrix} > 0 \\ & =
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
ax + by\\
bx+cy
\end{bmatrix} > 0 \\ &=
\begin{bmatrix}
ax + by&
bx+cy
\end{bmatrix} \begin{bmatrix}
x\\
y
\end{bmatrix}> 0 
\\ &=
axx + byx + bxy + cyy > 0 
\\ &=
ax^2 + 2bxy + cy^2 > 0 
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ax%5ETSx+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0Ab%26c%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D+%3E+0+%5C%5C+%26+%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aax+%2B+by%5C%5C%0Abx%2Bcy%0A%5Cend%7Bbmatrix%7D+%3E+0+%5C%5C+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Aax+%2B+by%26%0Abx%2Bcy%0A%5Cend%7Bbmatrix%7D+%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%3E+0+%0A%5C%5C+%26%3D%0Aaxx+%2B+byx+%2B+bxy+%2B+cyy+%3E+0+%0A%5C%5C+%26%3D%0Aax%5E2+%2B+2bxy+%2B+cy%5E2+%3E+0+%0A%5Cend%7Balign%2A%7D%0A)



a, b, b, c  
give 4 parts of   
x<sup>T</sup>Sx.  

from a and c diagonal entries come pure squares ax<sup>2</sup> and cy<sup>2</sup>   

from b and b off diagonal entries come the cross terms bxy and byx.  

their sum = x<sup>T</sup>Sx   

from this enery based definition comes a basic fact:  

if S and T are symmetric positive definite   
so then must S + T be symmetric positive definite  
because  
x<sup>T</sup>(S + T)x = x<sup>T</sup>Sx + x<sup>T</sup>Tx   
and those two terms are positive for x ≠ 0  
so that sum S+T is also positive definite   

the pivots and eigenvalues are not so easy to follow when matrices are added   
but the energies just add.   

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/110553914-ca141500-8107-11eb-9c07-282d5e265c87.png">


x<sup>T</sup>Sx  
connects with the final test of a positive definite matrix:  
start with any matrid A   
which can be rectangular and not symmetric     
but 
we know   
S = A<sup>T</sup>A  
is square and symmetric  
we know   
S = A<sup>t</sup>A  
is positive definite when A has independent vectors  

test:   
if the columns of A are independent,  
then S = A<sup>T</sup>A is positive definite   

proof:   
pivots and eigenvalues are long to compute, but  
the numbers of x<sup>T</sup>Sx is the same as x<sup>T</sup>A<sup>T</sup>Ax.  
[so for the same reason as we know x<sup>T</sup>Sx is positive so is x<sup>T</sup>A<sup>T</sup>Ax]
x<sup>T</sup>Sx = x<sup>T</sup>A<sup>T</sup>Ax = (x<sup>T</sup>A<sup>T</sup>)(Ax) = (Ax)<sup>T</sup>(Ax) = || Ax ||<sup>T</sup> > 0 when x ≠ 0.  (This is [how?] the meaning of independent columns [because Ax ≠ 0 unelss x = 0 so null space is empty except x = 0?])
Then x<sup>T</sup>Sx is the positive number || Ax ||<sup>2</sup> [= x<sup>T</sup>&lambda;x?] and the matrix S is positive definite. 

to collect this theory together, 5 equivalent statements are possible for positive defnitiveness.  these 5 statements connect pivots, determinants, eigenvalues, and least squares (from A<sup>T</sup>A).

**when a symmetric matrix S has one of these 5 properties, that S has all 5 of these properties:**  
1. all n pivots of S are positive  
2. all n upper left determinants are positive   
3. all n eigenvalues of S are positive   
4. x<sup>T</sup>Sx is positive except at x = 0 (the energy based definition)   
5. S = A<sup>T</sup>A for a matrix A with independent columns.  


The upper left determinants are 1x1, 2x2, 3x3, ... , nxn.  
The last determinant is the determinant of the complete matrix S.  
The theorem ties together the whole linear algebra course.


Example: 

pivots of S = 2, 3/2, 4/3  
upper left determinants of S = 2, 3, 4  
eigenvalues of S = 2, 2-√2, 2+√2

all determine that S is positive definite.

![\begin{align*}
S &=
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} 
& T &=
\begin{bmatrix}
2&-1&b\\
-1&2&-1\\
b&-1&2
\end{bmatrix} 
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%0A%26+T+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%26b%5C%5C%0A-1%262%26-1%5C%5C%0Ab%26-1%262%0A%5Cend%7Bbmatrix%7D+%0A%5Cend%7Balign%2A%7D)

3 ways, via matrices A<sup>1</sup>, A<sup>2</sup>, A<sup>3</sup> to decompose S into A<sup>T</sup>A that show S is positive definite.   

1. A<sup>1</sup> is 1st difference matrix

**the 3 columns of A<sup>1</sup> are independent and therefore S is positive definite.**

![\begin{align*}
S &=
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} 
=A_1^TA_1 =
\begin{bmatrix}
1&-1&0&0\\
0&1&-1&0\\
0&0&1&-1
\end{bmatrix} 
\begin{bmatrix}
1&0&0\\
1&-1&0\\
0&-1&1\\
0&0&-1
\end{bmatrix} 
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%0A%3DA_1%5ETA_1+%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-1%260%260%5C%5C%0A0%261%26-1%260%5C%5C%0A0%260%261%26-1%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A1%26-1%260%5C%5C%0A0%26-1%261%5C%5C%0A0%260%26-1%0A%5Cend%7Bbmatrix%7D+%0A%5Cend%7Balign%2A%7D)

2. A<sub>2</sub> comes from LDL<sup>T</sup> which is the symmetric form of LU.  
Elimination gives the pivots 2, 3/2, 4/3 in D and the multipliers -1/2, 0, -2/3 in L.  Just make A<sub>2</sub> = L√D so that A<sub>2</sub><sup>T</sup>A<sub>2</sub> = (L√D) (L√D)<sup>T</sup> = L√D√D<sup>T</sup>L<sup>T</sup> = LDL<sup>T</sup>

**The pivots of S are positive and so S is positive definite.**

[seems that counter to book, A<sub>2</sub> = (L√D)<sup>T</sup> and A<sub>2</sub><sup>T</sup> = L√D so that A<sub>2</sub><sup>T</sup>A<sub>2</sub> = L√D(L√D)<sup>T</sup> = L√D√D<sup>T</sup>L<sup>T</sup> = L√D√DL<sup>T</sup> = LDL<sup>T</sup> = S

A<sub>2</sub> is the Cholesky factor of S [ = √DL<sup>T</sup> = (L√D)<sup>T</sup> = A<sub>2</sub> ]

This triangular choice of A has square roots (not pretty) and is called the "Cholesky factor" of S.  

![\begin{align*}
S =
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} 
=A_2^TA_2 &= (L\sqrt{D})(L\sqrt{D})^T \\ & = 
(\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} )
(\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} )^T \\ &= 
L\sqrt{D}\sqrt{D}L^T \\ & =
 (\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} 
\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix}^T \\ & =
LDL^T \\ & = 
\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix} 
\begin{bmatrix}
2&0&0\\
0&\frac{3}{2}&0\\
0&0&\frac{4}{3}
\end{bmatrix}
\begin{bmatrix}
1&-\frac{1}{2}&0\\
0&1&-\frac{2}{3}\\
0&0&1
\end{bmatrix} 
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%0A%3DA_2%5ETA_2+%26%3D+%28L%5Csqrt%7BD%7D%29%28L%5Csqrt%7BD%7D%29%5ET+%5C%5C+%26+%3D+%0A%28%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%29%0A%28%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%29%5ET+%5C%5C+%26%3D+%0AL%5Csqrt%7BD%7D%5Csqrt%7BD%7DL%5ET+%5C%5C+%26+%3D%0A+%28%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D%5ET+%5C%5C+%26+%3D%0ALDL%5ET+%5C%5C+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A2%260%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%260%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-%5Cfrac%7B1%7D%7B2%7D%260%5C%5C%0A0%261%26-%5Cfrac%7B2%7D%7B3%7D%5C%5C%0A0%260%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cend%7Balign%2A%7D)

3. Eigenvalues are teh symmetric matrix choice A<sub>3</sub> = (Q√&Lambda;)<sup>T</sup> so that A<sub>3</sub><sup>T</sup>A<sub>3</sub> = Q&Lambda;Q<sup>T</sup> = S.

**the eigenvalues of S are positive and so S is positive definite**

![\begin{align*}
S = S^T &= 
\begin{bmatrix}
2&-1&\\
-1&2&-1\\
&-1&2
\end{bmatrix}\\
det(A-&lambda;I) &=
\begin{bmatrix}
2-&lambda;&-1&\\
-1&2-&lambda;&-1\\
&-1&2-&lambda;
\end{bmatrix} \\ 
&= [2-&lambda;] [(2-&lambda;)(2-&lambda;)-(-1)(-1)] + (-1)[-1][(-1)(2-&lambda;)] \\
&= [2-&lambda;] [(2-&lambda;)^2-1] + (-1)(2-&lambda;) \\
&= (2-&lambda;)(2-&lambda;)^2 + (2-&lambda;)(-1)+ (2-&lambda;)(-1) \\
&= (2-&lambda;)((2-&lambda;)^2 -2) \\
&= (2-&lambda;)(&lambda;^2 -4&lambda; +4 -2) \\
&= (2-&lambda;)(&lambda;^2 -4&lambda; +2) \\
\\
&lambda; &= 2, \frac{4+\sqrt{4^2-4*2}}{2}, \frac{4-\sqrt{4^2-4*2}}{2} \\
&= 2, \frac{4+\sqrt{8}}{2}, \frac{4-\sqrt{8}}{2} \\
&= 2, \frac{4+2\sqrt{2}}{2}, \frac{4-2\sqrt{2}}{2} \\
&= 2, 2+\sqrt{2}, 2-\sqrt{2} \\
&lambda;_1 = 2 \longrightarrow (A + 2I) &= 
\begin{bmatrix}
0&-1&\\
-1&0&-1\\
&-1&0
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix} =
\begin{bmatrix}
0\\0\\0
\end{bmatrix}
\longrightarrow x_1 = 
\begin{bmatrix}
1\\0\\-1
\end{bmatrix}
\\
&lambda;_2 = 2+\sqrt{2}  \longrightarrow (A -(2+\sqrt{2})I)& = 
\begin{bmatrix}
\sqrt{2}&-1&\\
-1&\sqrt{2}&-1\\
&-1&\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix} =
\begin{bmatrix}
0\\0\\0
\end{bmatrix}
\longrightarrow x_2 = 
\begin{bmatrix}
1\\ \sqrt{2}\\1
\end{bmatrix}\\
&lambda;_3 = 2-\sqrt{2} \longrightarrow (A -(2-\sqrt{2})I) &= 
\begin{bmatrix}
-\sqrt{2}&-1&\\
-1&-\sqrt{2}&-1\\
&-1&-\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix} =
\begin{bmatrix}
0\\0\\0
\end{bmatrix}
\longrightarrow x_3 = 
\begin{bmatrix}
1\\ -\sqrt{2}\\1
\end{bmatrix}\\
\\
S = S^T = A^TA & = Q\sqrt{&Lambda;}(Q\sqrt{&Lambda;})^T \\
&= \begin{bmatrix}
1&1&1\\
0&\sqrt{2}&-\sqrt{2}\\
1&1&1
\end{bmatrix} 
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix} ^ \frac{1}{2}
(\begin{bmatrix}
1&1&1\\
0&\sqrt{2}&-\sqrt{2}\\
1&1&1
\end{bmatrix} 
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix}^ \frac{1}{2})^T\\
&= X\sqrt{&Lambda;}\sqrt{&Lambda;}^TX^T \\
& =A^TA \\
&= X\sqrt{&Lambda;}\sqrt{&Lambda;}X^T \\
&= \begin{bmatrix}
1&1&1\\
0&\sqrt{2}&-\sqrt{2}\\
1&1&1
\end{bmatrix} 
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix} ^ \frac{1}{2}
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix}^ \frac{1}{2}
\begin{bmatrix}
1&1&1\\
0&\sqrt{2}&-\sqrt{2}\\
1&1&1
\end{bmatrix}^T\\
&=X&Lambda;X^T \\
&= \begin{bmatrix}
1&1&1\\
0&\sqrt{2}&-\sqrt{2}\\
1&1&1
\end{bmatrix} 
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
1&1&1\\
0&\sqrt{2}&-\sqrt{2}\\
1&1&1
\end{bmatrix}^T\\
& = X[norm]&Lambda;(X[norm])^T \\
&= \begin{bmatrix}
1&1&1\\
0&\sqrt{2}&-\sqrt{2}\\
1&1&1
\end{bmatrix} 
\begin{bmatrix}
\frac{1}{\sqrt{2}}&&\\
&\frac{1}{2}&\\
&&\frac{1}{2}
\end{bmatrix} 
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix}
(\begin{bmatrix}
1&1&1\\
0&\sqrt{2}&-\sqrt{2}\\
1&1&1
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}}&&\\
&\frac{1}{2}&\\
&&\frac{1}{2}
\end{bmatrix} )^T\\
& = Q&Lambda;Q^T \\
&= \begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}\\
0&\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}
\end{bmatrix}
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}\\
0&\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}
\end{bmatrix}^T\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%3D+S%5ET+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%26%5C%5C%0A-1%262%26-1%5C%5C%0A%26-1%262%0A%5Cend%7Bbmatrix%7D%5C%5C%0Adet%28A-%26lambda%3BI%29+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A2-%26lambda%3B%26-1%26%5C%5C%0A-1%262-%26lambda%3B%26-1%5C%5C%0A%26-1%262-%26lambda%3B%0A%5Cend%7Bbmatrix%7D+%5C%5C+%0A%26%3D+%5B2-%26lambda%3B%5D+%5B%282-%26lambda%3B%29%282-%26lambda%3B%29-%28-1%29%28-1%29%5D+%2B+%28-1%29%5B-1%5D%5B%28-1%29%282-%26lambda%3B%29%5D+%5C%5C%0A%26%3D+%5B2-%26lambda%3B%5D+%5B%282-%26lambda%3B%29%5E2-1%5D+%2B+%28-1%29%282-%26lambda%3B%29+%5C%5C%0A%26%3D+%282-%26lambda%3B%29%282-%26lambda%3B%29%5E2+%2B+%282-%26lambda%3B%29%28-1%29%2B+%282-%26lambda%3B%29%28-1%29+%5C%5C%0A%26%3D+%282-%26lambda%3B%29%28%282-%26lambda%3B%29%5E2+-2%29+%5C%5C%0A%26%3D+%282-%26lambda%3B%29%28%26lambda%3B%5E2+-4%26lambda%3B+%2B4+-2%29+%5C%5C%0A%26%3D+%282-%26lambda%3B%29%28%26lambda%3B%5E2+-4%26lambda%3B+%2B2%29+%5C%5C%0A%5C%5C%0A%26lambda%3B+%26%3D+2%2C+%5Cfrac%7B4%2B%5Csqrt%7B4%5E2-4%2A2%7D%7D%7B2%7D%2C+%5Cfrac%7B4-%5Csqrt%7B4%5E2-4%2A2%7D%7D%7B2%7D+%5C%5C%0A%26%3D+2%2C+%5Cfrac%7B4%2B%5Csqrt%7B8%7D%7D%7B2%7D%2C+%5Cfrac%7B4-%5Csqrt%7B8%7D%7D%7B2%7D+%5C%5C%0A%26%3D+2%2C+%5Cfrac%7B4%2B2%5Csqrt%7B2%7D%7D%7B2%7D%2C+%5Cfrac%7B4-2%5Csqrt%7B2%7D%7D%7B2%7D+%5C%5C%0A%26%3D+2%2C+2%2B%5Csqrt%7B2%7D%2C+2-%5Csqrt%7B2%7D+%5C%5C%0A%26lambda%3B_1+%3D+2+%5Clongrightarrow+%28A+%2B+2I%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A0%26-1%26%5C%5C%0A-1%260%26-1%5C%5C%0A%26-1%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C0%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+x_1+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C0%5C%5C-1%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%26lambda%3B_2+%3D+2%2B%5Csqrt%7B2%7D++%5Clongrightarrow+%28A+-%282%2B%5Csqrt%7B2%7D%29I%29%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%26-1%26%5C%5C%0A-1%26%5Csqrt%7B2%7D%26-1%5C%5C%0A%26-1%26%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C0%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+x_2+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C+%5Csqrt%7B2%7D%5C%5C1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26lambda%3B_3+%3D+2-%5Csqrt%7B2%7D+%5Clongrightarrow+%28A+-%282-%5Csqrt%7B2%7D%29I%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-%5Csqrt%7B2%7D%26-1%26%5C%5C%0A-1%26-%5Csqrt%7B2%7D%26-1%5C%5C%0A%26-1%26-%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5Cy%5C%5Cz%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C0%5C%5C0%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+x_3+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C+-%5Csqrt%7B2%7D%5C%5C1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0AS+%3D+S%5ET+%3D+A%5ETA+%26+%3D+Q%5Csqrt%7B%26Lambda%3B%7D%28Q%5Csqrt%7B%26Lambda%3B%7D%29%5ET+%5C%5C%0A%26%3D+%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26%5Csqrt%7B2%7D%26-%5Csqrt%7B2%7D%5C%5C%0A1%261%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D+%5E+%5Cfrac%7B1%7D%7B2%7D%0A%28%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26%5Csqrt%7B2%7D%26-%5Csqrt%7B2%7D%5C%5C%0A1%261%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%5E+%5Cfrac%7B1%7D%7B2%7D%29%5ET%5C%5C%0A%26%3D+X%5Csqrt%7B%26Lambda%3B%7D%5Csqrt%7B%26Lambda%3B%7D%5ETX%5ET+%5C%5C%0A%26+%3DA%5ETA+%5C%5C%0A%26%3D+X%5Csqrt%7B%26Lambda%3B%7D%5Csqrt%7B%26Lambda%3B%7DX%5ET+%5C%5C%0A%26%3D+%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26%5Csqrt%7B2%7D%26-%5Csqrt%7B2%7D%5C%5C%0A1%261%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D+%5E+%5Cfrac%7B1%7D%7B2%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%5E+%5Cfrac%7B1%7D%7B2%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26%5Csqrt%7B2%7D%26-%5Csqrt%7B2%7D%5C%5C%0A1%261%261%0A%5Cend%7Bbmatrix%7D%5ET%5C%5C%0A%26%3DX%26Lambda%3BX%5ET+%5C%5C%0A%26%3D+%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26%5Csqrt%7B2%7D%26-%5Csqrt%7B2%7D%5C%5C%0A1%261%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26%5Csqrt%7B2%7D%26-%5Csqrt%7B2%7D%5C%5C%0A1%261%261%0A%5Cend%7Bbmatrix%7D%5ET%5C%5C%0A%26+%3D+X%5Bnorm%5D%26Lambda%3B%28X%5Bnorm%5D%29%5ET+%5C%5C%0A%26%3D+%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26%5Csqrt%7B2%7D%26-%5Csqrt%7B2%7D%5C%5C%0A1%261%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%26%5C%5C%0A%26%5Cfrac%7B1%7D%7B2%7D%26%5C%5C%0A%26%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%28%5Cbegin%7Bbmatrix%7D%0A1%261%261%5C%5C%0A0%26%5Csqrt%7B2%7D%26-%5Csqrt%7B2%7D%5C%5C%0A1%261%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%26%5C%5C%0A%26%5Cfrac%7B1%7D%7B2%7D%26%5C%5C%0A%26%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D+%29%5ET%5C%5C%0A%26+%3D+Q%26Lambda%3BQ%5ET+%5C%5C%0A%26%3D+%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%5C%5C%0A0%26%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%26-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%5C%5C%0A0%26%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%26-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%5ET%5C%5C%0A%5Cend%7Balign%2A%7D)


All three versions show that -1, 2, -1 matrix is positive definite:
- independent columns of A   
- pivots of S = (A<sup>T</sup>)(A) = (L√D)(L√D)<sup>T</sup>   
- eigenvalues of S = (A<sup>T</sup>)(A) = (Q√&Lambda;)(Q√&Lambda;)<sup>T</sup>

![\begin{align*}
S = S^T &= 
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix}
\begin{matrix}
r_2 - (\frac{-1}{2})r_1
\end{matrix} \longrightarrow
\begin{bmatrix}
2&-1&0\\
0&\frac{3}{2}&-1\\
0&-1&2
\end{bmatrix}
\begin{matrix}
r_3 - (\frac{-2}{3})r_2
\end{matrix} \longrightarrow
\begin{bmatrix}
2&-1&0\\
0&\frac{3}{2}&-1\\
0&0&\frac{4}{3}
\end{bmatrix}\\
&= 
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix}
\begin{matrix}
r_2 - (L_{21})r_1
\end{matrix} \longrightarrow
\begin{bmatrix}
2&-1&0\\
0&\frac{3}{2}&-1\\
0&-1&2
\end{bmatrix}
\begin{matrix}
r_3 - (L_{32})r_2
\end{matrix} \longrightarrow
\begin{bmatrix}
2&-1&0\\
0&\frac{3}{2}&-1\\
0&0&\frac{4}{3}
\end{bmatrix}\\
E_{21}S &=
\begin{bmatrix}
1&0&0\\
\frac{1}{2}&1&0\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} =
\begin{bmatrix}
2&-1&0\\
0&\frac{3}{2}&-1\\
0&-1&2
\end{bmatrix}\\
E_{32}E_{21}S &=
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&\frac{2}{3}&1
\end{bmatrix}
\begin{bmatrix}
1&0&0\\
\frac{1}{2}&1&0\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} =
\begin{bmatrix}
2&-1&0\\
0&\frac{3}{2}&-1\\
0&0&\frac{4}{3}
\end{bmatrix} =U \\
E_{32}E_{21}S &=
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&-L_{32}&1
\end{bmatrix}
\begin{bmatrix}
1&0&0\\
-L_{21}&1&0\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} =
\begin{bmatrix}
2&-1&0\\
0&\frac{3}{2}&-1\\
0&0&\frac{4}{3}
\end{bmatrix} =U \\
S =E_{21}^{-1}E_{32}^{-1}U &=
\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix}
\begin{bmatrix}
2&-1&0\\
0&\frac{3}{2}&-1\\
0&0&\frac{4}{3}
\end{bmatrix} = 
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} =S
 \\
S=LU &=
\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix}
\begin{bmatrix}
2&-\frac{1}{2}&0\\
0&\frac{2}{3}&-\frac{2}{3}\\
0&0&\frac{4}{3}
\end{bmatrix}= 
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} =S \\
S=LU &=
\begin{bmatrix}
1&0&0\\
L_{21}&1&0\\
0&L_{32}&1
\end{bmatrix}
\begin{bmatrix}
2&-\frac{1}{2}&0\\
0&\frac{2}{3}&-\frac{2}{3}\\
0&0&\frac{4}{3}
\end{bmatrix}= 
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} =S \\
S=LDU &=
\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix}
\begin{bmatrix}
2&0&0\\
0&\frac{2}{3}&0\\
0&0&\frac{4}{3}
\end{bmatrix}
\begin{bmatrix}
2&-\frac{1}{2}&0\\
0&\frac{2}{3}&-\frac{2}{3}\\
0&0&\frac{4}{3}
\end{bmatrix}= 
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} =S
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%3D+S%5ET+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bmatrix%7D%0Ar_2+-+%28%5Cfrac%7B-1%7D%7B2%7D%29r_1%0A%5Cend%7Bmatrix%7D+%5Clongrightarrow%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bmatrix%7D%0Ar_3+-+%28%5Cfrac%7B-2%7D%7B3%7D%29r_2%0A%5Cend%7Bmatrix%7D+%5Clongrightarrow%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%26-1%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bmatrix%7D%0Ar_2+-+%28L_%7B21%7D%29r_1%0A%5Cend%7Bmatrix%7D+%5Clongrightarrow%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bmatrix%7D%0Ar_3+-+%28L_%7B32%7D%29r_2%0A%5Cend%7Bmatrix%7D+%5Clongrightarrow%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%26-1%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0AE_%7B21%7DS+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%260%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D%5C%5C%0AE_%7B32%7DE_%7B21%7DS+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A0%261%260%5C%5C%0A0%26%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%260%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%26-1%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D+%3DU+%5C%5C%0AE_%7B32%7DE_%7B21%7DS+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A0%261%260%5C%5C%0A0%26-L_%7B32%7D%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-L_%7B21%7D%261%260%5C%5C%0A0%260%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%26-1%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D+%3DU+%5C%5C%0AS+%3DE_%7B21%7D%5E%7B-1%7DE_%7B32%7D%5E%7B-1%7DU+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%260%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A0%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%26-1%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%3DS%0A+%5C%5C%0AS%3DLU+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-%5Cfrac%7B1%7D%7B2%7D%260%5C%5C%0A0%26%5Cfrac%7B2%7D%7B3%7D%26-%5Cfrac%7B2%7D%7B3%7D%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%3DS+%5C%5C%0AS%3DLU+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0AL_%7B21%7D%261%260%5C%5C%0A0%26L_%7B32%7D%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-%5Cfrac%7B1%7D%7B2%7D%260%5C%5C%0A0%26%5Cfrac%7B2%7D%7B3%7D%26-%5Cfrac%7B2%7D%7B3%7D%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%3DS+%5C%5C%0AS%3DLDU+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%260%260%5C%5C%0A0%26%5Cfrac%7B2%7D%7B3%7D%260%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-%5Cfrac%7B1%7D%7B2%7D%260%5C%5C%0A0%26%5Cfrac%7B2%7D%7B3%7D%26-%5Cfrac%7B2%7D%7B3%7D%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%3DS%0A%5Cend%7Balign%2A%7D)


<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/110581943-70c4d980-8139-11eb-8c33-80b940a30743.png">


to see the energy of x<sup>T</sup>Sx is positive,   
write it out as a sum of squares, 
in detail,  
using the 3 choices that identify key tests:   
- independence: x<sup>T</sup>Sx = &lambda;x = x<sup>T</sup>A<sup>T</sup>Ax = (Ax)<sup>T</sup>(Ax) = || Ax ||<sup>2</sup>   
- pivots: x<sup>T</sup>Sx = &lambda;x = x<sup>T</sup>A<sup>T</sup>Ax = LDL<sup>T</sup> = L√D√DL<sup>T</sup> = L√D(L√D)<sup>T</sup>   
- eigenvalues: = Q&Lambda;Q<sup>T</sup> = Xnorm&Lambda;(Xnorm)<sup>T</sup> = A<sup>T</sup>A


Sx - &lambda;x ––> x<sup>T</sup>Sx = &lambda;x<sup>T</sup>x  
with knowledge that 
- &lambda; > 0, and   
- x<sup>T</sup>x = || x ||<sup>2</sup>,  
comes knowledge that  
- x<sup>T</sup>Sx > 0    

THE POINT:   
&lambda; > 0 allows us to say x<sup>T</sup>Sx > 0   
which allows us to decompose positive definite S three different ways:   

notice because S is symmetric, it does not matter which direction we multiply the x vectors: 

(1 x 3)(3 x 3)(3 x 1) ––> (1 x 3)(3 x 1)

the matrix components:
- off diagonal matrix components are summed in their symmetric positions: -1 + -1 = -2 coefficients for x<sub>12</sub> and x<sub>23</sub> crosses:  -2x<sub>12</sub> and -2x<sub>23</sub>
- diagonal matrix components are taken as given: +2 coefficient for each of the x<sub>1</sub><sup>2</sup>, x<sub>2</sub><sup>2</sup>, x<sub>3</sub><sup>2</sup> squares: 2x<sub>1</sub><sup>2</sup>, 2x<sub>2</sub><sup>2</sup>, 2x<sub>3</sub><sup>2</sup>

- result is:

2x<sub>1</sub><sup>2</sup> - 2x<sub>12</sub> + 2x<sub>2</sub><sup>2</sup> - 2x<sub>23</sub> + 2x<sub>3</sub><sup>2</sup>


![\begin{align*}
x^TSx &= 
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}
\\ &=
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
2x_1-1x_2\\
-1x_1+2x_2-1x_3\\
-1x_2+2x_3
\end{bmatrix}
\\ &=
\begin{bmatrix}
2x_1-1x_2 & -1x_1+2x_2-1x_3 & -1x_2+2x_3
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}
\\ &= 2x_1x_1 - 1x_1x_2 - 1x_1x_2 +2x_2x_2 - 1x_2x_3   - 1x_2x_3 + 2x_3x_3 
\\ &= 2x_1^2 - 2x_1x_2 +2x_2^2 - 2x_2x_3 + 2x_3^2 
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ax%5ETSx+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1+%5C%5C%0Ax_2+%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%0A%5C%5C+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2x_1-1x_2%5C%5C%0A-1x_1%2B2x_2-1x_3%5C%5C%0A-1x_2%2B2x_3%0A%5Cend%7Bbmatrix%7D%0A%5C%5C+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A2x_1-1x_2+%26+-1x_1%2B2x_2-1x_3+%26+-1x_2%2B2x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1+%5C%5C%0Ax_2+%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%0A%5C%5C+%26%3D+2x_1x_1+-+1x_1x_2+-+1x_1x_2+%2B2x_2x_2+-+1x_2x_3+++-+1x_2x_3+%2B+2x_3x_3+%0A%5C%5C+%26%3D+2x_1%5E2+-+2x_1x_2+%2B2x_2%5E2+-+2x_2x_3+%2B+2x_3%5E2+%0A%5Cend%7Balign%2A%7D)

**1st way:**

||A<sub>1</sub>x||<sup>2</sup> = x<sub>1</sub><sup>2</sup> + ( x<sub>2</sub> -  x<sub>1</sub>)<sup>2</sup> + ( x<sub>3</sub>- x<sub>2</sub>)<sup>2</sup> +  x<sub>3</sub><sup>2</sup>

3 independent vectors in A<sub>1</sub> make S = A<sub>1</sub><sup>T</sup>A<sub>1</sub> where A is a 1st difference matrix:

again here it doesnt matter the order of multiplication because x<sup>T</sup>A<sub>1</sub><sup>T</sup> is just wide where A<sub>1</sub>x is tall.

length of Ax = || Ax || = ( (Ax)<sup>T</sup>(Ax) )<sup>1/2</sup>

x<sup>T</sup>Sx = x<sup>T</sup>A<sup>T</sup>Ax = (Ax)<sup>T</sup>(Ax) = || Ax ||<sup>2</sup> = ( ( (Ax)<sup>T</sup>(Ax) )<sup>1/2</sup> )<sup>2</sup> = ( ( x<sub>1</sub><sup>2</sup>
+(-x<sub>1</sub>+x<sub>2</sub>)<sup>2</sup>
+(-x<sub>2</sub>+x<sub>3</sub>)<sup>2</sup>
+x<sub>3</sub><sup>2</sup> )<sup>1/2</sup>)<sup>2</sup>

![\begin{align*}
a_1 &= 
\begin{bmatrix}
1 \\
-1 \\
0 \\
0
\end{bmatrix} \,
a_2 = 
\begin{bmatrix}
0 \\
1 \\
-1 \\
0 
\end{bmatrix} \,
a_3 =
\begin{bmatrix}
0 \\
0 \\
1 \\
-1  
\end{bmatrix}\\
\\
x^T&lambda;x = x^TSx &= x^TA^TAx 
\\&=
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
1&-1&0&0\\
0&1&-1&0\\
0&0&1&-1
\end{bmatrix}
\begin{bmatrix}
1&0&0\\
-1&1&0\\
0&-1&1\\
0&0&-1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}
\\ & = (x^TA^T)(Ax) = (Ax)^T(Ax) = || Ax ||^2
\\ &=
\begin{bmatrix}
x_1&-x_1+x_2&-x_2+x_3&-x_3
\end{bmatrix}
\begin{bmatrix}
x_1\\
-x_1+x_2\\
-x_2+x_3\\
-x_3
\end{bmatrix} =
\begin{bmatrix}
x_1\\
-x_1+x_2\\
-x_2+x_3\\
-x_3
\end{bmatrix}^T
\begin{bmatrix}
x_1\\
-x_1+x_2\\
-x_2+x_3\\
-x_3
\end{bmatrix}
\\ &= x_1^2 + (-x_1+x_2)^2 +(-x_2+x_3)^2 + x_3^2
\\&= ||Ax||^2 = (\sqrt{((Ax)^T(Ax))} \, )^2 = (\sqrt{(x_1^2 + (-x_1+x_2)^2 +(-x_2+x_3)^2 + x_3^2)} \,)^2
\\ & =x_1^2 + x_1^2 -x_1x_2 + x_2^2 + x_2^2 -x_2x_3 +x_3^2+ x_3^2 
\\ & =2x_1^2 - x_1x_2 + 2x_2^2 - x_2x_3 + 2x_3^2 
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Aa_1+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1+%5C%5C%0A-1+%5C%5C%0A0+%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D+%5C%2C%0Aa_2+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A0+%5C%5C%0A1+%5C%5C%0A-1+%5C%5C%0A0+%0A%5Cend%7Bbmatrix%7D+%5C%2C%0Aa_3+%3D%0A%5Cbegin%7Bbmatrix%7D%0A0+%5C%5C%0A0+%5C%5C%0A1+%5C%5C%0A-1++%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Ax%5ET%26lambda%3Bx+%3D+x%5ETSx+%26%3D+x%5ETA%5ETAx+%0A%5C%5C%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-1%260%260%5C%5C%0A0%261%26-1%260%5C%5C%0A0%260%261%26-1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-1%261%260%5C%5C%0A0%26-1%261%5C%5C%0A0%260%26-1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1+%5C%5C%0Ax_2+%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%0A%5C%5C+%26+%3D+%28x%5ETA%5ET%29%28Ax%29+%3D+%28Ax%29%5ET%28Ax%29+%3D+%7C%7C+Ax+%7C%7C%5E2%0A%5C%5C+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26-x_1%2Bx_2%26-x_2%2Bx_3%26-x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0A-x_1%2Bx_2%5C%5C%0A-x_2%2Bx_3%5C%5C%0A-x_3%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0A-x_1%2Bx_2%5C%5C%0A-x_2%2Bx_3%5C%5C%0A-x_3%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0A-x_1%2Bx_2%5C%5C%0A-x_2%2Bx_3%5C%5C%0A-x_3%0A%5Cend%7Bbmatrix%7D%0A%5C%5C+%26%3D+x_1%5E2+%2B+%28-x_1%2Bx_2%29%5E2+%2B%28-x_2%2Bx_3%29%5E2+%2B+x_3%5E2%0A%5C%5C%26%3D+%7C%7CAx%7C%7C%5E2+%3D+%28%5Csqrt%7B%28%28Ax%29%5ET%28Ax%29%29%7D+%5C%2C+%29%5E2+%3D+%28%5Csqrt%7B%28x_1%5E2+%2B+%28-x_1%2Bx_2%29%5E2+%2B%28-x_2%2Bx_3%29%5E2+%2B+x_3%5E2%29%7D+%5C%2C%29%5E2%0A%5C%5C+%26+%3Dx_1%5E2+%2B+x_1%5E2+-x_1x_2+%2B+x_2%5E2+%2B+x_2%5E2+-x_2x_3+%2Bx_3%5E2%2B+x_3%5E2+%0A%5C%5C+%26+%3D2x_1%5E2+-+x_1x_2+%2B+2x_2%5E2+-+x_2x_3+%2B+2x_3%5E2+%0A%5Cend%7Balign%2A%7D)


**2nd way:**   

||A<sub>2</sub>x||<sup>2</sup> = (2)(x<sub>1</sub> - (1/2)x<sub>2</sub>)<sup>2</sup> + (3/2)(x<sub>2</sub> -  (2/3)x<sub>3</sub>)<sup>2</sup> + (4/3)(x<sub>3</sub>)<sup>2</sup>

[seems that counter to book, A<sub>2</sub> = (L√D)<sup>T</sup> and A<sub>2</sub><sup>T</sup> = L√D so that A<sub>2</sub><sup>T</sup>A<sub>2</sub> = L√D(L√D)<sup>T</sup> = L√D√D<sup>T</sup>L<sup>T</sup> = L√D√DL<sup>T</sup> = LDL<sup>T</sup> = S

A<sub>2</sub> is the Cholesky factor of S [ = √DL<sup>T</sup> = (L√D)<sup>T</sup> = A<sub>2</sub> ]

This triangular choice of A has square roots (not pretty) and is called the "Cholesky factor" of S.  

![\begin{align*}
x^T&lambda;x &= x^TSx =
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix} 
\\&=x^TA_2^TA_2x 
\\&=x^T(A_2^T)(A_2)x 
\\&= x^T(L\sqrt{D})(L\sqrt{D})^Tx 
\\ & = 
(\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix} 
(\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} )
(\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} )^T 
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix} 
\\ &= 
x^TL\sqrt{D}\sqrt{D}L^Tx 
\\ & =
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix} 
\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} 
\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix}^T 
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix} 
\\ & =
x^TLDL^Tx 
\\ & = 
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix} 
\begin{bmatrix}
1&0&0\\
-\frac{1}{2}&1&0\\
0&-\frac{2}{3}&1
\end{bmatrix} 
\begin{bmatrix}
2&0&0\\
0&\frac{3}{2}&0\\
0&0&\frac{4}{3}
\end{bmatrix}
\begin{bmatrix}
1&-\frac{1}{2}&0\\
0&1&-\frac{2}{3}\\
0&0&1
\end{bmatrix} 
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix} 
\\ & =
(x^TL)D(L^Tx) 
\\ & = 
\begin{bmatrix}
x_1-\frac{1}{2}x_2&x_2-\frac{2}{3}x_3&x_3
\end{bmatrix} 
\begin{bmatrix}
2&0&0\\
0&\frac{3}{2}&0\\
0&0&\frac{4}{3}
\end{bmatrix}
\begin{bmatrix}
x_1-\frac{1}{2}x_2\\
x_2-\frac{2}{3}x_3\\
x_3
\end{bmatrix} 
\\ & =
(x^TLD)(L^Tx) 
\\ &=
\begin{bmatrix}
2(x_1-\frac{1}{2}x_2)&\frac{3}{2}(x_2-\frac{2}{3}x_3)&\frac{4}{3}(x_3)
\end{bmatrix} 
\begin{bmatrix}
x_1-\frac{1}{2}x_2\\
x_2-\frac{2}{3}x_3\\
x_3
\end{bmatrix}\\ & = 
(x^TL)(DL^Tx) 
\\ & =
\begin{bmatrix}
x_1-\frac{1}{2}x_2 & x_2-\frac{2}{3}x_3& x_3
\end{bmatrix} \begin{bmatrix}
2(x_1-\frac{1}{2}x_2)\\
\frac{3}{2}(x_2-\frac{2}{3}x_3)\\
\frac{4}{3}(x_3)
\end{bmatrix} 
\\ &= 2(x_1-\frac{1}{2}x_2)^2 + \frac{3}{2}(x_2-\frac{2}{3}x_3)^2+\frac{4}{3}(x_3)^2
\\ &= 
x^TL\sqrt{D}\sqrt{D}L^Tx 
\\ & =
x^T(L\sqrt{D})(L\sqrt{D})^Tx = x^T(A^T)Ax \longleftarrow A = (L\sqrt{D})^T
\\ & =
(x^TL)\sqrt{D}\sqrt{D}^T(L^Tx)
\\ & = 
\begin{bmatrix}
x_1-\frac{1}{2}x_2&x_2-\frac{2}{3}x_3&x_3
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}&0&0\\
0&\sqrt{\frac{3}{2}}&0\\
0&0&\sqrt{\frac{4}{3}}
\end{bmatrix} 
\begin{bmatrix}
x_1-\frac{1}{2}x_2\\
x_2-\frac{2}{3}x_3\\
x_3
\end{bmatrix} 
\\ & =
(x^TL\sqrt{D})(\sqrt{D}^TL^Tx)
\\ & =
(x^TL\sqrt{D})((L\sqrt{D})^Tx) \longleftarrow A = (L\sqrt{D})^T
\\ & = 
(x^TA^T)(Ax)\\ &=
(Ax)^T(Ax)\\ & = 
((L\sqrt{D})^Tx)^T((L\sqrt{D})^Tx)\\ &=
\begin{bmatrix}
\sqrt{2}(x_1-\frac{1}{2}x_2)&\sqrt{\frac{3}{2}}(x_2-\frac{2}{3}x_3)&\sqrt{\frac{4}{3}}(x_3)
\end{bmatrix} 
\begin{bmatrix}
\sqrt{2}(x_1-\frac{1}{2}x_2)\\
\sqrt{\frac{3}{2}}(x_2-\frac{2}{3}x_3)\\
\sqrt{\frac{4}{3}}(x_3)
\end{bmatrix} 
\\&=||(Ax)||^2 = (\sqrt{(Ax)^T(Ax)}\,)^2 \\  
\\ & = ||((L\sqrt{D})^Tx)||^2 = (\sqrt{((L\sqrt{D})^Tx)^T((L\sqrt{D})^Tx)}\,)^2
\\&= (\sqrt{2})^2(x_1-\frac{1}{2}x_2)^2+(\sqrt{\frac{3}{2}})^2(x_2-\frac{2}{3}x_3)^2+(\sqrt{\frac{4}{3}})^2(x_3)^2
\\&= 2(x_1-\frac{1}{2}x_2)^2+\frac{3}{2}(x_2-\frac{2}{3}x_3)^2+\frac{4}{3}(x_3)^2
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ax%5ET%26lambda%3Bx+%26%3D+x%5ETSx+%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%260%5C%5C%0A-1%262%26-1%5C%5C%0A0%26-1%262%0A%5Cend%7Bbmatrix%7D+%0A%5C%5C%26%3Dx%5ETA_2%5ETA_2x+%0A%5C%5C%26%3Dx%5ET%28A_2%5ET%29%28A_2%29x+%0A%5C%5C%26%3D+x%5ET%28L%5Csqrt%7BD%7D%29%28L%5Csqrt%7BD%7D%29%5ETx+%0A%5C%5C+%26+%3D+%0A%28%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D+%0A%28%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%29%0A%28%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%29%5ET+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D+%0A%5C%5C+%26%3D+%0Ax%5ETL%5Csqrt%7BD%7D%5Csqrt%7BD%7DL%5ETx+%0A%5C%5C+%26+%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D%5ET+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D+%0A%5C%5C+%26+%3D%0Ax%5ETLDL%5ETx+%0A%5C%5C+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-%5Cfrac%7B1%7D%7B2%7D%261%260%5C%5C%0A0%26-%5Cfrac%7B2%7D%7B3%7D%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A2%260%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%260%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-%5Cfrac%7B1%7D%7B2%7D%260%5C%5C%0A0%261%26-%5Cfrac%7B2%7D%7B3%7D%5C%5C%0A0%260%261%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D+%0A%5C%5C+%26+%3D%0A%28x%5ETL%29D%28L%5ETx%29+%0A%5C%5C+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1-%5Cfrac%7B1%7D%7B2%7Dx_2%26x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%26x_3%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A2%260%260%5C%5C%0A0%26%5Cfrac%7B3%7D%7B2%7D%260%5C%5C%0A0%260%26%5Cfrac%7B4%7D%7B3%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1-%5Cfrac%7B1%7D%7B2%7Dx_2%5C%5C%0Ax_2-%5Cfrac%7B2%7D%7B3%7Dx_3%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D+%0A%5C%5C+%26+%3D%0A%28x%5ETLD%29%28L%5ETx%29+%0A%5C%5C+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%28x_1-%5Cfrac%7B1%7D%7B2%7Dx_2%29%26%5Cfrac%7B3%7D%7B2%7D%28x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%29%26%5Cfrac%7B4%7D%7B3%7D%28x_3%29%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1-%5Cfrac%7B1%7D%7B2%7Dx_2%5C%5C%0Ax_2-%5Cfrac%7B2%7D%7B3%7Dx_3%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%5C%5C+%26+%3D+%0A%28x%5ETL%29%28DL%5ETx%29+%0A%5C%5C+%26+%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1-%5Cfrac%7B1%7D%7B2%7Dx_2+%26+x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%26+x_3%0A%5Cend%7Bbmatrix%7D+%5Cbegin%7Bbmatrix%7D%0A2%28x_1-%5Cfrac%7B1%7D%7B2%7Dx_2%29%5C%5C%0A%5Cfrac%7B3%7D%7B2%7D%28x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%29%5C%5C%0A%5Cfrac%7B4%7D%7B3%7D%28x_3%29%0A%5Cend%7Bbmatrix%7D+%0A%5C%5C+%26%3D+2%28x_1-%5Cfrac%7B1%7D%7B2%7Dx_2%29%5E2+%2B+%5Cfrac%7B3%7D%7B2%7D%28x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%29%5E2%2B%5Cfrac%7B4%7D%7B3%7D%28x_3%29%5E2%0A%5C%5C+%26%3D+%0Ax%5ETL%5Csqrt%7BD%7D%5Csqrt%7BD%7DL%5ETx+%0A%5C%5C+%26+%3D%0Ax%5ET%28L%5Csqrt%7BD%7D%29%28L%5Csqrt%7BD%7D%29%5ETx+%3D+x%5ET%28A%5ET%29Ax+%5Clongleftarrow+A+%3D+%28L%5Csqrt%7BD%7D%29%5ET%0A%5C%5C+%26+%3D%0A%28x%5ETL%29%5Csqrt%7BD%7D%5Csqrt%7BD%7D%5ET%28L%5ETx%29%0A%5C%5C+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1-%5Cfrac%7B1%7D%7B2%7Dx_2%26x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%26x_3%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%260%260%5C%5C%0A0%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%260%5C%5C%0A0%260%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1-%5Cfrac%7B1%7D%7B2%7Dx_2%5C%5C%0Ax_2-%5Cfrac%7B2%7D%7B3%7Dx_3%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D+%0A%5C%5C+%26+%3D%0A%28x%5ETL%5Csqrt%7BD%7D%29%28%5Csqrt%7BD%7D%5ETL%5ETx%29%0A%5C%5C+%26+%3D%0A%28x%5ETL%5Csqrt%7BD%7D%29%28%28L%5Csqrt%7BD%7D%29%5ETx%29+%5Clongleftarrow+A+%3D+%28L%5Csqrt%7BD%7D%29%5ET%0A%5C%5C+%26+%3D+%0A%28x%5ETA%5ET%29%28Ax%29%5C%5C+%26%3D%0A%28Ax%29%5ET%28Ax%29%5C%5C+%26+%3D+%0A%28%28L%5Csqrt%7BD%7D%29%5ETx%29%5ET%28%28L%5Csqrt%7BD%7D%29%5ETx%29%5C%5C+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%28x_1-%5Cfrac%7B1%7D%7B2%7Dx_2%29%26%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%28x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%29%26%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%28x_3%29%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Csqrt%7B2%7D%28x_1-%5Cfrac%7B1%7D%7B2%7Dx_2%29%5C%5C%0A%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%28x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%29%5C%5C%0A%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%28x_3%29%0A%5Cend%7Bbmatrix%7D+%0A%5C%5C%26%3D%7C%7C%28Ax%29%7C%7C%5E2+%3D+%28%5Csqrt%7B%28Ax%29%5ET%28Ax%29%7D%5C%2C%29%5E2+%5C%5C++%0A%5C%5C+%26+%3D+%7C%7C%28%28L%5Csqrt%7BD%7D%29%5ETx%29%7C%7C%5E2+%3D+%28%5Csqrt%7B%28%28L%5Csqrt%7BD%7D%29%5ETx%29%5ET%28%28L%5Csqrt%7BD%7D%29%5ETx%29%7D%5C%2C%29%5E2%0A%5C%5C%26%3D+%28%5Csqrt%7B2%7D%29%5E2%28x_1-%5Cfrac%7B1%7D%7B2%7Dx_2%29%5E2%2B%28%5Csqrt%7B%5Cfrac%7B3%7D%7B2%7D%7D%29%5E2%28x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%29%5E2%2B%28%5Csqrt%7B%5Cfrac%7B4%7D%7B3%7D%7D%29%5E2%28x_3%29%5E2%0A%5C%5C%26%3D+2%28x_1-%5Cfrac%7B1%7D%7B2%7Dx_2%29%5E2%2B%5Cfrac%7B3%7D%7B2%7D%28x_2-%5Cfrac%7B2%7D%7B3%7Dx_3%29%5E2%2B%5Cfrac%7B4%7D%7B3%7D%28x_3%29%5E2%0A%5Cend%7Balign%2A%7D)

**3rd way**

||A<sub>3</sub>x||<sup>2</sup> = &lambda;<sub>1</sub>(q<sub>1</sub>x)<sup>T</sup>q<sub>1</sub>x + &lambda;<sub>2</sub>(q<sub>2</sub>x)<sup>T</sup>q<sub>2</sub>x +&lambda;<sub>3</sub>(q<sub>3</sub>x)<sup>T</sup>q<sub>3</sub>x   
= || (Q√&Lambda;)<sup>T</sup>x||

![\begin{align*}
x^T&lambda;x = x^TSx = x^TA^TAx & = x^TQ\sqrt{&Lambda;}(Q\sqrt{&Lambda;})^Tx \\
&= 
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}\\
0&\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}
\end{bmatrix}
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix} ^ \frac{1}{2}
(\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}\\
0&\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}
\end{bmatrix}
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix}^ \frac{1}{2})^T
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix} \\
&= x^TQ\sqrt{&Lambda;}\sqrt{&Lambda;}^TQ^Tx \\
& =x^TA^TAx \\
&= x^TQ\sqrt{&Lambda;}\sqrt{&Lambda;}Q^Tx \\
&= 
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}\\
0&\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}
\end{bmatrix} 
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix} ^ \frac{1}{2}
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix}^ \frac{1}{2}
\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}\\
0&\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}
\end{bmatrix}^T
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
\\& = x^TQ&Lambda;Q^Tx
\\&= 
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}\\
0&\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}
\end{bmatrix}
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}\\
0&\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\
\frac{1}{\sqrt{2}}&\frac{1}{2}&\frac{1}{2}
\end{bmatrix}^T
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
\\& = (x^TQ)&Lambda;(Q^Tx)
\\&= 
\begin{bmatrix}
\frac{1}{\sqrt{2}}x_1 +\frac{1}{\sqrt{2}}x_3 &
\frac{1}{2}x_1+\frac{\sqrt{2}}{2}x_2+\frac{1}{2}x_3 &
\frac{1}{2}x_1-\frac{\sqrt{2}}{2}x_2+\frac{1}{2}x_3
\end{bmatrix}
\begin{bmatrix}
2&&\\
&2-\sqrt{2}&\\
&&2+\sqrt{2}
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}}x_1 +\frac{1}{\sqrt{2}}x_3\\
\frac{1}{2}x_1+\frac{\sqrt{2}}{2}x_2+\frac{1}{2}x_3\\
\frac{1}{2}x_1-\frac{\sqrt{2}}{2}x_2+\frac{1}{2}x_3
\end{bmatrix}
\\& = 
(2)(\frac{1}{\sqrt{2}}x_1 +\frac{1}{\sqrt{2}}x_3)^2 
+(2-\sqrt{2})(\frac{1}{2}x_1+\frac{\sqrt{2}}{2}x_2+\frac{1}{2}x_3)^2 
+(2-\sqrt{2})(\frac{1}{2}x_1-\frac{\sqrt{2}}{2}x_2+\frac{1}{2}x_3)^2
\\& = &lambda;_1((q_1x)^T(q_1x) + &lambda;_2(q_2x)^T(q_2x) + &lambda;_3(q_3^Tx)(q_3x)
\\&= x^TQ\sqrt{&Lambda;}\sqrt{&Lambda;}^TQ^Tx 
\\&= (x^TQ\sqrt{&Lambda;})(\sqrt{&Lambda;}^TQ^Tx) \\
\\&= (x^TQ\sqrt{&Lambda;})((Q\sqrt{&Lambda;})^Tx) \\
\\&= ((Q\sqrt{&Lambda;})^Tx)^T((Q\sqrt{&Lambda;})^Tx) \\
\\& =(Ax)^T(Ax) 
\\&=||Ax||^2 
\\&= ||(Q\sqrt{&Lambda;})^Tx||^2
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ax%5ET%26lambda%3Bx+%3D+x%5ETSx+%3D+x%5ETA%5ETAx+%26+%3D+x%5ETQ%5Csqrt%7B%26Lambda%3B%7D%28Q%5Csqrt%7B%26Lambda%3B%7D%29%5ETx+%5C%5C%0A%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%5C%5C%0A0%26%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%26-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D+%5E+%5Cfrac%7B1%7D%7B2%7D%0A%28%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%5C%5C%0A0%26%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%26-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%5E+%5Cfrac%7B1%7D%7B2%7D%29%5ET%0A%5Cbegin%7Bbmatrix%7D%0Ax_1+%5C%5C%0Ax_2+%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%26%3D+x%5ETQ%5Csqrt%7B%26Lambda%3B%7D%5Csqrt%7B%26Lambda%3B%7D%5ETQ%5ETx+%5C%5C%0A%26+%3Dx%5ETA%5ETAx+%5C%5C%0A%26%3D+x%5ETQ%5Csqrt%7B%26Lambda%3B%7D%5Csqrt%7B%26Lambda%3B%7DQ%5ETx+%5C%5C%0A%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%5C%5C%0A0%26%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%26-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D+%5E+%5Cfrac%7B1%7D%7B2%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%5E+%5Cfrac%7B1%7D%7B2%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%5C%5C%0A0%26%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%26-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26+%3D+x%5ETQ%26Lambda%3BQ%5ETx%0A%5C%5C%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%5C%5C%0A0%26%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%26-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%5C%5C%0A0%26%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%26-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B2%7D%26%5Cfrac%7B1%7D%7B2%7D%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26+%3D+%28x%5ETQ%29%26Lambda%3B%28Q%5ETx%29%0A%5C%5C%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx_1+%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx_3+%26%0A%5Cfrac%7B1%7D%7B2%7Dx_1%2B%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7Dx_2%2B%5Cfrac%7B1%7D%7B2%7Dx_3+%26%0A%5Cfrac%7B1%7D%7B2%7Dx_1-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7Dx_2%2B%5Cfrac%7B1%7D%7B2%7Dx_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A2%26%26%5C%5C%0A%262-%5Csqrt%7B2%7D%26%5C%5C%0A%26%262%2B%5Csqrt%7B2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx_1+%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx_3%5C%5C%0A%5Cfrac%7B1%7D%7B2%7Dx_1%2B%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7Dx_2%2B%5Cfrac%7B1%7D%7B2%7Dx_3%5C%5C%0A%5Cfrac%7B1%7D%7B2%7Dx_1-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7Dx_2%2B%5Cfrac%7B1%7D%7B2%7Dx_3%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26+%3D+%0A%282%29%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx_1+%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx_3%29%5E2+%0A%2B%282-%5Csqrt%7B2%7D%29%28%5Cfrac%7B1%7D%7B2%7Dx_1%2B%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7Dx_2%2B%5Cfrac%7B1%7D%7B2%7Dx_3%29%5E2+%0A%2B%282-%5Csqrt%7B2%7D%29%28%5Cfrac%7B1%7D%7B2%7Dx_1-%5Cfrac%7B%5Csqrt%7B2%7D%7D%7B2%7Dx_2%2B%5Cfrac%7B1%7D%7B2%7Dx_3%29%5E2%0A%5C%5C%26+%3D+%26lambda%3B_1%28%28q_1x%29%5ET%28q_1x%29+%2B+%26lambda%3B_2%28q_2x%29%5ET%28q_2x%29+%2B+%26lambda%3B_3%28q_3%5ETx%29%28q_3x%29%0A%5C%5C%26%3D+x%5ETQ%5Csqrt%7B%26Lambda%3B%7D%5Csqrt%7B%26Lambda%3B%7D%5ETQ%5ETx+%0A%5C%5C%26%3D+%28x%5ETQ%5Csqrt%7B%26Lambda%3B%7D%29%28%5Csqrt%7B%26Lambda%3B%7D%5ETQ%5ETx%29+%5C%5C%0A%5C%5C%26%3D+%28x%5ETQ%5Csqrt%7B%26Lambda%3B%7D%29%28%28Q%5Csqrt%7B%26Lambda%3B%7D%29%5ETx%29+%5C%5C%0A%5C%5C%26%3D+%28%28Q%5Csqrt%7B%26Lambda%3B%7D%29%5ETx%29%5ET%28%28Q%5Csqrt%7B%26Lambda%3B%7D%29%5ETx%29+%5C%5C%0A%5C%5C%26+%3D%28Ax%29%5ET%28Ax%29+%0A%5C%5C%26%3D%7C%7CAx%7C%7C%5E2+%0A%5C%5C%26%3D+%7C%7C%28Q%5Csqrt%7B%26Lambda%3B%7D%29%5ETx%7C%7C%5E2%0A%5Cend%7Balign%2A%7D)


Now turn to the example matrix T.    
the cells (1,3) and (3,1) in this symmetric matrix   
move from 0 to b as move from example matrix S to example matix T  

the determinant test is easist:  
- the 1x1 determinant is 2  
- the 2x2 determinant is 4 - 1 = 3  
- the 3x3 determinant involves b:  

det T = 4 + 2b - 2b<sup>2</sup> = (1 + b)(4 - 2b) > 0

det T ≤ 0 for 2 ≤ b ≤ -1   

T has positive energy, det T > 0, for 2 ≥ b ≥ -1

![\begin{align*}
T &= 
\begin{bmatrix}
2&-1&b\\
-1&2&-1\\
b&-1&2
\end{bmatrix}\\
det(T) & = (+1)*(2) * ((2*2) - (-1*-1)) \\
&+(-1) * (-1)((-1*2)-(-1*b) \\
&+(+1) * (b)((-1*-1)-(2*b))\\
&=6\\
&-2+b\\
&+b -2b^2\\
&= -2b^2 + 2b +4\\
&=(-2b+4)(b+1)
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AT+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%26b%5C%5C%0A-1%262%26-1%5C%5C%0Ab%26-1%262%0A%5Cend%7Bbmatrix%7D%5C%5C%0Adet%28T%29+%26+%3D+%28%2B1%29%2A%282%29+%2A+%28%282%2A2%29+-+%28-1%2A-1%29%29+%5C%5C%0A%26%2B%28-1%29+%2A+%28-1%29%28%28-1%2A2%29-%28-1%2Ab%29+%5C%5C%0A%26%2B%28%2B1%29+%2A+%28b%29%28%28-1%2A-1%29-%282%2Ab%29%29%5C%5C%0A%26%3D6%5C%5C%0A%26-2%2Bb%5C%5C%0A%26%2Bb+-2b%5E2%5C%5C%0A%26%3D+-2b%5E2+%2B+2b+%2B4%5C%5C%0A%26%3D%28-2b%2B4%29%28b%2B1%29%0A%5Cend%7Balign%2A%7D%0A)

**positive semi definite matrices**

the smallest &lambda; is zero. 

the energy **in its eigenvector** is   
x<sup>T</sup>Sx = x<sup>t</sup>0x = 0

these matrices on the edge of positive defninitiveness are positive semi definite.  

here are 2 examples, that of course are not invertible since determinants are zero:  

S has eigenvalues 5, 0  
S upper left determinants are 1 for 1x1 and zero for 2x2  
S rank is 1  
S factors into A<sup>T</sup> with dependent columns in A:  


![\begin{align*}
S &= 
\begin{bmatrix}
1&2\\
2&4
\end{bmatrix} = A^TA = 
\begin{bmatrix}
1&0\\
2&0
\end{bmatrix}
\begin{bmatrix}
1&2\\
0&0
\end{bmatrix}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%262%5C%5C%0A2%264%0A%5Cend%7Bbmatrix%7D+%3D+A%5ETA+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A2%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%262%5C%5C%0A0%260%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D%0A)


this cyclic T matric also has determinant zero as computed above when b = -1  
T is thus singular.  
the eigenvector x = (1,1,1) has Tx = &lambda;x = 0 and thusly x<sup>T</sup>Tx = x<sup>Tx = 0.   
[because T is singular, the eigenvalue of 0 has the null space as this eigenvector and T has this eigenvector as its null space; thus when x<sub>1</sub> = (1,1,1) we know Tx<sub>1</sub> = zero by null space and by &lambda;<sub>1</sub>x<sub>1</sub> = zero because &lambda;<sub>1</sub> = 0]
vectors in all directions other than x<sub>1</sub> = (1,1,1) do give positive energy.  
[for example &lambda;<sub>2</sub> = 3 has x<sub>2</sub> = (2,-1,-1]

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/110717280-bedbea80-81d6-11eb-91dc-56ed56264cfa.png">

T can be written as A<sup>T</sup> in many ways, but A will always have dependent columns with (1,1,1) in it's null space.  

here, "second difference" T from "1st difference" A 
or "cyclic" T from "cyclic" A

because X is singular, with the 2nd and 3rd columns identical, T is not diagonalizable into X&Lambda;X<sup>-1</sup>.

T = -ones(3) + 3*eye(3)
trace(T) = 6
det(T) = 0 • 3 • 3

![\begin{align*}
T &= 
\begin{bmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{bmatrix}
=\begin{bmatrix}
1&-1&0\\
0&1&-1\\
-1&0&1
\end{bmatrix}
\begin{bmatrix}
1&0&-1\\
1&-1&0\\
0&-1&1
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AT+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2%26-1%26-1%5C%5C%0A-1%262%26-1%5C%5C%0A-1%26-1%262%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A1%26-1%260%5C%5C%0A0%261%26-1%5C%5C%0A-1%260%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%26-1%5C%5C%0A1%26-1%260%5C%5C%0A0%26-1%261%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

positive semi definite matrics all have &lambda;s ≥ 0 and all x<sup>Sx ≥ 0.  
these weak inequalities include positive definite S and singular matrices at the edge (positive semi definite.)

**the ellipse**

ax<sup>2</sup> + bxy + cy<sup>2</sup> = 1

think of a tilted ellipse x<sup>T</sup>Sx = 1  
its center is (0,0) 

turn it to line up with coordinate axes (X and Y)

these 2 ellipses show the geometry behind the factorization of S = Q&Lambda;Q<sup>-1</sup> = Q&Lambda;Q<sup>T</sup>

1. the tilted ellipse is associated with S: its equation is x<sup>T</sup>Sx = 1.  
2. the lined up ellipse is associated with &Lambda: its equation is X<sup>T</sup>&Lambda;X = 1.  
3. the rotation matrix that lines up the ellipse is the eigenvector matrix Q.  

[x<sup>T</sup>Sx = X<sup>T</sup>&Lambda;X is the origin of this in order to prove PDef PSDef NDef.  x<sup>T</sup>Sx = x<sup>T</sup>A<sup>T</sup>Ax = LDL<sup>T</sup> = Q&Lambda;Q<sup>T</sup> = ||Ax||<sup>2</sup> ]


titled ellipse:  5x<sup>2</sup> + 8xy + 5y<sup>2</sup> = x<sup>T</sup>Sx = 1    
lined up ellipse = 9X<sup>2</sup> + Y<sup>2</sup> = &lambda;<sub>1</sub>X<sup>2</sup> + &lambda;<sub>2</sub>Y<sup>2</sup> = 1     

ellipse tilting to the LHS:  
x1 = (1,-1) upon which ellipse intersects (x<sub>1</sub>, y<sub>1</sub>) = (1/3)(1/√2,1/√2)   
x2 = (1,1) upon which ellipse intersects (x<sub>2</sub>, y<sub>2</sub>) = (1)(1/√2,-1/√2)   
5x<sup>2</sup> + 8xy + 5y<sup>2</sup> = x<sup>T</sup>Sx = 1  

ellipse lined up taller than wide:   
intersects (X<sub>1</sub>, Y<sub>1</sub>) = (0,1) and (X<sub>2</sub>, Y<sub>2</sub>) = (1/2,0)
9Y<sup>2</sup> + Y<sup>2</sup> = 1

https://courses.lumenlearning.com/waymakercollegealgebra/chapter/equations-of-ellipses/


**example 2**

find axes of this titled ellipse: 5x<sup>2</sup> + 8xy + 5y<sup>2</sup> = 1

solution:  
start with the positive definite matrix that makes this equation   

![\begin{align*}
&5x^2 + 8xy + 5y^2 = 1\\
x^TSx =&
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
5&4\\
4&5
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
(x^TS)x=&
\begin{bmatrix}
5x+4y & 4x+5y
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
x^T(Sx)=&
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
5x+4y\\
4x+5y
\end{bmatrix}
\\&=
5xx+4xy+4xy+5yy
\\&=
5x^2+8xy+5y^2
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%265x%5E2+%2B+8xy+%2B+5y%5E2+%3D+1%5C%5C%0Ax%5ETSx+%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5%264%5C%5C%0A4%265%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%28x%5ETS%29x%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A5x%2B4y+%26+4x%2B5y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0Ax%5ET%28Sx%29%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5x%2B4y%5C%5C%0A4x%2B5y%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%26%3D%0A5xx%2B4xy%2B4xy%2B5yy%0A%5C%5C%26%3D%0A5x%5E2%2B8xy%2B5y%5E2%0A%5Cend%7Balign%2A%7D%0A)

decompose x<sup>T</sup>Sx into x<sup>T</sup>Q&Lambda;Q<sup>T</sup>x   
the eigenvectors are (1,1) and (1,-1)  
divide by length √2 for unit vectors   
then S = Q&Lambda;Q<sup>T</sup>
eigenvectors in Q and eigenvalues 9 and 1 in &Lambda;

![\begin{align*}
&5x^2 + 8xy + 5y^2 = 1\\
S =&
\begin{bmatrix}
5&4\\
4&5
\end{bmatrix}\\
det(S-&lambda;I) =&
det
\begin{bmatrix}
5-&lambda;&4\\
4&5-&lambda;
\end{bmatrix} =0\\
=& &lambda;^2 - 10&lambda; + 25 -16 =0\\
=& &lambda;^2 - 10&lambda; + 9 =0 \\
=& (&lambda; - 9)(&lambda; -1) = 0 \\
\longrightarrow & &lambda;_1 =9, &lambda;_2 =1 \\
(S-&lambda;_1I)x_1 = (S-9I)x_1=&
\begin{bmatrix}
5-&lambda;_1&4\\
4&5-&lambda;_1
\end{bmatrix}
\begin{bmatrix}
x_1
\end{bmatrix} =0\\
=&
\begin{bmatrix}
5-9&4\\
4&5-9
\end{bmatrix}
\begin{bmatrix}
x_1
\end{bmatrix} =0\\
=&
\begin{bmatrix}
-4&4\\
4&-4
\end{bmatrix}
\begin{bmatrix}
x_1
\end{bmatrix} = 0 \\
\longrightarrow & x_1 = 
\begin{bmatrix}
1\\
1
\end{bmatrix}\\
||x_1|| = \sqrt{1^2+1^2} = \sqrt{2} \longrightarrow & q_1 = 
\begin{bmatrix}
\frac{1}{\sqrt{2}}\\
\frac{1}{\sqrt{2}}
\end{bmatrix}\\
(S-&lambda;_2I)x_2 = (S-1I)x_2=&
\begin{bmatrix}
5-&lambda;_2&4\\
4&5-&lambda;_2
\end{bmatrix}
\begin{bmatrix}
x_2
\end{bmatrix} =0\\
=&
\begin{bmatrix}
5-1&4\\
4&5-1
\end{bmatrix}
\begin{bmatrix}
x_2
\end{bmatrix} =0\\
=&
\begin{bmatrix}
4&4\\
4&4
\end{bmatrix}
\begin{bmatrix}
x_2
\end{bmatrix} = 0 \\
\longrightarrow & x_2 = 
\begin{bmatrix}
1\\
-1
\end{bmatrix}\\
||x_2|| = \sqrt{1^2+(-1)^2} = \sqrt{2} \longrightarrow & q_2 = 
\begin{bmatrix}
\frac{1}{\sqrt{2}}\\
\frac{-1}{\sqrt{2}}
\end{bmatrix}\\
\\
S =
\begin{bmatrix}
5&4\\
4&5
\end{bmatrix} =& Q&Lambda;Q^T \\
=& \frac{1}{\sqrt{2}} 
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
9&\\
&1
\end{bmatrix}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}^T
\frac{1}{\sqrt{2}} \\
x^TSx =
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
5&4\\
4&5
\end{bmatrix} 
\begin{bmatrix}
x\\
y
\end{bmatrix}
=& x^TQ&Lambda;Q^Tx \\
=& 
\begin{bmatrix}
x&y
\end{bmatrix}
\frac{1}{\sqrt{2}} 
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
9&\\
&1
\end{bmatrix}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}^T
\frac{1}{\sqrt{2}}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
=& 
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\
\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}
\end{bmatrix}
\begin{bmatrix}
9&\\
&1
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\
\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}
\end{bmatrix}^T
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
=& 
\begin{bmatrix}
(\frac{1}{\sqrt{2}}x+\frac{1}{\sqrt{2}}y) &
(\frac{1}{\sqrt{2}}x-\frac{1}{\sqrt{2}}y)
\end{bmatrix}
\begin{bmatrix}
9&\\
&1
\end{bmatrix}
\begin{bmatrix}
(\frac{1}{\sqrt{2}}x+\frac{1}{\sqrt{2}}y)\\
(\frac{1}{\sqrt{2}}x-\frac{1}{\sqrt{2}}y)
\end{bmatrix}\\
=& 
\begin{bmatrix}
9(\frac{1}{\sqrt{2}}x+\frac{1}{\sqrt{2}}y) &
1(\frac{1}{\sqrt{2}}x-\frac{1}{\sqrt{2}}y)
\end{bmatrix}
\begin{bmatrix}
(\frac{1}{\sqrt{2}}x+\frac{1}{\sqrt{2}}y)\\
(\frac{1}{\sqrt{2}}x-\frac{1}{\sqrt{2}}y)
\end{bmatrix}\\
=& 
\begin{bmatrix}
(\frac{1}{\sqrt{2}}x+\frac{1}{\sqrt{2}}y) &
(\frac{1}{\sqrt{2}}x-\frac{1}{\sqrt{2}}y)
\end{bmatrix}
\begin{bmatrix}
9(\frac{1}{\sqrt{2}}x+\frac{1}{\sqrt{2}}y)\\
1(\frac{1}{\sqrt{2}}x-\frac{1}{\sqrt{2}}y)
\end{bmatrix}\\
=& 
9(\frac{1}{\sqrt{2}}x+\frac{1}{\sqrt{2}}y)^2 + 1(\frac{1}{\sqrt{2}}x-\frac{1}{\sqrt{2}}y)^2\\
=& 
9(\frac{x}{\sqrt{2}}+\frac{y}{\sqrt{2}})^2 + 1(\frac{x}{\sqrt{2}}-\frac{y}{\sqrt{2}})^2\\
=& 
9(\frac{x+y}{\sqrt{2}})^2 + 1(\frac{x-y}{\sqrt{2}})^2
\\
\\
x^TSx = 5x^2 +8xy+5y^2
=& x^TQ&Lambda;Q^Tx \\
\\
=& 
9 ( \frac{x+y}{\sqrt{2}})^2 + 1 ( \frac{x-y}{\sqrt{2}})^2\\
=& 
x^T
\begin{bmatrix}
q_1&q_2
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
q_1&q_2
\end{bmatrix}^T
x\\
=& 
x^T
\begin{bmatrix}
q_1&q_2
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
q_1^T\\
q_2^T
\end{bmatrix}
x\\
=& 
\begin{bmatrix}
x^Tq_1&x^Tq_2
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
q_1^Tx\\
q_2^Tx
\end{bmatrix}\\
=& 
\begin{bmatrix}
x^Tq_1&lambda;_1&x^Tq_2&lambda;_1
\end{bmatrix}
\begin{bmatrix}
q_1^Tx\\
q_2^Tx
\end{bmatrix}
\\
=& 
\begin{bmatrix}
x^Tq_1&x^Tq_2
\end{bmatrix}
\begin{bmatrix}
&lambda;_1q_1^Tx\\
&lambda;_2q_2^Tx
\end{bmatrix}\\
=&
x^Tq_1&lambda;_1q_1^Tx +x^Tq_2&lambda;_2q_2^Tx
\\
 \\
\\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%265x%5E2+%2B+8xy+%2B+5y%5E2+%3D+1%5C%5C%0AS+%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A5%264%5C%5C%0A4%265%0A%5Cend%7Bbmatrix%7D%5C%5C%0Adet%28S-%26lambda%3BI%29+%3D%26%0Adet%0A%5Cbegin%7Bbmatrix%7D%0A5-%26lambda%3B%264%5C%5C%0A4%265-%26lambda%3B%0A%5Cend%7Bbmatrix%7D+%3D0%5C%5C%0A%3D%26+%26lambda%3B%5E2+-+10%26lambda%3B+%2B+25+-16+%3D0%5C%5C%0A%3D%26+%26lambda%3B%5E2+-+10%26lambda%3B+%2B+9+%3D0+%5C%5C%0A%3D%26+%28%26lambda%3B+-+9%29%28%26lambda%3B+-1%29+%3D+0+%5C%5C%0A%5Clongrightarrow+%26+%26lambda%3B_1+%3D9%2C+%26lambda%3B_2+%3D1+%5C%5C%0A%28S-%26lambda%3B_1I%29x_1+%3D+%28S-9I%29x_1%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A5-%26lambda%3B_1%264%5C%5C%0A4%265-%26lambda%3B_1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%0A%5Cend%7Bbmatrix%7D+%3D0%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A5-9%264%5C%5C%0A4%265-9%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%0A%5Cend%7Bbmatrix%7D+%3D0%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A-4%264%5C%5C%0A4%26-4%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%0A%5Cend%7Bbmatrix%7D+%3D+0+%5C%5C%0A%5Clongrightarrow+%26+x_1+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%7C%7Cx_1%7C%7C+%3D+%5Csqrt%7B1%5E2%2B1%5E2%7D+%3D+%5Csqrt%7B2%7D+%5Clongrightarrow+%26+q_1+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%28S-%26lambda%3B_2I%29x_2+%3D+%28S-1I%29x_2%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A5-%26lambda%3B_2%264%5C%5C%0A4%265-%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_2%0A%5Cend%7Bbmatrix%7D+%3D0%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A5-1%264%5C%5C%0A4%265-1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_2%0A%5Cend%7Bbmatrix%7D+%3D0%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A4%264%5C%5C%0A4%264%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_2%0A%5Cend%7Bbmatrix%7D+%3D+0+%5C%5C%0A%5Clongrightarrow+%26+x_2+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%7C%7Cx_2%7C%7C+%3D+%5Csqrt%7B1%5E2%2B%28-1%29%5E2%7D+%3D+%5Csqrt%7B2%7D+%5Clongrightarrow+%26+q_2+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%5C%5C%0A%5Cfrac%7B-1%7D%7B%5Csqrt%7B2%7D%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0AS+%3D%0A%5Cbegin%7Bbmatrix%7D%0A5%264%5C%5C%0A4%265%0A%5Cend%7Bbmatrix%7D+%3D%26+Q%26Lambda%3BQ%5ET+%5C%5C%0A%3D%26+%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D+%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%26-1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A9%26%5C%5C%0A%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%26-1%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D+%5C%5C%0Ax%5ETSx+%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5%264%5C%5C%0A4%265%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%0A%3D%26+x%5ETQ%26Lambda%3BQ%5ETx+%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D+%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%26-1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A9%26%5C%5C%0A%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%261%5C%5C%0A1%26-1%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26-%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A9%26%5C%5C%0A%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%5C%5C%0A%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%26-%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29+%26%0A%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx-%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A9%26%5C%5C%0A%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%5C%5C%0A%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx-%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A9%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29+%26%0A1%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx-%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%5C%5C%0A%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx-%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29+%26%0A%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx-%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A9%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%5C%5C%0A1%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx-%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A9%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx%2B%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%5E2+%2B+1%28%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dx-%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7Dy%29%5E2%5C%5C%0A%3D%26+%0A9%28%5Cfrac%7Bx%7D%7B%5Csqrt%7B2%7D%7D%2B%5Cfrac%7By%7D%7B%5Csqrt%7B2%7D%7D%29%5E2+%2B+1%28%5Cfrac%7Bx%7D%7B%5Csqrt%7B2%7D%7D-%5Cfrac%7By%7D%7B%5Csqrt%7B2%7D%7D%29%5E2%5C%5C%0A%3D%26+%0A9%28%5Cfrac%7Bx%2By%7D%7B%5Csqrt%7B2%7D%7D%29%5E2+%2B+1%28%5Cfrac%7Bx-y%7D%7B%5Csqrt%7B2%7D%7D%29%5E2%0A%5C%5C%0A%5C%5C%0Ax%5ETSx+%3D+5x%5E2+%2B8xy%2B5y%5E2%0A%3D%26+x%5ETQ%26Lambda%3BQ%5ETx+%5C%5C%0A%5C%5C%0A%3D%26+%0A9+%28+%5Cfrac%7Bx%2By%7D%7B%5Csqrt%7B2%7D%7D%29%5E2+%2B+1+%28+%5Cfrac%7Bx-y%7D%7B%5Csqrt%7B2%7D%7D%29%5E2%5C%5C%0A%3D%26+%0Ax%5ET%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%26q_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%26q_2%0A%5Cend%7Bbmatrix%7D%5ET%0Ax%5C%5C%0A%3D%26+%0Ax%5ET%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%26q_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%5ET%5C%5C%0Aq_2%5ET%0A%5Cend%7Bbmatrix%7D%0Ax%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5ETq_1%26x%5ETq_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%5ETx%5C%5C%0Aq_2%5ETx%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5ETq_1%26lambda%3B_1%26x%5ETq_2%26lambda%3B_1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%5ETx%5C%5C%0Aq_2%5ETx%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5ETq_1%26x%5ETq_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1q_1%5ETx%5C%5C%0A%26lambda%3B_2q_2%5ETx%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0Ax%5ETq_1%26lambda%3B_1q_1%5ETx+%2Bx%5ETq_2%26lambda%3B_2q_2%5ETx%0A%5C%5C%0A+%5C%5C%0A%5C%5C%0A%5Cend%7Balign%2A%7D)


repeats some of the above but generalizes to terms:

![\begin{align*}
x^TSx =
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
5&4\\
4&5
\end{bmatrix} 
\begin{bmatrix}
x\\
y
\end{bmatrix}
=& x^TQ&Lambda;Q^Tx \\
\\
x^TSx =
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
s_{11}&s_{12}\\
s_{21}&s_{22}
\end{bmatrix} 
\begin{bmatrix}
x\\
y
\end{bmatrix}
=& x^TQ&Lambda;Q^Tx \\
=& 
\begin{bmatrix}
x&y
\end{bmatrix}
\frac{1}{||q||} 
\begin{bmatrix}
q_{11}&q_{12}\\
q_{21}&q_{22}
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
q_{11}&q_{12}\\
q_{21}&q_{22}
\end{bmatrix}^T
\frac{1}{||q||}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
=& 
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
\frac{q_{11}}{||q_1|}&\frac{q_{12}}{||q_2||}\\
\frac{q_{21}}{||q_1}&-\frac{q_{22}}{||q_2||}
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
\frac{q_{11}}{||q_1|}&\frac{q_{12}}{||q_2||}\\
\frac{q_{21}}{||q_1}&-\frac{q_{22}}{||q_2||}
\end{bmatrix}^T
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
=& 
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
\frac{q_{11}}{||q_1||}&\frac{q_{12}}{||q_2||}\\
\frac{q_{21}}{||q_1||}&-\frac{q_{22}}{||q_2||}
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
\frac{q_{11}}{||q_1||}&\frac{q_{21}}{||q_1||}\\
\frac{q_{12}}{||q_2||}&-\frac{q_{22}}{||q_2||}
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
=& 
\begin{bmatrix}
(\frac{q_{11}}{||q_1|}x+\frac{q_{21}}{||q_1||}y)&
(\frac{q_{12}}{||q_2}x-\frac{q_{22}}{||q_2||}y)
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
(\frac{q_{11}}{||q_1||}x+\frac{q_{21}}{||q_1||}y)\\
(\frac{q_{12}}{||q_2||}x-\frac{q_{22}}{||q_2||}y)
\end{bmatrix}\\
=& 
\begin{bmatrix}
&lambda;_1(\frac{q_{11}}{||q_1||}x+\frac{q_{21}}{||q_1||}y) &
&lambda;_2(\frac{q_{12}}{||q_2||}x-\frac{q_{22}}{||q_2||}y)
\end{bmatrix}
\begin{bmatrix}
(\frac{q_{11}}{||q_1||}x+\frac{q_{21}}{||q_1||}y)\\
(\frac{q_{12}}{||q_2||}x-\frac{q_{22}}{||q_2||}y)
\end{bmatrix}\\
=& 
\begin{bmatrix}
(\frac{q_{11}}{||q_1||}x+\frac{q_{21}}{||q_1||}y)&
(\frac{q_{12}}{||q_2||}x-\frac{q_{22}}{||q_2||}y)
\end{bmatrix}
\begin{bmatrix}
&lambda;_1(\frac{q_{11}}{||q_1||}x+\frac{q_{21}}{||q_1||}y)\\
&lambda;_2(\frac{q_{12}}{||q_2||}x-\frac{q_{22}}{||q_2||}y)
\end{bmatrix}\\
=& 
&lambda;_1(\frac{q_{11}}{||q_1||}x+\frac{q_{21}}{||q_1||}y)^2 + &lambda;_2(\frac{q_{12}}{||q_2||}x-\frac{q_{22}}{||q_2||}y)^2\\
=& 
&lambda;_1(\frac{q_{11}x + q_{21}y}{||q_1||})^2 + &lambda;_2(\frac{q_{12}x + q_{22}y}{||q_2||})^2 \\
\\
X = & \frac{q_{11}x + q_{21}y}{||q_1||} \\
Y =& \frac{q_{12}x + q_{22}y}{||q_2||} \\
x^TQ&Lambda;Q^Tx
=&  &lambda;_1 X^2 + &lambda;_2 Y^2
=& 
9(\frac{x}{\sqrt{2}}+\frac{y}{\sqrt{2}})^2 + 1(\frac{x}{\sqrt{2}}-\frac{y}{\sqrt{2}})^2\\
=& 
9(\frac{x+y}{\sqrt{2}})^2 + 1(\frac{x-y}{\sqrt{2}})^2
\\
\\
X = & \frac{x+y}{\sqrt{2}}\\
Y =& \frac{x-y}{\sqrt{2}}\\
x^TQ&Lambda;Q^Tx
=&  9 X^2 + 1 Y^2
\\
\\
x^TSx = 5x^2 +8xy+5y^2
=& x^TQ&Lambda;Q^Tx \\
\\
=& 
9 ( \frac{x+y}{\sqrt{2}})^2 + 1 ( \frac{x-y}{\sqrt{2}})^2\\
=& 
x^T
\begin{bmatrix}
q_1&q_2
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
q_1&q_2
\end{bmatrix}^T
x\\
=& 
x^T
\begin{bmatrix}
q_1&q_2
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
q_1^T\\
q_2^T
\end{bmatrix}
x\\
=& 
\begin{bmatrix}
x^Tq_1&x^Tq_2
\end{bmatrix}
\begin{bmatrix}
&lambda;_1&\\
&&lambda;_2
\end{bmatrix}
\begin{bmatrix}
q_1^Tx\\
q_2^Tx
\end{bmatrix}\\
=& 
\begin{bmatrix}
x^Tq_1&lambda;_1&x^Tq_2&lambda;_1
\end{bmatrix}
\begin{bmatrix}
q_1^Tx\\
q_2^Tx
\end{bmatrix}
\\
=& 
\begin{bmatrix}
x^Tq_1&x^Tq_2
\end{bmatrix}
\begin{bmatrix}
&lambda;_1q_1^Tx\\
&lambda;_2q_2^Tx
\end{bmatrix}\\
=&
x^Tq_1&lambda;_1q_1^Tx +x^Tq_2&lambda;_2q_2^Tx
\\
 \\
\\
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ax%5ETSx+%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5%264%5C%5C%0A4%265%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%0A%3D%26+x%5ETQ%26Lambda%3BQ%5ETx+%5C%5C%0A%5C%5C%0Ax%5ETSx+%3D%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0As_%7B11%7D%26s_%7B12%7D%5C%5C%0As_%7B21%7D%26s_%7B22%7D%0A%5Cend%7Bbmatrix%7D+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%0A%3D%26+x%5ETQ%26Lambda%3BQ%5ETx+%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cfrac%7B1%7D%7B%7C%7Cq%7C%7C%7D+%0A%5Cbegin%7Bbmatrix%7D%0Aq_%7B11%7D%26q_%7B12%7D%5C%5C%0Aq_%7B21%7D%26q_%7B22%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_%7B11%7D%26q_%7B12%7D%5C%5C%0Aq_%7B21%7D%26q_%7B22%7D%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cfrac%7B1%7D%7B%7C%7Cq%7C%7C%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7D%26%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7D%5C%5C%0A%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7D%26-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7D%26%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7D%5C%5C%0A%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7D%26-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7D%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7C%7D%26%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7D%5C%5C%0A%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7C%7C%7D%26-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7C%7D%26%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7C%7C%7D%5C%5C%0A%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7D%26-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7Dx%2B%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7C%7C%7Dy%29%26%0A%28%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7Dx-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7Dy%29%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7C%7Dx%2B%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7C%7C%7Dy%29%5C%5C%0A%28%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7Dx-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7Dy%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%28%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7C%7Dx%2B%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7C%7C%7Dy%29+%26%0A%26lambda%3B_2%28%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7Dx-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7Dy%29%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7C%7Dx%2B%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7C%7C%7Dy%29%5C%5C%0A%28%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7Dx-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7Dy%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A%28%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7C%7Dx%2B%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7C%7C%7Dy%29%26%0A%28%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7Dx-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7Dy%29%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%28%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7C%7Dx%2B%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7C%7C%7Dy%29%5C%5C%0A%26lambda%3B_2%28%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7Dx-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7Dy%29%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%26lambda%3B_1%28%5Cfrac%7Bq_%7B11%7D%7D%7B%7C%7Cq_1%7C%7C%7Dx%2B%5Cfrac%7Bq_%7B21%7D%7D%7B%7C%7Cq_1%7C%7C%7Dy%29%5E2+%2B+%26lambda%3B_2%28%5Cfrac%7Bq_%7B12%7D%7D%7B%7C%7Cq_2%7C%7C%7Dx-%5Cfrac%7Bq_%7B22%7D%7D%7B%7C%7Cq_2%7C%7C%7Dy%29%5E2%5C%5C%0A%3D%26+%0A%26lambda%3B_1%28%5Cfrac%7Bq_%7B11%7Dx+%2B+q_%7B21%7Dy%7D%7B%7C%7Cq_1%7C%7C%7D%29%5E2+%2B+%26lambda%3B_2%28%5Cfrac%7Bq_%7B12%7Dx+%2B+q_%7B22%7Dy%7D%7B%7C%7Cq_2%7C%7C%7D%29%5E2+%5C%5C%0A%5C%5C%0AX+%3D+%26+%5Cfrac%7Bq_%7B11%7Dx+%2B+q_%7B21%7Dy%7D%7B%7C%7Cq_1%7C%7C%7D+%5C%5C%0AY+%3D%26+%5Cfrac%7Bq_%7B12%7Dx+%2B+q_%7B22%7Dy%7D%7B%7C%7Cq_2%7C%7C%7D+%5C%5C%0Ax%5ETQ%26Lambda%3BQ%5ETx%0A%3D%26++%26lambda%3B_1+X%5E2+%2B+%26lambda%3B_2+Y%5E2%0A%3D%26+%0A9%28%5Cfrac%7Bx%7D%7B%5Csqrt%7B2%7D%7D%2B%5Cfrac%7By%7D%7B%5Csqrt%7B2%7D%7D%29%5E2+%2B+1%28%5Cfrac%7Bx%7D%7B%5Csqrt%7B2%7D%7D-%5Cfrac%7By%7D%7B%5Csqrt%7B2%7D%7D%29%5E2%5C%5C%0A%3D%26+%0A9%28%5Cfrac%7Bx%2By%7D%7B%5Csqrt%7B2%7D%7D%29%5E2+%2B+1%28%5Cfrac%7Bx-y%7D%7B%5Csqrt%7B2%7D%7D%29%5E2%0A%5C%5C%0A%5C%5C%0AX+%3D+%26+%5Cfrac%7Bx%2By%7D%7B%5Csqrt%7B2%7D%7D%5C%5C%0AY+%3D%26+%5Cfrac%7Bx-y%7D%7B%5Csqrt%7B2%7D%7D%5C%5C%0Ax%5ETQ%26Lambda%3BQ%5ETx%0A%3D%26++9+X%5E2+%2B+1+Y%5E2%0A%5C%5C%0A%5C%5C%0Ax%5ETSx+%3D+5x%5E2+%2B8xy%2B5y%5E2%0A%3D%26+x%5ETQ%26Lambda%3BQ%5ETx+%5C%5C%0A%5C%5C%0A%3D%26+%0A9+%28+%5Cfrac%7Bx%2By%7D%7B%5Csqrt%7B2%7D%7D%29%5E2+%2B+1+%28+%5Cfrac%7Bx-y%7D%7B%5Csqrt%7B2%7D%7D%29%5E2%5C%5C%0A%3D%26+%0Ax%5ET%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%26q_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%26q_2%0A%5Cend%7Bbmatrix%7D%5ET%0Ax%5C%5C%0A%3D%26+%0Ax%5ET%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%26q_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%5ET%5C%5C%0Aq_2%5ET%0A%5Cend%7Bbmatrix%7D%0Ax%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5ETq_1%26x%5ETq_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1%26%5C%5C%0A%26%26lambda%3B_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%5ETx%5C%5C%0Aq_2%5ETx%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5ETq_1%26lambda%3B_1%26x%5ETq_2%26lambda%3B_1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Aq_1%5ETx%5C%5C%0Aq_2%5ETx%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%5ETq_1%26x%5ETq_2%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A%26lambda%3B_1q_1%5ETx%5C%5C%0A%26lambda%3B_2q_2%5ETx%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0Ax%5ETq_1%26lambda%3B_1q_1%5ETx+%2Bx%5ETq_2%26lambda%3B_2q_2%5ETx%0A%5C%5C%0A+%5C%5C%0A%5C%5C%0A%5Cend%7Balign%2A%7D%0A)


x<sup>T</sup>Sx becomes the sum of squres 5x<sup>2</sup> + 8xy + 5y<sup>2</sup> = 9((x+y)/
2)<sup>2</sup> + 1((x-y)/2)<sup>2</sup>

- the coefficients of the titled ellipse are = 5, 8, 5 which are the diagonal, sum of off-diagonal, and diagonal components of S   
- the axes of the titled ellipse point along the axes of the eigenvectors x<sub>1</sub> = (1,1) and x<sub>2</sub> = (1,-1) and the titled ellipse intersects those axes at q<sub>1</sub> = (1/√2,1√2) and x<sub>2</sub> = (1/√2,-1/√2)
- the coefficients of the lines-up ellipse are 9 and 1 from &Lambda;'s diagonal   
- the pivots are 5 and 9/5. 

this explains why S = Q&Lambda;Q<sup>T</sup> is called the "Principle Axis Theorem".  Q displays the axes.  Not only axis directions, from the eigenvectors, but also the axis lengths, from the eigenvalues.  To see it all, including why the largest eigenvalues, &lambda;<sub>1</sub> = 9 has shortest length, use capital letters for the new coordinates that line up the ellipse.  

lined up:

X = (x+y) / √2

Y = (x-y) / √2 

9 [ (x+y) / √2 ]<sup>2</sup> + 1 [ (x-y) / √2 ]<sup>2</sup> = 1

becomes 

9 X<sup>2</sup> + 1 Y<sup>2</sup> = 1

the largest value of X<sup>2</sup> = 1/9 when Y = 0  
the largest value of X<sup>2</sup> = 1 when X = 0

the endpoit of the shorter axis has X = 1/3 so that X<sup>2</sup> = 1/9 and Y = 0

the bigger eigenvalue 9 gives the shorter axis where the half length that extends from the (0,0) origin = 1/3 = 1/√&lambda;<sub>1</sub>

the smaller eigenvalue 1 gives the longer axis where the half length that extends from the (0,0) origin = 1/1 = 1/√&lambda;<sub>2</sub>


![\begin{align*}
X &=\frac{x+y}{\sqrt{2}}\\
Y &=\frac{x-y}{\sqrt{2}}\\
1&=9(\frac{x+y}{\sqrt{2}})^2 +1(\frac{x-y}{\sqrt{2}})^2\\
\\
1&=9X^2 +1Y^2\\
1&=(&lambda;_1=9)(X=\frac{1}{\sqrt{&lambda;_1=9}})+(&lambda;_2=1)(Y=0)\\
1&=(&lambda;_1=9)(X=0)+(&lambda;_2=1)(Y=\frac{1}{\sqrt{&lambda;_2=1}})
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AX+%26%3D%5Cfrac%7Bx%2By%7D%7B%5Csqrt%7B2%7D%7D%5C%5C%0AY+%26%3D%5Cfrac%7Bx-y%7D%7B%5Csqrt%7B2%7D%7D%5C%5C%0A1%26%3D9%28%5Cfrac%7Bx%2By%7D%7B%5Csqrt%7B2%7D%7D%29%5E2+%2B1%28%5Cfrac%7Bx-y%7D%7B%5Csqrt%7B2%7D%7D%29%5E2%5C%5C%0A%5C%5C%0A1%26%3D9X%5E2+%2B1Y%5E2%5C%5C%0A1%26%3D%28%26lambda%3B_1%3D9%29%28X%3D%5Cfrac%7B1%7D%7B%5Csqrt%7B%26lambda%3B_1%3D9%7D%7D%29%2B%28%26lambda%3B_2%3D1%29%28Y%3D0%29%5C%5C%0A1%26%3D%28%26lambda%3B_1%3D9%29%28X%3D0%29%2B%28%26lambda%3B_2%3D1%29%28Y%3D%5Cfrac%7B1%7D%7B%5Csqrt%7B%26lambda%3B_2%3D1%7D%7D%29%0A%5Cend%7Balign%2A%7D%0A)

in the xy system the axes are along the eigenvectors of S: (1,1) and (1,-1) 

in the XY system the axes are along the eigenvectors of &Lambda;: (1,0) and (0,1)

![\begin{align*}
&Lambda; &= 
\begin{bmatrix}
9&\\
&1
\end{bmatrix}\\
det(&Lambda;-&lambda;I) &=
(\begin{bmatrix}
9-&lambda;&\\
&1-&lambda;
\end{bmatrix})=(9-&lambda;)(1-&lambda;)=0\\
&lambda;_1 = 9 &\longrightarrow
\begin{bmatrix}
0&0\\
0&-8
\end{bmatrix}
\begin{bmatrix}
x_1
\end{bmatrix}
\longrightarrow 
x_1=
\begin{bmatrix}
1\\
0
\end{bmatrix}\\
&lambda;_2 = 1 &\longrightarrow
\begin{bmatrix}
8&0\\
0&0
\end{bmatrix}
\begin{bmatrix}
x_2
\end{bmatrix}
\longrightarrow 
x_2=
\begin{bmatrix}
0\\
1
\end{bmatrix}\\
X &=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%26Lambda%3B+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A9%26%5C%5C%0A%261%0A%5Cend%7Bbmatrix%7D%5C%5C%0Adet%28%26Lambda%3B-%26lambda%3BI%29+%26%3D%0A%28%5Cbegin%7Bbmatrix%7D%0A9-%26lambda%3B%26%5C%5C%0A%261-%26lambda%3B%0A%5Cend%7Bbmatrix%7D%29%3D%289-%26lambda%3B%29%281-%26lambda%3B%29%3D0%5C%5C%0A%26lambda%3B_1+%3D+9+%26%5Clongrightarrow%0A%5Cbegin%7Bbmatrix%7D%0A0%260%5C%5C%0A0%26-8%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+%0Ax_1%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26lambda%3B_2+%3D+1+%26%5Clongrightarrow%0A%5Cbegin%7Bbmatrix%7D%0A8%260%5C%5C%0A0%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_2%0A%5Cend%7Bbmatrix%7D%0A%5Clongrightarrow+%0Ax_2%3D%0A%5Cbegin%7Bbmatrix%7D%0A0%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%5C%5C%0AX+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A0%261%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D%0A)


for reference here is the LDL<sup>T</sup> decomposition

![\begin{align*}
S =&
\begin{bmatrix}
5&4\\
4&5
\end{bmatrix}\\
E_{21}S =&
\begin{bmatrix}
1&0\\
-\frac{4}{5}&1
\end{bmatrix}
\begin{bmatrix}
5&4\\
4&5
\end{bmatrix} \\
=&U\\
=&
\begin{bmatrix}
5&4\\
0&\frac{4}{5}
\end{bmatrix}\\
S =&
\begin{bmatrix}
5&4\\
4&5
\end{bmatrix} \\
=& LDU = LDL^T \\
=&
\begin{bmatrix}
1&0\\
\frac{4}{5}&1
\end{bmatrix}
\begin{bmatrix}
5&0\\
0&\frac{9}{5}
\end{bmatrix}
\begin{bmatrix}
1&\frac{4}{5}\\
0&1
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A5%264%5C%5C%0A4%265%0A%5Cend%7Bbmatrix%7D%5C%5C%0AE_%7B21%7DS+%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A-%5Cfrac%7B4%7D%7B5%7D%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5%264%5C%5C%0A4%265%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%3D%26U%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A5%264%5C%5C%0A0%26%5Cfrac%7B4%7D%7B5%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0AS+%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A5%264%5C%5C%0A4%265%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%3D%26+LDU+%3D+LDL%5ET+%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A%5Cfrac%7B4%7D%7B5%7D%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5%260%5C%5C%0A0%26%5Cfrac%7B9%7D%7B5%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26%5Cfrac%7B4%7D%7B5%7D%5C%5C%0A0%261%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)


S = I gives a circle x<sup>2</sup> + y<sup>2</sup> = 1.

if one eigenvalue is negative  
(e.g. switching a 4 and 5 in the S example above)  
then the ellipse changes to a hyperbola.   
the sum of squares becomes a difference of squares  
9X<sup>2</sup> - 1Y<sup>2</sup> = 1   

for a negative definite matrix like S = -I   
with both &lambda;s negative,  
the graph of -X<sup>2</sup> - Y<sup>2</sup> =1 has no points at all     

if S is n x n, x<sup>T</sup>Sx = 1   
is an ellipsoid in R<sup>n</sup>  [fills up space]   
its axes are the eigenvectors of S   


S = Q&Lambda;Q<sup>T</sup> is positive definite when all &lambda;<sub>i</sub> >0.   
the graph of x<sup>T</sup>Sx = 1 is an ellipse.   
the axes point along eigenvectors of S.  
the half lengths are 1/√&lambda;<sub>1</sub> and 1/√&lambda;<sub>2</sub>

![\begin{align*}
\begin{bmatrix}
x&y
\end{bmatrix}
Q&Lambda;Q^T
\begin{bmatrix}
x\\
y
\end{bmatrix}=
\begin{bmatrix}
X&Y
\end{bmatrix}
&Lambda;
\begin{bmatrix}
X\\
Y
\end{bmatrix}
= &lambda;_1X^2 + &lambda;_2X^2 = 1
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0AQ%26Lambda%3BQ%5ET%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0AX%26Y%0A%5Cend%7Bbmatrix%7D%0A%26Lambda%3B%0A%5Cbegin%7Bbmatrix%7D%0AX%5C%5C%0AY%0A%5Cend%7Bbmatrix%7D%0A%3D+%26lambda%3B_1X%5E2+%2B+%26lambda%3B_2X%5E2+%3D+1%0A%5Cend%7Balign%2A%7D%0A)

**Important application: Test for a Minimum**

Does F(x,y) have a minimum if 
∂F/∂x = 0 and ∂F/∂y = 0 at the point (x,y) = (0,0)?

for f(x) the test for minimum comes from calculus  
if ∂f/∂x = 0 and ∂<sup>2</sup>f/∂x<sup>2</sup> > 0.  

two variables in F(x,y)   
produce a symmetric matrix S   
which contains 4 second derivatives  
**Positive ∂<sup>2</sup>f/∂x<sup>2</sup> changes to positive definite S**

![\begin{align*}
S = 
\begin{bmatrix}
\frac{\partial^2 F}{\partial x^2}&\frac{\partial^2 F}{\partial x\partial y}\\
\frac{\partial^2 F}{\partial x\partial y}&\frac{\partial^2 F}{\partial y^2}
\end{bmatrix}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A%5Cfrac%7B%5Cpartial%5E2+F%7D%7B%5Cpartial+x%5E2%7D%26%5Cfrac%7B%5Cpartial%5E2+F%7D%7B%5Cpartial+x%5Cpartial+y%7D%5C%5C%0A%5Cfrac%7B%5Cpartial%5E2+F%7D%7B%5Cpartial+x%5Cpartial+y%7D%26%5Cfrac%7B%5Cpartial%5E2+F%7D%7B%5Cpartial+y%5E2%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D%0A)

F(x,y) has a minimum if ∂F/∂x = ƒF/∂y = 0 and S is positive definite.  Reason is that S reveals all important terms ax<sup>2</sup> + 2bxy + cy<sup>2</sup> near (x,y) = (0,0)  
The second derivatives of F are 2a, 2b, 2b, 2c.   
For F(x,y,z) the matrix will be 3x3.


review:  
1. positive definite matrices have positive eigenvalues and positive pivots   
2. quick test is given by the UL determinants: a > 0 and ad - b<sup>2</sup> > 0   
3. the graph of energy x<sup>T</sup>Sx is the "bowl" going up from **x = 0**   
x<sup>T</sup>Sx = ax<sup>2</sup> + 2bxy + cy<sup>2</sup> is positive except at x,y = 0,0  

[ x<sup>T</sup>Sx = ax<sup>2</sup> + 2bxy + cy<sup>2</sup> > 0 always except x,y = 0,0  because of positive eigenvalues; this was proven ]   
4.   S = A<sup>T</sup>A is automatically positive definite if A has independent columns.   
5.  the ellipsoid x<sup>T</sup>Sx = 1 has its axes along the eigenvectors of S and lengths 1/√&lambda;   
6. minimum of F(x,y) if ∂F/∂x = ∂F/∂y = 0 and 2nd derivative matrix is positive definite.  

6.5 A 

numpy has lots of features.

scipy libraries are fast.  
https://docs.scipy.org/doc/scipy/reference/linalg.html
https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.ldl.html#scipy.linalg.ldl

sympy is very convenient but slow: e.g. this diagonalization doesnt work for pascal(6) might be too much processing whereas scipy can do it
https://docs.sympy.org/latest/tutorial/matrices.html#eigenvalues-eigenvectors-and-diagonalization     

also very convenient from sympy
LDL via Matrix.LDLdecomposition
https://docs.sympy.org/latest/modules/matrices/matrices.html#matrixbase-class-reference

S = LDL<sup>T</sup> from pivots and multipliers   
S  =Q&Lambda;Q<sup>T</sup> from eigenvalues and eigenvectors  

try nxn tests on pascal(6) and ones(6) and hilb(6) and other matrices in MatLab galliery; I do it here with numpy and scipy for the above reasons:   
- pascal is positive definite because all its pivots are 1   
- ones is positive semidefnite because its eigenvalues are (0,0,0,0,0,6)    
- hilb is positive definite even though eig(H) shows eigenvaleus very near zero. [there is a 1 and 5 zeros when integerized]
hilbert matric x<sup>T</sup>Hx = &Integral;
- rand(6) + rand(6).T can be positive or negative definite.  here are 20,000 experiments where add up the number of positive eigenvalues of the A + A.T matrix that are > 0 and then take the proportion.  If completely random should be able to run this 20,000 experiment 1000 times and get 3 of 6 eigenvalues > 0 but here I consistently get 3+.

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/111038528-8b2bdb00-83f7-11eb-95bf-f3c9b1a09b2a.png">


6.5 B

When is symmetric block matrix M = [ [ A, B ], [ B.T, C ] ] positive definite ? 

multiply the first row of M by B<sup>T</sup>A<sup>-1</sup> and subtract from the second row to get a block of zeros.  The Schur complement S = C - B<sup>T</sup>A<sup>-1</sup>B appears in the corner.   These 2 blocks A and S must be positive definite.  Their pivots are the pivots of M. 

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/111038819-d692b900-83f8-11eb-9aa0-1344e477c7cf.png">


6.5 C

find eigenvalues of the -1, 2, -1 tridiagonal n x n matrix S.

The best way is zzzzzz


problems: 

2x2 tests for positive definitiveness: 
- a > 0
- ac - b<sup>2</sup> > 0

if these are passed then you know c > b<sup>2</sup> / a > 0

which of S<sub>1</sub>, S<sub>2</sub>, S<sub>3</sub>, S<sub>4</sub> have 2 postivie eigenvalues.

- S<sub>1</sub> passes first fails second but there is a vector [x,y] = [4,2] for which x<sup>T</sub>Sx > 0. the tests only tell you if they are positive **always** - there might be other cases that have positive energy. 
- S<sub>2</sub> fails first passes second
- S<sub>3</sub> passes first fails second, semidefinite
- S<sub>4</sub> passes first passes second


![\begin{align*}
S &= 
\begin{bmatrix}
a&b\\
b&c
\end{bmatrix}\\
\\
S_1 &= 
\begin{bmatrix}
5&6\\
6&7
\end{bmatrix}\\
a& > 0\\
ac - b^2 &< 0\\
\\
x^TS_1x & = 
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
5&6\\
6&7
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
& = \begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
5x+6y\\
6x+7y
\end{bmatrix} \\
& = \begin{bmatrix}
5x+6y&
6x+7y
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
& = 5xx+6yx + 6xy+7yy \\
& = 5x^2+6xy + 6xy+7y^2 \\
& = 5x^2+12xy+7y^2 \\
& = ax^2+bxy + bxy+cy^2 \\
& = ax^2+2bxy+cy^2 \\
\begin{bmatrix}
x\\
y
\end{bmatrix} &=
\begin{bmatrix}
4\\
2
\end{bmatrix} \longrightarrow x^TSx = 5*4^2+12*4*2+7*2^2 > 0\\
\\
\\S_2 &= 
\begin{bmatrix}
-1&-2\\
-2&-5
\end{bmatrix}\\
a& < 0\\
ac - b^2 &> 0\\
\\
S_3 &= 
\begin{bmatrix}
1&10\\
10&100
\end{bmatrix}\\
a& > 0\\
ac - b^2 &= 0\\
\\
S_4 &= 
\begin{bmatrix}
1&10\\
10&101
\end{bmatrix}\\
a& > 0\\
ac - b^2 &> 0
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Aa%26b%5C%5C%0Ab%26c%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0AS_1+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A5%266%5C%5C%0A6%267%0A%5Cend%7Bbmatrix%7D%5C%5C%0Aa%26+%3E+0%5C%5C%0Aac+-+b%5E2+%26%3C+0%5C%5C%0A%5C%5C%0Ax%5ETS_1x+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5%266%5C%5C%0A6%267%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26+%3D+%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5x%2B6y%5C%5C%0A6x%2B7y%0A%5Cend%7Bbmatrix%7D+%5C%5C%0A%26+%3D+%5Cbegin%7Bbmatrix%7D%0A5x%2B6y%26%0A6x%2B7y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%26+%3D+5xx%2B6yx+%2B+6xy%2B7yy+%5C%5C%0A%26+%3D+5x%5E2%2B6xy+%2B+6xy%2B7y%5E2+%5C%5C%0A%26+%3D+5x%5E2%2B12xy%2B7y%5E2+%5C%5C%0A%26+%3D+ax%5E2%2Bbxy+%2B+bxy%2Bcy%5E2+%5C%5C%0A%26+%3D+ax%5E2%2B2bxy%2Bcy%5E2+%5C%5C%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D+%26%3D%0A%5Cbegin%7Bbmatrix%7D%0A4%5C%5C%0A2%0A%5Cend%7Bbmatrix%7D+%5Clongrightarrow+x%5ETSx+%3D+5%2A4%5E2%2B12%2A4%2A2%2B7%2A2%5E2+%3E+0%5C%5C%0A%5C%5C%0A%5C%5CS_2+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-1%26-2%5C%5C%0A-2%26-5%0A%5Cend%7Bbmatrix%7D%5C%5C%0Aa%26+%3C+0%5C%5C%0Aac+-+b%5E2+%26%3E+0%5C%5C%0A%5C%5C%0AS_3+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%2610%5C%5C%0A10%26100%0A%5Cend%7Bbmatrix%7D%5C%5C%0Aa%26+%3E+0%5C%5C%0Aac+-+b%5E2+%26%3D+0%5C%5C%0A%5C%5C%0AS_4+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%2610%5C%5C%0A10%26101%0A%5Cend%7Bbmatrix%7D%5C%5C%0Aa%26+%3E+0%5C%5C%0Aac+-+b%5E2+%26%3E+0%0A%5Cend%7Balign%2A%7D)

5.
writing f(x,y) as difference of squares necessitated decompose into LDL or Q&Lambda;Q 

no minimum at 0,0 even though positive coefficients. 
minimum at 2 and -1 where the squares are zero. 

![\begin{align*}
f(x,y) =& x^2 + 4xy + 3y^2 \\
= &x^T Sx = 
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
1&2\\
2&3
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
=& 
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
1x+2y\\
2x+3y
\end{bmatrix}
\\=& 1x^2 + 4xy +3y^2 \\
=& x^TLDL^Tx  \\
=& 
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
1&0\\
2&1
\end{bmatrix}
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
=& 
\begin{bmatrix}
1x+2y&
0x+1y
\end{bmatrix}
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}
\begin{bmatrix}
1x+2y\\
0x+1y
\end{bmatrix}\\
=& 
\begin{bmatrix}
1(1x+2y) &-1(0x+1y)
\end{bmatrix}
\begin{bmatrix}
1x+2y\\
0x+1y
\end{bmatrix}\\
=& 1(1x+2y)^2 -1(0x+1y)^2 \\
=&  (x+2y)^2 -y^2 \\
=& x^2 +4xy +4y^2- y^2
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Af%28x%2Cy%29+%3D%26+x%5E2+%2B+4xy+%2B+3y%5E2+%5C%5C%0A%3D+%26x%5ET+Sx+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%262%5C%5C%0A2%263%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1x%2B2y%5C%5C%0A2x%2B3y%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%3D%26+1x%5E2+%2B+4xy+%2B3y%5E2+%5C%5C%0A%3D%26+x%5ETLDL%5ETx++%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A2%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A0%26-1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%262%5C%5C%0A0%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A1x%2B2y%26%0A0x%2B1y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A0%26-1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1x%2B2y%5C%5C%0A0x%2B1y%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0A1%281x%2B2y%29+%26-1%280x%2B1y%29%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1x%2B2y%5C%5C%0A0x%2B1y%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+1%281x%2B2y%29%5E2+-1%280x%2B1y%29%5E2+%5C%5C%0A%3D%26++%28x%2B2y%29%5E2+-y%5E2+%5C%5C%0A%3D%26+x%5E2+%2B4xy+%2B4y%5E2-+y%5E2%0A%5Cend%7Balign%2A%7D)


6. 
f(x,y) = 2xy has a saddle point and not a minimum at (0,0)     
the symmetric matrix producing 2xy is [ [0,1], [1,0] ]   
a = c = 0 and b = 1   

S = [ [0,1], [1,0] ] produces f(x,y) = [x y] [ [0,1], [1,0] ] [ x y ]<sup>T</sup> = 2xy has &lambda;s = 1 and -1: S is an indefinite matrix and f(x,y) has a saddle point. 


7.  A<sup>T</sup>A are PD in each case.  A needs independent columns only.  A doesnt need independent rows: e.g. A<sup>2</sup> with independent columns and dependent rows vs A<sup>3</sup> with dependent columns and independent rows

A<sup>T</sup> is invertible if A has independent columns.  AA<sup>T</sup> is not necessarily invertible with A having independent columns.  

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/111052058-b7f6e700-8425-11eb-9656-6561f4929028.png">

8.
the function f(x,y) = 3 (x+2y)<sup>2</sup> +4y<sup>2</sup> is positive except at (0,0)    

the matrix that represents this equation is S

pivots outside squares and L multipliers inside 


![\begin{align*}
f(x,y) =& 3(x+2y)^2 +4y^2 \\
=& 3(x^2 + 4xy + 4y^2) + 4y^2 \\
=& 3x^2 + 12xy + 12y^2 + 4y^2 \\
=& 3x^2 + 12xy + 16y^2 \\
= &x^TSx \\
= &
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
3&6\\
6&16
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
\\
LDL^T factor:&\\
E_{21} S =& U \\
\begin{bmatrix}
1&0\\
-2&1
\end{bmatrix}
\begin{bmatrix}
3&6\\
6&16
\end{bmatrix}
=&
\begin{bmatrix}
3&6\\
0&4
\end{bmatrix}\\
=& DL^T\\
=&
\begin{bmatrix}
3&0\\
0&4
\end{bmatrix}
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}\\
\\
f(x,y) =& x^TSx \\
=& x^TLDL^Tx \\
=&
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
1&0\\
2&1
\end{bmatrix}
\begin{bmatrix}
3&0\\
0&4
\end{bmatrix}
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
=&
\begin{bmatrix}
x&y
\end{bmatrix}
\begin{bmatrix}
L_{11}&L_{12}\\
L_{21}&L_{22}
\end{bmatrix}
\begin{bmatrix}
D_{11}&0\\
0&D_{22}
\end{bmatrix}
\begin{bmatrix}
L_{11}^T&L_{21}^T\\
L_{12}^T&L_{22}^T
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}\\
=&
\begin{bmatrix}
1x+2y&
0x + 1y
\end{bmatrix}
\begin{bmatrix}
3&0\\
0&4
\end{bmatrix}
\begin{bmatrix}
1x+2y\\
0x+1y
\end{bmatrix}\\
=&
\begin{bmatrix}
3(1x+2y)&
4(0x + 1y)
\end{bmatrix}
\begin{bmatrix}
1x+2y\\
0x+1y
\end{bmatrix}
\\
=&
3(1x+2y)^2 +4(0x + 1y)^2
\\
=&
3(x+2y)^2 +4y^2\\
=&
D_{11}(L_{11}x+L_{21}y)^2 +D_{22}(L_{12}x +L_{22}y)^2
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Af%28x%2Cy%29+%3D%26+3%28x%2B2y%29%5E2+%2B4y%5E2+%5C%5C%0A%3D%26+3%28x%5E2+%2B+4xy+%2B+4y%5E2%29+%2B+4y%5E2+%5C%5C%0A%3D%26+3x%5E2+%2B+12xy+%2B+12y%5E2+%2B+4y%5E2+%5C%5C%0A%3D%26+3x%5E2+%2B+12xy+%2B+16y%5E2+%5C%5C%0A%3D+%26x%5ETSx+%5C%5C%0A%3D+%26%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A3%266%5C%5C%0A6%2616%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0ALDL%5ET+factor%3A%26%5C%5C%0AE_%7B21%7D+S+%3D%26+U+%5C%5C%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A-2%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A3%266%5C%5C%0A6%2616%0A%5Cend%7Bbmatrix%7D%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A3%266%5C%5C%0A0%264%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+DL%5ET%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A3%260%5C%5C%0A0%264%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%262%5C%5C%0A0%261%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%0Af%28x%2Cy%29+%3D%26+x%5ETSx+%5C%5C%0A%3D%26+x%5ETLDL%5ETx+%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%5C%5C%0A2%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A3%260%5C%5C%0A0%264%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%262%5C%5C%0A0%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax%26y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AL_%7B11%7D%26L_%7B12%7D%5C%5C%0AL_%7B21%7D%26L_%7B22%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AD_%7B11%7D%260%5C%5C%0A0%26D_%7B22%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AL_%7B11%7D%5ET%26L_%7B21%7D%5ET%5C%5C%0AL_%7B12%7D%5ET%26L_%7B22%7D%5ET%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax%5C%5C%0Ay%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A1x%2B2y%26%0A0x+%2B+1y%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A3%260%5C%5C%0A0%264%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1x%2B2y%5C%5C%0A0x%2B1y%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A3%281x%2B2y%29%26%0A4%280x+%2B+1y%29%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1x%2B2y%5C%5C%0A0x%2B1y%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0A%3D%26%0A3%281x%2B2y%29%5E2+%2B4%280x+%2B+1y%29%5E2%0A%5C%5C%0A%3D%26%0A3%28x%2B2y%29%5E2+%2B4y%5E2%5C%5C%0A%3D%26%0AD_%7B11%7D%28L_%7B11%7Dx%2BL_%7B21%7Dy%29%5E2+%2BD_%7B22%7D%28L_%7B12%7Dx+%2BL_%7B22%7Dy%29%5E2%0A%5Cend%7Balign%2A%7D)


9. 3x3 matrix S and its pivot, rank, eigenvalues and determinant for 4(x<sub>1</sub> - x<sub>2</sub> + 2x<sub>3</sub>)<sup>2</sup>

can see where the L, D and S matrix cells come from 

since there is only pivot, rank = 1  
since trace = 4 +4+16 = 24, it can have only 1 non-zero eigenvalue = 24 and the remaining two eigenvalues are 0 so that 0 • 0 • 24 = 0 = determinant = 0

one positive eigenvalue
one positive pivot

![\begin{align*}
f(x_1,x_2, x_3) =& 4(x_1-x_2+2x_3)^2 \\
\\
=& x^TSx \\
=& x^TLDL^Tx \\
=&
\begin{bmatrix}
x
\end{bmatrix}^T
\begin{bmatrix}
L
\end{bmatrix}
\begin{bmatrix}
D
\end{bmatrix}
\begin{bmatrix}
L
\end{bmatrix}^T
\begin{bmatrix}
x
\end{bmatrix}\\
=&
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
L_{11}&L_{12}&L_{13}\\
L_{21}&L_{22}&L_{23}\\
L_{31}&L_{32}&L_{33}\\
\end{bmatrix}
\begin{bmatrix}
D_{11}&0&0\\
0&D_{22}&0\\
0&0&D_{33}
\end{bmatrix}
\begin{bmatrix}
L_{11}^T&L_{21}^T&L_{31}^T\\
L_{12}^T&L_{22}^T&L_{32}^T\\
L_{13}^T&L_{23}^T&L_{33}^T
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}\\
=&
D_{11}(L_{11}x_1+L_{21}x_2+L_{31}x_3)^2 +D_{22}(L_{12}x_1 +L_{22}x_2+L_{32})^2+D_{33}(L_{13}x_1 +L_{23}x_2+L_{33})^2 \\
=&
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
1&L_{12}&L_{13}\\
-1&L_{22}&L_{23}\\
2&L_{32}&L_{33}\\
\end{bmatrix}
\begin{bmatrix}
4&0&0\\
0&D_{22}&0\\
0&0&D_{33}
\end{bmatrix}
\begin{bmatrix}
1&-1&2\\
L_{12}^T&L_{22}^T&L_{32}^T\\
L_{13}^T&L_{23}^T&L_{33}^T
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}\\
=&
4(1x_1-1x_2+2x_3)^2 +D_{22}(L_{12}x_1 +L_{22}x_2+L_{32})^2+D_{33}(L_{13}x_1 +L_{23}x_2+L_{33})^2 \\
=&
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
1&0&0\\
-1&0&0\\
2&0&0\\
\end{bmatrix}
\begin{bmatrix}
4&0&0\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}
1&-1&2\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
\\=&
\begin{bmatrix}
x^TL
\end{bmatrix}
\begin{bmatrix}
D
\end{bmatrix}
\begin{bmatrix}
L^Tx
\end{bmatrix}
\\=&
\begin{bmatrix}
1x_1-1x_2+2x_3&0&0
\end{bmatrix}
\begin{bmatrix}
4&0&0\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}
1x_1-1x_2+2x_3\\
0\\
0
\end{bmatrix}\\
\\=&
\begin{bmatrix}
4(1x_1-1x_2+2x_3)&0&0
\end{bmatrix}
\begin{bmatrix}
1x_1-1x_2+2x_3\\
0\\
0
\end{bmatrix}\\
=&
4(1x_1-1x_2+2x_3)^2 \\
=& x^TLDL^Tx \\
\\
=&
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
1&0&0\\
-1&0&0\\
2&0&0\\
\end{bmatrix}
\begin{bmatrix}
4&0&0\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}
1&-1&2\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}\\
=& [x^T][LD][L^T]x \\
=& 
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
4&0&0\\
-4&0&0\\
8&0&0
\end{bmatrix}
\begin{bmatrix}
1&-1&2\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}\\
=& x^TSx \\
=&
\begin{bmatrix}
x_1&x_2&x_3
\end{bmatrix}
\begin{bmatrix}
4&-4&8\\
-4&4&8\\
8&-8&16
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}\\
=& [x^TS]x \\
=&
\begin{bmatrix}
4x_1-4x_2+8x_3&-4x_1+4x_2-8x_3&8x_1-8x_2+16x_3
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}\\
=&
4\begin{bmatrix}
x_1-x_2+2x_3&-x_1+x_2-2x_3&2x_1-2x_2+4x_3
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}\\
=&
4(x_1x_1-x_1x_2+2x_1x_3-x_1x_2+x_2x_2-2x_2x_3+2x_1x_3-2x_2x_3+4x_3x_3)\\
=&
4x_1x_1-4x_1x_2+8x_1x_3-4x_1x_2+4x_2x_2-8x_2x_3+8x_1x_3-8x_2x_3+16x_3x_3)\\
=&
S_{11}x_1x_1-S_{12}x_1x_2+S_{13}x_1x_3-S_{21}x_1x_2+S_{22}x_2x_2-S_{32}x_2x_3+S_{13}x_1x_3-S_{23}x_2x_3+S_{33}x_3x_3)\\
=&
4(x_1^2-2x_1x_2+4x_1x_3+x_2^2-4x_2x_3-2x_2x_3+4x_3^2)\\
=&
4(1x_1-1x_2+2x_3)^2 \\
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Af%28x_1%2Cx_2%2C+x_3%29+%3D%26+4%28x_1-x_2%2B2x_3%29%5E2+%5C%5C%0A%5C%5C%0A%3D%26+x%5ETSx+%5C%5C%0A%3D%26+x%5ETLDL%5ETx+%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cbegin%7Bbmatrix%7D%0AL%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AD%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AL%0A%5Cend%7Bbmatrix%7D%5ET%0A%5Cbegin%7Bbmatrix%7D%0Ax%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AL_%7B11%7D%26L_%7B12%7D%26L_%7B13%7D%5C%5C%0AL_%7B21%7D%26L_%7B22%7D%26L_%7B23%7D%5C%5C%0AL_%7B31%7D%26L_%7B32%7D%26L_%7B33%7D%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AD_%7B11%7D%260%260%5C%5C%0A0%26D_%7B22%7D%260%5C%5C%0A0%260%26D_%7B33%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AL_%7B11%7D%5ET%26L_%7B21%7D%5ET%26L_%7B31%7D%5ET%5C%5C%0AL_%7B12%7D%5ET%26L_%7B22%7D%5ET%26L_%7B32%7D%5ET%5C%5C%0AL_%7B13%7D%5ET%26L_%7B23%7D%5ET%26L_%7B33%7D%5ET%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0AD_%7B11%7D%28L_%7B11%7Dx_1%2BL_%7B21%7Dx_2%2BL_%7B31%7Dx_3%29%5E2+%2BD_%7B22%7D%28L_%7B12%7Dx_1+%2BL_%7B22%7Dx_2%2BL_%7B32%7D%29%5E2%2BD_%7B33%7D%28L_%7B13%7Dx_1+%2BL_%7B23%7Dx_2%2BL_%7B33%7D%29%5E2+%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26L_%7B12%7D%26L_%7B13%7D%5C%5C%0A-1%26L_%7B22%7D%26L_%7B23%7D%5C%5C%0A2%26L_%7B32%7D%26L_%7B33%7D%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A4%260%260%5C%5C%0A0%26D_%7B22%7D%260%5C%5C%0A0%260%26D_%7B33%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-1%262%5C%5C%0AL_%7B12%7D%5ET%26L_%7B22%7D%5ET%26L_%7B32%7D%5ET%5C%5C%0AL_%7B13%7D%5ET%26L_%7B23%7D%5ET%26L_%7B33%7D%5ET%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0A4%281x_1-1x_2%2B2x_3%29%5E2+%2BD_%7B22%7D%28L_%7B12%7Dx_1+%2BL_%7B22%7Dx_2%2BL_%7B32%7D%29%5E2%2BD_%7B33%7D%28L_%7B13%7Dx_1+%2BL_%7B23%7Dx_2%2BL_%7B33%7D%29%5E2+%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-1%260%260%5C%5C%0A2%260%260%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A4%260%260%5C%5C%0A0%260%260%5C%5C%0A0%260%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-1%262%5C%5C%0A0%260%260%5C%5C%0A0%260%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax%5ETL%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AD%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AL%5ETx%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A1x_1-1x_2%2B2x_3%260%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A4%260%260%5C%5C%0A0%260%260%5C%5C%0A0%260%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1x_1-1x_2%2B2x_3%5C%5C%0A0%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%5C%5C%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A4%281x_1-1x_2%2B2x_3%29%260%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1x_1-1x_2%2B2x_3%5C%5C%0A0%5C%5C%0A0%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0A4%281x_1-1x_2%2B2x_3%29%5E2+%5C%5C%0A%3D%26+x%5ETLDL%5ETx+%5C%5C%0A%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%260%260%5C%5C%0A-1%260%260%5C%5C%0A2%260%260%5C%5C%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A4%260%260%5C%5C%0A0%260%260%5C%5C%0A0%260%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-1%262%5C%5C%0A0%260%260%5C%5C%0A0%260%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%5Bx%5ET%5D%5BLD%5D%5BL%5ET%5Dx+%5C%5C%0A%3D%26+%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A4%260%260%5C%5C%0A-4%260%260%5C%5C%0A8%260%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A1%26-1%262%5C%5C%0A0%260%260%5C%5C%0A0%260%260%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+x%5ETSx+%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%26x_2%26x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A4%26-4%268%5C%5C%0A-4%264%268%5C%5C%0A8%26-8%2616%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26+%5Bx%5ETS%5Dx+%5C%5C%0A%3D%26%0A%5Cbegin%7Bbmatrix%7D%0A4x_1-4x_2%2B8x_3%26-4x_1%2B4x_2-8x_3%268x_1-8x_2%2B16x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0A4%5Cbegin%7Bbmatrix%7D%0Ax_1-x_2%2B2x_3%26-x_1%2Bx_2-2x_3%262x_1-2x_2%2B4x_3%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ax_1%5C%5C%0Ax_2%5C%5C%0Ax_3%0A%5Cend%7Bbmatrix%7D%5C%5C%0A%3D%26%0A4%28x_1x_1-x_1x_2%2B2x_1x_3-x_1x_2%2Bx_2x_2-2x_2x_3%2B2x_1x_3-2x_2x_3%2B4x_3x_3%29%5C%5C%0A%3D%26%0A4x_1x_1-4x_1x_2%2B8x_1x_3-4x_1x_2%2B4x_2x_2-8x_2x_3%2B8x_1x_3-8x_2x_3%2B16x_3x_3%29%5C%5C%0A%3D%26%0AS_%7B11%7Dx_1x_1-S_%7B12%7Dx_1x_2%2BS_%7B13%7Dx_1x_3-S_%7B21%7Dx_1x_2%2BS_%7B22%7Dx_2x_2-S_%7B32%7Dx_2x_3%2BS_%7B13%7Dx_1x_3-S_%7B23%7Dx_2x_3%2BS_%7B33%7Dx_3x_3%29%5C%5C%0A%3D%26%0A4%28x_1%5E2-2x_1x_2%2B4x_1x_3%2Bx_2%5E2-4x_2x_3-2x_2x_3%2B4x_3%5E2%29%5C%5C%0A%3D%26%0A4%281x_1-1x_2%2B2x_3%29%5E2+%5C%5C%0A%5Cend%7Balign%2A%7D)


10. 
