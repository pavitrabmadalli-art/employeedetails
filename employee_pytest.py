from employee import employee_details


def test_employee_details():
    actual = employee_details("Pavitra", "101", "BCA", "50000")

    expected = (
        "\nEmployee Details\n"
        "--------------------\n"
        "Employee Name: Pavitra\n"
        "Employee ID: 101\n"
        "Department: BCA\n"
        "Salary: 50000"
    )

    assert actual == expected