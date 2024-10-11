import logging
import json
from init import random_hex_string, init
from getToken import getSmsCode, getToken
from show import get_show
from sign import sign
from refreshToken import refresh_token
from signMoYu import signMoYu

logging.basicConfig(level=logging.INFO)

def login():
    logging.info("开始登录")
    with open('config.json', 'r') as f:
        config = json.load(f)
        devcode = config['devcode']
    logging.info("请输入手机号")
    phone = input()
    getSmsCode(phone, devcode)
    logging.info("请输入验证码")
    smscode = input()
    token, refreshToken = getToken(phone, smscode, devcode)

    # 更新config.json文件
    config['phone'] = phone
    config['token'] = token
    config['refreshToken'] = refreshToken
    
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

def MoYuShe():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            devcode = config['devcode']
            phone = config['phone']
            token = config['token']
            refreshToken = config['refreshToken']
            if phone == "" or token == "" or refreshToken == "":
                logging.info("配置文件不完整，开始登录")
                login()
            logging.info("读取配置文件成功")
    except FileNotFoundError:
        init(random_hex_string())
        logging.info("未发现配置文件，已自动初始化")

        logging.info("开始登录")
        login()

    get_show(token)
    logging.info("开始灵魂潮汐每日签到")
    res = sign(token)
    if not res:
        get_show(token)
        sign(token)
    logging.info("开始摸鱼社每日签到")
    signMoYu(devcode, token)

if __name__ == '__main__':
    MoYuShe()