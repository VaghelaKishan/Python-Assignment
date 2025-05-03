# CLIUniApp

CLIUniApp is a Command-Line Interface application for managing a university student system. It supports two subsystems: **Admin** and **Student**, each with specific functionalities.

---

## 🚀 Features

### 👩‍🎓 Student
- Register a new account
- Login with credentials
- Enroll in up to 4 subjects
- Remove a subject
- Change password
- View enrolled subjects

### 👨‍💼 Admin
- Login (no registration required)
- View all students
- Remove a student
- Partition students as PASS or FAIL
- Group students by grade
- Clear all student data

---

## 📁 Project Structure

CLIUniApp/
├── app/
│ ├── controllers/
│ ├── models/
│ ├── services/
│ ├── utils/
│ └── data/
├── main.py
├── requirements.txt
└── README.md



## 💻 How to Run

1. Navigate to the project root directory:
   ```bash
   cd CLIUniApp


## Admin credentials are hardcoded as:
Username: adi
Password: 123

##  Data Storage
data/students.data
