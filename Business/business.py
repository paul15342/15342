# coding=utf-8

from Login import login , race_zone_manager

def business_num(self):
    #提取当前页面的记录数量
    driver = self.driver
    text = driver.find_element_by_id("data_table_info").text
    print (type(text))
    ts = text.split("共")[1].split("条")[0].strip()
    TTT = int(ts)
    print (TTT)
    return TTT

def business_td_five(self):     #抓取赛区的名称(第四个格子)
    driver = self.driver
    text= driver.find_element_by_xpath("//div[@class=\"col-sm-12\"]/table/tbody/tr[1]/td[5]").text
    # Text = text.decode(encoding="utf-8")

    print (type(text))
    return text

def business_edit_race(self): #抓取赛事的名称
    driver = self.driver
    text = driver.find_element_by_xpath("//div[@class=\"col-sm-12\"]/table/tbody/tr[1]/td[5]").text
    print (text)
    return text

def business_race_status(self): #抓取赛事状态
    driver = self.driver
    text = driver.find_element_by_xpath("//div[@class=\"col-sm-12\"]/table/tbody/tr[1]/td[5]").text
    print (text)
    return text

def business_team_name(self):    #抓取战队名称
    driver = self.driver
    text = driver.find_element_by_xpath("//tbody//tr[1]//a[@id=\"edit_btn\"][4]").text
    return text



