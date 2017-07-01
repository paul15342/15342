# -*- coding:utf-8 -*-

from selenium.webdriver.support.ui import Select
import time




def click_race_zone(self):  #赛区编辑
    driver = self.driver
    #点击赛区编辑
    driver.find_element_by_xpath("//a[text()=\"赛区编辑\"]").click()
    time.sleep(2)


def bulid_new_zone(self):
    driver = self.driver
    time.sleep(2)
    driver.find_element_by_name("Zone[name]").send_keys("test_01")
    #输入赛区描述
    driver.find_element_by_name("Zone[cdesc]").send_keys(u"自动化测试")
    #输入状态
    Select(driver.find_element_by_name("Zone[status]")).select_by_value("0")

def modify_zone(self):
    # 修改赛区名称
    driver = self.driver
    driver.find_element_by_id("edit_btn").click()    # 点击编辑
    time.sleep(2)
    A = driver.find_element_by_name("Zone[cdesc]")   # 点位到赛区描述
    A.clear()
    A.send_keys(u"修改名称")                         # 输入要修改成的名称








