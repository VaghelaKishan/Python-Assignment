import random
from models.subject import Subject

class Student:
    def __init__(self, name, email, password):
        self.id = f"{random.randint(1,999999):06d}"
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    def enrol_subject(self, name):
        self.subjects.append(Subject(name))

    def drop_subject(self, name):
        self.subjects = [s for s in self.subjects if s.name.lower() != name.lower()]

    def change_password(self, new_password):
        self.password = new_password

    def average_mark(self):
        return sum(s.mark for s in self.subjects) / len(self.subjects) if self.subjects else 0

    def has_passed(self):
        return self.average_mark() >= 50

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'subjects': [s.to_dict() for s in self.subjects]
        }

    @staticmethod
    def from_dict(data):
        student = Student(data['name'], data['email'], data['password'])
        student.id = data['id']
        student.subjects = [Subject.from_dict(s) for s in data['subjects']]
        return student