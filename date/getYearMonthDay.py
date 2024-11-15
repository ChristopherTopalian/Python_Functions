# getYearMonthDay.py

import datetime as dt

def getYearMonthDay():
    currentDate = dt.date.today()

    yearMonthDay = currentDate.strftime('%Y-%m-%d')

    return yearMonthDay

####

if __name__ == '__main__':
    print(getYearMonthDay())
    input('')

####

'''
2024-11-15
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

