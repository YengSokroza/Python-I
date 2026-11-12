import subprocess
subprocess.run("cls", shell=True)

# create an empty list
student_list = []

def menu():
    print("=" * 30)
    print("Student Grade Registration".upper().center(30, " "))
    print("=" * 30)
    print("1. Register & calculate student grade")
    print("2. View All Student")
    print("3. Exit")
    print("=" * 30)
    
def calculate_grade(score):

    # TODO 1: use proper exception (score must be a number (int or float).
  
    # TODO 2: use proper exception (score must be between 0 and 100..)

    if score >= 90:
        return "A"
    
    elif score >= 80:
        return "B"
    
    elif score >= 70:
        return "C"
    
    elif score >= 60:
        return "D"
    else:
        return "F"
    

def register_student():

    try:
        # Get student information
       

        # Get and convert score into a number
        

        # Calculate student's grade
      

        # Store student information in a dictionary
        student = {
            "name": name,
            "subject": subject,
            "score": score,
            "grade": grade
        }

        # add student into student_list
        
        return student

    except (ValueError, TypeError) as error:

        print(f"Error: {error}")

        return None

def display_students(students):

    print("\n========== STUDENT RESULTS ==========")

    for student in students:

        print(f"\nName: {student['name']}")
        print(f"Subject: {student['subject']}")
        print(f"Score: {student['score']}")
        print(f"Grade: {student['grade']}")

        print("-" * 40)

    print(f"Total successful registrations: {len(students)}")

while True:
    menu()
    option = int(input("Select an option: "))
    subprocess.run("cls", shell=True)
    if option == 1:
        register_student()
    elif option == 2:
        display_students(student_list)
    elif option == 3:
        print("Exiting program....")
        break
    else:
        print("Invalid Option! Please try again.")
    