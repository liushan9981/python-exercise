# -*- coding: utf-8 -*-

class HideX(object):
    def __init__(self, x):
        '''
        到底是self.__x = x 还是 self.x = x 这个不清楚
        :param x:
        '''
        print("# init")
        self.x = x
        print("get_x", self.x)

    def get_x(self):
        print("# get_x")
        # print("get_x", self.x)
        return ~self.__x

    def set_x(self, x):
        print("# set_x")
        assert isinstance(x, int), "'x' must be an integer"
        self.__x = ~(x + 1)
    z = property(get_x, set_x)




def run_hidex1():
    inst = HideX(20)
    print('haha')
    print(inst.x)
    print('-----')
    inst.z = 30
    print(inst.z)
    inst.z = 50
    print(inst.z)
    # 定义其他的变量
    inst.y = 10
    print(inst.y)
    inst.y = 20
    print(inst.y)


