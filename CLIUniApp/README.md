# CLIUniApp - University Management System (Python CLI)

This is a command-line interface (CLI) based University Management System that allows students to register, log in, enroll in subjects, and manage their academic records. Administrators can manage students and perform advanced operations like grouping, partitioning, and clearing student records.

---

## 📁 Project Structure

CLIUniApp/
│
├── main.py
│
├── controllers/
│ ├── student_controller.py
│ └── admin_controller.py
│
├── models/
│ ├── student.py
│ ├── subject.py
│ └── database.py
│
├── services/
│ ├── admin_service.py
│ └── student_service.py
│
├── utils/
│ └── file_handler.py
│
├── data/
│ └── students.data # Auto-generated student data storage (JSON)
│
└── README.md


---

## 🧩 Features

### 👨‍🎓 Student Features
- Register with name, email, and password
- Login/logout functionality
- Enroll/drop subjects (max 4)
- View enrolled subjects with marks and grades
- Change password

### 👨‍💼 Admin Features
- View all registered students
- Remove a student by email
- Partition students into PASS/FAIL based on average marks
- Group students by grade (HD, D, C, P, F)
- Clear all student data

---

## 🛠️ Requirements

- **Python 3.10+**

---

## 🔧 Installation (For Windows)

### 1. 📥 Install Python

If Python is not installed, follow these steps:

1. Download: [Python 3.12.3 for Windows](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe)
2. Run the installer
3. ✅ Make sure to **check the box**: `Add Python 3.12 to PATH`
4. Click **Install Now**

After installation, verify by running:

```powershell
python --version


5. How to Run the App

Navigate to the project folder:
cd path\to\CLIUniApp

Run the application:
python main.py

-------------
# Notes:
Student data is saved persistently in the data/students.data file (in JSON format).

Passwords must:

Start with an uppercase letter

Contain at least 5 letters and 3 digits

Email format must be: firstname.lastname@university.com