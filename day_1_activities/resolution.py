# -----------------------------------------
# Existing student data (example starter)
# -----------------------------------------
students = [
    {
        "cps_id": "123456",
        "name": "Lopez, Maria",
        "middle_name": "Isabel",
        "homeroom": "301",
        "grade": 7,
        "primary_email": "mlopez@cps.edu",
        "secondary_email": "mlopez2@cps.edu"
    },
    {
        "cps_id": "789012",
        "name": "Johnson, Malik",
        "middle_name": "Andre",
        "homeroom": "204",
        "grade": 8,
        "primary_email": "mjohnson@cps.edu",
        "secondary_email": "mjohnson2@cps.edu"
    }
]


# -----------------------------------------
# SEARCH FUNCTION
# -----------------------------------------
def search_student(full_name):
    """
    Students must be able to describe this process:
    - Loop through the list of student dictionaries
    - Compare the 'name' field to the search term
    - If found, return the dictionary
    - If not found, return None
    """
    # first step: 
    # create a loop to loop throughthe students
    for student in students:
    # then compare the name field to the search term
       if student["name"].lower() == full_name.lower():
            # if found, return the dictionary
            return student
       
    # if not found, return None
    


# -----------------------------------------
# ADD NEW STUDENT FUNCTION
# -----------------------------------------
def add_student():
    print("\n--- Add a New Student ---")

    # Get user input for all required fields
    cps_id= input("CPS ID: ")

    # Check for duplicate CPS ID
    # Loop through existing students to see if cps_id already exists
    for student in students:
        # Check if the current student's cps_id matches the new cps_id
        if student["cps_id"] == cps_id:
            # If a match is found, print an error and exit the function
            print("ERROR: A student with this CPS ID already exists")
            # Exit the function early to prevent adding a duplicate
        return            

    # Continue gathering the rest of the information
    # Prompt the user for each piece of information
    first = input("First Name: ")
    last = input("Last Name: ")
    middle = input("Middle Name: ")
    homeroom = input("Homeroom: ")
    grade = int(input("Grade Level: "))
    primary = input("Primary Email: ")
    secondary = input("Secondary Email: ")

    # Format name as "Last, First"
    full_name = f"{last}, {first}"

    # Build the dictionary
    # Create a new dictionary with all the collected information from the user inputs
    new_student = {
        "cps_id": cps_id,
        "name": full_name,
        "middle_name": middle,
        "homeroom": homeroom,
        "grade": grade,
        "primary_email": primary,
        "secondary_email": secondary
    }

    # Add to the list
    students.append(new_student)

    # Confirmation
    print("Student added sucessfully.")
    print(new_student)
    print("-------------------------")
    print(f"Total students in system: {len(students)}")
    print("new record:" , new_student)


# -----------------------------------------
# MAIN PROGRAM LOOP
# this is where the program starts running

# -----------------------------------------
while True: #run until user says to stop
    # Menu
    print("\n===== STUDENT LOOKUP TOOL =====")
    print("1. Search for a student")
    print("2. Add a new student")
    print("3. Quit")

    # Get user choice
    choice = input("Choose an option: ")
    # Handle user choice
    if choice == "1":
        # Search for a student
        name=input("\n Enter the student's full name (Last, First): ")
        # Call the search function and store the result
        result= search_student(name)
        

        # Display results
        if result:
           print("\n Student found:")
           print("CPD ID:", result["cps_id"])
           print("Name:", result["name"])
           print("Homeroom:", result["homeroom"])
           print("Grade level:", result["grade"])
           #for key, value in result.items()3
           #    print(f"{key}: {value}")
        else:
            # Inform the user if the student was not found
            print("\nStudent not found.")

    elif choice == "2":
        add_student()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")