'''
Author: Tyke Anfield
Last Revision 11-1-2022
Program name: Student_gpa.py
Purpose: Takes input for students names, then input for GPA. if GPA is equal or greater than 3.5 the program outputs the students name and declares they made it on the Dean's list,
if  GPA is equal or greater than 3.25 the program outputs the students name and declares they made it on the Honor Roll.
'''

# Input Students last name or Quits the program
lName = input("Enter students last name or ZZZ to quit: ")

# loop to cycle through entering inputs for students name and GPA
while lName != "ZZZ":
    # Input students name
    fName = input("Enter students first name: ")
    # Input GPA
    gpa = float(input("Enter "+fName+" "+lName+"'s GPA: "))
    
    # Compare GPA inputs with default condition
    if gpa >= 3.5:
    # Output students name if they made the Dean's list
        print(fName, lName, "has made the Dean's List.")
        # empty string to create new line before starting new student
        print("")
    elif gpa >= 3.25:
        # Output students name if they made the Honor Roll
        print(fName, lName, "has made the Honor Roll.")
        # empty string to create new line before starting new student
        print("")
    else:
        print(fName, lName, "did not made the Honor Roll or the Dean's list.")
        # empty string to create new line before starting new student
        print("")
    # Input Students last name or Quits the program
    lName = input("Enter students last name or ZZZ to quit: ")
    
