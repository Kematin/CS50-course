import os
import pathlib
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Finds the Uniform Resourse Identifier of a file
def file_url(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Open local file in selenium
def open_page() -> webdriver.Chrome:
    url = file_url("selenium.html")
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

# Use Selenium for get info about website
def main(driver):
    print(driver.title)
    print(driver.page_source)

    increase = driver.find_element(By.ID, "increase")
    decrease = driver.find_element(By.ID, "decrease")

    for _ in range(20):
        sleep(0.2)
        increase.click()
    decrease.click()


class WebpageTest(unittest.TestCase):
    def test_title(self):
        """Test for make sure title is correct"""
        driver = open_page()
        self.assertEqual(driver.title, "Selenium Test")

    def test_increase(self):
        """Test for check workability of increase button"""
        driver = open_page()
        increase = driver.find_element(By.ID, "increase")
        increase.click()

        num = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(num.text, "1")

    def test_decrease(self):
        """Test for check workability of decrease button"""
        driver = open_page()
        decrease = driver.find_element(By.ID, "decrease")
        decrease.click()

        num = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(num.text, "-1")

    def test_multiple_increase(self):
        """Test for make sure header updated to 3 after 3 clicks of increase button"""
        driver = open_page()
        increase = driver.find_element(By.ID, "increase")

        for _ in range(3):
            increase.click()

        num = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(num.text, "3")


if __name__ == "__main__":
    unittest.main()
