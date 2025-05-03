import json, os
from models.student import Student

class Database:
    PATH = "data/students.data"

    def __init__(self):
        if not os.path.exists(self.PATH):
            with open(self.PATH, 'w') as f:
                json.dump([], f)

    def load_students(self):
        with open(self.PATH, 'r') as f:
            return [Student.from_dict(s) for s in json.load(f)]

    def save_students(self, students):
        with open(self.PATH, 'w') as f:
            json.dump([s.to_dict() for s in students], f, indent=4)

    def clear_students(self):
        with open(self.PATH, 'w') as f:
            json.dump([], f)