from Ztest_jiekou.data import *
import requests,json

def modify_team(cookie):

    url = "http://192.168.10.11:81/matchs/team/update.html"
    data ={
        "_csrf":"Wk5oZmUwSzAXLRIPLEo5AQJ2JzcLWR1lGzovPwZCc2dvOFwWPAMqAQ==",
        "team_id":"2000399",
        "Team[zone_id]":"2000337",
        "Team[logo]":"2.png"
    }

    res = requests.post(url,data =data,cookies =cookie)
    t = json.loads(res.text)
    assert (t["code"]==1)

    print (res.status_code)


if __name__=="__main__":
    cookie = cookies()
    modify_team(cookie)



