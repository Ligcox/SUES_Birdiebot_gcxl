from CMDsender import *
from sender import *


if __name__ == "__main__":
    cmd_sender = CMDSend()
    # 获取飞控数据
    # communicater = Communication_LX(0xff, 0xe1, ["0000"])
    communicater = Communication_LX(0xff, 0xe0, [10, 00, "01"])

    cmd_sender.send_LX(communicater.getInfo())