section 6.4 

selected problems

1. find 2 &lambda;s and x's so that u = e<sup>&lambda;t</sup>x solves:

∂u/∂t = [[4,3],[0,1]] u 

what combination of u = c<sub>1</sub>e<sup>&lambda;t</sup>x<sub>1</sub> + c<sub>2</sub>e<sup>&lambda;t</sup>x<sub>2</sub> starts from u(0) = (5,-2) ?

from eigenvalues trace and determinant identities:   
&lambda;<sub>1</sub> + &lambda;<sub>2</sub> = 5  
&lambda;<sub>1</sub>&lambda;<sub>2</sub> = 4  
determine &lambda;<sub>1</sub> =1, &lambda;<sub>2</sub> = 4  

for &lambda;<sub>1</sub> the eigenvector is given by the null space of [[3,3],[0,0]] or x<sub>2</sub> = (1,-1)

for &lambda;<sub>2</sub> the eigenvector is given by the null space of [[0,3],[0-3]] or x<sub>2</sub> = (1,0)

thus the 2 pure solutions to the given differential equation are:

x<sub>1</sub>(t) = [1,-1]<sup>T</sup>e<sup>1t</sup>   
x<sub>2</sub>(t) = [1,0]<sup>T</sup>e<sup>4t</sup>

the general [complete] solution is a linear combination of pure solutions.   
to have a general solution equal to the initial condition, set c<sub>1</sub> and c<sub>2</sub>:

u(0) = [5,2]<sup>T</sup> = c<sub>1</sub>[1,-1]<sup>T</sup> + c<sub>2</sub>[1,0]<sup>T</sup>

