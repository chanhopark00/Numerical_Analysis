# Numerical_Analysis and Optimisation
   This is a collection of algorithms learnt during numerical analysis and optimisation.
   Code includes libraries: Numpy and Pyplot 

## Interpolation
  #### Newton interpolation
   <img src="https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/cher_polynomal.PNG" width="400">
   <img src="https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/cher_error.PNG" width="400">
  
  #### Error Analysis
    I have chosen a fixed x-value to compare the error of polynomials of different orders. 
    As the order increases it is clear that the error is lower.
    However due to the runge's phenomenon, as the polynomial's order increase and further the x-value is from the nodes chosen, the error becomes significant.
    
## Integral Approximation
   #### Simpson's Rule and Trapezoid Rule comparison 
   <img src="https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/simpson_err.PNG" width="400">
   <img src="https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/trapezoid_err.PNG" width="400">
   
   #### Error Anaylsis
    The code is an approximation of integral of the function e^x * cos(x) from 0 to pi.
    It is clear that the trapezoid rule is much effective in terms of approximation.
    However the computational power is the trade off.
## ODE Approximation
   #### Runge-Kutta 4th Order approximation
   <img src="https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/rk_method.PNG" width="400">
   <img src="https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/rk_erro.PNG" width="400">

   #### Error Analysis
   It can be noticed that the local errors of the method accumulates over iterations hence the error increases as t increases from the initial value 0. A method ofreducing error order would be to implement with a higher order runge-kutta method.
## Solving Linear-System equations.
   #### Gauss-Seidel, Jabobi Iterative Method 
   <img src="https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/Jacobi_Question.PNG" width="300">
   
   <img src="https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/Gauss_Seidel.PNG" width="400">
   
   <img src="https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/Jacobi_iteration.PNG" width="400">
      
  #### Error Analysis
    I have approximated the error as the distance between the approximation vector and solution vector with the usual metric. 
    It is clear that Gauss Seidel Method converges faster to the solution than Jacobi Iteration method.
  
