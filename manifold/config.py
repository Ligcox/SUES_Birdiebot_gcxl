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



