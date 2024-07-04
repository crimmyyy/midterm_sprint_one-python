#DESCRIPTION: Library to quickly convert dates to and from strings using the MM/DD/YYYY format.
#AUTHOR:      Zachary Collier
#DATE:        June 15th, 2024

import datetime

def strToDateConv(dateToConv):
    dateReturn = datetime.datetime.strptime(dateToConv, '%m/%d/%Y')
    return dateReturn

def dateToStrConv(dateToConv):
    dateReturn = datetime.datetime.strftime(dateToConv, '%m/%d/%Y')
    return dateReturn
