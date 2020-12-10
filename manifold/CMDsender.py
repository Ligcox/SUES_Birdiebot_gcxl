import serial
from config import *
from time import time, sleep


class CMDSend():
    def __init__(self, *parameter_list):
        """
        飞控消息发送类
        """
        self.ser = serial.Serial(PORTX, BPS, timeout=TIMEX)

    def send_LX(self, s):
        """
        发送数据至凌霄
        """
        print(s)
        info = s.decode("utf-8")
        print("--------", info)
        import sys
        sys.stdout.write(info)
        res = self.ser.write(info.encode("utf-8"))
        print("写总字节数:{}".format(res))
        # self.ser.close()#关闭串口

    def reception(self):#接收函数
        while True:
            a = time()
            # sleep(0.5)
            myout = self.ser.read(16)#读取串口传过来的字节流，这里我根据文档只接收7个字节的数据
            # my_need = int(hex(int(myout,16)),16)#将十六进制转化为十进制
            print(myout , time()-a)