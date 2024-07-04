# Title : Something Old, Something New
# Description : Something new that has not been covered yet in class. This feature being the "import platform" function, which pulls your current system info with various different functions. (ex. determining Python version, CPU architecture, etc.)
# Author : Crimson / Scarlett (Kyle Budgell)

# Do the imports

import platform # A platform used to pull system information, among other things about your system and current versions of certain languages that are running on your system.
import sys


# Do the results.

Machine = input("Do you wish to know your system specifications? (Y / N) Note: Choosing 'N' will exit the program: ")
if Machine.upper() == "Y":
    # Machine type query (ex. AMD64 or x86)
    if Machine.upper() == "Y":
        print("Machine type:", platform.machine()) 
    elif Machine.upper() == "N":
        sys.exit("Thank you for using Machine Spec detector. Have a wonderful day!")

    # Platform version query. Tells you which version of the operating system you are running (ex. 1.1.1111)
    PlatVersion = input("Do you wish to know the platform version? (Y / N): ")
    if PlatVersion.upper() == "Y":
        print("Platform version:", platform.version())
    elif PlatVersion.upper() == "N":
        sys.exit("Thank you for using Machine Spec detector. Have a wonderful day!")

    # Operating system with version query. Includes your operating system name, along with the version you are running (ex. Windows, 1.1.1111)
    OpSystem = input("Do you wish to know the operating system and version? (Y / N): ")
    if OpSystem.upper() == "Y":
        print("Operating System and version:", platform.platform())
    elif OpSystem.upper() == "N":
        sys.exit("Thank you for using Machine Spec detector. Have a wonderful day!")

    # uname information query. Includes things like name, release, and version of the current operating system, name of the machine on the network, and hardware identifier.
    PlatUName = input("Do you wish to know detailed uname info? (Y / N): ")
    if PlatUName.upper() == "Y":
        print("System Uname:", platform.uname())
    elif PlatUName.upper() == "N":
        sys.exit("Thank you for using Machine Spec detector. Have a wonderful day!")

    # System name query. Used to retrieve information about the platform on which the program is being currently executed.
    Sys = input("Do you wish to know the system name? (Y / N): ")
    if Sys.upper() == "Y":
        print("System Name:", platform.system())
    elif Sys.upper() == "N":
        sys.exit("Thank you for using Machine Spec detector. Have a wonderful day!")

    # Processor details query. Includes your processor make, model and version.
    SysProcessor = input("Do you wish to know the processor details? (Y / N): ")
    if SysProcessor.upper() == "Y":
        print("Processor Details:", platform.processor())
    elif SysProcessor.upper() == "N":
        sys.exit("Thank you for using Machine Spec detector. Have a wonderful day!")

    # Python version query. Determines the version of Python running on your system.
    PyVersion = input("Do you wish to know the Python version? (Y / N): ")
    if PyVersion.upper() == "Y":
        print("Python Version:", platform.python_version(), "; Build:", platform.python_build())
    elif PyVersion.upper() == "N":
        sys.exit("Thank you for using Machine Spec detector. Have a wonderful day!")






          
          
                    
          
          
     
     
     
          
           
             
           
        
