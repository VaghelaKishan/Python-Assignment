from utils.file_handler import read_students, write_students
from models.student import Student


def get_all_students():
    return [Student.from_dict(s) for s in read_students()]


def save_all_students(students):
    write_students([s.to_dict() for s in students])


def remove_student(username):
    students = get_all_students()
    students = [s for s in students if s.username != username]
    save_all_students(students)
    return True


def partition_pass_fail():
    students = get_all_students()
    passed = [s for s in students if s.grade is not None and s.grade >= 50]
    failed = [s for s in students if s.grade is None or s.grade < 50]
    return passed, failed


def group_by_grade():
    students = get_all_students()
    grouped = {}
    for s in students:
        if s.grade is not None:
            grouped.setdefault(s.grade, []).append(s)
    return grouped


def clear_all_data():
    write_students([])
