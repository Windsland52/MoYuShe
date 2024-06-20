import requests
import json

token = json.load(open('config.json', 'r'))['token']

def get_show():
    url = "https://herobox.yingxiong.com:26723/encourage/signin/show"

    headers = {
        "Host": "herobox.yingxiong.com:26723",
        "Content-Length": "10",
        "lang": "zh-Hans",
        "Content-Type": "application/x-www-form-urlencoded",
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

    # gameId: 649 代表6/1-6/30福利补给站，暂时不知会不会根据月份不同而改变
    data = {
        "gameId": "649"
    }

    response = requests.post(url, headers=headers, data=data)
    response_content = response.text
    response_dict = json.loads(response_content)

    if response.status_code == 200:
        with open('show.json', 'w', encoding='utf-8') as f:
            json.dump(response_dict, f, ensure_ascii=False, indent=4)
    else:
        print(response.status_code, response_dict['msg'])

if __name__ == '__main__':
    get_show()