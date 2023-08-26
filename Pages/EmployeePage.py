"""Importing necessary modules"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeePage:
    """class for handling base employee operations"""
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_pim(self):
        """navigating to the component"""
        pim_button = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]')))
        time.sleep(3)
        pim_button.click()

    def add_employee(self, first_name, last_name):
        """adding the employee"""
        add_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']")))
        add_button.click()
        first_name_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='First Name']")))
        time.sleep(1)
        first_name_field.send_keys(first_name)
        last_name_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Last Name']")))
        time.sleep(2)
        last_name_field.send_keys(last_name)
        save_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        save_button.click()
        
        
        
        