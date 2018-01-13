"""
__author__ = "Patrick Doyle"
__license__ = "The Unlicense"
__email__ = "me@pcdoyle.com"

Calculating the sum of the digits of a integer.
"""
def sumOfDigits(number):
    '''
    Will get a sum of all digits in an int.
    '''
    numberSum = 0

    while number > 0:
        numberSum += number % 10
        number -= number % 10
        number //= 10

    return numberSum

if __name__ == "__main__":
    print(sumOfDigits(123456))
