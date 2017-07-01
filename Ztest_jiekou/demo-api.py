"""
前台模拟用户注单(单注)
注单数据连接数据库,从数据库中取出数据。 handicap中status=5的盘口为可注单


"""
import requests,json
import pymongo,random,time,multiprocessing
from Ztest_jiekou.data import *


def params():
    """从MongoDB数据口中随机取一个开盘盘口参数"""
    con =pymongo.MongoClient("mongodb://192.168.10.11:27018")
    db =con["dm_data"]
    handicap = db["handicap"]
    #获取开盘的盘口
    cap = handicap.find({"status":5})  #盘口状态为5时为开盘
    handicap_list = []
    handicap_dict = {}
    #随机取一个可用盘口
    handicap_dict["isString"] = "false"
    handicap_dict["betType"] = 0
    handicap_dict["betAmount"] = 5         #注单金额
    handicap_dict["betSrc"] = 1

    for xx in cap:
        handicap_list.append(xx)
    print (len(handicap_list))
    if len(handicap_list)>1:
        get_num = random.randint(0,len(handicap_list)-1)
        i =handicap_list[get_num]
    else:
        i = handicap_list[0]


    matchID = i["match_id"]
    game_id = i["game_id"]
    handicap_dict["gameID"] = i["game_id"]
    handicap_dict["matchID"] = i["match_id"]
    handicap_dict["matchName"] = i["race_name"]
    handicap_dict["raceID"] = i["race_id"]
    raceName = i["race_name"]
    handicap_dict["raceName"] = i["race_name"]
    handicapID = i["han_id"]
    handicap_dict["handicapID"] = i["han_id"]
    handicap_dict["handicapName"] = i["name"]
    handicap_dict["amountMin"] = int(i["betminamount"])
    handicap_dict["amountMax"] = int(i["betmaxamount"])
    handicap_dict["round"] = i["round"]
    handicap_dict["handicapType"] = i["hantype"]



    #获取赔率,赔率名称
    handicap_odds =db["handicap_odds"]
    p = handicap_odds.find({"han_id":handicapID})
    part_list = []
    for x in p :
        part_list.append(x)
    num =  random.randint(0,len(part_list)-1)   #求随机数
    handicap_odds_num = part_list[num]      #随机取一个赔率字典
    handicap_dict["partOdds"] =  handicap_odds_num["part_initodds"]

    handicap_dict["partName"] =  handicap_odds_num["part_name"]
    handicap_dict["partID"] = handicap_odds_num["part_id"]

    #获取站队ID  ,
    db2 = con["dm_game"]
    race = db2["race"]
    r = race.find_one({"name":raceName,"match_id":matchID})    #find_one取出的类型是字典, find是函数
    team1ID = r["team1_id"]
    team2ID = r["team2_id"]
    handicap_dict["raceOpenTime"] = r["opentime"]
    handicap_dict["team1ID"] = r["team1_id"]
    handicap_dict["team2ID"] = r["team2_id"]


    team = db2["team"]
    handicap_dict["team1Name"] = team.find_one({"team_id":team1ID})["name"]
    handicap_dict["team2Name"] = team.find_one({"team_id":team2ID})["name"]

    game = db2["game"]
    handicap_dict["gameName"] = game.find_one({"game_id":game_id})["name"]


    print (handicap_dict)
    return  handicap_dict



def post(url2,cookies,params,header):
    res = requests.post(url2, cookies=cookies, data=params, headers=header)
    text = json.loads(res.text)
    try:
        if  res.status_code == 200 and text["code"]==0:
            print (res.text)
            print ("注单成功，handicapID: {}".format(text["data"]["handicapID"]))
    except Exception as e :
        print ("注单失败: {}".format(e))



def main(cookies,params,header):
    url = "http://192.168.10.11:82/data/takebetsingle?t=%s" % (int(time.time()))
    post(url, cookies, params, header)

if __name__=="__main__":
    header = header()
    cookies =cookies_first()
    params = params()
    for i in range(1):
        p = multiprocessing.Process(target=main,args=(cookies,params,header))
        p.start()
        p.join()






