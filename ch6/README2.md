section 6.5 positive definite matrices

1. symmetric S: all eigenvalues > 0 &longleftrightarrow; all pivots > 0 &longleftrigtharrow; all upper left determinants > 0    
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
the numbers of x<sup>T</supSx is the same as x<sup>T</sup>A<sup>T</sup>Ax.  
[so for the same reason as we know x<sup>T</supSx is positive so is x<sup>T</sup>A<sup>T</sup>Ax]
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


