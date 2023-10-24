from root_bisect import BisectionMethod
from root_newtons import NewtonsMethod

if __name__ == "__main__":
    # initialize objects for each method
    bisection = BisectionMethod()
    newtons   = NewtonsMethod()
    
    # run built in tests
    bisection.run_test()
    newtons.run_test()

