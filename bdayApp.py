__author__ = "byteme8bit"
import datetime


# Header
def print_header():
    print('----------------------')
    print('|    Birthday App    |')
    print('----------------------')
    print()


# User info
def getUserBday():
    print('When were you born?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    bday = datetime.date(year, month, day)
    return bday


# Calculations
def compute2Dates():
    pass


# Return
def printBdayInfo():
    pass


# Main
def main():
    print_header()
    bday = getUserBday()
    now = None
    numDays = compute2Dates(bday, now)
    printBdayInfo(numDays)


main()
