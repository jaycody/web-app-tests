#! /usr/bin/env python

"""jstephens - 2014 july ==> prototype test case: verify login

Requirements:
- Member Account
"""


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class loginTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def testLogin(self):
		driver = self.driver
		driver.get("https://www.homejoy.com")

		# Verify presence of website before test starts
		self.assertIn("Homejoy", driver.title)

		# Verify Login when 'Log In' button is pushed

		#verify absence of login error message
		#"Incorrect email and password combination."


	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":	
	unittest.main()