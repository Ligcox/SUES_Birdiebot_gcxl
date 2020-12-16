import threading

from sender import *
from config import *
from serialPort import *

if __name__ == "__main__":
    # 获取飞控数据
    serListener = SerialThread()
    serListener.start()
    serListener.join()
    communicater = LX_Sender(*unlock)
    communicater1 = LX_Sender(*set_high)
    communicater2 = LX_Sender(*lock)

    send_LX(communicater.getInfo())
    # sleep(10)
    send_LX(communicater1.getInfo())
    send_LX(communicater2.getInfo())
    # sleep(10)
    # cmd_sender.reception()