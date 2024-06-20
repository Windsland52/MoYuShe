def init():
    # 写入 config.py 文件
    config_content = 'token = ""\n'

    with open('config.py', 'w') as config_file:
        config_file.write(config_content)

    # 创建 show.json 空文件
    with open('show.json', 'w') as json_file:
        pass  # pass 表示什么也不做，只创建一个空文件

if __name__ == '__main__':
    init()