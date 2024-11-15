# getDayOfWeekNumber7.py

import datetime as dt

def getDayOfWeekNumber7():
    currentDate = dt.datetime.today()

    # monday is 0, sunday is 6
    dayOfWeekNumber = currentDate.weekday()

    # adjust so that monday is 1, sunday is 7
    dayOfWeekNumberAdjusted = dayOfWeekNumber + 1

    return dayOfWeekNumberAdjusted

####

if __name__ == '__main__':
    print(getDayOfWeekNumber7())
    input('')

####

'''
3, if today is wednesday
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
