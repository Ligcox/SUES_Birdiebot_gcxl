import serial
from config import *


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
        # res = self.ser.write(s)
        res = self.ser.write(s.encode("UTF-8"))
        print("写总字节数:{}".format(res))
        self.ser.close()#关闭串口