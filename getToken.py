import requests
import json
from datetime import datetime

with open("config.json", "r") as f:
    config = json.load(f)

devcode = config.get("devcode")
phone = config.get("phone")

def timeStamp2datetime(ts):
    return datetime.fromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S')

def nowtime2timeStamp(dt):
    return int(dt.timestamp() * 1000)

def getSmsCode(phone):
    url = "https://micromoyu-api.yingxiong.com/user/getSmsCode"

    headers = {
        "devcode": f"{devcode}",
        "source": "mc",
        "version": "3.2.0"
    }

    data = {
        "mobile": phone
    }

    response = requests.post(url, headers=headers, data=data)
    
    if json.loads(response.text)["code"] == 200 and json.loads(response.text)["success"] == True:
        print("短信验证码发送成功")
    else:
        print("短信验证码发送失败", json.loads(response.text)["msg"])
    
    return json.loads(response.text)

def getToken(phone, smsCode):
    url = "https://micromoyu-api.yingxiong.com/user/sdkLoginForMC"

    headers = {
        "devcode": f"{devcode}",
        "origin": "https://micromoyu.yingxiong.com",
        "source": "mc",
        "version": "3.2.0"
    }

    data = {
        "code": f"{smsCode}",
        "gameId": "649",
        "mobile": f"{phone}"
    }

    response = requests.post(url, headers=headers, data=data)
    
    if json.loads(response.text)["code"] == 200 and json.loads(response.text)["success"] == True:
        print("登录成功")
        print(response.text)
        print("token:", json.loads(response.text)["data"]["token"])
    else:
        print(response.text)
        print("登录失败", json.loads(response.text)["msg"])
    
    return json.loads(response.text)

if __name__ == '__main__':
    print("请输入手机号:")
    phone = input()
    getSmsCode(phone)
    print("请输入短信验证码:")
    smsCode = input()
    getToken(phone, smsCode)