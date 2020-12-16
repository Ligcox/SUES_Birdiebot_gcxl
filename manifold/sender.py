import numpy as np
import serial
import copy

from monitor import *
from communication_data import *


class Communication_LX():
    """
    凌霄飞控通讯协议
    """
    
    def __init__(self, d_addr, id):
        '''
        data: 传入一个数字十六进制的字符列表,element应为数字，如出现0000这样的，分两位传入
        LEN: 根据data的长度自动计算长度，以U8为一个数据长度
        '''
        self.INFO = copy.deepcopy(D_INFO)
        self.monitor = Monitor()
        self.INFO["D_ADDR"] = d_addr
        self.INFO["ID"] = id

    def getInfo(self):
        '''获得十六进制的长度的文件
        返回一个bytearray

        '''
        s = bytearray([
            self.INFO["HEAD"],
            self.INFO["D_ADDR"],
            self.INFO["ID"],
            self.INFO["LEN"],
        ])
        s += self.INFO["DATA"]
        s.append(self.INFO["SUM_CHECK"])
        s.append(self.INFO["ADD_CHECK"])
        return s

    def sumcheck_cal(self):
        sumcheck = 0
        addcheck = 0
        for i in [(k, v) for k, v in self.INFO.items()][:-3]:
            sumcheck += i[1]
            addcheck += sumcheck
        
        for i in self.INFO["DATA"]:
            sumcheck += i
            addcheck += sumcheck

        self.INFO["SUM_CHECK"] = int(sumcheck) & 0XFF
        self.INFO["ADD_CHECK"] = int(addcheck) & 0XFF

        return self.INFO["SUM_CHECK"], self.INFO["ADD_CHECK"]

class LX_Sender(Communication_LX):
    """
    凌霄发送程序
    """
    def __init__(self, d_addr, id, data):
        super().__init__(d_addr, id)
        self.setDATA(data)
        self.sumcheck_cal()
        self.monitor.monitor(self.INFO)

    def setDATA(self, data):
        '''
        初始化传送器中的data信息
        '''
        for i in data:
            if i<255:
                  self.INFO["DATA"].append(i)
            else:
                for j in range((i // 256)+1):
                    self.INFO["DATA"].append(i<<(8*j) & 0xFF)

        self.INFO["LEN"] = len(self.INFO["DATA"])

class LX_Receiver(Communication_LX):
    '''
    飞控数据接收器
    '''
    def __init__(self, d_addr, id, data):
        super().__init__(d_addr, id)
        self.setDATA(data)
        self.sumcheck_cal()

    
    def sumcheck_cal(self):
        res = super.sumcheck_cal()
        if res != receive_SUM_CHECK, receive_ADD_CHECK:
            self.__del__()

    def __del__(self):
            print("data error!!")


