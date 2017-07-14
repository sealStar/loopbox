# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://test.zhihuiup.com/"
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        self.driver.get(self.base_url)
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]/img').click()
        time.sleep(2)
        self.driver.find_element_by_id('mobile').send_keys('15021794801')
        self.driver.find_element_by_id('psd').send_keys('abc123')
        self.driver.find_element_by_id('securityCode2').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="rightNow"]').click()
        print(self.driver.title)
        time.sleep(3)
        title=self.driver.title
        self.assertEqual(title,u'智仟汇-场景式售卖智能设备电商平台')
    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
        unittest.main()
