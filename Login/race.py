# -*- coding:utf-8 -*-

from selenium.webdriver.support.ui import Select
import time,random
from Business import business
from Data import data


def click_race_edit(self):
    #点击赛事编辑
    driver = self.driver
    driver.find_element_by_xpath("/html/body/div[2]/aside[1]/section/ul/li[3]/ul/li[3]/a").click()
    time.sleep(5)


def edit_race_info(self):
    # 输入赛事信息
    driver = self.driver
    # 选择游戏名称
    time.sleep(2)
    Select(driver.find_element_by_id("game_id")).select_by_value("1")
    # 选择赛区
    Select(driver.find_element_by_id("zone_id")).select_by_value("1000152")
    # 输入赛事名称
    num = random.randint(1,10)
    driver.find_element_by_name("Matches[name]").send_keys(u"比利林恩%s" % num)
    #选择状态 0:未激活  1:激活
    Select(driver.find_element_by_id("status")).select_by_value("1")

def modify_race_info(self):
    #编辑赛事
    driver = self.driver
    time.sleep(2)
    #选取游戏名称
    name = business.business_edit_race(self)
    if name=="未激活":
        Select(driver.find_element_by_id("status")).select_by_value("1")
    else:
        Select(driver.find_element_by_id("status")).select_by_value("0")

def modify_race_status(self):
    #修改赛事状态，点击激活或未激活按钮
    driver = self.driver
    driver.find_element_by_xpath("//div[@class=\"col-sm-12\"]/table/tbody/tr[1]/td[6]/a[2]").click()



