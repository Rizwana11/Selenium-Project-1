"""Importing necessary modules"""
import pytest
from selenium import webdriver
from LoginPage import LoginPage
from EmployeePage import EmployeePage
from EmployeeDetailsPage import EmployeeDetailsPage

FIRST_NAME = "Rizwana"
LAST_NAME = "Begum"

PATH = "C:/Users/Arshad/Desktop/chromedriver/chromedriver.exe"

@pytest.fixture
def driver():
    """Initializing Web Driver"""
    driver = webdriver.Chrome(PATH)
    yield driver
    driver.quit()


def test_project(driver):
    """Function for testing all functionalities"""
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    employee_page = EmployeePage(driver)
    employee_page.navigate_to_pim()
    employee_page.add_employee(FIRST_NAME, LAST_NAME)

    employee_details_page = EmployeeDetailsPage(driver)
    employee_details_page.navigate_to_employee_details()
    employee_details_page.search_employee(FIRST_NAME)
    employee_details_page.delete_employee()
