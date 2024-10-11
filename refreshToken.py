import requests
import json
import logging


def refresh_token(token=None, devcode=None, refreshToken=None):
    url = "https://herobox.yingxiong.com:25362/user/refreshToken"

    headers = {
        'log-header': 'I am the log request header.',
        'countrycode': 'CN',
        'devcode': f"{devcode}",
        'ip': '172.16.1.6',
        'key': 'Tym2wxIxyP5iTGj4rlNkOlxeSafhfHr+35A3eYq+2/rR32isp3srNKSwAYVeA2pOhC2hyBwJXlnCYwEbqOESwgp8E77KwNoI6ZAv6e4Xz/sDramgL36Wxh3KCrGtAhDvB+1X6ufffKlNWpfniaBGj16Guah5bLPfvUuNaYWRCsI=',
        'lang': 'zh-Hans',
        'model': 'HD1910',
        'osversion': '28',
        'rv': 'yyzR89NlSxdxehj5',
        'source': 'android',
        'token': f"{token}",
        'version': '3.3.0',
        'versioncode': '55',
        'content-type': 'application/x-www-form-urlencoded',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/3.10.0'
    }

    data = {
        "refreshToken": f"{refreshToken}"
    }

    response = requests.post(url, headers=headers, data=data)
    response_content = response.text
    # print(response_content)
    response_dict = json.loads(response_content)
    
    if response.status_code == 200:
        with open('config.json', 'r') as f:
            config = json.load(f)
        # 修改refreshToken的值
        try:
            config['token'] = response_dict['data']['token']
        except:
            logging.error("刷新token失败")
            exit()
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
            logging.info("刷新token成功")
    else:
        print(response.status_code, response_dict['msg'])

if __name__ == '__main__':
    with open('config.json', 'r') as f:
        config = json.load(f)
    token = config['token']
    devcode = config['devcode']
    refreshToken = config['refreshToken']
    refresh_token(token, devcode, refreshToken)