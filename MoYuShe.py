import init

def MoYuShe():
    import show
    import sign
    import signMoYu
    show.get_show()
    print("开始灵魂潮汐每日签到：")
    res = sign.sign()
    if not res:
        show.get_show()
        sign.sign()
    print("开始摸鱼社每日签到：")
    signMoYu.signMoYu()

if __name__ == '__main__':
    try:
        with open('config.json', 'r') as f:
            pass
    except FileNotFoundError:
        init.init()
        print("初始化完成，请在config.json中填写相关信息后再次运行！")
        exit()
    MoYuShe()