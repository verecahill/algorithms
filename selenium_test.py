import unittest
import HTMLTestRunner
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertEqual("Welcome to Python.org", driver.title)
        print(driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")

        driver.get("http://google.com")
        driver.back()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #unittest.main()
    HTMLTestRunner.main()
