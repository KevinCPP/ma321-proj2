from roots.root_bisect import BisectionMethod
from roots.root_newtons import NewtonsMethod
from roots.root_secant import SecantMethod

def demo():
    # initialize objects for each method
    bisection = BisectionMethod()
    newtons   = NewtonsMethod()
    secant    = SecantMethod()
    
    # run built in tests
    bisection.run_test()
    newtons.run_test()
    secant.run_test()

if __name__ == "__main__":
    demo()

