# 通讯协议相关配置
# Author by ligcox
# 2020.12


D_INFO = {
        "HEAD": 0xAA,
        "D_ADDR": None,
        "ID": None,
        "LEN": None,
        "DATA": bytearray(),
        "SUM_CHECK": None,
        "ADD_CHECK": None
}


'''
通讯协议
'''
unlock = (0xff, 0xe0, [0x10, 0x00, 0x01])
set_high = (0xff, 0xe0, [0x10, 0,  0x05, 257])
lock = (0xff, 0xe0, [0x10, 0,  0x02])