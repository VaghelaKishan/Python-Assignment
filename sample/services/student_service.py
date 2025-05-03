from models.student import Student
from utils.file_handler import read_students, write_students

MAX_SUBJECTS = 4

def get_all_students():
    return [Student.from_dict(s) for s in read_students()]

def save_students(students):
    write_students([s.to_dict() for s in students])

def find_student(username):
    for s in get_all_students():
        if s.username == username:
            return s
    return None

def update_student(updated):
    students = get_all_students()
    for i, s in enumerate(students):
        if s.username == updated.username:
            students[i] = updated
    save_students(students)


def add_student(student):
    students = get_all_students()
    students.append(student)
    save_students(students)