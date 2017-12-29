def factorial(n):
    res = 1
    for i in range(1, n+1):
        res = res * i

    return res

# For a grid of size x
# the number of paths through it is defined as
# from 2x choose x
# which is 2x! / x!x!

grid = 20 

div = factorial(grid)

paths = int((factorial(2*grid) / div) / div)


print("Grid of size {}x{} has {} paths".format(grid, grid, paths))

