import employee_info

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(25, 35)

    test_result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                   {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    
    assert (test_result == result)

def test_calculate_average_salary():
    average = employee_info.calculate_average_salary()

    test_average = 361000 / 6

    assert (test_average == average)

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Sales")

    test_result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                   {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    
    assert (test_result == result)
