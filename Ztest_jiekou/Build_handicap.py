"""
api新建盘口
"""
import requests,time,xlrd
import multiprocessing
from Ztest_jiekou.data import *
path = r"C:\Users\SCF\Desktop\test\params.xlsx"

def data1(csrf,team_id,team_name,race_id,id,date,part_odds01,part_odds02):
    """盘口参数"""
    # TODO 可进一步加强对数据自动化的提取
    data ={
            "_csrf":csrf,
            "han_id":"",
            "Handicap[game_id]":"3",
            "Handicap[match_id]":"2000253",
            "team_id":team_id,
            "teamname":team_name,
            "race_id":race_id,
            "Handicap[race_id]":id,
            "Handicap[play_id]":"2000127",
            "Handicap[round][]":"1",
            "Handicap[name]":u"First Blood2",
            "Handicap[buytype]":"2",
            "Handicap[part_name][0]":"A",
            "Handicap[part_odds][0]":part_odds01,
            "Handicap[canbuy][0]":0,
            "Handicap[part_name][1]": "B",
            "Handicap[part_odds][1]": part_odds02,
            "Handicap[canbuy][1]": "1",
            "Handicap[advancedpaid]":"10000",
            "Handicap[hantype]":"1",
            "Handicap[canstring]":"1",
            "Handicap[displaystatus]":"1",
            "opentime[ymd]":date,
            "opentime[his]":"19:22:00",
            "Handicap[opentime]": "%s 19:22:00" % date,
            "closetime[ymd]":date,
            "closetime[his]":"22:20:00",
            "Handicap[closetime]":"%s 22:22:00" % date,
            "Handicap[betminamount]":"2",
            "Handicap[betmaxamount]":"8000",
            "Handicap[userhanmaxamount]":"9000",
            "Handicap[maxamount]":"10000",
            "Handicap[operate_admin_user_id]":"2000101",
            "_csrf":csrf
}
    return data

def params(num):
    """建立盘口变动的参宿"""
    para = excel_table_byname()
    p = para[num]
    csrf,race_id,id,team_id,teamname =p["csrf"],p["race_id"],p["id"],p["team_id"],p["teamname"]
    # print (csrf,race_id,id,team_id,team_name)
    return csrf,race_id,id,team_id,teamname

def post(url,header,cookies,data):
    """发送请求"""
    print ("开始时间: %s" % time.ctime())
    res = requests.post(url, headers=header, cookies=cookies, data=data)
    print (res.status_code)
    print (res.text)
    time.sleep(1)
    print ("结束: %s" % time.ctime())


if __name__=="__main__":
    """
    建立盘口
    赔率在data1中设置
    """
    url = "http://192.168.10.11:81/handicaps/handicap-insert/create.html"
    header = header()
    cookies = cookies()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    date_now = now_time.split(" ")[0]  # 获取当前时间的年月日
    for i in range(2):
        param = params(i)
        csrf, race_id,id,team_id,team_name = param[0],param[1],param[2],param[3],param[4]
        print (team_id,team_name,race_id,id )
        data = data1(csrf,team_id,team_name,race_id,id,date=date_now,part_odds01="1.65",part_odds02="1.32")

        # post(url, header, cookies, data1)
        process = multiprocessing.Process(target=post,args=(url, header, cookies, data))   #多进程
        process.start()
        process.join()




