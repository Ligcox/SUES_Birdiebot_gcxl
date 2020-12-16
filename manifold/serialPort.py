import threading
from sender import *
from config import *

# 串口对象
SER = serial.Serial(PORTX, BPS, timeout=TIMEX)

def send_LX(s):
    """
    发送数据至凌霄
    """
    print(s)
    s = bytes(s)
    ser = SER.write(s)
    print("写总字节数:{}".format(ser))

def close_post():
    SER.close()


class SerialThread(threading.Thread):
    '''
    串口对象监听器
    '''
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadID = 0
        self.name = "串口监听器"

    def run(self):
        print ("开始线程：" + self.name)
        self.reception()
        print ("退出线程：" + self.name)

    def reception(self):
        # temp = []
        while True:
            LX_data = SER.read(256)
            temp = []
            dataEND = 0

            try:
                while True:
                    dataHEAD = LX_data.index(170, dataEND)
                    d_addr = dataHEAD + 1
                    if LX_data[d_addr] == 175:
                        dataLEN = LX_data[d_addr+2]
                        dataEND = d_addr+4+dataLEN
                        info = LX_data[d_addr-1: dataEND]
                        LX_Receiver(info)
                    else:
                        dataEND = dataHEAD
            except:
                # 后面完善吧，
                # 最后超出255的部分数据会丢失
                pass
