'''
Newtons Method
Authors: Kevin Cosby, Jackson Simpson, Sarah Weber, William Bentley
Purpose: To recreate Newton's Method in Python to find roots for given equations.
'''
import numpy as np
import math

class NewtonsMethod:
    def __init__(self):
        self.name = "Newton's Method"

    def root_newton(self, mathematical_function, initial_guess, tolerance, max_iterations):
        """
        Newton's root finding method

        Inputs:
        mathematical_function - function that you want to find the root of
        initial_guess - starting point for the function
        tolerance - how much room for error can there be?
        max_iterations - more iterations will make the result more accurate, but will take longer.

        Output: values that differs from a root f(x) = 0 by less than tolerance
        """
    
        def finite_differences(f, x, h):
            '''
            input f: function for which we are trying to approximate the derivative.
            input x: point to evaluate the at derivative.
            input h: small step size for finite difference method

            output: approximated derivative of the function at point x
            '''
            return (f(x+h)-f(x-h)) / (2*h) #second order accuracy 

        # initializes current approx with initial guess
        xi = initial_guess
        
        # iterates through formula for xi
        for i in range(max_iterations):
            # calculates derivative using finite difference function
            df = finite_differences(mathematical_function, xi, 1e-10)
            
            # prevents division by zero
            if abs(df) < 1e-10:
                #continue
                raise ValueError(f"Cannot divide by zero in newton's method. abs(df) < 1e-10, abs(df) = {abs(df)}")

            # make our new approximation of the root
            x_next = xi - (mathematical_function(xi) / df)
            
            # checks out tolerance
            if abs(x_next - xi) < tolerance:
                return x_next
            
            # update approximation
            xi = x_next
        
        raise RuntimeError("Newton's method failed")

    def run_test(self, log=True):
        # e^(x) - sin(x)
        def function1(x):
            return np.exp(x) - np.sin(x)

        # (x - 1)^(3)
        def function2(x):
            return (x - 1)**3

        # (x - 1)^(1/3)
        def function3(x):
            return np.cbrt(x - 1)
 
        init_guess = 1.1
        tol = 0.00001
        max_iter = 100000
        
        result1 = self.root_newton(function1, init_guess, tol, max_iter)
        result2 = self.root_newton(function2, init_guess, tol, max_iter)

        # newton's method will fail on function 3
        result3 = ""
        try:
            # temporarily added
            init_guess = 1.0
            result3 = self.root_newton(function3, init_guess, tol, max_iter)
        except ValueError:
            result3 = "n/a"

        if log:
            print (
                f"""{self.name} test:
                \r    e^x - sin(x)  = {result1}
                \r    (x - 1)^3     = {result2}
                \r    (x - 1)^(1/3) = {result3}
                """
            )
        
        return (result1, result2, result3)

if __name__ == "__main__":
    newtons = NewtonsMethod()
    newtons.run_test()
