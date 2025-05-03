import random

class Subject:
    def __init__(self, name):
        self.id = f"{random.randint(1,999):03d}"
        self.name = name
        self.mark = random.randint(25, 100)
        self.grade = self.get_grade()

    def get_grade(self):
        if self.mark >= 85: return 'HD'
        if self.mark >= 75: return 'D'
        if self.mark >= 65: return 'C'
        if self.mark >= 50: return 'P'
        return 'F'

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'mark': self.mark, 'grade': self.grade}

    @staticmethod
    def from_dict(data):
        s = Subject(data['name'])
        s.id = data['id']
        s.mark = data['mark']
        s.grade = data['grade']
        return s