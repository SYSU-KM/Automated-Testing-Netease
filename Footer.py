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


'''底栏链接点击跳转测试'''
def Footer():
    driver=webdriver.Edge()
    url="https://mail.163.com/"
    driver.get(url)
    time.sleep(2)

    state1=get_status("http://www.163.com/")
    if(state1==200):
        driver.find_element_by_id("footer163Logo").click()
        time.sleep(2)
        windows=driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current=driver.current_url
        if(current=="https://www.163.com/"):
            print("Passed! - Footer Netease Logo Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Footer_Logo_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Footer Netease Logo Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Footer_Logo_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Netease Website Response Failure")



    #'''底部导航栏其余元素点击测试'''
    #网易首页
    time.sleep(2)
    state3 = get_status("http://www.163.com/")
    if (state3 == 200):
        driver.find_element_by_xpath("//div[@class='footer-nav']/a[2]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "https://www.163.com/"):
            print("Passed! - Netease Homepage Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Netease_Homepage_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Netease Homepage Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Netease_Homepage_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Netease Homepage Response Failure")

    #关于网易免费邮
    time.sleep(2)
    state4 = get_status("http://mail.163.com/html/mail_intro")
    if (state4 == 200):
        driver.find_element_by_xpath("//div[@class='footer-nav']/a[3]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://mail.163.com/html/mail_intro/"):
            print("Passed! - About 163 Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_About_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - About 163 Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_About_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - About 163 Mailbox Response Failure")


    #网易智造
    time.sleep(2)
    state5 = get_status("https://3c.163.com/?from=pdengluyetoutu1")
    if (state5 == 200):
        driver.find_element_by_xpath("//div[@class='footer-nav']/a[4]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "https://3c.163.com/?from=pdengluyetoutu1"):
            print("Passed! - Netease Made Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Made_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Netease Made Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Made_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Netease Made Response Failure")


    #网易.有钱
    time.sleep(2)
    state6 = get_status("http://qian.163.com")
    if (state6 == 200):
        driver.find_element_by_xpath("//div[@class='footer-nav']/a[5]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://qian.163.com/"):
            print("Passed! - Netease Money Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Money_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Netease Money Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Money_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Netease Money Response Failure")

    # 网易严选
    time.sleep(2)
    state7 = get_status("http://you.163.com/")
    if (state7 == 200):
        driver.find_element_by_xpath("//div[@class='footer-nav']/a[6]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://you.163.com/"):
            print("Passed! - Netease Select Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Select_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Netease Select Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Select_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Netease Select Response Failure")


    #网易一起拼
    time.sleep(2)
    state8 = get_status("http://pin.mail.163.com?utm_source=maillogin&utm_medium=163")
    if (state8 == 200):
        driver.find_element_by_xpath("//div[@class='footer-nav']/a[7]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(2)
        current = driver.current_url
        #print(current)
        if (current=="http://pin.mail.163.com/?utm_source=maillogin&utm_medium=163"):
            print("Passed! - Netease Pin Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Pin_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Netease Pin Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Pin_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Netease Pin Response Failure")

    #政府公益热线
    time.sleep(2)
    state9 = get_status("http://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2842e8b50ff6a4ebb")
    if (state9 == 200):
        driver.find_element_by_xpath("//div[@class='footer-nav']/a[8]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2842e8b50ff6a4ebb"):
            print("Passed! - Government Charity Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Charity_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Government Charity Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Charity_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Government Charity Response Failure")

    #邮箱黄页
    time.sleep(2)
    state10 = get_status("http://mail.163.com/html/160513_yellow/")
    if (state10 == 200):
        driver.find_element_by_xpath("//div[@class='footer-nav']/a[9]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://mail.163.com/html/160513_yellow/#"):
            print("Passed! - Netease Yellow Page Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Yellow_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Netease Yellow Page Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Yellow_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Netease Yellow Page Response Failure")

    #证书
    time.sleep(2)
    state11 = get_status("https://mimg.127.net/p/icp.jpg")
    if (state11 == 200):
        driver.find_element_by_class_name("icp").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "https://mimg.127.net/p/icp.jpg"):
            print("Passed! - Zhengshu Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_zhangshu_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Zhangehu Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_zhengshu_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Zhengshu Response Failure")

    driver.quit()

if __name__=='__main__':
    Footer()