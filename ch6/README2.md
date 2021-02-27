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

4. door opened between room sholding v(0) = 30 people and w(0) = 10 people.  the movement between rooms is proportional to the difference v - w from which we can take ∂v/∂t = w - v = positive inflow if w contains more people or negative outflow if w contains fewer people at  and ∂w/∂t = v - w.  show that the total v + w is constant at 40 people.   find the matrix in ∂u/∂t = Au and its eigenvalues and eigenvectors.  what are v and w at t=1 and t=∞.

∂u/∂t where u = [v,w]<sup>T</sup> 

∂u/∂t = ∂[v,w]<sup>T</sup>/∂tAu must be = [[-1,1],[1,-1]][v,w]<sup>T</sup> = [[w-v],[v-w]]

<img width="602" alt="image" src="https://user-images.githubusercontent.com/38410965/109375628-2cf5e880-788c-11eb-86ef-1adf00454452.png">



