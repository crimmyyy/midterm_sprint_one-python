#DESCRIPTION: Main Menu Program for Midterm Sprint
#AUTHOR:      Zachary Collier
#DATE:        June 17th, 2024

#Import Libraries
import subprocess
import sys

#Define Constants

#Define Functions

#Gather user inputs
while True:

    print('''
    Midterm Sprint - Main Menu
    Welcome! Please choose an option:

    1. Complete a travel claim.
    2. Fun interview question.
    3. Cool stuff with strings and dates.
    4. A little bit of everything.
    5. Something old, something new.
    6. Quit program.
    ''')
    while True:
        try:
            choice = int(input("Enter choice (1-6): "))
        except:
            print("ERR: Please enter a number.")
        else:
            if choice < 1 or choice > 6:
                print("ERR: Please enter a number between 1 and 6.")
            else:
                break
    
    #Perform calculations
    if choice == 1:
        subprocess.run([ "python3" , "TravelClaim.py" ])
    elif choice == 2:
        subprocess.run([ "python3" , "FunInterviewQuestion.py"])
    elif choice == 3:
        subprocess.run([ "python3" , "CoolStuff.py"])
    elif choice == 4:
        subprocess.run([ "python3" , "LittleBitOfEverything.py"])
    elif choice == 5:
        subprocess.run([ "python3" , "SomethingOldSomethingNew.py"])
    else:
        sys.exit("Thank you for using our programs!")