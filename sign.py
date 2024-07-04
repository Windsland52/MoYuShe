import requests
import json

token = json.load(open('config.json', 'r', encoding='utf-8'))['token']

def sign():
    url = "https://herobox.yingxiong.com:26723/encourage/signin/signin"

    headers = {
        "Host": "herobox.yingxiong.com:26723",
        "Content-Length": "39",
        "lang": "zh-Hans",
        "Content-Type": "application/x-www-form-urlencoded;",
        "source": "h5",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; HD1910 Build/PQ3A.190705.11150959; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36CP6.TgzO Hero/3.3.0",
        "token": f"{token}",
        "version": "2.11",
        "Accept": "*/*",
        "Origin": "https://herobox.yingxiong.com:8023",
        "X-Requested-With": "com.hero.time",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://herobox.yingxiong.com:8023/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    show_dict = {}

    with open('show.json', 'r', encoding='utf-8') as f:
        show_dict = json.load(f)
        signinTime = show_dict['data']['signinTime']
        periodID = show_dict['data']['period']['id']


    # for item in show_dict['data']['dayAward']:
    dayAwardId = show_dict['data']['dayAward'][signinTime]['id']

    data = {
        "dayAwardId": f"{dayAwardId}",
        "signinType": "1",
        "periodId": f"{periodID}"
    }

    response = requests.post(url, headers=headers, data=data)
    # print(response.text)
    if response.status_code == 200:
        if response.json()['code'] == 200:
            print(f"签到成功！获得{show_dict['data']['DayAward'][signinTime]['awardName']}")
            if response.json()['data']['signinTimeNow'] in ["5", "10", "15", 5, 10, 15]:
                signinTimeNow = int(response.json()['data']['signinTimeNow'])
                continueAwardList = []
                for item in show_dict['data']['continueAward']:
                    if item['achieveDays'] == signinTimeNow:
                        continueAwardList.append(item['awardName'])
                print(type(response.json()['data']['sendContinueAwardName']))
                print(f"累计签到{signinTimeNow}天，获得{continueAwardList}")
        elif response.json()['code'] == 711:
            print(f"今天已经签到过了！")
        elif response.json()['code'] == 10000:
            print(f"签到失败！{response.json()['msg']}")

if __name__ == '__main__':
    sign()