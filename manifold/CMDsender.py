from config import *

class CMDSend():
    def send_LX(self, s):
        """
        发送数据至凌霄
        """
        print(s)
        s = bytes(s)
        ser = SER.write(s)
        print("写总字节数:{}".format(ser))
        # self.ser.close()#关闭串口

    def reception(self):#接收函数
        while True:
            a = time()
            myout = SER.read(8)#读取串口传过来的字节流，这里我根据文档只接收7个字节的数据
            # print("----飞控返回数据----")
            # print(myout , "时间：", time()-a)