# getTime24.py

import datetime as dt

def getTime24():
    currentTime = dt.datetime.now()

    formattedTime = currentTime.strftime('%H:%M:%S')

    return formattedTime

####

if __name__ == '__main__':
    print(getTime24())
    input('')

####

'''
17:07:29
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
