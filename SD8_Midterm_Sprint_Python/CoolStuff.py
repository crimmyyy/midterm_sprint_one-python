# Description: This program will give employees their work credentials, along with additional information regarding retirement and birthday.
# Author: Sarah Murphy
# Date: June 16, 2024 - June 18, 2024

# Define required libraries.
import datetime
import random

# Define program constants.


# Define program functions.
def DaysTilBirthday(EmpBirthday):
    # To calculate and display the number of days until the employee's birthday.

    CurrDate = datetime.datetime.today()

    EmpBirthday = datetime.datetime(CurrDate.year, 11, 10)
    if CurrDate.month == 11 and CurrDate.day > 10:
        EmpBirthday = datetime.datetime(CurrDate.year + 1, 11, 10)
    DaysToBday = (EmpBirthday - CurrDate).days
    return DaysToBday

def TimeTilRetirement(EmpBirthdate, RetireAge=65):
    # To calculate the time until retirement.

    CurrDate = datetime.datetime.today()
    EmpBirthdate = datetime.datetime(1997, 11, 10)

    if CurrDate.month == 11 and CurrDate.day < 10:
        CurrAge = CurrDate.year - (1997 - 1)
    else:
        CurrAge = CurrDate.year - EmpBirthdate.year

    RetireTime = RetireAge - CurrAge
    return RetireTime
    
def TimeWorked(StartDatedto):
    # To calculate how long the employee has been working with us.

    CurrDate = datetime.datetime.today()
    StartDatedto = datetime.datetime(2022, 1, 15)

    EmpTimeWorked = CurrDate - StartDatedto
    
    years = EmpTimeWorked.days // 365
    remainingdays = EmpTimeWorked.days % 365
    months = remainingdays // 30
    days = remainingdays % 30
    return years, months, days


# Main program starts here.

# Gather user inputs.
EmpFirst = "Sarah"
EmpLast = "Murphy"
PhoneNum = "7091234567"
StartDate = "2022-01-15"
EmpBirthdate = "1997-01-10"

# Perform required calculations.
CurrDate = datetime.datetime.today
PassDigits = random.randint(100,999)

    # Employee ID formatted as first initial, last initial - last 4 digits of phone number - birthyear 
EmpID = EmpFirst[0] + EmpLast[0] + "-" + PhoneNum[6:] + "-" + EmpBirthdate[0:4]

    # Employee username formatted as first 3 letters of first name, ., last name
EmpUsername = EmpFirst[0:3] + "." + EmpLast

    # Employee password formatted as first 3 letters of last name, last 2 digits of start date year, 3 random digits
EmpPassword = EmpLast[0:3] + StartDate[2:4] + str(PassDigits)

EmpBirthdatedto = datetime.datetime.strptime(EmpBirthdate, "%Y-%m-%d").date()
DaysToBday = DaysTilBirthday(EmpBirthdatedto)

RetireTime = TimeTilRetirement(EmpBirthdatedto)

StartDatedto = datetime.datetime.strptime(StartDate, "%Y-%m-%d").date()

startdate = StartDatedto
YearsWorked, MonthsWorked, DaysWorked = TimeWorked(startdate)
        
# Display user outputs.
print()
print(f" Employee ID: {EmpID}")
print(f" Employee username: {EmpUsername}")
print(f" Employee password: {EmpPassword}")
print(f" Time worked: {YearsWorked} years, {MonthsWorked} months, and {DaysWorked} days.")
print(f" Days until next birthday: {DaysToBday} days")
print(f" Years until retirement: {RetireTime} years")

