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


class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)


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


'''
执行的输出如下:
setting value
getting value
0
setting value
getting value
10
Traceback (most recent call last):
  File "/Users/bach.liu/mylab/python-exercise/main.py", line 100, in <module>
    main()
  File "/Users/bach.liu/mylab/python-exercise/main.py", line 95, in main
    run_celsius()
  File "/Users/bach.liu/mylab/python-exercise/myclass/myproperty.py", line 66, in run_celsius
    c.temperature = -300
  File "/Users/bach.liu/mylab/python-exercise/myclass/myproperty.py", line 38, in set_temperature
    raise ValueError("Temperature below -273 is not possible")
ValueError: Temperature below -273 is not possible
'''
def run_celsius():
    c = Celsius()
    print(c.temperature)
    c.temperature = 10
    print(c.temperature)
    c.temperature = -300
