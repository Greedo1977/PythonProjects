import pytest
from Company import Company


@pytest.fixture
def company():
    company = Company('HSBC', 'Banking', 100_000)
    return company

def test_company_default(company):
    company.change_employees()
    assert 110000 == company.employees


def test_company_custom(company):
    company.change_employees(200000)
    assert 300000 == company.employees
