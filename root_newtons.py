'''
Newtons Method
Authors: Kevin Cosby, Jackson Simpson, Sarah Weber, William Bentley
Purpose: To recreate Newton's Method in Python to find roots for given equations.
'''
import math

def f(x):
    '''
    CHANGE THIS FUNCTION FOR EACH NEW EQUATION
    '''
    return math.pow(x-1, 1/3)

def finite_differences(f, x, h = 1e-5):
    '''
    input f: function for which we are trying to approximate the derivative.
    input x: point to evaluate the at derivative.
    input h: small step size for finite difference method

    output: approximated derivative of the function at point x
    '''
    return (f(x+h)-f(x-h)) / (2*h) #second order accuracy 
    
def root_newton(f, x0, max_iterations, h=1e-5, tolerance = 1e-5,):
    '''
    input f: function which we wish to find the root of
    input x0: initial guess for the root of f
    input tolerance: Tolerance for which we stop computation
    input max_iterations: maximum number of iterations of the algo

    output: approximate root of the function
    '''
    #initializes current approx with our inital guess
    xi = x0

    #Loops through our formula for xi
    for i in range(max_iterations):

        #calculates derivaitve using our finite difference function
        df = finite_differences(f, xi, h)

        #prevents division by zero
        if abs(df) < 1e-10:
            return "Division By Zero Preventative Called!"

        #make our new approximation of the root
        x_next = xi - (f(xi) / df)

        #checks our tolerance
        if abs(x_next - xi) < tolerance:
            return x_next

        #update the current approx
        xi = x_next
    print("Did not converge here is last known approximation for the root of f")
    return xi

y = root_newton(f, 1, tolerance = 1e-5, max_iterations = 1500)
print(y)
