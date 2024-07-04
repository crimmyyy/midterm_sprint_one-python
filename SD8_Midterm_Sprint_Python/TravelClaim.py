#DESCRIPTION: Program for NL Chocolate Company to process employee travel claims.
#AUTHOR:      Zachary Collier
#DATE:        June 15th, 2024

#Import Libraries
import sys
import datetime
import DollarConvLib
import DateConvLib

#Define Constants
DIEM_RATE = 85.00
MILEAGE_RATE = 0.17
CAR_RENT_RATE = 65.00

BONUS_3_DAY = 100.00
BONUS_1000_DISTANCE_RATE = 0.04
BONUS_EXECUTIVE_RATE = 45.00
BONUS_DEC_RATE = 50.00

HST_RATE = 0.15

#Define Functions

#Gather user inputs
while True:
    while True:
        employeeNum = input("Enter the employee's number (5 digits): ")
        if employeeNum.isdigit() == False:
            print("ERR: Employee Number must consist of numbers only.")
        elif len(employeeNum) != 5:
            print("ERR: Employee Number must be 5 digits long.")
        else:
            break

    while True:
        employeeFirst = input("Enter the employee's first name: ").title()
        if employeeFirst == "":
            print("ERR: Please enter the employee's first name.")
        else:
            break

    while True:
        employeeLast = input("Enter the employee's last name: ").title()
        if employeeLast == "":
            print("ERR: Please enter the employee's last name.")
        else:
            break

    tripLocation = input("Enter the trip location: ")

    while True:
        try:
            dateStart = input("Enter start date (MM/DD/YYYY): ")
            dateStartCalc = DateConvLib.strToDateConv(dateStart)
        except:
            print("ERR: Please enter the date in the format MM/DD/YYYY.")
        else:
            break

    while True:
        try:
            dateEnd = input("Enter end date (MM/DD/YYYY): ")
            dateEndCalc = DateConvLib.strToDateConv(dateEnd)
            #Calculate dayDiff in here since it's useful for validations
            dayDiff =  datetime.datetime.date(dateEndCalc) - datetime.datetime.date(dateStartCalc)
        except:
            print("ERR: Please enter the date in the format MM/DD/YYYY.")
        else:
            if dayDiff < datetime.timedelta(days = 1):
                print("ERR: Please make sure the end date is later than the start date.")
            elif dayDiff > datetime.timedelta(days = 7):
                print("ERR: The end date must not be over 7 days later than the start date.")
            else:
                break
            
    while True:
        carOwnership = input("Enter whether the employee drove their own car or rented a car (O for Owned, R for Rented): ").upper()
        if len(carOwnership) != 1:
            print("ERR: Please enter either O for Owned or R for Rented.")
        elif carOwnership != "O" and carOwnership != "R":
            print("ERR: Please enter either O for Owned or R for Rented.")
        else:
            break

    while True:
        if carOwnership == "O":
            try:
                carDistance = int(input("Please enter employee mileage (km, must be under 2000km): "))
            except:
                print("ERR: Please input a number under 2000.")
            else:
                if carDistance > 2000 or carDistance < 0:
                    print("ERR: Please input a number between 0 and 2000.")
                else:
                    break
        else:
            carDistance = "N/A"
            break

    while True:
        claimType = input("Enter the employee's claim type (S for Standard, E for Executive): ").upper()
        if len(claimType) != 1:
            print("ERR: Please enter either S for Standard or E for Executive.")
        elif claimType != "S" and claimType != "E":
            print("ERR: Please enter either S for Standard or E for Executive.")
        else:
            break
    
    #Perform calculations
    dayDiff = dayDiff.days

    diemAmount = dayDiff * DIEM_RATE

    if carOwnership == "O":
        mileageAmount = carDistance * MILEAGE_RATE
    else:
        mileageAmount = dayDiff * CAR_RENT_RATE

    bonusAmount = 0.00

    if dayDiff > 3:
        bonusAmount += BONUS_3_DAY
    if str(carDistance).isdigit() and carDistance > 1000 and carOwnership == "O":
        bonusAmount += (carDistance * BONUS_1000_DISTANCE_RATE)
    if claimType == "E":
        bonusAmount += (dayDiff * BONUS_EXECUTIVE_RATE)
    if dateStartCalc.month == 12 and dateStartCalc.day >= 15 and dateStartCalc.day <= 22:
        bonusAmount += (dayDiff * BONUS_DEC_RATE)

    claimAmount = diemAmount + mileageAmount + bonusAmount

    taxes = claimAmount * HST_RATE
    claimTotal = claimAmount + taxes

    if carOwnership == "O":
        carOwnership = "Owned"
    else:
        carOwnership = "Rented"
    
    if claimType == "S":
        claimType = "Standard"
    else:
        claimType = "Executive"

    #Display outputs
    print(f'''
    NL Chocolate Company - Employee Travel Claim

    Employee Name & Number:
    {employeeFirst} {employeeLast} : {employeeNum}
    
    Trip Location:
    {tripLocation}
    
    Start Date:
    {dateStart}
    End Date:
    {dateEnd}
    Travel Days:
    {dayDiff}
    
    Car Ownership: {carOwnership}
    Distance Traveled: {carDistance}
    Claim Type: {claimType}
    
    Diem Amount:
    {DollarConvLib.dollarConv(diemAmount)}
    Mileage Amount:
    {DollarConvLib.dollarConv(mileageAmount)}
    Total Bonuses:
    {DollarConvLib.dollarConv(bonusAmount)}
    
    Claim Subtotal:
    {DollarConvLib.dollarConv(claimAmount)}
    HST:
    {DollarConvLib.dollarConv(taxes)}
    Claim Total:
    {DollarConvLib.dollarConv(claimTotal)}
    
    -----
    ''')

    #Termination Prompt
    while True:
        terminate = input("Do another travel claim? (Y to repeat the program, N to return to main menu): ").upper()
        if len(terminate) != 1:
            print("ERR: Please enter either Y to repeat the program or N to return to main menu.")
        elif terminate != "Y" and terminate != "N":
            print("ERR: Please enter either Y to repeat the program or N to return to main menu.")
        elif terminate == "Y":
            print("Okay!")
            break
        else:
            sys.exit("Okay! Thanks for using this program! Returning to menu...")