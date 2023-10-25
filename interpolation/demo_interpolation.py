from interpolation.lagrange import LagrangeInterpolation
from interpolation.newtons import NewtonsInterpolation
from interpolation.divided_diff import DividedDiff

def demo():
    # initialize objects for each method
    divdif = DividedDiff()
    lagrange = LagrangeInterpolation()
    newtons = NewtonsInterpolation(divdif.divided_diff)

    # run built in tests
    divdif.run_test()
    lagrange.run_test()
    newtons.run_test()

