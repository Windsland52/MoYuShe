import requests
import json
import logging

def getSmsCode(phone, devcode):
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
        logging.info("短信验证码发送成功")
    else:
        logging.error("短信验证码发送失败", json.loads(response.text)["msg"])
    
    return json.loads(response.text)

def getToken(phone, smsCode, devcode):
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
        logging.info("登录成功")
        logging.info("token:", json.loads(response.text)["data"]["token"])
        return json.loads(response.text)["data"]["token"], json.loads(response.text)["data"]["refreshToken"]
    else:
        logging.error("登录失败", json.loads(response.text)["msg"])
        return False

if __name__ == '__main__':
    with open("config.json", "r") as f:
        config = json.load(f)
    devcode = config.get("devcode")
    phone = config.get("phone")
    getSmsCode(phone, devcode)
    print("正在发送短信验证码...")
    print("请输入短信验证码:")
    smsCode = input()
    getToken(phone, smsCode, devcode)