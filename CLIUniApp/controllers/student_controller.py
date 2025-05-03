from services.student_service import StudentService

class StudentController:
    def __init__(self):
        self.service = StudentService()

    def student_menu(self):
        while True:
            print("\n(L) Login\n(R) Register\n(X) Exit")
            choice = input("Enter choice: ").lower()
            match choice:
                case 'l': self.service.login()
                case 'r': self.service.register()
                case 'x': break
                case _: print("Invalid option.")