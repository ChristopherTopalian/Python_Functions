# getMonthNumber.py

import datetime as dt

def getMonthNumber():
    currentDate = dt.datetime.now()

    # 1 is Jan, 12 is December
    month = currentDate.month

    return month

####

if __name__ == '__main__':
    print(getMonthNumber())
    input('')

####

'''
11
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

