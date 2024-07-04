import init
import show
import sign
import signMoYu

def MoYuShe():
    show.get_show()
    print("开始灵魂潮汐每日签到：")
    sign.sign()
    print("开始摸鱼社每日签到：")
    signMoYu.signMoYu()

if __name__ == '__main__':
    try:
        with open('config.json', 'r') as f:
            pass
    except FileNotFoundError:
        init.init()
    MoYuShe()