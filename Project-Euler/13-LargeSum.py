"""
__author__ = "Patrick Doyle"
__license__ = "The Unlicense"
__email__ = "me@pcdoyle.com"

Project Euler:
    Large sum
    Problem 13
    https://projecteuler.net/problem=13

    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    (The numbers are in "13-LargeSum.txt")
"""
def largeSum(file):
    """
    The function will get the sum of the large number.
    """
    with open(file, 'r') as f:  # Open the file of numbers.
        numbers = f.readlines() # Read the lines from the file of numbers, store them into a list.

    summ = sum(map(int, numbers)) # Convert the list to int, then sum all the numbers in the list.

    return str(summ)[:10]  # Returns the first 10 digits of the sum.

# Start the program.
if __name__ == "__main__":
    print(largeSum("13-LargeSum.txt")) # Get the results from the provided file and return them.
