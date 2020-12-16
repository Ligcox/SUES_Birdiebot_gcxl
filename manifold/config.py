import serial
from config import *
from time import time, sleep

'''
串口相关配置
'''
# 串口号
PORTX = "COM10"
# 波特率
BPS = 500000
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
TIMEX=5
# 串口对象
SER = serial.Serial(PORTX, BPS, timeout=TIMEX)


'''
通讯协议
'''
unlock = (0xff, 0xe0, [0x10, 0x00, 0x01])
set_high = (0xff, 0xe0, [0x10, 0,  0x05, 257])
lock = (0xff, 0xe0, [0x10, 0,  0x02])