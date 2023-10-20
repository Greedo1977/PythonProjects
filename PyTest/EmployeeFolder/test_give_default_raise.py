import pytest
from EmployeeClass import Employee


@pytest.fixture
def employee():
    employee_ = Employee('Madhu', 'Mepani', 25000)
    return employee_


def test_give_default_raise(employee):
    employee.give_raise()
    assert 30000 == employee.salary


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert 35000 == employee.salary