import pymongo,xlrd

def uncheck():
    con = pymongo.MongoClient("mongodb://192.168.10.11:27018")
    db =con["dm_data"]
    handicap =db["handicap"]
    han_id_list = []
    for i in handicap.find({"status":8}):    #status:8 状态时未审核
        han_id_list.append(i["han_id"])
    return han_id_list



def unsubmit():
    con = pymongo.MongoClient("mongodb://192.168.10.11:27018")

    db =con["dm_data"]

    handicap =db["handicap"]
    han_id_list = []
    for i in handicap.find({"status":10}):     #status:10  状态时未提交
        han_id_list.append(i["han_id"])
    return han_id_list


path = r"C:\Users\SCF\Desktop\test\params.xlsx"

def excel_table_byname():
    """从Excel表格获取数据"""
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)
    nrows = table.nrows #行数

    colnames =  table.row_values(0) #第一行的数据
    # print ("colnames:%s" % colnames)
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list


def header():
    header = {
		    'Accept-Encoding':'gzip, deflate',
		    'Accept-Language':'zh-CN,zh;q=0.8',
		    'Connection':'keep-alive',
		    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    return header

def cookies():
    f = open("C:\\Users\\SCF\\Desktop\\test\\cookies_hou.txt","r")
    cookies={}
    for line in f.read().split(";"):
        name,value=line.strip().split("=",1)
        cookies[name]=value
    return cookies

def cookies_first():
    f = open("C:\\Users\\SCF\\Desktop\\test\\cookies_hou.txt", "r")
    cookies = {}
    for line in f.read().split(";"):
        name, value = line.strip().split("=", 1)
        cookies[name] = value
    return cookies
#
# if __name__=="__main__":
#     excel_table_byname()