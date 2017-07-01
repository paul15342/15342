# -*- coding:utf-8 -*-

import HTMLTestRunner,unittest,time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from test_case import test_case

testsuit = unittest.TestSuite()
testsuit.addTest(test_case.Race_build("test_build_race_zone"))
testsuit.addTest(test_case.Race_build("test_close_race_zone"))
testsuit.addTest(test_case.Race_build("test_edit_zone"))
testsuit.addTest(test_case.Race_build("test_build_race"))
testsuit.addTest(test_case.Race_build("test_close_race"))
testsuit.addTest(test_case.Race_build("test_edit_race"))
now = time.strftime("%Y-%m-%d %H_%M_%S")
fp=open("E:\\Z_Demo\\Report\\"+now+"result.html",'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="Z_Demo Report",description=u"赛区自动化测试")
runner.run(testsuit)
fp.close()


