# Numerical_Analysis and Optimisation

## Solving Linear equations.
   ### Gauss-Seidel, Jabobi Iterative Method
    ![Given Linear System](https://raw.githubusercontent.com/chanhopark00/Numerical_Analysis/tree/master/Image/Jacobi_Question.PNG)
    ![Error Visualisation of Gauss Seidel Method](https://raw.githubusercontent.com/chanhopark00/Numerical_Analysis/tree/master/Image/Gauss_seidel.PNG)
    ![Error Visualisation of Jacobi Method](
https://raw.githubusercontent.com/chanhopark00/Numerical_Analysis/tree/master/Image/Jacobi_iteartion.PNG)
  ### Error Analysis
    I have approximated the error as the distance between the approximation vector and solution vector with the usual metric. 
    It is clear that Gauss Seidel Method converges faster to the solution than Jacobi Iteration method.

## Interpolation
  ### Newton interpolation
    ![Approximated Polynomial Plot](
https://raw.githubusercontent.com/chanhopark00/Numerical_Analysis/tree/master/Image/cher_polynomial.PNG)
    ![Error Visualisation](
https://raw.githubusercontent.com/chanhopark00/Numerical_Analysis/tree/master/Image/cher_error.PNG)
  ### Error Analysis
    I have chosen a fixed x-value to compare the error of polynomials of different orders. 
    As the order increases it is clear that the error is lower.
    However due to the runge's phenomenon, as the polynomial's order increase and further the x-value is from the nodes chosen, the error becomes significant.
    
## Integral Approximation
  ### Simpson's Rule and Trapezoid Rule comparison 
    ![Trapezoid's Rule Error](
https://raw.githubusercontent.com/chanhopark00/Numerical_Analysis/tree/master/Image/trapezoid_err.PNG)
    ![Simpson's Rule Error](
https://raw.githubusercontent.com/chanhopark00/Numerical_Analysis/tree/master/Image/trapezoid_err.PNG)
  ### Error Anaylsis
    The code is an approximation of integral of the function e^x * cos(x) from 0 to pi.
    It is clear that the trapezoid rule is much effective in terms of approximation.
    However the computational power is the trade off.
  
  
