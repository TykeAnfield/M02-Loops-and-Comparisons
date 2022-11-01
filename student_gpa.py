'''
Author: Tyke Anfield
Last Revision 11-1-2022
Program name: Student_gpa.py
Purpose: Takes input for students name, then input for GPA. if  GPA is equal or greater than 3.5 the program outputs the students name and declares they made it on the Dean's list,
if  GPA is equal or greater than 3.25 the program outputs the students name and declares they made it on the Honor Roll.
'''

# Quits or breaks out of the program
quit = input("Press Enter to continue or ZZZ to quit: ")

# loop to cycle through entering inputs for students name and GPA
while quit != "ZZZ":
  #input for students name
  student = input("Enter students name: ")
  #input for GPA
  gPA = float(input("Enter students GPA: "))
  # If loop to compare GPA input with  
  if gPA >= 3.5:
    # output students name if they made the Dean's list
    print(student, "has made the Dean's List")
  elif gPA >= 3.25:
    print(student, "has made the Honor Roll.")
  # Quits or breaks out of the program
  quit = input("Press Enter to continue or ZZZ to quit: ")