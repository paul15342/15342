# coding=utf-8
"""
赛区编辑自动化测试
1,2,3,4,5,6
1, 数据模块
2, 定位模块
3，用例模块
4，断言模块
5, 异常处理
6, 生产报告
"""
from selenium import webdriver
from Login import login,race_zone_manager,race,team
from Business import business
from Ztest_jiekou.modify_team import *
from Ztest_jiekou.data import *
import unittest
import sys
sys.path.append("E:\Test\Login")


class Race_build(unittest.TestCase):
    """赛事管理"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get("http://192.168.10.11:81/")

    def test_build_race_zone(self):
        """新建赛区"""
        driver = self.driver
        login.login_input(self)
        login.click_race_manager(self)                                                               #点击赛事编辑
        race_zone_manager.click_race_zone(self)                                                      #点击赛区编辑
        num_before = business.business_num(self)                                                     #获取左下角的赛区数量
        login.click_new(self)                                                                        #点击新增
        race_zone_manager.bulid_new_zone(self)                                                       #输入赛区信息
        login.submit(self)
        driver.refresh()                                                                             #刷新页面
        num_after = business.business_num(self)
        # # try:
        self.assertEqual(num_before, num_after-1)                                                    # 断言,数量增加即新增
        # except Exception, e:
        #     print ("%s +1 != %s 赛区添加失败 "% (Num1, Num2))

    def test_close_race_zone(self):
        """新增赛区   新建时关闭,实际没有新增"""
        driver = self.driver
        login.login_input(self)
        login.click_race_manager(self)                                                  # 点击赛事管理
        race_zone_manager.click_race_zone(self)                                         # 点击赛区编辑
        Num1 = business.business_num(self)                                              # 获取左下角的赛区数量
        login.click_new(self)                                                           # 点击新增
        race_zone_manager.bulid_new_zone(self)                                          # 输入赛区信息
        login.edit_close(self)                                                          # 点击关闭
        driver.refresh()                                                                # 刷新页面
        Num2 = business.business_num(self)
        # try:
        self.assertEqual(Num1, Num2)                                                    # 断言,数量没增加即没有新增
        # except Exception ,e:
        #     print ("%s != %s 用例失败" %(Num1,Num2) )

    def test_edit_zone(self):
        """编辑赛区"""
        driver = self.driver
        login.login_input(self)
        login.click_race_manager(self)                                                           # 点击赛事管理
        race_zone_manager.click_race_zone(self)                                                  # 点击赛区编辑
        race_zone_manager.modify_zone(self)                                                      # 修改赛区名称
        login.submit(self)                                                                       # 保存
        driver.refresh()
        Text = business.business_td_five(self)                                                   # 抓取赛区名称
        # try:
        self.assertEqual(Text,u"修改名称")
        # except Exception ,e:
        #     print ("抓取到的信息:%s" % Text,  "实际信息:修改名称")

    def test_build_race(self):
        """新增赛事"""
        driver = self.driver
        login.login_input(self)
        login.click_race_manager(self)                                                          #点击赛事管理
        race.click_race_edit(self)                                                              #点击赛事编辑
        Num1 = business.business_num(self)
        login.click_new(self)                                                                   #新增
        race.edit_race_info(self)                                                               #输入赛事信息
        login.submit(self)                                                                      #提交
        driver.refresh()
        Num2 = business.business_num(self)
        # try:
        self.assertEqual(Num1, Num2-1)
        #   print ("新增成功:%s == %s" % (Num1, Num2))
        # except Exception,e:
        #     print ("%s != %s 用例失败" % (Num1, Num2))

    def test_close_race(self):
        """新增赛事,关闭不保存,实际没新增"""
        driver = self.driver
        driver = self.driver
        login.login_input(self)
        login.click_race_manager(self)  # 点击赛事管理
        race.click_race_edit(self)      # 点击赛事编辑
        Num1 = business.business_num(self)
        login.click_new(self)  # 新增
        race.edit_race_info(self)  # 输入赛事信息
        login.edit_close(self)              #关闭不保存
        driver.refresh()
        Num2 = business.business_num(self)
        self.assertEqual(Num1, Num2)

    def test_edit_race(self):
        """赛事编辑"""
        driver = self.driver
        login.login_input(self)
        login.click_race_manager(self)  # 点击赛事管理
        race.click_race_edit(self)  # 点击赛事编辑
        Name1 = business.business_edit_race(self)
        login.click_edit(self)      #点击编辑按钮
        race.modify_race_info(self)  #修改赛事信息
        login.submit(self)
        driver.refresh()
        Name2 = business.business_edit_race(self)
        self.assertNotEqual(Name1,Name2)

    def test_modify_race_status(self):
        """激活赛事"""
        driver =self.driver
        login.login_input(self)
        login.click_race_manager(self)  # 点击赛事管理
        race.click_race_edit(self)  # 点击赛事编辑
        text_before = business.business_race_status(self)
        race.modify_race_status(self)  #修改赛事状态
        driver.refresh()
        text_now = business.business_race_status(self)
        self.assertNotEqual(text_before,text_now)


    def test_build_team(self):
        """新增战队"""
        driver = self.driver
        login.login_input(self)
        login.click_race_manager(self)  # 点击赛事编辑
        team.click_team(self)               # 点击战队编辑
        Num_before = business.business_num(self)
        login.click_new(self)              #点击新增
        team.team_info(self)               #输入战队信息
        login.submit(self)                 #提交
        driver.refresh()
        Num_now = business.business_num(self)
        self.assertEqual(Num_before+1,Num_now)













    def tearDown(self):
        print ("close the window")
        self.driver.quit()

if __name__=="__main__":
    print (__doc__)
    unittest.main()