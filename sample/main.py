from controllers import student_controller, admin_controller

ADMINS = {"admin": "admin123"}

def main():
    while True:
        print("\nCLIUniApp Main Menu")
        print("1. Student Login")
        print("2. Student Registration")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_controller.login_student()
        elif choice == "2":
            student_controller.register_student()
        elif choice == "3":
            uname = input("Admin username: ")
            pw = input("Admin password: ")
            if ADMINS.get(uname) == pw:
                admin_controller.admin_menu()
            else:
                print("Invalid admin credentials.")
        elif choice == "4":
            print("Exiting CLIUniApp.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()