# This program takes a 9x9 Sudoku grid and solves it using recursion and backtracking

# Import NumPy library
import numpy as np

# Declaration of Sudoku grid 9x9
grid = [
    [6,0,9,0,0,0,0,1,0],
    [0,0,0,9,0,0,6,0,0],
    [2,7,0,0,4,0,0,3,0],
    [3,0,0,0,0,0,0,0,0],
    [8,0,6,2,0,0,0,0,9],
    [0,0,0,0,7,0,1,0,0],
    [0,0,0,0,0,1,7,0,5],
    [0,0,0,0,0,3,0,0,6],
    [0,9,0,0,0,2,0,0,0],
     ]

# Print out unsolved sudoku grid
print("Unsolved Sudoku grid:")
print(np.matrix(grid), "\n")

# Function determines whether sudoku is possible to solve, false in not possible, true if possible
def possible(y, x, n):

    # Import grid as a global variable
    global grid

    # Loop through grid in x axis
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    # Loop through grid in y axis
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    x0 = (x//3) * 3
    y0 = (y//3) * 3

    # Check that grid values are not repeated
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+1][x0+j] == n:
                return False
    return True

# Function solves sudoku grid using backtracking
def solve():

    # Import grid as a global variable
    global grid

    # Loop through values of y axis 0-9
    for y in range(9):
        # Loop through values of y axis 0-9
        for x in range(9):
            # If grid square is empty, try to put in a number
            if grid[y][x] == 0:
                # Try each number from 1 to 9
                for n in range(1, 10):
                    # Check whether number is possible, if yes put it in
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return

    # Print solved sudoku grid and prompt user for more
    print("Solved Sudoku grid:")
    print(np.matrix(grid))
    input("\nMore?")

# Call solve function
solve()