from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController

def university_menu():
    while True:
        print("\n--- University System Menu ---")
        print("(A) Admin")
        print("(S) Student")
        print("(X) Exit")
        choice = input("Choose an option: ").lower()

        if choice == 'a':
            AdminController().admin_menu()
        elif choice == 's':
            StudentController().student_menu()
        elif choice == 'x':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    university_menu()