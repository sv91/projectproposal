from selenium import webdriver
from testslocal import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class ConnectTestCase(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
        
	def tearDown(self):
		self.browser.close()

	def testLogin(self):
		driver = self.browser
		driver.get('https://localhost:8000/formular/')
		element = WebDriverWait(driver, 10).until(EC.title_contains('OpenID'))
		sub = driver.find_element_by_id('j_username').send_keys(id)
		driver.find_element_by_id('j_password').send_keys(password)
		driver.find_element_by_xpath("html/body/div/div/div/form/div/input").click()
		element = WebDriverWait(driver, 10).until(EC.title_contains('HPC'))
		self.assertIn('HPC', driver.title)
	

if __name__ == '__main__':
	unittest.main(verbosity=2)
		
