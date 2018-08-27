import unittest2
import urllib
import urllib.request
import time
import os
import requests

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def Yanxuan():
    driver=webdriver.Edge()
    url="https://mail.163.com/"
    driver.get(url)
    time.sleep(2)

    driver.find_element_by_id("theme").click()
    time.sleep(2)
    windows=driver.window_handles
    driver.switch_to_window(windows[1])

    current=driver.current_url
    if((current.find("you.163.com/item/"))!=-1):
        print("Passed! - Netease Yanxuan Item Page Redirect")
        driver.get_screenshot_as_file("D:\\Netease\\Passed_Yanxuan.png")
        time.sleep(1)
        driver.close()
        driver.switch_to_window(windows[0])
        time.sleep(1)
    else:
        print("Failed! - Netease Yanxuan Item Page Redirect")
        driver.get_screenshot_as_file("D:\\Netease\\Failed_Yanxuan.png")
        time.sleep(1)
        driver.close()
        driver.switch_to_window(windows[0])
        time.sleep(1)

    driver.quit()

if __name__=='__main__':
    Yanxuan()