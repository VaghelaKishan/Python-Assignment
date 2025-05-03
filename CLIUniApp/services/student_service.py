import os, json
from models.student import Student
from models.database import Database
from utils.file_handler import validate_email, validate_password

class StudentService:
    def __init__(self):
        self.db = Database()
        self.students = self.db.load_students()
        self.logged_in = None

    def register(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        if not validate_email(email):
            print("Invalid email.")
            return
        password = input("Enter password: ")
        if not validate_password(password):
            print("Invalid password.")
            return
        if any(s.email == email for s in self.students):
            print("Email already registered.")
            return
        student = Student(name, email, password)
        self.students.append(student)
        self.db.save_students(self.students)
        print("Registration successful.")

    def login(self):
        email = input("Email: ")
        password = input("Password: ")
        for s in self.students:
            if s.email == email and s.password == password:
                self.logged_in = s
                print(f"Welcome {s.name}!")
                self.subject_menu()
                return
        print("Login failed.")

    def subject_menu(self):
        while self.logged_in:
            print("\n(1) Enrol\n(2) Drop\n(3) View\n(4) Change Password\n(x) Logout")
            choice = input("Enter choice: ").lower()
            match choice:
                case '1':
                    if len(self.logged_in.subjects) >= 4:
                        print("Max subjects reached.")
                        return
                    sub = input("Enter subject name: ")
                    self.logged_in.enrol_subject(sub)
                case '2':
                    sub = input("Subject to drop: ")
                    self.logged_in.drop_subject(sub)
                case '3':
                    print("\nSubjects:")
                    for sub in self.logged_in.subjects:
                        print(f"{sub.name} - {sub.mark} ({sub.grade})")
                    print(f"Average: {self.logged_in.average_mark():.2f}, Status: {'PASS' if self.logged_in.has_passed() else 'FAIL'}")
                case '4':
                    new_pass = input("New password: ")
                    if validate_password(new_pass):
                        self.logged_in.change_password(new_pass)
                    else:
                        print("Invalid format.")
                case 'x':
                    self.db.save_students(self.students)
                    self.logged_in = None