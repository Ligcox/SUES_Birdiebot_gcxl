import threading

from serialPort import *
from sender import *
from config import *

class AppThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)



if __name__ == "__main__":


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