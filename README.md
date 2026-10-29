# Employee Management System | Python OOP

## 📌 Project Overview

The **Employee Management System** is a menu-driven Python application developed to demonstrate Object-Oriented Programming (OOP) concepts. It allows users to add, view, search, update, and remove employee records while managing different employee roles, such as Managers and Developers.

This project focuses on understanding classes, objects, inheritance, encapsulation, method overriding, and other fundamental Python OOP concepts.

## 🎯 Objectives

- Implement Object-Oriented Programming concepts in Python.
- Manage employee information using classes and objects.
- Demonstrate inheritance and method overriding.
- Protect sensitive attributes using encapsulation.
- Use constructors, destructors, getters, and setters.
- Create a simple menu-driven user interface.

## ✨ Features

- **Add Employee:** Add General Employees, Managers, and Developers.
- **View Employees:** Display all registered employees and their details.
- **Search Employee:** Find an employee using their unique ID.
- **Update Employee:** Modify employee name, age, or salary.
- **Remove Employee:** Delete an employee record.
- **Duplicate ID Validation:** Prevent adding employees with an existing ID.
- **Inheritance Verification:** Check whether Manager and Developer are subclasses of Employee.
- **Menu-Driven Interface:** Navigate through the application using simple numbered options.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Object-Oriented Programming (OOP)
- **Editor:** Visual Studio Code (VS Code)
- **Version Control:** Git and GitHub

## 📂 Project Structure

```text
OOP-Wrapper/
│
├── employee_management.py
└── README.md
```

## 🧠 OOP Concepts Implemented

| Concept | Description |
|---|---|
| Classes and Objects | Models employees and their roles. |
| Constructor (`__init__`) | Initializes employee attributes. |
| Destructor (`__del__`) | Demonstrates the destructor method. |
| Encapsulation | Keeps employee ID and salary as private attributes. |
| Getter and Setter Methods | Access and update private attributes. |
| Inheritance | Manager and Developer inherit from Employee. |
| Method Overriding | Child classes implement their own `display()` methods. |
| Constructor Flexibility | Default arguments allow different ways to create Employee objects. |
| `super()` | Calls parent-class methods and constructors. |
| `issubclass()` | Verifies inheritance relationships. |
| `self` | Refers to the current object instance. |

## ⚙️ Installation and Setup

### Prerequisites

Install Python 3 on your computer.

Check whether Python is installed:

```bash
python --version
```

### Steps to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/OOP-Wrapper.git
   ```

2. Open the project folder:

   ```bash
   cd OOP-Wrapper
   ```

3. Run the Python program:

   ```bash
   python employee_management.py
   ```

**Note:** Replace `YOUR-USERNAME` with your actual GitHub username.

## 🖥️ Application Menu

```text
===== EMPLOYEE MANAGEMENT SYSTEM =====

1. Add Employee
2. View All Employees
3. Search Employee
4. Update Employee
5. Remove Employee
6. Check Inheritance
7. Exit

Enter your choice:
```

## 👨‍💻 Employee Roles

### 1. Employee

The base class contains common attributes:

- Employee ID
- Name
- Age
- Salary

### 2. Manager

The Manager class inherits from Employee and includes an additional attribute:

- Department (e.g., HR, Finance)

### 3. Developer

The Developer class inherits from Employee and includes an additional attribute:

- Programming Language (e.g., Python, Java)

## 🔐 Data Handling

The employee ID and salary are encapsulated using private attributes. Getter and setter methods provide controlled access to these attributes.

**Storage limitation:** Employee records are stored in a Python list during program execution. Data is not permanently saved, so records are lost when the application exits.

## 🚀 Future Improvements

- Store employee records in a database such as MySQL or SQLite.
- Add permanent file-based storage.
- Introduce employee login and authentication.
- Add department-specific salary reports.
- Develop a graphical user interface (GUI).
- Improve input validation and error handling.

## 🎓 Learning Outcomes

Through this project, I practiced Python OOP concepts, including encapsulation, inheritance, method overriding, constructor flexibility, and the use of `super()` and `issubclass()`.

The project provides a foundation for developing more advanced employee management applications.

## 👤 Author

**Your Name**

- GitHub: [YOUR-USERNAME](https://github.com/YOUR-USERNAME)

## 📄 License

This project is intended for educational and learning purposes. You may adapt it for personal practice and further development.
