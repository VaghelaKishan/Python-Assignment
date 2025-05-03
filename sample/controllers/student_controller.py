from models.student import Student
from services import student_service

def register_student():
    username = input("Choose username: ")
    if student_service.find_student(username):
        print("Username already exists.")
        return
    password = input("Choose password: ")
    student = Student(username, password)
    student_service.add_student(student)
    print("Registration successful.")

def login_student():
    username = input("Username: ")
    password = input("Password: ")
    student = student_service.find_student(username)
    if student and student.password == password:
        student_menu(student)
    else:
        print("Invalid credentials.")

def student_menu(student):
    while True:
        print(f"\nWelcome {student.username}, choose an option:")
        print("1. Enroll in subject")
        print("2. Remove subject")
        print("3. View subjects")
        print("4. Change password")
        print("5. Logout")
        choice = input("Choice: ")

        if choice == "1":
            if len(student.subjects) >= 4:
                print("Max subjects reached.")
            else:
                subject = input("Enter subject: ")
                if subject in student.subjects:
                    print("Already enrolled.")
                else:
                    student.subjects.append(subject)
                    student_service.update_student(student)
                    print(f"Enrolled in {subject}.")
        elif choice == "2":
            subject = input("Enter subject to remove: ")
            if subject in student.subjects:
                student.subjects.remove(subject)
                student_service.update_student(student)
                print(f"Removed {subject}.")
            else:
                print("Subject not found.")
        elif choice == "3":
            print("Subjects:", student.subjects)
        elif choice == "4":
            new_pw = input("Enter new password: ")
            student.password = new_pw
            student_service.update_student(student)
            print("Password updated.")
        elif choice == "5":
            break
        else:
            print("Invalid option.")