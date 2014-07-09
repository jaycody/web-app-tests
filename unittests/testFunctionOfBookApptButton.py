#! /usr/bin/env python

""" jstephens  -  webapp test automation  ==> Selenium unittests

Method:
- created with SE-Builder in Firefox
- exported to python unittest version
- updated .py file to run as a standalone test case.

Test Case:
- Verify the presence and functionality of the Book Appointment Button
"""


# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class testFunctionOfBookApptButton(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_testFunctionOfBookApptButton(self):
        success = True
        wd = self.wd
        wd.get("https://www.homejoy.com/")
        time.sleep(float("1000") / 1000)
        if wd.title != "Homejoy":
            success = False
            print("verifyTitle failed")
        wd.find_element_by_link_text("BOOK APPOINTMENT").click()
        time.sleep(float("1000") / 1000)
        if not ("Tell us about your home!" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
