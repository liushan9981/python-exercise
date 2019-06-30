# -*- coding: utf-8 -*-


class WrapMe(object):
    '''
    授权
    带两个下划线开头的属性，被隐藏
    '''
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return 'self.__data'

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, attr):
        # return getattr(self.__data, 'real')
        # 原始对象的其他属性，授权给新对象访问
        return getattr(self.__data, attr)


class WrapMe2(object):
    '''
    授权
    带两个下划线开头的属性，被隐藏
    '''
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return 'self.__data'

    def __str__(self):
        print('ha str')
        return str(self.__data)

    def __getattr__(self, attr):
        # return getattr(self.__data, 'real')
        # 原始对象的其他属性，授权给新对象访问
        return getattr(self.__data, attr)

    def __getattribute__(self, item):
        # 属性被访问时，该特殊方法会被调用
        print("this is:", item)
        return object.__getattribute__(self, item)





def run_wrap():
    wra = WrapMe(3.5 + 4.3j)
    print(wra)
    print(wra.real)

def run_wrap2():
    wrap2 = WrapMe2(3.5 + 4.4j)
    print(wrap2)
    print(wrap2.real)

