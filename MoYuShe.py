import init
import show
import sign

def MoYuShe():
    show.get_show()
    sign.sign()

if __name__ == '__main__':
    try:
        with open('config.json', 'r') as f:
            pass
    except FileNotFoundError:
        init.init()
    MoYuShe()