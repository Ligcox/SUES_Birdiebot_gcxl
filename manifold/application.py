from CMDsender import *
from sender import *
from config import *


if __name__ == "__main__":
    cmd_sender = CMDSend()
    # 获取飞控数据
    communicater = LX_sender(*unlock)
    communicater1 = LX_sender(*set_high)
    communicater2 = LX_sender(*lock)

    cmd_sender.send_LX(communicater.getInfo())
    # sleep(10)
    cmd_sender.send_LX(communicater1.getInfo())
    cmd_sender.send_LX(communicater2.getInfo())
    # sleep(10)
    cmd_sender.reception()