from interpolation.lagrange import LagrangeInterpolation
from interpolation.newtons import NewtonsInterpolation

def demo():
    # initialize objects for each method
    lagrange = LagrangeInterpolation()
    newtons = NewtonsInterpolation()

    # run built in tests
    lagrange.run_test()
    newtons.run_test()

