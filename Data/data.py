# -*- coding:utf-8 -*-
"""连接测试数据库,从数据库中取数据"""
import pymongo
import random
def get_zone_name():
    con = pymongo.MongoClient("mongodb://192.168.10.11:27018")
    db=con["dm_game"]
    zone = db["zone"]
    name_list = []
    dict = {}

    for x in zone.find({"game_id":1}):   #将赛区名称添加到列表中, 赛区名称：赛区id 以字典形式添加到字典中
        name_list.append(x["name"])
        dict[x["name"]] = x["zone_id"]

    i = "欧美赛区"
    if i in name_list:     #若列表中存在i,在利用赛区名称i在字典dict中获取相应的赛区id
        return dict[i]
    else:                  #若不存在,则在列表中随机取一个值,在列表中获取相应的赛区id
        index = random.randint(0,len(name_list)-1)
        zone_name =  name_list[index]
        return dict[zone_name]

# if __name__=="__main__":
#     get_zone_name()


