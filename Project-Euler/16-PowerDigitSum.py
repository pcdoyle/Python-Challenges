"""
__author__ = "Patrick Doyle"
__license__ = "The Unlicense"
__email__ = "me@pcdoyle.com"

Project Euler:
    Power digit sum
    Problem 16 
    https://projecteuler.net/problem=16

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2^1000?
"""
def digitSum(number):
    """
    The function will get the sum of the number.
    """
    sumNum = 0

    while number:
        sumNum += number % 10 # Get last digit of the number.
        number //= 10         # Remove the last digit of the number.

    return sumNum

# Start the program.
if __name__ == "__main__":
    print(digitSum(2**1000)) # Prints result of the provided exponent.