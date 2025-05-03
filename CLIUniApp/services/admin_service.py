from models.database import Database

class AdminService:
    def __init__(self):
        self.db = Database()
        self.students = self.db.load_students()

    def remove_student(self):
        email = input("Email to remove: ")
        original = len(self.students)
        self.students = [s for s in self.students if s.email != email]
        if len(self.students) < original:
            self.db.save_students(self.students)
            print("Removed.")
        else:
            print("Not found.")

    def partition_pass_fail(self):
        passed = [s for s in self.students if s.has_passed()]
        failed = [s for s in self.students if not s.has_passed()]
        print("\nPASS:")
        for s in passed:
            print(f"{s.name} - {s.average_mark():.2f}")
        print("\nFAIL:")
        for s in failed:
            print(f"{s.name} - {s.average_mark():.2f}")

    def group_by_grade(self):
        groups = {'HD': [], 'D': [], 'C': [], 'P': [], 'F': []}
        for s in self.students:
            for sub in s.subjects:
                groups[sub.grade].append((s.name, sub.name, sub.mark))
        for grade, lst in groups.items():
            print(f"\n{grade}:")
            for entry in lst:
                print(f"{entry[0]} - {entry[1]} ({entry[2]})")

    def view_all_students(self):
        for s in self.students:
            print(f"{s.name} ({s.email}) - {len(s.subjects)} subjects")

    def clear_all_students(self):
        if input("Clear ALL students? (yes/no): ").lower() == 'yes':
            self.db.clear_students()
            print("Cleared.")