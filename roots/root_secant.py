"""
Secant Method
Authors: Kevin Cosby, Jackson Simpson, Sarah Weber, William Bentley
Purpose: Calculates and includes testing functionality for bisection root finding method.
"""

import numpy as np


class SecantMethod:
    def __init__(self):
        self.name = "Secant Method"

    def root_secant(self, mathematical_function, initial_guess_1, initial_guess_2, tolerance, max_iterations):
        # Initialize the counter for iterations and create a list to store errors at each iteration
        iteration_count = 0
#        error_list = []
        
        # Set initial guesses
        x_previous = initial_guess_1
        x_current = initial_guess_2
        
        # Start the loop for the iterative process
        while iteration_count < max_iterations:
            # Calculate the function values at the previous and current guesses
            f_previous = mathematical_function(x_previous)
            f_current = mathematical_function(x_current)
            
            # Use the Secant formula to find the next approximation
            x_next = x_current - f_current * (x_current - x_previous) / (f_current - f_previous)
            
            # Calculate the error between the new and previous approximation
            error = abs(x_next - x_current)
            
            # Add the error to the list
#            error_list.append(error)
            
            # Check if the error is below the set tolerance level
            if error < tolerance:
#                print(f"The root is {x_next} found in {iteration_count} iterations.")
                return x_next
            
            # Update the initial guesses for the next iteration
            x_previous, x_current = x_current, x_next
            
            # Increase the iteration counter
            iteration_count += 1
        
        # Print a message if the method does not converge within the set number of iterations
        raise RuntimeError("Secant method failed.") 

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
        
        min_guess = 1.005
        max_guess = 1.5
        tol = 0.0000001
        max_iter = 1000000
        result1 = self.root_secant(function1, min_guess, max_guess, tol, max_iter)
        result2 = self.root_secant(function2, min_guess, max_guess, tol, max_iter)
        result3 = self.root_secant(function3, 0.5, max_guess, tol, max_iter)

        # print results if enabled
        if log:
            print (
                f"""{self.name} test:
                \r    e^x - sin(x)  = {result1}
                \r    (x - 1)^3     = {result2}
                \r    (x - 1)^(1/3) = {result3}
                """
            )
        
        # return results for later use
        return (result1, result2, result3) 

if __name__ == "__main__":
    secant = SecantMethod()
    secant.run_test()


