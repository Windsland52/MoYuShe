import requests
import json
import logging

def signMoYu(devcode=None, token=None):
    url = "https://herobox.yingxiong.com:25362/user/signIn"

    headers = {
        "log-header": "I am the log request header.",
        "countrycode": "CN",
        "devcode": f"{devcode}",
        "key": "FCxkCfRLV65O9+rIgo6FRfPAFp3o0j5YD+UZnd+ffc/ADdiLRnEIT2+dNBKzizPT+HHsg8ev4vNvXOzjuc3Ub/yelKXNok9zVTimirOnoPSQfpLJC//Sm/NB0U839f3UozYwItAMtlE8llYbFSygCr15OZBxhnZpTvUEYxhLsmU=",
        "lang": "zh-Hans",
        "model": "HD1910",
        "osversion": "28",
        "rv": "NmGlr5VQmyqepRvT",
        "source": "android",
        "token": f"{token}",
        "version": "3.3.0",
        "versioncode": "55",
        "content-type": "application/x-www-form-urlencoded",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.10.0"
    }

    data = {
        "gameId": "649"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.json()['code'] == 200:
        logging.info(f"签到成功！{response.json()['msg']}")
    else:
        logging.info(f"签到失败！{response.json()['msg']}")

if __name__ == '__main__':
    token = json.load(open('config.json'))['token']
    devcode = json.load(open('config.json'))['devcode']
    signMoYu(token, devcode)