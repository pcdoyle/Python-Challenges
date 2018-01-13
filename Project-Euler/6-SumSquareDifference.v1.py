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

    VERSION 1:
        This brute forces the answer with a for loops and
        is not the best method to do this. See Version 2.
"""
def sumSquare(number):
    """
    This function will do the math required to calculate the
    difference in the stated problem.
    """
    sumSq = 0    # Sum of the squares.
    sqOfSum = 0  # Square of the sum.

    for i in range(1, number+1):
        sumSq += i**2  # Get the sum of the squares.
        sqOfSum += i   # Get the sum of natural numbers.

    sqOfSum = sqOfSum**2    # Squaring the sum.
    diff = sqOfSum - sumSq  # Difference of the Sum of Square.

    return diff  # Print the difference of the sums.

# Start the program.
if __name__ == "__main__":
    print(sumSquare(100))  # Start the program asking to solve for 100.
