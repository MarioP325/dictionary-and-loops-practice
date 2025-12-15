# This activity:
#     Reinforces nested dictionaries & lists
#     Ties directly to real school systems
#     Builds search logic & data modeling
    

# You are working with a real school-style student database where:

# Each student is a dictionary

# All students are stored inside one list

# Each student dictionary contains:

            #     CPSID

            #     Combo,Name

            #     LName

            #     FName

            #     MName

            #     HR

            #     GL

            #     Email (a list with 2 emails)

# Alright, let's simplify and rephrase the problem set to avoid using functions:

# Exercise 2 — Accessing Data by Index

#     Without writing new code, answer:

    #     What does students[0] represent?

    #     What would students[0]['Email'][1] return?

    #     Why does students[0]['Email'][0] use two sets of brackets?
import student_data

# print(student_data.students)
students = student_data.students
print(len(students))
# print(students[0]['Combo,Name'])
# print(students[0]['Email'][0])
# print(students[0]['Email'][1])
# print(students[0]['FName'])
# print(students[0]['LName'])
# print(students[0]['GL'])
# print(students[1]['Email'][0])
# print(students[1]['CPSID'])
# print(students[1]['GL'])
# print(students[1]['HR'])
# print(students[35]['CPSID'])
# print(students[35]['Email'][1])
# print(students[35]['GL'])
# print(students[35]['HR'])

# What is being counted?

# If the output is 36, what does that tell you?

# If one new student enrolls, what happens to this number?

# Why would a school use this in a real attendance system?





# for loops allow us to
#iterate through the data
#and perform some function

#we are iterating through the data
#and printing the name and email of the students
#we are also printing a line of underscores to separate the students
#we are also printing a line of underscores to separate the students
# for student in students:
#     print(student['Combo,Name'])
#     print(student['Email'][0])
#     print(student['Email'][1])
#     print(student['CPSID'])
#     print(student['HR'])
#     print(student['GL'])
#     if student["GL"] >= 10:
#         print("you can go to off campus")
#         if student["LName"][0] == "R":
#             print(student['Combo,Name'])
#             print(student['HR'])
#             if student["LName"][0] == "L":
#                 break
# print("_"*25)
# What does the loop variable student represent on each pass?

# How many times will this loop run?

# Why does each student print two emails?

# What is the purpose of the line of underscores?




# we are asking the user to input their name
# then we are checking if the name is in the data
# if the name is in the data we are printing the name and "this works"
name = input("what is you name?") 
for student in students:
    if name == student['Combo,Name']:
        print(student['Combo,Name'])
        print("this works")

# What is the goal of this search?

# What happens if the name is not found?

# Why is the comparison happening inside the loop?

# What would happen if two students had the same name?








# practice challenge: 

# Let's try to print out the emails of the students:    

# how  would you use this dataset to:

# Email all students in homeroom B233

# List all students in grade 10

# Find the CPS ID of a student when given only their name

# Send an email to only the second email address of every student




# Modify the Dataset 

#  describe how you  would:

        # Update a student who changed homeroom

        # Add a new student to the school

        # Remove a student who transferred out

        # Correct a student whose last name was misspelled

# Challenge Scenarios (Higher-Order Thinking)

    # Students respond in writing:

    # The district wants to pull all students whose last name starts with “M.”
    # → How would the system search for this?

    # An email system crashes because one student is missing an Email key.
    # → What does that tell you about real-world data validation?

    # Why would a dictionary be faster than a list for finding one student instantly?