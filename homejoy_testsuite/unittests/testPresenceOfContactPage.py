#! /usr/bin/env python

""" jstephens  -  webapp test automation for homejoy  ==> Selenium unittests

Method:
- created with SE-Builder in Firefox
- exported to python unittest version
- updated .py file to run as a standalone test case.

Test Case:
- Verify the presence of Homejoy's "Contact Us" page
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

class testPresenceOfContactPage(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_testPresenceOfContactPage(self):
        success = True
        wd = self.wd
        wd.get("https://www.homejoy.com/")
        time.sleep(float("1000") / 1000)
        if not ("It's simple, affordable, and convenient" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        wd.find_element_by_link_text("Contact Us").click()
        time.sleep(float("1000") / 1000)
        if not ("Contact Us" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(("Contact Us" in wd.find_element_by_tag_name("html").text))
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
