class Student:
    def __init__(self, username, password, subjects=None, grade=None):
        self.username = username
        self.password = password
        self.subjects = subjects or []
        self.grade = grade

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "subjects": self.subjects,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(
            username=data['username'],
            password=data['password'],
            subjects=data.get('subjects', []),
            grade=data.get('grade')
        )