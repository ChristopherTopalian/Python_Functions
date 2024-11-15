# getTime12.py

import datetime as dt

def getTime12():
    currentTime = dt.datetime.now()

    formattedTime = currentTime.strftime("%I:%M:%S %p")

    return formattedTime

####

if __name__ == '__main__':
    print(getTime12())
    input('')

####

'''
05:43:07 PM
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
