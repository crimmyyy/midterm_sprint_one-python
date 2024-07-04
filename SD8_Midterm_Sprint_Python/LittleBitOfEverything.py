# Title: A Little Bit of Everything
# Description: Using a little bit of everything, this is a program used to determine the maitenance schedule for Mario's Plumbing. 
# Author: Scarlett / Crimson (Kyle Budgell)

# Import libraries.

import sys # Import info credit: craftxbox on GitHub
import datetime
import math
import random
from datetime import date
from datetime import timedelta

# Define constants.

SALVAGE_PERC = 10

MONTHS = 12

EQUIP_LIFE = 180

# Gather user inputs.

while True:
    while True:
        Cost = input("Enter the cost for the maintenance. (DIGITS ONLY. You may also wish to exit the program by typing END.): ")
        if Cost.upper() == 'END':
            sys.exit("Thank you for using Mario's Plumbing Maintenance Tracker. Have a good day.")
        elif Cost == "":
            print("Cost error: cannot be blank. Please try again.")
        elif not Cost.isdigit():
            print("Cost error: not a digit. Please try again.")
        else:
            Cost = float(Cost)
            print("Cost entered:", Cost)
            
            PurrDate = input("Please enter the purchase date (YYYY-MM-DD): ")
            try:
                date = datetime.datetime.strptime(PurrDate, "%Y-%m-%d")
                print("Date entered:", date.strftime("%Y-%m-%d"))

                # Determine future dates based on the entered purchase date
                BasicClean = date + datetime.timedelta(days=10)
                TubeChecks = date + datetime.timedelta(days=21)  # 3 weeks
                Inspection = date + datetime.timedelta(days=182)  # 6 months
                InvDate = datetime.date.today()

                print("Next basic cleaning on:", BasicClean.strftime("%Y-%m-%d"))
                print("Next tube checks on:", TubeChecks.strftime("%Y-%m-%d"))
                print("Next inspection on:", Inspection.strftime("%Y-%m-%d"))
                print("Invoice date:", InvDate)
                
                break  

            except ValueError:
                print("Date error - incorrect format. Please use the YYYY-MM-DD format.")

    # Do the other necessary calculations.


    SalvValue = (SALVAGE_PERC * Cost) / 100

    SalvValue = float(SalvValue)

    Amort = (Cost - SalvValue) * MONTHS

    Amort = float(Amort)

    MonAmort = float(round(Cost / EQUIP_LIFE))


    # Do the following outputs

    print("---------------------------------------------------------------------------") # there are 75 lines to work with.
    print(                                                                             )
    print("Mario's Plumbing and Maitenance")
    print(f"Purchase date: {PurrDate}                          Invoice Date: {InvDate}")                                
    print("---------------------------------------------------------------------------")
    print(                                                                             )
    print(f"Initial cost: ${Cost:.2f}                    Perform cleaning on:         ")
    print(f"-------------------------                     {BasicClean}                ")
    print("                                          --------------------------       ")
    print("                                              Check the tubes on:          ")
    print(f"                                              {TubeChecks}                ")
    print("                                          --------------------------       ")
    print("                                            Perform inspection on:         ")
    print(f"                                              {Inspection}                ")
    print("                                          --------------------------       ")
    print("Salvage value:                                                             ")
    print("---------------                                                            ")
    print(f" ${SalvValue:.2f}                                                         ")
    print("----------------------------------------                                   ")
    print("Monthly amortization (based on 15 years):                                  ")
    print("----------------------------------------                                   ")
    print(f" ${MonAmort:.2f}                                                          ")
    print("-------------------                                                        ")
    print("Total amortization:                                                        ")
    print("----------------------                                                     ")
    print(f" ${Amort:.2f}                                                             ")
    print("----------------                                                           ")
    print(                                                                             )
    print("---------------------------------------------------------------------------")
    print("                       The best plumbing job in town!                      ")
    print(                                                                             )
