from services.admin_service import AdminService

class AdminController:
    def __init__(self):
        self.service = AdminService()

    def admin_menu(self):
        while True:
            print("\n--- Admin System Menu ---")
            print("(1) Remove a Student")
            print("(2) Partition PASS/FAIL Students")
            print("(3) Group Students by Grade")
            print("(4) View All Students")
            print("(5) Clear All Students")
            print("(x) Exit Admin Menu")
            choice = input("Choose an option: ").lower()

            match choice:
                case '1': self.service.remove_student()
                case '2': self.service.partition_pass_fail()
                case '3': self.service.group_by_grade()
                case '4': self.service.view_all_students()
                case '5': self.service.clear_all_students()
                case 'x': print("Exiting Admin Menu..."); break
                case _: print("Invalid option. Try again.")