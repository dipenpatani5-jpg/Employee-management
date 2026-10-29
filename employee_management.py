
class Employee:
    def __init__(self, employee_id=None, name="Unknown",
                 age=0, salary=0.0):
        # Private attributes (Encapsulation)
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    # Getter for employee ID
    def get_employee_id(self):
        return self.__employee_id

    # Setter for employee ID
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative!")

    # Display employee details
    def display(self):
        print("\n--- Employee Details ---")
        print("Employee ID:", self.__employee_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.__salary)

    # Destructor
    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    # Method Overriding
    def display(self):
        super().display()
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, employee_id, name, age, salary,
                 programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        super().display()
        print("Programming Language:", self.programming_language)


# Employee Management System
employees = []


def add_employee():
    print("\n1. General Employee")
    print("2. Manager")
    print("3. Developer")

    choice = input("Choose employee type: ")

    try:
        employee_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))

        if age < 0 or salary < 0:
            print("Age and salary cannot be negative.")
            return

        if any(e.get_employee_id() == employee_id for e in employees):
            print("Employee ID already exists!")
            return

        if choice == "1":
            employee = Employee(employee_id, name, age, salary)

        elif choice == "2":
            department = input("Enter Department: ")
            employee = Manager(
                employee_id, name, age, salary, department
            )

        elif choice == "3":
            language = input("Enter Programming Language: ")
            employee = Developer(
                employee_id, name, age, salary, language
            )

        else:
            print("Invalid employee type!")
            return

        employees.append(employee)
        print("Employee added successfully!")

    except ValueError:
        print("Please enter valid numeric values.")


def view_employees():
    if not employees:
        print("\nNo employees found.")
        return

    for employee in employees:
        employee.display()


def search_employee():
    try:
        employee_id = int(input("Enter Employee ID to search: "))

        for employee in employees:
            if employee.get_employee_id() == employee_id:
                employee.display()
                return

        print("Employee not found.")

    except ValueError:
        print("Employee ID must be a number.")


def update_employee():
    try:
        employee_id = int(input("Enter Employee ID to update: "))

        for employee in employees:
            if employee.get_employee_id() == employee_id:
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Salary")

                choice = input("Choose field: ")

                if choice == "1":
                    employee.name = input("Enter new name: ")

                elif choice == "2":
                    age = int(input("Enter new age: "))
                    if age < 0:
                        print("Age cannot be negative.")
                        return
                    employee.age = age

                elif choice == "3":
                    salary = float(input("Enter new salary: "))
                    employee.set_salary(salary)

                else:
                    print("Invalid choice!")
                    return

                print("Employee updated successfully!")
                return

        print("Employee not found.")

    except ValueError:
        print("Please enter valid numeric values.")


def remove_employee():
    try:
        employee_id = int(input("Enter Employee ID to remove: "))

        for employee in employees:
            if employee.get_employee_id() == employee_id:
                employees.remove(employee)
                print("Employee removed successfully!")
                return

        print("Employee not found.")

    except ValueError:
        print("Employee ID must be a number.")


def check_oop():
    print("\n--- OOP Verification ---")
    print("Is Manager a subclass of Employee?",
          issubclass(Manager, Employee))
    print("Is Developer a subclass of Employee?",
          issubclass(Developer, Employee))


def main():
    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Remove Employee")
        print("6. Check Inheritance")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            remove_employee()
        elif choice == "6":
            check_oop()
        elif choice == "7":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

