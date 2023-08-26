"""Importing necessary modules"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeeDetailsPage:
    """class for handling other employee operations"""
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_employee_details(self):
        """navigating to the component"""
        employee_details_tab = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Employee List']" )))
        time.sleep(2)
        employee_details_tab.click()

    def search_employee(self, first_name):
        """searching for the relevant employee"""
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...'])[1]")))
        search_input.send_keys(first_name)
        time.sleep(2)
        search_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Search']")))
        search_button.click()

    def edit_employee(self):
        """editing employee details"""
        edit_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@role='row'])[2]")))
        time.sleep(2)
        edit_button.click()

    def delete_employee(self):
        """deleting the employee record"""
        delete_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[5]")))
        delete_button.click()
        time.sleep(2)
        confirm_delete_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes, Delete']")))
        confirm_delete_button.click()