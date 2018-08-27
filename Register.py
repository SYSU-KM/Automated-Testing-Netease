import unittest2
import urllib
import urllib.request
import time
import os
import requests

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def get_status(url):
    res=urllib.request.urlopen(url)
    page_status=res.getcode()
    return page_status

def Register():
    driver = webdriver.Edge()
    url = "https://mail.163.com/"
    driver.get(url)
    time.sleep(2)

    state1 = get_status("http://reg.email.163.com/unireg/call.do?cmd=register.entrance&from=163mail_right")
    if (state1 == 200):
        driver.find_element_by_class_name("header-163logo").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://reg.email.163.com/unireg/call.do?cmd=register.entrance&from=163mail_right"):
            print("Passed! - Register Page Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Register_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Register Page Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Register_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Register Page Response Failure")

if __name__=='__main__':
    Register()