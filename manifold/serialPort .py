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

def reception():
    while True:
        a = time()
        myout = SER.read(8)

def close_post():
    SER.close()