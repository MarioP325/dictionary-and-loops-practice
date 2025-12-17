# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

# 2. Combine the First and Last name into this format:
    #    "Last, First"  

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken


import student_data2 #imports our data from our other set
student_data = student_data2.students # reference to our dictionary set

def New_Response(): #function for when the person wants to create a new response (needed for the end of the loop as well) 
    global create_response
    create_response = False

    global Fix
    Fix = True

    Start_New_Response = input("Would you like to add a new response? (Yes or No): ") #ask for if they want a new response

    while Fix:
        if Start_New_Response.lower() == "yes": #this part works
            create_response = True # Boolean to create response if the person wants to
        else:
            print("Response Declined, Rerun program to add a response")
            create_response = False # Boolean to create response if the person wants to
            break

New_Response()

while create_response: # if create_reponse == true then we are taking responses 
    for response in student_data: # Creates a loop to iterate through our data
        student_ID = int(input("CPS ID?: "))

        if student_ID == response["CPSID"]: #checks if ID's are the same, otherwise it breaks the loop and reruns it
            print("ID is already in the system, Please Retry")
            break

        student_data[-1].update({"CPSID":student_ID}) #Add student ID to dictionary
        
        student_data[-1]["LName"] = input("Last Name?: ")
        student_data[-1]["FName"] = input("First Name?: ")
        student_data[-1]["MName"] = input("Middle Name?: ")

        student_data[-1]["Combo,Name"] = student_data[-1]["LName"] + ' ' + student_data[-1]["FName"]

        student_data[-1]["HR"] = input("Home Room?: ")
        student_data[-1]["GL"] = int(input("Grade Level?: "))

        student_data[-1]["Email"] = input("Primary Email?: ") + ", " + input("Secondary Email?: ")

        student_data.append(response)
        
        print(student_data) #for testing
      
        New_Response()
        create_response = False


#end

#print(student_data) #prints final list
