"""
Bisection Method
Authors: Kevin Cosby, Jackson Simpson, Sarah Weber, William Bentley
Purpose: Calculates and includes testing functionality for bisection root finding method.
"""

import numpy as np


class BisectionMethod:
    def __init__(self):
        self.name = "Bisection Method"

    def root_bisect(self, mathematical_function, endpoint_a, endpoint_b, tolerance, max_iterations):
        """
        Bisection root finding method.

        Inputs:
        mathematical_function - function that you want to find the root of
        endpoint_a - lower bound for the interval you want to search
        endpoint_b - upper bound for the interval you want to search
        tolerance  - how much room for error can there be?
        max_iterations - more iterations will make the result more accurate, but it will take longer.

        Output: values that differs from a root f(x) = 0 by less than tolerance.

        Conditions: a < b, either f(a) < 0 and f(b) > 0 or f(a) > 0 and f(b) < 0
        """

        def approx_equal(input1, input2, tol):
            return abs(input1 - input2) < tol 

        def signs_equal(input1, input2):
            return (input1 * input2) >= 0

        N = 1
        while N <= max_iterations:
            c = (endpoint_a + endpoint_b) / 2
            value_a = mathematical_function(endpoint_a)
            value_b = mathematical_function(endpoint_b)
            value_c = mathematical_function(c)

            if approx_equal(value_c, 0, tolerance) or (((endpoint_b - endpoint_a)/2) < tolerance):
                return c

            N += 1
            if signs_equal(value_a, value_c):
                endpoint_a = c
            else:
                endpoint_b = c
                
        raise RuntimeError("Bisection method failed.")

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
        
        a = -10
        b = 10
        tol = 0.0000001
        max_iter = 10000000
        result1 = self.root_bisect(function1, a, b, tol, max_iter)
        result2 = self.root_bisect(function2, a, b, tol, max_iter)
        result3 = self.root_bisect(function3, a, b, tol, max_iter)

        if log:
            print (
                f"""{self.name} test:
                e^x - sin(x)  = {result1}
                (x - 1)^3     = {result2}
                (x - 1)^(1/3) = {result3}
                """
            )
        
        return (result1, result2, result3) 

if __name__ == "__main__":
    bisect = BisectionMethod()
    bisect.run_test()
