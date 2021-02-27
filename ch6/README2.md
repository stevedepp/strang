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
