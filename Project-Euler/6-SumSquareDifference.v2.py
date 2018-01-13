"""
__author__ = "Patrick Doyle"
__license__ = "The Unlicense"
__email__ = "me@pcdoyle.com"

Project Euler:
    Sum square difference
    Problem 6
    https://projecteuler.net/problem=6

    Find the difference between the sum of the squares
    for the first 100 natural numbers and the square sum.

    VERSION 2 (IMPROVED):
        This uses math formulas instead of brute forcing the
        answer with a for loop.
"""
def sumSquare(number):
    """
    This function will do the math required to calculate the
    difference in the stated problem.
    """
    sumSq = (2 * number + 1) * (number + 1) * number // 6 # Sum of the squares.
    sqOfSum = (number * (number + 1) // 2) ** 2           # Square of the sum.
    return sqOfSum - sumSq

# Start the program.
if __name__ == "__main__":
    print(sumSquare(100))  # Start the program asking to solve for 100.
