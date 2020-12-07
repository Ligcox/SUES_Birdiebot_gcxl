class Monitor(object):
    """
    发送文件打印器
    """

    def __init__(self, *parameter_list):
        """
        TODO
        """
        pass

    def monitor(self, ditc_info):
        """
        iter:可迭代字典
        """
        for k, v in ditc_info.items():
            if k == "DATA":
                print("{:10}: {}".format(k, v))
            else:
                print("{:10}: {:02X}".format(k, v))


                