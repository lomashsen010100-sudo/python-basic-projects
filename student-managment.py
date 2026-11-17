students = []
password = "12345"


# Load students from file
def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, course = line.strip().split(",")
                students.append({
                    "name": name,
                    "roll_number": int(roll),
                    "course": course
                })
    except FileNotFoundError:
        pass


# Save students
def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(
                f"{student['name']},"
                f"{student['roll_number']},"
                f"{student['course']}\n"
            )


# Add student
def add_student():
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    course = input("Enter course: ")

    for student in students:
        if student["roll_number"] == roll:
            print("Roll number already exists!")
            return

    students.append({
        "name": name,
        "roll_number": roll,
        "course": course
    })

    save_students()
    print("Student Added Successfully!")


# Show students
def show_student():
    if not students:
        print("No students found!")
        return

    for student in students:
        print(student)


# Search student
def search_student():
    roll = int(input("Enter roll number: "))

    for student in students:
        if student["roll_number"] == roll:
            print(student)
            return

    print("Student Not Found!")


# Delete student
def delete_student():
    roll = int(input("Enter roll number: "))

    for student in students:
        if student["roll_number"] == roll:
            students.remove(student)
            save_students()
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


# Login
while True:
    user = input("Enter password: ")

    if user == password:
        print("Login Successful!")
        break
    else:
        print("Invalid Password!")


# Load saved data
load_students()


# Main Menu
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")