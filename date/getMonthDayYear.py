# getMonthDayYear.py

import datetime as dt

def getMonthDayYear():
    currentDate = dt.date.today()

    monthDayYear = currentDate.strftime('%m-%d-%Y')

    return monthDayYear

####

if __name__ == '__main__':
    print(getMonthDayYear())
    input('')

####

'''
11-15-2024
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

