'''
Author: Tyke Anfield
Last Revision 11-1-2022
Program name: Student_gpa.py
Purpose: Takes input for students name, then input for GPA. if  GPA is equal or greater than 3.5 the program outputs the students name and declares they made it on the Dean's list,
if  GPA is equal or greater than 3.25 the program outputs the students name and declares they made it on the Honor Roll.
'''

# Quits or breaks out of the program
lName = input("Enter students last name or ZZZ to quit: ")

# loop to cycle through entering inputs for students name and GPA
while lName != "ZZZ":
    #inputs for students name
    fName = input("Enter students first name: ")
    #input for GPA
    gpa = float(input("Enter "+fName+" "+lName+"'s GPA: "))
    # If loop to compare GPA input with  
    if gpa >= 3.5:
    # output students name if they made the Dean's list
        print(fName, lName, "has made the Dean's List")
    elif gpa >= 3.25:
        print(fName, lName, "has made the Honor Roll.")
    # Quits or breaks out of the program
    lName = input("Enter students last name or ZZZ to quit: ")