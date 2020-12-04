import numpy as np
import serial

from monitor import *


class Communication_LX(object):
    """
    凌霄飞控通讯协议
    """
    INFO = {
            "HEAD": 0xAA,
            "D_ADDR": None,
            "ID": None,
            "LEN": None,
            "DATA": [],
            "SUM_CHECK": None,
            "ADD_CHECK": None
    }
    monitor = Monitor()

    def __init__(self, d_addr, id, data):
        '''
        data: 传入一个数字十六进制的字符列表,element应为字符串
        LEN: 根据data的长度自动计算长度，以U8为一个数据长度
        '''
        self.INFO["D_ADDR"] = d_addr
        self.INFO["ID"] = id
        self.setDATA([("0x"+str(i)) for i in data])
        self.sumcheck_cal()
        self.monitor.monitor(self.INFO)


    def setDATA(self, data):
        '''
        初始化传送器中的data信息
        '''
        print("--------",data)
        LEN = 0
        for num, i in enumerate(data):
            print(num, i)
            elelen = len(i)
            LEN += elelen-2
            i = eval(i)
            LEN+=0 if i == 0 else LEN
            if elelen == 2:
                self.INFO["DATA"].append("0x{:02X}".format(i))
            elif elelen == 4:
                self.INFO["DATA"].append("0x{:04X}".format(i))
            elif elelen == 8:
                self.INFO["DATA"].append("0x{:08X}".format(i))
            elif elelen == 16:
                self.INFO["DATA"].append("0x{:016X}".format(i))
            elif elelen == 32:
                self.INFO["DATA"].append("0x{:032X}".format(i))
        
        self.INFO["LEN"] = int(LEN/2)

    def sumcheck_cal(self):
        sumcheck = 0
        addcheck = 0
        for i in [(k, v) for k, v in self.INFO.items()][:-3]:
            sumcheck += i[1]
            addcheck += sumcheck
        
        for i in self.INFO["DATA"]:
            for j in range(len(i[3:])):
                if j % 2 == 0:
                    sumcheck += eval("0x" + i[j+2: j+4])
                    addcheck += sumcheck

        self.INFO["SUM_CHECK"] = int(sumcheck) & 0X0FF
        self.INFO["ADD_CHECK"] = int(addcheck) & 0X0FF

    def getInfo(self):
        iter = self.INFO
        s = ''
        for i in iter:
            if i == "DATA":
                for j in iter[i]:
                    s += j[2:]
            else:
                s += "{:02X}".format(iter[i])
        return s

    def setInfo(self):
        if D_ADDR is not None:
            self.INFO["D_ADDR"] = D_ADDR
        if ID is not None:
            self.INFO["ID"] = ID
        if LEN is not None:
            self.INFO["LEN"] = LEN
        if DATA is not None:
            self.INFO["DATA"] = DATA

