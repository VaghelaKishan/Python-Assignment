import json
import os

DATA_FILE = "data/students.data"

def read_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_students(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)