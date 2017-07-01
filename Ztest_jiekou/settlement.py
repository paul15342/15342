"""
赛果结算
注意:_csrf 有时会变动, cookies 也会变动
"""
#TODO 面向对象编程
import requests,time

from Ztest_jiekou.data import *


def data1():
    """已录入赛果,未审核的盘口
       _csrf参数每日都会变化
    """
    han_id = uncheck()
    list = []
    for id in han_id:
        data = {
            "han_id": id,
            "operateType": 1,
            "_csrf":"UnZMb0pwMmxkKTwJGSECOCQYCAESJmMNNww4DCg8QhgGEWEbexNfBg=="
        }
        list.append(data)
    print("list:%s" % list)
    return list

def data2():
    """盘口结算,盘口已审核未提交"""
    han_id = unsubmit()
    list = []
    for id in han_id:
        data ={
        "han_id": id,
        "operateType": 2,
        "_csrf": "UnZMb0pwMmxkKTwJGSECOCQYCAESJmMNNww4DCg8QhgGEWEbexNfBg=="
        }
        list.append(data)
    return list

def post1(url,header,cookies,data1):
    print (u"审核开始时间: %s" % time.ctime())
    requests.post(url, headers=header, cookies=cookies, data=data1)
    print ("审核结束: %s" % time.ctime())


def post2(url,header,cookies,param2):
    res = requests.post(url, headers=header, cookies=cookies, data=param2)
    print(res.status_code)


def main(header,cookie,data1,data2):
    """赛果结算：审核+结算"""
    start_time = time.time()
    #审核
    urll = "http://192.168.10.11:81/handicaps/handicap-settlement/update.html"
    if len(data1) == 0:
        print("赛果结算中,没有未审核的盘口")
    else:
        try:
            for param in data1:
                post1(urll, header, cookie, param)
        except Exception as e:
            print("error %s" % e)

    #提交结算
    url2 = "http://192.168.10.11:81/handicaps/handicap-settlement/settlement.html"

    if len(data1) == 0:
        print("赛果结算中,没有未结算的盘口")
    else:
        try:
            for param2 in data2:
                post2(url2, header, cookies, param2)
        except Exception as e:
            print("error %s" % e)
    end_time = time.time()
    print ("运行时间: %s" % (end_time-start_time))

if __name__=="__main__":
    header =header()
    cookie = cookies()
    data1 = data1()
    data2 = data2()
    main(header,cookie,data1,data2)