X = [[1,-1],[1,0]] --> X<sup>-1</sup> = [[0,1],[-1,1]  

X<sup>-1</sup>u(0) = c = [-2,7]<sup>T</sup>

u(0) = [5,2]<sup>T</sup> = -2•[1,-1]<sup>T</sup> + 7•[1,0]<sup>T</sup>

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/109374432-45153a00-7883-11eb-825c-81b88c79f820.png">

2. solve problem 1 for u = (y,z) by back substitution, z before y.    
solve ∂z/∂t = z from z(0) = -2  
solve ∂y/∂t = 4y + 3z from y(0) = 5

∂ [y, z]<sup>T</sup> / ∂t = c<sub>1</sub>[1,-1]<sup>T</sup>e<sup>1(t=0)</sup> + c<sub>2</sub>[1,0]<sup>T</sup>e<sup>4(t=0)</sup>

z takes the second component of each eigenvector, or -1 and 0, making c<sub>1</sub> the only available coefficient to determine.   

z(0) = -2 = c<sub>1</sub>-1e<sup>1(t=0)</sup> + c<sub>2</sub>0<sup>T</sup>e<sup>4(t=0)</sup> = c<sub>1</sub>-1e<sup>1(t=0)</sup> --> c_1 = -2 and z(t) = (-2)(-1)e<sup>1t</sup> = 2e<sup>t</sup>

plug z(t) = 2e<sup>t</sup> into ∂y/∂t = 4y + 3z to derive ∂y/∂t =  4y + 3(2e<sup>t</sup>) 

then knowing c<sub>1</sub> = 2 and y's getting the first component of each eigenvector, set y(0) = 5 = (c<sub>1</sub>=2)(1)e<sup>1(t=0)</sup> + c<sub>2</sub>(1)e<sup>4(t=0)</sup> = 2 + c<sub>2</sub> deriving c<sub>2</sub> = 3. thus y(t) = 2e<sup>t</sup> + 3e<sup>4t</sup> as in problem 1 because y(0) has same value as u's first component.




3. 
a. if every column of A adds to zero then the rows add to the zero row because the matrix is singular with dependent columns AND rows and thus &lambda; = 0 is one of the eigenvalues.  
b. with negaitve diagonal and positive off diagonal adding to zero, u' = Au will be a continuous Markov equation.  find eigenvalues and eigenvectors and steady state as t --> ∞.  

solve ∂u/∂t = [[-2,3],[2,-3]] u with u(0) = [4,1]<sup>T</sup>  
see below for answer using specific X, but generally the u(t) that solves ∂u/∂t is x<sup>1</sup> + e<sup>-5t</sup>x<sup>2</sup>   

what is u(∞)   
since e<sup>-5t</sup> --> 0 as t --> ∞, steady state u(∞) = (3,2) as shown by the answer below when t = 1000 since exp(-5000 is &lambda;t) = 0

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109375628-2cf5e880-788c-11eb-86ef-1adf00454452.png">


4. door opened between room sholding v(0) = 30 people and w(0) = 10 people.  the movement between rooms is proportional to the difference v - w from which we can take ∂v/∂t = w - v = positive inflow if w contains more people or negative outflow if w contains fewer people at  and ∂w/∂t = v - w.  show that the total v + w is constant at 40 people.   find the matrix in ∂u/∂t = Au and its eigenvalues and eigenvectors.  what are v and w at t=1 and t=∞.

∂u/∂t where u = [v,w]<sup>T</sup> 

∂u/∂t = ∂[v,w]<sup>T</sup>/∂tAu must be = [[-1,1],[1,-1]][v,w]<sup>T</sup> = [[w-v],[v-w]]

the python code show diagonalization of the singular matrix and steady state is 20 persons in each room. 

differential equations ∂w/∂t = v-w and ∂v/∂t = w-v  
consider y = v+w and ∂<sup>∞</sup>y/∂t<sup>∞</sup> is the steady state of people is more easily derived by knowing ∂y/∂t = ∂(v+w)/∂t = ∂v/∂t + ∂w/∂t = w - v + v - w = 0  
so the function y(t) = v(t) + w(t) is constant for all time.  
y(t) thus is always equal to its initial condition y(t) = y(0) = v(0) + w(0) = 30 + 10 = 40

defining vector of unknowns u as u = [v(t],w(t)] then we have that u satisfies ∂u/∂t = [w-v. v-w] = [[-1,1][1.-1]][v,w]<sup>T</sup> = Au.


<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109376057-db4f5d00-788f-11eb-918e-6c8cb5fbd527.png">

![\begin{align*}
\frac{\partial u}{\partial t} &= 
\frac{\partial 
\begin{bmatrix}
v(t)\\
w(t)
\end{bmatrix}}{\partial t} = 
\begin{bmatrix}
w-v\\
v-w
\end{bmatrix} = 
\begin{bmatrix}
-1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
v\\w
\end{bmatrix}\\
u(0) &= 
\begin{bmatrix}
30\\
10
\end{bmatrix} =
c_1
\begin{bmatrix}
1\\
-1
\end{bmatrix}+
c_2
\begin{bmatrix}
1\\
1
\end{bmatrix}
\\
u(t) &= 
10 
\begin{bmatrix}
1\\
-1
\end{bmatrix}
e^{-2t}
+20 
\begin{bmatrix}
1\\
1
\end{bmatrix}
e^{0t}\\
&= 
\begin{bmatrix}
v(t)\\
w(t)
\end{bmatrix} =
\begin{bmatrix}
10*1*e^{-2t} + 20*1*e^{0t}\\
10*-1*e^{-2t} + 20*1*e^{0t}
\end{bmatrix} =
\begin{bmatrix}
10*e^{-2t} + 20\\
-10*e^{-2t} + 20
\end{bmatrix}\\
u(t=1) &= 
\begin{bmatrix}
v(t=1)\\
w(t=1)
\end{bmatrix}=
\begin{bmatrix}
10*e^-2 + 20\\
-10*e^-2 + 20
\end{bmatrix}\\
u(t=\infty) &= 
\begin{bmatrix}
v(t=\infty)\\
w(t=\infty)
\end{bmatrix}=
\begin{bmatrix}
10*e^{-2\infty} + 20\\
-10*e^{-2\infty} + 20
\end{bmatrix}
=\begin{bmatrix}
20\\
20
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%26%3D+%0A%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D%7D%7B%5Cpartial+t%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Aw-v%5C%5C%0Av-w%0A%5Cend%7Bbmatrix%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A-1%261%5C%5C%0A1%26-1%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Av%5C%5Cw%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%280%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A30%5C%5C%0A10%0A%5Cend%7Bbmatrix%7D+%3D%0Ac_1%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%2B%0Ac_2%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0Au%28t%29+%26%3D+%0A10+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B-2t%7D%0A%2B20+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B0t%7D%5C%5C%0A%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A10%2A1%2Ae%5E%7B-2t%7D+%2B+20%2A1%2Ae%5E%7B0t%7D%5C%5C%0A10%2A-1%2Ae%5E%7B-2t%7D+%2B+20%2A1%2Ae%5E%7B0t%7D%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A10%2Ae%5E%7B-2t%7D+%2B+20%5C%5C%0A-10%2Ae%5E%7B-2t%7D+%2B+20%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%28t%3D1%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%3D1%29%5C%5C%0Aw%28t%3D1%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A10%2Ae%5E-2+%2B+20%5C%5C%0A-10%2Ae%5E-2+%2B+20%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%28t%3D%5Cinfty%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%3D%5Cinfty%29%5C%5C%0Aw%28t%3D%5Cinfty%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A10%2Ae%5E%7B-2%5Cinfty%7D+%2B+20%5C%5C%0A-10%2Ae%5E%7B-2%5Cinfty%7D+%2B+20%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A20%5C%5C%0A20%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

5. reverse the diffusion of peple in problem 4 ∂u/∂t = -Au: ∂y/∂t = v-w and ∂w/∂t = w-v  
total ∂(v+w)/∂t is unchanged = (w-v)+(v-w) = 0 

∂u/∂t = -Au means that the &lambda;'s change, or in this case, the one non-zero &lambda; changes sign.  since &lambda is positive and > 1 it blows up.

eigenvalues swap sign.  
eigenvectors are unchanged because all we are doing is changing the direction of A from 1 to -1.

v(t) on top goes to infinity and w(t) on bottom goes to -infinity

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109377228-f58d3900-7897-11eb-8061-7f12d27760b0.png">

![\begin{align*}
\frac{\partial u}{\partial t} &= 
\frac{\partial 
\begin{bmatrix}
v(t)\\
w(t)
\end{bmatrix}}{\partial t} = 
\begin{bmatrix}
v-w\\
w-v
\end{bmatrix} = 
\begin{bmatrix}
1&-1\\
-1&1
\end{bmatrix}
\begin{bmatrix}
v\\w
\end{bmatrix}\\
u(0) &= 
\begin{bmatrix}
30\\
10
\end{bmatrix} =
c_1
\begin{bmatrix}
1\\
1
\end{bmatrix}+
c_2
\begin{bmatrix}
1\\
-1
\end{bmatrix}
\\
u(t) &= 
20 
\begin{bmatrix}
1\\
1
\end{bmatrix}
e^{0t}
+10 
\begin{bmatrix}
1\\
-1
\end{bmatrix}
e^{2t}\\
&= 
\begin{bmatrix}
v(t)\\
w(t)
\end{bmatrix} =
\begin{bmatrix}
20*1*e^{0t} + 10*1*e^{2t}\\
20*1*e^{0t} + 10*-1*e^{2t}
\end{bmatrix} =
\begin{bmatrix}
20 + 10*e^{2t}\\
20 - 10*e^{2t}
\end{bmatrix}\\
u(t=1) &= 
\begin{bmatrix}
v(t=1)\\
w(t=1)
\end{bmatrix}=
\begin{bmatrix}
20 + 10*e^2\\
20 -10*e^2
\end{bmatrix}\\
u(t=\infty) &= 
\begin{bmatrix}
v(t=\infty)\\
w(t=\infty)
\end{bmatrix}=
\begin{bmatrix}
20 + 10*e^{2\infty}\\
 20 -10*e^{2\infty}
\end{bmatrix}
=\begin{bmatrix}
+\infty\\
-\infty
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5Cpartial+u%7D%7B%5Cpartial+t%7D+%26%3D+%0A%5Cfrac%7B%5Cpartial+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D%7D%7B%5Cpartial+t%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av-w%5C%5C%0Aw-v%0A%5Cend%7Bbmatrix%7D+%3D+%0A%5Cbegin%7Bbmatrix%7D%0A1%26-1%5C%5C%0A-1%261%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Av%5C%5Cw%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%280%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A30%5C%5C%0A10%0A%5Cend%7Bbmatrix%7D+%3D%0Ac_1%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%2B%0Ac_2%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%0A%5C%5C%0Au%28t%29+%26%3D+%0A20+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A1%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B0t%7D%0A%2B10+%0A%5Cbegin%7Bbmatrix%7D%0A1%5C%5C%0A-1%0A%5Cend%7Bbmatrix%7D%0Ae%5E%7B2t%7D%5C%5C%0A%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A20%2A1%2Ae%5E%7B0t%7D+%2B+10%2A1%2Ae%5E%7B2t%7D%5C%5C%0A20%2A1%2Ae%5E%7B0t%7D+%2B+10%2A-1%2Ae%5E%7B2t%7D%0A%5Cend%7Bbmatrix%7D+%3D%0A%5Cbegin%7Bbmatrix%7D%0A20+%2B+10%2Ae%5E%7B2t%7D%5C%5C%0A20+-+10%2Ae%5E%7B2t%7D%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%28t%3D1%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%3D1%29%5C%5C%0Aw%28t%3D1%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A20+%2B+10%2Ae%5E2%5C%5C%0A20+-10%2Ae%5E2%0A%5Cend%7Bbmatrix%7D%5C%5C%0Au%28t%3D%5Cinfty%29+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0Av%28t%3D%5Cinfty%29%5C%5C%0Aw%28t%3D%5Cinfty%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A20+%2B+10%2Ae%5E%7B2%5Cinfty%7D%5C%5C%0A+20+-10%2Ae%5E%7B2%5Cinfty%7D%0A%5Cend%7Bbmatrix%7D%0A%3D%5Cbegin%7Bbmatrix%7D%0A%2B%5Cinfty%5C%5C%0A-%5Cinfty%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)


6.
a and b are real  
A = [[a,1],[1,a]] has real eigenvalues   
B = [[b,-1],[1,b]] [has complex eigenvalues    

find conditions on a and b so all solutions ∂u/∂t = Au and ∂v/∂t = Bv approach zero as t --> 0 i.e. Re&lambda; < 0 for all eigenvalues.   

for A, stability requires:  
T<sub>A</sub> = a + a =  2a < 0 or a < 0  for at least one &lambda; < 0
AND
D<sub>A</sub> = a<sup>2</sup> - 1 > 0 or a<sup>2</sup> > 1 or -1 > a > 1 for both signs to be the same
so a < -1

for B, stability requires:  
T<sub>B</sub> = b + b =  2b < 0 or b < 0  
D<sub>B</sub> = b<sup>2</sup> + 1 > 0 or b<sup>2</sup> > -1or b > i   
not sure how to evaluate the D part so will say b < 0

for a 2x2 this is not necessary:

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/109391654-285e1e00-78e6-11eb-8d04-e32e35acdfc7.png">

7.  P is projection matrix onto 45 degree line y = x in R<sup>2</sup>.  what are eigenvalues

if ∂u/∂t = -Pu what is the limit of u(t) as t --> ∞ starting from u(0) = (3,1)?

a = (1,1)

P = aa<sup>T</sup>/a<sup>T</sup> = [[1,1],[1,1]] / 2

projection matrix has eigenvalues of 1 and 0.  
[for &lambda;<sub>1</sub>] eigenvectors Px = 1x fill the subspace P projects onto x = (1,1).  
[for &lambda;<sub>2</sub>] eigenvectors with Px = 0x fill the perpendicular subspace: x = (1,-1)

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109399060-725afa00-790e-11eb-99ad-13ac2f0cfd68.png">

to solve u' = -P change signs for &lambda;s: but eigenvectors stay the same so u(0) still has c = [2,1]:

u(0) = 2[1,1]<sup>T</sup> + 1[1,-1]<sup>T</sup>

notice the -&lambda;s:

u(t) = e<sup>-1t</sup>[2,2]<sup>T</sup> + e<sup>-0t</sup>[1,-1]<sup>T</sup> which approaches [1,-1]<sup>T</sup> as t--> ∞ because the first eigenvalue causes the first part to go to zero.

-P coefficient matrix is -1 times P which means Px = &lambda;x becomes -Ax = -&lambda;x; eigenvectors of -P are same as P and eigenvalues of -P are the negative of P.

8.  the rabbit population grows 6r but declines due to wolves -2w.  
the wolf population grows always: -w<sup>2</sup> would control the wolves. 

r/t = 6r - 2w  
w/t = 2r + w

find eigenvalues and eigenvectors.  
if r(0) = w(0) = 30 what are the populations at t?   
after a long time what is the ratio rabbits to wolves?   


<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109400075-94f01180-7914-11eb-8ab4-ece1bf27e339.png">

r(t) and w(t) must satisfy ∂r/∂t = 6r - 2w and ∂w/∂t = 2r + w as shown in matrix form below.  this coefficient matrix has eignvalues 2 and 5.  for their respective &lambda;s, the eigenvectors are given by the null spaces shown below A - &lambda; I and the total solutions is given by the linear combination of the two solutions here:

x<sub>1</sub>(t) = [1,2]<sub>T</sub>e<sup>2t</sup>  
x<sub>2</sub>(t) = [2,1]<sub>T</sub>e<sup>5t</sup>  

the initial condition u(0) forces c<sub>1</sub> and c<sub>2</sub> to satisfy u(0) = Xc which produces c = (10,10) for an entire solution of u(t) = 10[1,2]<sub>T</sub>e<sup>2t</sup> + 10[2,1]<sub>T</sub>e<sup>5t</sup> 

the population of rabbits and wolves is from the components of the complete solution:  
r(t) = 10e<sup>2t</sup> + 20e<sup>5t</sup>    
w(t) = 20e<sup>2t</sup> + 10e<sup>5t</sup>   
and the ratio after a while r/w is (10e<sup>2t</sup> + 20e<sup>5t</sup> )/(20e<sup>2t</sup> + 10e<sup>5t</sup>) = 2 since the eigenvector [2,1]<sub>T</sub> with the &lambda; = 5 dominates the the other eigenvector with &lambda; = 2.



![\begin{align*}
u(t) & = 
\begin{bmatrix}
r(t)\\
w(t)
\end{bmatrix}=
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}
\begin{bmatrix}
e^{2t}&\\
&e^{5t}
\end{bmatrix}
\begin{bmatrix}
10\\
10
\end{bmatrix}
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au%28t%29+%26+%3D+%0A%5Cbegin%7Bbmatrix%7D%0Ar%28t%29%5C%5C%0Aw%28t%29%0A%5Cend%7Bbmatrix%7D%3D%0A%5Cbegin%7Bbmatrix%7D%0A2%261%5C%5C%0A1%262%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0Ae%5E%7B2t%7D%26%5C%5C%0A%26e%5E%7B5t%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A10%5C%5C%0A10%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D%0A)


9. write (4,0) as combination of these two eigenvectors c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> of A:

Au = &lambda;u:  
[[0,1],[-1,0]] [1,i].<sup>T</sup> = i [1,i].<sup>T</sup>  
[[0,1],[-1,0]] [1,i].<sup>T</sup> =  -i [1,i].<sup>T</sup>

the solution to ∂u/∂t = Au starting from (4,0) is c<sub>1</sub>e<sup>it</sup>x<sub>1</sub> + c<sub>2</sub>e<sup>-it</sup>x<sub>2</sub>.  substitute e<sup>it</sup> = cos t + i sin t and e<sup>-it</sup> = cost t -i sin t to find u(t)

can see the derivation of c: u<sub>0<sub> = 2 [1,i]<sup>T</sup> + 2[1,-i]<sup>T</sup> = [4,0]<sup>T</sup>   
could also have eyeballed the 2 x's given and seen that 2 works for c's.

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109404173-83693280-7931-11eb-9215-0bd92edbae1e.png">


if substitute Euler's into the complete solution:

2e<sup>it</sup>[1,i]<sup>T</sup> + c<sub>2</sub>e<sup>-it</sup>[1,-i]<sup>T</sup>

[Strang and Waxworth computed a 4 cost not -4cost for 2nd component.]

![\begin{align*}
u_t &= 
2e^{it}\begin{bmatrix}1\\i\end{bmatrix}+
2e^{-it}\begin{bmatrix}1\\-i\end{bmatrix} \\ &= 
2(cost + isint)\begin{bmatrix}1\\i\end{bmatrix}+
2(cost - isint)\begin{bmatrix}1\\-i\end{bmatrix} \\ &= 
\begin{bmatrix}
2cost + 2isint + 2cost - 2isint\\
2icost + 2i^2sint -2icost - -2i^2sint
\end{bmatrix} \\ &= 
\begin{bmatrix}
4cost \\
-4sint 
\end{bmatrix}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Au_t+%26%3D+%0A2e%5E%7Bit%7D%5Cbegin%7Bbmatrix%7D1%5C%5Ci%5Cend%7Bbmatrix%7D%2B%0A2e%5E%7B-it%7D%5Cbegin%7Bbmatrix%7D1%5C%5C-i%5Cend%7Bbmatrix%7D+%5C%5C+%26%3D+%0A2%28cost+%2B+isint%29%5Cbegin%7Bbmatrix%7D1%5C%5Ci%5Cend%7Bbmatrix%7D%2B%0A2%28cost+-+isint%29%5Cbegin%7Bbmatrix%7D1%5C%5C-i%5Cend%7Bbmatrix%7D+%5C%5C+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A2cost+%2B+2isint+%2B+2cost+-+2isint%5C%5C%0A2icost+%2B+2i%5E2sint+-2icost+-+-2i%5E2sint%0A%5Cend%7Bbmatrix%7D+%5C%5C+%26%3D+%0A%5Cbegin%7Bbmatrix%7D%0A4cost+%5C%5C%0A-4sint+%0A%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign%2A%7D)

10. find A to change scalar equation y'' = 5y' + 4y into a vector equation for u = (y, y'):

∂u/∂t = [y',y'']<sup>T</sup> = ∂[y,y']<sup>T</sup>/∂t = [[0,1],[4,5]] [y,y'] = Au 

what are the eigenvalues of A.  
find them by substituting y = e<sup>&lambda;t</sup> into y'' = 5y' + 4y

substitution: &lambda;t<sup>2</sup>e<sup>&lambda;t</sup> = &lambda;t5e<sup>&lambda;t</sup> + 4e<sup>&lambda;t</sup> --> &lambda;t<sup>2</sup>e<sup>&lambda;t</sup> - &lambda;t5e<sup>&lambda;t</sup> - 4e<sup>&lambda;t</sup> = (&lambda;t<sup>2</sup> - 5&lambda; - 4)e<sup>&lambda;t</sup> = 0 --> &lambda;t<sup>2</sup> - 5&lambda; - 4 = 0 --> &lambda;<sub>1</sub>, &lambda;<sub>2</sub> = 5 &pm; (41)<sup>1/2</sup>/2

[and find the traditional way for me]
A - &lambda; I = [[-&lambda;,1],[4,5-&lambda;]]  
det(A - &lambda; I) = &lambda;<sup>2</sup> - 5&lambda; - 4 = 0 which is the same quadratic found by subsitution of e<sup>&lambda;t</sup>

11. the solution to y'' = 0 is a straight line y = C + Dt.  Convert to a matrix equation.  

[are we double integrating when we move from y'' to y?]

∂ [y,y']<sup>T</sup>/∂t = [[0,1],[0,0]] [y,y']<sup>T</sup> has the solution [y,y']<sup>T</sup> = e<sup>At [y(0),y'(0)]<sup>T</sup>

[with this matrix, ∂y/∂t in 1st component is [0,1]<sup>T</sup>[y,y']=y' and ∂y/∂t = 0]
[coupling allows us to use component 2 (y') to solve component 1 (∂y/∂t) and when diagonalized it is uncoupled into pure solutions that can be recombined with c.]

so y'' = 0y +0y'

[this was the same A as seen earlier which could not be diagonalized.]

&lambda;<sub>1</sub> = &lambda;<sub>2</sub> = 0   
and so this matrix cannot be diagonalized;   

[it's columns are not independent since column 1 = a multiple zero fo column 2]

find A<sup>2</sup> and compute e<sup>At</sup> = I + At + (1/2)A<sup>2</sup>t<sup>2</sup> + ...    
then multiply the computed e<sup>At</sup> times [y(0), y'(0)] to check the straight line y(t) = y(0) + y'(0)t   
[that will be ∂u/∂t = Au]

let vector u be defined as u(t) = [y,y']   
then ∂u/∂t = [y,y']' = [y',y'']  = [[0,1],[0,0]] [y,y'] which has it's complete solution u(t) = [y(t),y'(t)] = e<sup>At</sup>[y(0),y'(0)].

**good**
[the complete solution is injected to the problem as ∂u(t)/∂t = [[0,1],[0,0]] [y(t),y'(t)] = [[0,1],[0,0]] e<sup>At</sup>[y(0),y'(0)] which if A held independent vectors could be diagonalized to Xe<sup>&Lambda;t</sup>X<sup>-1</sup>[y(0),y'(0)] = Xe<sup>&Lambda;t</sup>X<sup>-1</sup>u(0) = Xe<sup>&Lambda;t</sup>c = AX = e<sup>&Lambda;</sup>X = ∂u/∂t.]   

can evaluate e<sup>At</sup> using the definition in terms of Taylor series that is 

e≤sup>At</sup> = I + At + A<sup>2</sup>t<sup>2</sup>/2! + A<sup>3</sup>t<sup>3</sup>/3! + ...    

which stops at A<sup>2</sup> because A<sup>2</sup> = [[0,1],[0,0]] [[0,1],[0,0]] = [[0,0],[0,0]] 

so e<sup>At</sup> = I + At = [[1,0],[0,1]] + [[0,1],[0,0]]t = [[1,t],[0,1]]   

thus, u(t) = [y(t),y'(t)] = [[1,t],[0,1]] [y(0),y'(0)] = [y(0)+y'(0)t],y'(0)] which decouples into  

y(t) = y(0)+y'(0)t and y'(t) = y'(0) where  

y(t) = y(0)+y'(0)t = intercept at time zero + (slope at time zero)(time) which is a flat line with given slope multiplied by t.  [it is y=mx+b or y=b+mt in this case.] 

the factor t tells us that A had only one eigenvector for its two eigenvalues, 0 and 0 and thus is not diagonalizable.  [if both eigenvalues had eigenvectors Algebraic Mutliplicity = Geometric Multiplicity and there would be two t's in the complete solution]
[i guess in some sense then this y(t) = y(0)+y'(0)t is similar to u(t) = linear combination of the eigenvectors weighted by eigenvalues which are exponents in e<sup>(&lambda=0)(t=0)</sup> = 1 that we have seen as complete solution before.

[note for completeness sake:] u(t) is injected into ∂u/∂t = [y,y']' = Au = e<sup>At</sup>[y(0),y'(0)] = [[1,t],[0,1]] [y(0),y'(0)] = [y(0)+y'(0)],y'(0)]


