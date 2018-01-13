"""
__author__ = "Patrick Doyle"
__license__ = "The Unlicense"
__email__ = "me@pcdoyle.com"

r/dailyprogrammer:
    Get the day of the week from a date entered as "YYYY MM DD" (EX: 2017 10 30)
    https://www.reddit.com/r/dailyprogrammer/comments/79npf9/20171030_challenge_338_easy_what_day_was_it_again/

To solve this I'll be using Zeller's congruence.
    https://en.wikipedia.org/wiki/Zeller's_congruence
"""
WEEKDAY = ('Saturday',
           'Sunday',
           'Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday')

def getDate():
    '''
    Main function, gets the date from the user then prints the output. 
    '''
    print('What date do you want to check? Type in "Y M D" format:')
    date = input().split(' ')

    try:
        date = list(map(int, date))

        if len(date) == 3:
            dayNumber = calculateDate(date[0], date[1], date[2])
            print('{0}/{1}/{2} is a {3}'.format(date[0], date[1], date[2], WEEKDAY[dayNumber]))
        else:
            print('Please enter the date in "Y M D" format!')
    except ValueError:
        print('Please only enter integers!')

def calculateDate(year, month, day):
    '''
    Calculates the date and returns the week number.
    Zeller's Congruence formula for the Gregorian Calendar:
    h = (q+13(m+1)/5+K+k/4+J/4-2J) mod 7
    '''
    if month < 3:
        year -= 1
        month += 12

    yearCentury = year % 100
    zeroCentury = year // 100

    dayNumber = (day + 13 * (month + 1) // 5 + yearCentury + yearCentury // 4 + zeroCentury // 4 - 2 * zeroCentury) % 7

    return(dayNumber)

if __name__ == "__main__":
    getDate() # Start Program
