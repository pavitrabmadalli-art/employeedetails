import sys


def employee_details(name, employee_id, department, salary):
    return (
        "\nEmployee Details\n"
        "--------------------\n"
        f"Employee Name: {name}\n"
        f"Employee ID: {employee_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )


if __name__ == "__main__":
    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")

    print(employee_details(name, employee_id, department, salary))