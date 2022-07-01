"""
Diego Alvarado
CISA 3309-600
Professor Dr. Zechun Cao
June 30th 2022

Student Database Console
Retrieves student record information from a spreadsheet located in the same parent directory
and creates multi-dimensional array and reads, searches, and adds to the array
"""

import csv

def read_file(record_file):
    dblist = []
    with open(record_file, 'r') as stu_file:
        records = csv.reader(stu_file)
        for row in records:
            dblist.append([int(row[0]), (row[1]), (row[2]), (row[3]), float(row[4])])
    return dblist
student_db = read_file('student_records.csv')

### ^ SUPPLIED CODE, DO NOT EDIT ^ ###

#Print All Student Records
def displayAll():
    print()
    print("Displaying All Student Records")
    y = 0
    print("Stu ID".ljust(1), '', "Name".ljust(26), ' ', "Major".ljust(3), ' ', "Entry", "GPA")

    while y < len(student_db):
        x = 0
        statement = " "
        while x < len(student_db[y]):
            if x == 0:
                statement = statement + str(student_db[y][x]) + "".ljust(2)
                x += 1
            elif x == 1:
                statement = statement + str(student_db[y][x]) + "".ljust(30 - len(student_db[y][x]))
                x += 1
            elif x == 2:
                statement = statement + str(student_db[y][x]) + "".ljust(7 - len(student_db[y][x]))
                x += 1
            elif x == 4:
                statement = statement + ("{:.2f}".format(student_db[y][x]))
                x += 1
            else:
                statement = statement + str(student_db[y][x]) + " "
                x += 1
        print(statement)
        y += 1
    print()
    menu()

# Search for Student Record by ID
def searchID():
    print()
    studentID = int(input("Student ID to Search: "))
    x = 0
    statement = ""
    while x < len(student_db):
        if student_db[x][0] == studentID:
            statement = student_db[x]
            id = str(student_db[x][0])
            name = str(student_db[x][1])
            sub = str(student_db[x][2])
            ent = str(student_db[x][3])
            gpa = str(student_db[x][4])
        x += 1

    if statement == "":
        print("Student ID does not exist")
    else:
        print("\nRecord found in index " + str(x) + "\n")
        print("Stu ID".ljust(1), '', "Name".ljust(26), ' ', "Major".ljust(3), ' ', "Entry", "GPA")
        print(id.ljust(6),'', name.ljust(26),' ', sub.ljust(3),' ', ent.rjust(6), gpa)
    print()
    menu()

# Add a new Student to csv
def addStudent():
    print()
    studentID = int(input("New Student ID: "))
    x = 0
    exist = ""
    # Loop to search if ID already exists
    while x < len(student_db):
        if student_db[x][0] == studentID:
            exist = str(student_db[x])
        x += 1

    # If Student ID does NOT exist, requests values to create new list in student_db array
    if exist == "":
        print()
        print("Student ID available")
        studentName = str(input("Student First and Last Name: "))
        subjectAbbr = str(input("Subject Abbreviation: "))
        entryNum = int(input("Entry #: "))
        gpaFloat = float(input("Grade Point Average: "))

        student_db.append([studentID, studentName, subjectAbbr, entryNum, gpaFloat])

    # If Student ID exists, print error
    elif exist != "":
        print()
        print("! Student ID already exists !")
        print(exist)
    print()
    menu()

# Print menu
def menu():
    print()
    print("Student Record Menu System:")
    print("--------------------------------")
    print(" (1) Display all records")
    print(" (2) Get a Student Record")
    print(" (3) Add a new student record")
    print()
    print(" (0) Exit")
    print()
    option = int(input("Enter option code: "))

    # Supplying int(1) executes displayAll function, THEN menu again
    if option == 1:
        displayAll()

    # Supplying int(2) executes searchID function, THEN menu again
    elif option == 2:
        print("")
        searchID()

    # Supplying int(3) executes addStudent function, THEN menu again
    elif option == 3:
        print("")
        addStudent()

    # Supplying int(0) finishes menu() execution
    elif option == 0:
        print()
        print("Exiting Program")

    # No specified int in earlier statement finishes menu() execution, printing error
    else:
        print()
        print("Invalid Option Choice: Exiting Program")

# Start of Code Execution, Runs Menu Function
menu()
