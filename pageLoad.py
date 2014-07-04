#! /usr/bin/env python

"""jstephens - 2014 july ==> prototype test case: verify main page load

"""


import unittest
from selenium import webdriver



class pageLoadTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()

	def testPageLoad(self):
		driver = self.driver
		driver.get("https://www.homejoy.com")
		self.assertIn("Homejoy", driver.title)

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()

