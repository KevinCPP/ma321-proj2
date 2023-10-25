'''
JAckson Simpson, Kevin Cosby, William Bentley, Sarah Weber
Purpose: Use nested multiplication to evaluate the polynomial in Newton’s form.
'''

import numpy as np
import math

class NewtonsInterpolation:
    def __init__(self):
        self.name = "Newton's Interpolation"

    def poly_eval_newton(self, x, coeff_nt, x_data):
        """
        Evaluates a Newton’s polynomial with coefficients coeff_nt
        and x_data at x.
        If x is a list, then the output is a list where each element
        corresponds to p_n(x[i]).
        Parameters:
        - x: float or list of floats
        - coeff_nt: list of floats (coefficients from divided_diff)
        - x_data: list of floats (interpolation nodes)
        Returns:
        - float or list of floats (interpolated values)
        """
        
        def single_evaluation(x_val):
            """Evaluate the polynomial for a single value of x."""
            n = len(coeff_nt) - 1
            result = coeff_nt[n]
            for i in range(n-1, -1, -1):
                result = coeff_nt[i] + (x_val - x_data[i]) * result
            return result

        # Check if x is a single float value or a list of floats
        if isinstance(x, (float, int)):
            return single_evaluation(x)
        elif isinstance(x, list):
            return [single_evaluation(x_val) for x_val in x]
        else:
            raise ValueError("x must be either a float or a list of floats.")
    
    def divided_differences(self, x_data, y_data):
        """
        Calculate the coefficients for Newton's polynomial using divided differences.

        Parameters:
        - x_data: list of floats (interpolation nodes)
        - y_data: list of floats (function values at interpolation nodes)

        Returns:
        - list of floats (coefficients for Newton's polynomial)
        """
        n = len(y_data)
        coeff = [0.0] * n

        # Initialize the diagonal of the divided difference table with y_data
        for i in range(n):
            coeff[i] = y_data[i]

        # Build the divided difference table
        for j in range(1, n):
            for i in range(n-1, j-1, -1):
                coeff[i] = (coeff[i] - coeff[i-1]) / (x_data[i] - x_data[i-j])

        return coeff


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
        
        # create some sample data points for interpolation
        x_data = np.linspace(-10, 10, 10)
        
        # Generate coefficients using divided differences
        coeff_nt1 = self.divided_differences(x_data, [function1(x) for x in x_data])
        coeff_nt2 = self.divided_differences(x_data, [function2(x) for x in x_data])
        coeff_nt3 = self.divided_differences(x_data, [function3(x) for x in x_data])

        # points at which to evaluate the lagrange polynomial
        points_to_evaluate = [-5, 0, 5]
        
        # evaluate results
        result1 = self.poly_eval_newton(points_to_evaluate, coeff_nt1, x_data)
        result2 = self.poly_eval_newton(points_to_evaluate, coeff_nt2, x_data)
        result3 = self.poly_eval_newton(points_to_evaluate, coeff_nt3, x_data)

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
    newtons = NewtonsInterpolation()
    newtons.run_test()
