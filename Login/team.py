# -*- coding:utf-8 -*-

from selenium.webdriver.support.ui import Select
import time,random

def click_team(self):
    #点击战队编辑
    driver = self.driver
    time.sleep(2)
    driver.find_element_by_xpath("//a[text()=\"战队编辑\"]").click()

def team_info(self):
    #输入战队信息
    driver = self.driver
    time.sleep(5)
    Select(driver.find_element_by_name("Team[game_id]")).select_by_value("1")
    time.sleep(0.5)
    Select(driver.find_element_by_name("Team[zone_id]")).select_by_visible_text(u"欧美赛区")
    time.sleep(0.5)
    num = random.randint(1,100)
    driver.find_element_by_name("Team[name]").send_keys("MTMT {}".format(num))
    driver.find_element_by_xpath("//div[@id=\"logo_div\"]/div[1]/div[8]").click()


def modify_team_info(self):
    # 修改战队名称
    driver = self.driver
    driver.find_element_by_id("edit_btn").click()   #点击编辑
    time.sleep(2)
    A = driver.find_element_by_name("Team[name]")   #点位到赛区名称输入框
    A.clear()
    A.send_keys(u"修改名称")                        #输入要修改成的名称



