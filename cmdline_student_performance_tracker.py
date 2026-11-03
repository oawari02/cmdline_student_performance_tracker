import json
students = {}

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter name: ")
    try:
        math = int(input("Enter Math score: "))
        science = int(input("Enter Science score: "))
        english = int(input("Enter English score: "))

        students[student_id] = {
            "Name": name,
            "Scores": [math, science, english]
        }

    except ValueError:
        print("Error: Scores must be numbers!")

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    else:
        return "F"

def search_student():
    search_id = input("Enter ID: ")
    if search_id in students:
        student = students[search_id]
        total = sum(student["Scores"])
        average = total / 3
        grade = calculate_grade(average)
        print(f"Name: {student['Name']}, Total: {total}, Average: {average:.2f}, Grade: {grade}")
    else:
        print("Error: Student not found!")

def update_student():
    update_id = input("Enter ID: ")
    if update_id in students:
        try:
            math = int(input("Enter Math score: "))
            science = int(input("Enter Science score: "))
            english = int(input("Enter English score: "))
            students[update_id]["Scores"] = [math, science, english]
        except ValueError:
            print("Error: Scores must be numbers!")
    else:
        print("Error: Student not found!")

def delete_student():
    delete_id = input("Enter ID: ")
    if delete_id in students:
        del students[delete_id]
        print("Student deleted successfully!")
    else:
        print("Error: Student not found!")

def save_data():
    try:
        with open("students.json", "w") as file:
            json.dump(students, file)
    except (OSError, TypeError):
        print("Error saving data.")

def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except (OSError, json.JSONDecodeError):
        pass

load_data()

while True:
    print("\n1. Add student")
    print("2. Search student")
    print("3. Update student")
    print("4. Delete student")
    print("5. View students")
    print("6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print(students)
    elif choice == "6":
        save_data()
        break
    else:
        print("Invalid option.")