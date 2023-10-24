import numpy as np

class LagrangeInterpolation:
    def __init__(self):
        self.name = "Lagrange Interpolation"

    def poly_eval_lagrange(self, points, x_data, y_data):
        """
        Evaluates the lagrange polynomial p_n(x) corresponding to the interpolation
        points {x_data, y_data} at x. If x is a list, the output is a list where each
        element corresponds to p_n(x[i]).

        Inputs:
        points -- points to evaluate the lagrange polynomial at
        x_data -- list of floats (interpolation nodes)
        y_data -- list of floats (function values at interpolation nodes)

        Output: p_n(x) for each x in points
        """
        
        # ensure that the points to evaluate are in a list, even if there is only 1
        if isinstance(points, (int, float)):
            points = [points]
        
        # list to store the results in
        results = []
        
        # iterate through each point in points and perform algorithm
        for x in points:
            p_x = 0
            for i, x1_val in enumerate(x_data):
                term = y_data[i]
                for j, x2_val in enumerate(x_data):
                    if i != j:
                        term *= (x - x2_val) / (x1_val - x2_val)

                p_x += term
            results.append(p_x)
        
        # if no results were found, raise an error
        if not results:
            raise RuntimeError("Error in lagrange interpolation. results is not a valid array.")
        
        # just return a single float solution if only one point was passed
        if len(results) == 1:
            return results[0]
        
        # return the list of results
        return results
    
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
        y_data1 = [function1(x) for x in x_data]
        y_data2 = [function2(x) for x in x_data]
        y_data3 = [function3(x) for x in x_data]
        
        # points at which to evaluate the lagrange polynomial
        points_to_evaluate = [-5, 0, 5]
        
        # evaluate results
        result1 = self.poly_eval_lagrange(points_to_evaluate, x_data, y_data1)
        result2 = self.poly_eval_lagrange(points_to_evaluate, x_data, y_data2)
        result3 = self.poly_eval_lagrange(points_to_evaluate, x_data, y_data3)

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
    lagrange = LagrangeInterpolation()
    lagrange.run_test()
