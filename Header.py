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


'''顶栏Logo，文字点击跳转测试'''
def Header():
    driver=webdriver.Edge()
    url="https://mail.163.com/"
    driver.get(url)
    time.sleep(2)

    state1=get_status("http://mail.163.com/html/mail_intro/")
    if(state1==200):
        driver.find_element_by_class_name("header-163logo").click()
        time.sleep(2)
        windows=driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current=driver.current_url
        if(current=="http://mail.163.com/html/mail_intro/"):
            print("Passed! - Netease Logo Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Logo_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Netease Logo Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Logo_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Oversea Mail Intro Response Failure")

    '''中文邮箱第一品牌点击'''
    time.sleep(1)
    state2=get_status("http://mail.163.com/html/mail_intro/")
    if(state2==200):
        driver.find_element_by_class_name("headerIntro").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://mail.163.com/html/mail_intro/"):
            print("Passed! - Netease Intro Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Intro_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Netease Intro Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Intro_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - 163 Mail Intro Response Failure")


    #'''顶部导航栏其余元素点击测试'''
    #企业邮箱
    time.sleep(2)
    state3 = get_status("http://qiye.163.com/")
    if (state3 == 200):
        driver.find_element_by_xpath("//div[@class='headerNav']/a[1]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "https://qiye.163.com/"):
            print("Passed! - Netease Enterprise Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Netease_Enterprise_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Netease Enterprise Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Netease_Enterprise_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - 163 Enterprise Response Failure")

    #VIP邮箱
    time.sleep(2)
    state4 = get_status("http://vip.163.com?b08abh1")
    if (state4 == 200):
        driver.find_element_by_xpath("//div[@class='headerNav']/a[2]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://vip.163.com/?b08abh1"):
            print("Passed! - VIP Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_VIP_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - VIP Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_VIP_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - VIP Mailbox Response Failure")


    #国外用户登录
    time.sleep(2)
    state5 = get_status("http://hw.mail.163.com/#163")
    if (state5 == 200):
        driver.find_element_by_xpath("//div[@class='headerNav']/a[3]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "https://hw.mail.163.com/#163"):
            print("Passed! - Oversea Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Oversea_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Oversea Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Oversea_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Oversea Mailbox Response Failure")


    #手机版
    time.sleep(2)
    state6 = get_status("http://mail.163.com/dashi/dlpro.html?from=mail13")
    if (state6 == 200):
        driver.find_element_by_xpath("//div[@class='headerNav']/a[4]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://mail.163.com/dashi/?from=mail13&gotodownload=1"):
            print("Passed! - Phone Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Phone_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Phone Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Phone_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Phone Mailbox Response Failure")

    # 电脑版
    time.sleep(2)
    state7 = get_status("http://mail.163.com/dashi/dlpro.html?from=mail1&spread=pc")
    if (state7 == 200):
        driver.find_element_by_xpath("//div[@class='headerNav']/a[5]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://mail.163.com/dashi/?from=mail1&gotodownload=1"):
            print("Passed! - PC Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_PC_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - PC Mailbox Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_PC_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - PC Mailbox Response Failure")


    #帮助
    time.sleep(2)
    state8 = get_status("http://help.mail.163.com")
    if (state8 == 200):
        driver.find_element_by_xpath("//div[@class='headerNav']/a[7]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(2)
        current = driver.current_url
        #print(current)
        if ((current.find("http://help.mail.163.com"))!=-1):
            print("Passed! - Mailbox Help Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Help_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Mailbox Help Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Help_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Mailbox Help Response Failure")

    #常见问题
    time.sleep(2)
    state9 = get_status("http://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac24ebe7a3165848018")
    if (state9 == 200):
        driver.find_element_by_xpath("//div[@class='headerNav']/a[7]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "http://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac24ebe7a3165848018"):
            print("Passed! - Mailbox Problems Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Problems_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Mailbox Problems Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Problems_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Mailbox Problems Response Failure")

    #私人助理
    time.sleep(2)
    state10 = get_status("https://v.mail.163.com/?from=logintop")
    if (state10 == 200):
        driver.find_element_by_xpath("//div[@class='headerNav']/a[8]").click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current = driver.current_url
        if (current == "https://v.mail.163.com/?from=logintop"):
            print("Passed! - Mailbox Assistant Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Passed_Assistant_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
        else:
            print("Failed! - Mailbox Assistant Click Test")
            driver.get_screenshot_as_file("D:\\Netease\\Failed_Assistant_Click.png")
            driver.close()
            driver.switch_to_window(windows[0])
    else:
        print("Failed! - Mailbox Assistant Response Failure")

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

    driver.quit()

if __name__=='__main__':
    Header()