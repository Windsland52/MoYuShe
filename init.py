import random
import string
import json

def random_hex_string(length=33):
    return ''.join(random.choices(string.hexdigits, k=length)).lower()

def init(devcode=''):

    # 写入 config.json 文件
    config_data = {
        "phone": "",
        "token": "",
        "refreshToken": "",
        "devcode": devcode
    }

    with open('config.json', 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

    # 创建 show.json 空文件
    with open('show.json', 'w') as json_file:
        pass

if __name__ == '__main__':
    init(random_hex_string())