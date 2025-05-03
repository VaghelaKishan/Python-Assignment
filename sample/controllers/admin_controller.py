from services import student_service

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. View all students")
        print("2. Remove student")
        print("3. Partition PASS/FAIL")
        print("4. Group by grade")
        print("5. Clear all data")
        print("6. Logout")
        choice = input("Choice: ")

        students = student_service.get_all_students()

        if choice == "1":
            for s in students:
                print(f"{s.username} - Grade: {s.grade} - Subjects: {s.subjects}")
        elif choice == "2":
            uname = input("Enter username to remove: ")
            students = [s for s in students if s.username != uname]
            student_service.save_students(students)
            print(f"{uname} removed.")
        elif choice == "3":
            passed = [s.username for s in students if s.grade and s.grade >= 50]
            failed = [s.username for s in students if not s.grade or s.grade < 50]
            print("PASS:", passed)
            print("FAIL:", failed)
        elif choice == "4":
            groups = {}
            for s in students:
                if s.grade is not None:
                    groups.setdefault(s.grade, []).append(s.username)
            for g, names in groups.items():
                print(f"Grade {g}: {names}")
        elif choice == "5":
            confirm = input("Type CONFIRM to delete all student data: ")
            if confirm == "CONFIRM":
                student_service.save_students([])
                print("All data cleared.")
        elif choice == "6":
            break
        else:
            print("Invalid option.")
