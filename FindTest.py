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

def test():
    driver=webdriver.Edge()
    url="https://mail.163.com/"
    driver.get(url)
    time.sleep(2)
#反馈
    time.sleep(2)
    state11 = get_status("http://help.mail.163.com/newfeedback.do?m=add")
    if (state11 == 200):
        driver.find_element_by_xpath("//div[@class='headerNav']/a[9]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        driver.switch_to_alert().accept()
        time.sleep(1)
        current = driver.current_url
        if (current == "http://help.mail.163.com/newfeedback.do?m=add"):
            print("Passed! - Mailbox Feedback Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Feedback_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Mailbox Feedback Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Feedback_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Mailbox Feedback Response Failure")

if __name__=='__main__':
    test()