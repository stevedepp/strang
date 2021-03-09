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
