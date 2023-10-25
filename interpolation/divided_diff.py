

class DividedDiff:
    def __init__(self):
        self.name = "Divided Diff"

    def divided_diff(self, x_data, y_data):
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
        x_data = [1.0, 2.0, 3.0, 4.0]
        y_data = [0.0, 1.0, 27.0, 63.0]
        
        result1 = self.divided_diff(x_data, y_data)

        if log:
            print (
                f"""{self.name} test:
                \r    x-data: {x_data}
                \r    y-data: {y_data}
                \r    result: {result1}
                """
            )
        
        return result1

#diagonal_entries = divided_diff(x_data, y_data)
#print(diagonal_entries)
if __name__ == "__main__":
    divdif = DividedDiff()
    divdif.run_test()


