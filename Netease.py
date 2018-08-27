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
    Header()
    Yanxuan()

    username = ["zezealielie@163.com",
                "zezealielie",
                "zezealili"]

    password = ["12345678910fd",
                "12345678910fd/",
                "12345"]

    cnt = 1
    for usr in username:
        for pwd in password:
            Login(usr, pwd)

    Footer()