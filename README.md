# Numerical_Analysis and Optimisation
   This is a collection of algorithms learnt during numerical analysis and optimisation.
   Code includes libraries: Numpy and Pyplot 

## Solving Linear-System equations.
   Gauss-Seidel, Jabobi Iterative Method
    ![Given Linear System](https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/Jacobi_Question.PNG)
    ![Error Visualisation of Gauss Seidel Method](https://github.com/chanhopark00/Numerical_Analysis/master/Image/Gauss_seidel.PNG)
    ![Error Visualisation of Jacobi Method](https://github.com/chanhopark00/Numerical_Analysis/Image/Jacobi_iteration.PNG)
   Error Analysis
    I have approximated the error as the distance between the approximation vector and solution vector with the usual metric. 
    It is clear that Gauss Seidel Method converges faster to the solution than Jacobi Iteration method.

## Interpolation
  Newton interpolation
    ![Approximated Polynomial Plot](https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/cher_polynomial.PNG)
    ![Error Visualisation](https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/cher_error.PNG)
  Error Analysis
    I have chosen a fixed x-value to compare the error of polynomials of different orders. 
    As the order increases it is clear that the error is lower.
    However due to the runge's phenomenon, as the polynomial's order increase and further the x-value is from the nodes chosen, the error becomes significant.
    
## Integral Approximation
  Simpson's Rule and Trapezoid Rule comparison 
    ![Trapezoid's Rule Error](https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/trapezoid_err.PNG)
    ![Simpson's Rule Error](https://github.com/chanhopark00/Numerical_Analysis/blob/master/Image/trapezoid_err.PNG)
  Error Anaylsis
    The code is an approximation of integral of the function e^x * cos(x) from 0 to pi.
    It is clear that the trapezoid rule is much effective in terms of approximation.
    However the computational power is the trade off.
  
  
