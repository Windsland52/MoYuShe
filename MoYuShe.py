import logging
import json
from init import random_hex_string, init
from getToken import getSmsCode, getToken
from show import get_show
from sign import sign
from refreshToken import refresh_token
from signMoYu import signMoYu

# 配置 basicConfig，输出到文件
logging.basicConfig(
    level=logging.INFO,
    filename='MoYuShe.log',
    filemode='a',
    format='[%(asctime)s] [%(levelname)s] %(message)s'
)

# 获取根日志器
logger = logging.getLogger()

# 添加控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
console_handler.setFormatter(console_formatter)

# 添加控制台处理器到日志器
logger.addHandler(console_handler)

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
            phone = config['phone']
            refreshToken = config['refreshToken']
        if phone == "" or refreshToken == "":
            logging.info("配置文件不完整，开始登录")
            login()
    except FileNotFoundError:
        init(random_hex_string())
        logging.info("未发现配置文件，已自动初始化")
        login()

    with open('config.json', 'r') as f:
        config = json.load(f)
        token = config['token']
        devcode = config['devcode']
        refreshToken = config['refreshToken']
    logging.info("读取配置文件成功")
    get_show(token)
    logging.info("开始灵魂潮汐每日签到")
    res = sign(token, devcode, refreshToken)
    if not res:
        with open('config.json', 'r') as f:
            config = json.load(f)
            token = config['token']
        get_show(token)
        sign(token, devcode, refreshToken)
    logging.info("开始摸鱼社每日签到")
    signMoYu(devcode, token)

if __name__ == '__main__':
    logging.info("程序开始运行")
    logging.info("Version v1.0.0")
    logging.info("作者：Windsland")
    logging.info("Github：https://github.com/Windsland52/MoYuShe")
    logging.info("版权声明：本项目遵循CC BY-NC-SA 4.0协议，您可以自由地分享、修改、分发本项目，但请注明出处。祝您使用愉快！")
    MoYuShe()