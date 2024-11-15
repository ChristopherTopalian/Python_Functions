# getDayOfWeekNumber.py

import datetime as dt

def getDayOfWeekNumber():
    currentDate = dt.datetime.today()

    # sunday returns as 6
    dayOfWeekNumber = currentDate.weekday()

    # adjust so that sunday returns as 0
    dayOfWeekNumber = (dayOfWeekNumber + 1) % 7

    # adjust so that sunday returns as 1
    dayOfWeekNumberAdjusted = dayOfWeekNumber + 1

    return dayOfWeekNumberAdjusted

##

if __name__ == '__main__':
    print(getDayOfWeekNumber())
    input('')

####

'''
4, if wednesday
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
