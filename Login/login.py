# -*- coding:utf-8 -*-
import time

def login_input(self):
    #登录
    driver = self.driver
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("123456")
    driver.find_element_by_id("login_btn").click()

def click_race_manager(self):
    # 点击赛事管理
    driver = self.driver
    driver.find_element_by_xpath("/html/body/div[2]/aside[1]/section/ul/li[3]/a").click()
    time.sleep(0.5)

def click_new(self):
    # 点击新增按钮
    driver = self.driver
    time.sleep(2)
    driver.find_element_by_id("create_btn").click()

def submit(self):
    driver = self.driver
    #弹出框提交
    driver.find_element_by_id("edit_dialog_ok").click()

def edit_close(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@id=\"edit_dialog\"]/div/div/div[3]/a[1]").click()  # 取消新增

def click_edit(self):
    #点击编辑按钮
    driver = self.driver
    driver.find_element_by_xpath("//div[@class=\"col-sm-12\"]/table/tbody/tr[1]/td[6]/a[1]").click()


