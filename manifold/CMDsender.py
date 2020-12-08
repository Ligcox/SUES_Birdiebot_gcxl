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
        # res = self.ser.write(s.encode("UTF-8"))
        res = self.ser.write("AAFFE10200008C81".encode("UTF-8"))
        print("写总字节数:{}".format(res))
        self.ser.close()#关闭串口

    def reception(self):#接收函数
        while True:
            while self.ser.inWaiting()>0:
                myout = self.ser.read(7)#读取串口传过来的字节流，这里我根据文档只接收7个字节的数据
                my_need = int(hex(int(myout,16)),16)#将十六进制转化为十进制
                print(my_need)