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
