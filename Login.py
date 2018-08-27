import unittest2
import urllib
import urllib.request
import time
import os
import requests

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def Login(username,password):
    global cnt
    driver = webdriver.Edge()
    url = "https://mail.163.com/"
    driver.get(url)
    time.sleep(2)

    element=driver.find_element_by_id("lbApp")
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(2)
    driver.get_screenshot_as_file("D:\\Netease\\Passed_QR_Code_Login.png")

    element=driver.find_element_by_id("lbNormal")
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(2)
    driver.get_screenshot_as_file("D:\\Netease\\Passed_Account_Login.png")

    driver.switch_to.frame("x-URS-iframe")
    driver.find_element_by_class_name("j-inputtext dlemail").clear()
    driver.find_element_by_class_name("j-inputtext dlpwd").clear()

    driver.find_element_by_class_name("j-inputtext dlemail").send_keys(username)
    driver.find_element_by_class_name("j-inputtext dlpwd").send_keys(password)

    driver.find_element_by_id("dologin").click()
    time.sleep(2)

    current=driver.current_url
    #登录成功
    if((current.find("main.jsp"))!=-1):
        if(username=="zezealielie@163.com"):
            if(username=="zezealielie"):
                if(password=="12345678910fd/"):
                    print("Passed! - Login Test Case %r" %cnt)
                    driver.get_screenshot_as_file("D:\\Netease\\Passed_Login_Test_Case_%r.png" %cnt)
                    cnt=cnt+1
                else:
                    print("Failed! - Not Matched Account and Password-Login Test Case %r" % cnt)
                    driver.get_screenshot_as_file("D:\\Netease\\Failed_Login_Test_Case_%r.png" % cnt)
                    cnt = cnt + 1
        else:
            print("Failed! - Not Matched Account and Password-Login Test Case %r" % cnt)
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Login_Test_Case_%r.png" % cnt)
            cnt = cnt + 1
    else:
        print("Passed! - Login Test Case %r" % cnt)
        driver.get_screenshot_as_file("D:\\Netease\\Passed_Login_Test_Case_%r.png" % cnt)
        cnt = cnt + 1
    driver.quit()

if __name__=='__main__':
    username=["zezealielie@163.com",
              "zezealielie",
              "zezealili"]

    password=["12345678910fd",
              "12345678910fd/",
              "12345"]

    cnt=1
    for usr in username:
        for pwd in password:
            Login(usr,pwd)