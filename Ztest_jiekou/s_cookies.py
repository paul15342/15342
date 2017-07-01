"""后台登录"""
import requests


def s_cookies():
    Cookie = {
        "UM_distinctid":"15c7c6a144f56d-058cd23b1a25b8-6416107c-1fa400-15c7c6a14503c",
        "_csrf":"ef09c121aed2ee28a13548789892303891f48e76e6834ffda7ba1287d1a96584a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22fcQ0cfd0U6fe1ziU4oLWobOQp7BZThRh%22%3B%7D",
        "CNZZDATA1261653927":"32598367-1496732609-%7C1497939993",
        "DMID":"7325161997759be58ba682e4893bfc16",
        "DMBACKID":"jnkrdav5fkf7dsqd2tc1dgvov5"
    }
    header = {
		    'Accept-Encoding':'gzip, deflate',
		    'Accept-Language':'zh-CN,zh;q=0.8',
		    'Connection':'keep-alive',
		    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "http://192.168.10.11:81/site/login.html"
    data ={"_csrf":"bW1XcDZBbEgLDgZAVScIeDhbMRUHOwUdWQIbJ1kjIxkdWhUqYik.IA==",
           "username":"153421",
           "password":"PAYNiQPdwORs/cvXj5dSZA=="
    }
    res = requests.post(url,data=data,headers=header,cookies=Cookie)
    print (res.status_code)
    print (res.text)


if __name__=="__main__":
    s_cookies()









o = {
    'isString': 'false',
     'betSrc': 1,
    'partname': 'A组',
    'handicapID': 2007164,
    'team1Name1': 'AZE',
    'matchName': 'First Blood5',
    'partID': 1,
    'handicapType': 1,
    'gameName': 'DOTA2',
    #'playId': 2000127,
    'amountMax': 6000,
    'team2Name': 'CCB',
    'raceID': 2000456,
    'matchId': 2000253,
    'team2ID': 2000412,
    'amountMin': 2,
    'team1ID': 2000413,
    'betAmount': 3,
    'gameID': 3,
    'raceOpenTime': '2017-06-15 17:00:00',
    'partodds': 1260,
    'betType': 0,
    'round': 1,
    'raceName': '晋级赛',
    'handicapName': 'First Blood5'}

























