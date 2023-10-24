from roots.root_bisect import BisectionMethod
from roots.root_newtons import NewtonsMethod

def demo():
    # initialize objects for each method
    bisection = BisectionMethod()
    newtons   = NewtonsMethod()
    
    # run built in tests
    bisection.run_test()
    newtons.run_test()

if __name__ == "__main__":
    demo()

