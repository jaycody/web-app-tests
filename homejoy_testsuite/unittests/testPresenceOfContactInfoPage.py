#! /usr/bin/env python

""" jstephens  -  webapp test automation for homejoy  ==> Selenium unittests

Method:
- created with SE-Builder in Firefox
- exported to python unittest version
- updated .py file to run as a standalone test case.

Test Case:
- Verify the presence of the user's Contact Information Page at www.homejoy.com
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

class testPresenceOfContactInfoPage(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_testPresenceOfContactInfoPage(self):
        success = True
        wd = self.wd
        wd.get("https://www.homejoy.com/")
        if not ("Get Your Place Cleaned" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        wd.find_element_by_link_text("BOOK APPOINTMENT").click()
        if not ("Number of hours to book" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        if not wd.find_element_by_xpath("//form[@id='home-size-form']/div/div[1]/select//option[3]").is_selected():
            wd.find_element_by_xpath("//form[@id='home-size-form']/div/div[1]/select//option[3]").click()
        if not ("100% Satisfaction Guarantee" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        wd.find_element_by_xpath("//div[@id='info-pane-person']//button[.='Next']").click()
        if not ("Enter Contact Info" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
