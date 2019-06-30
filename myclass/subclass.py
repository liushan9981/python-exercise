# -*- coding: utf-8 -*-
from random import choice


class Parent():
    def parent_method(self):
        print("calling parent method")


class Child(Parent):
    def child_method(self):
        print("calling child method")


class SubA():
    pass


class SubB(SubA):
    pass

class SubC(SubB):
    pass

class SubD():
    pass

class SubE(SubA, SubD):
    # 这是多重继承
    pass



class ParentMethod():
    def foo(self):
        print('this is parent foo')


class ChildMethod(ParentMethod):
    def foo(self):
        # 使用父类未绑定方法
        super().foo()
        print("this is child foo")


class RoundFloat(float):
    def __new__(cls, val):
        # 在此,cls是什么意思，不理解
        return super().__new__(cls, round(val, 2))


class SortedKeyDict(dict):
    def keys(self):
        return sorted(super().keys())


class MyClass():
    def __init__(self):
        self.foo = 100



class RoundFloat2():
    def __init__(self, val):
        assert isinstance(val, float), 'value must be float!'
        self.value = round(val, 2)
    '''
    没有添加__str__之前，运行输出如下：
    /usr/bin/python3.7 /home/liushan/PycharmProjects/python-exercise/main.py
    <myclass.subclass.RoundFloat2 object at 0x7f05d9e5e5f8>
    
    Process finished with exit code 0
    
    在添加__str__之后，运行输出如下：
    /usr/bin/python3.7 /home/liushan/PycharmProjects/python-exercise/main.py
    6.57
    
    Process finished with exit code 0
    '''
    def __str__(self):
        return "%.2f" % self.value

    __repr__ = __str__


class Time60():
    def __init__(self, hour, min):
        assert isinstance(hour, int)
        assert isinstance(min, int)
        self.hour = hour
        self.min = min

    def __str__(self):
        return "%s:%s" % (self.hour, self.min)

    def __add__(self, other):
        assert isinstance(other, self.__class__)
        return self.__class__(self.hour + other.hour, self.min + other.min)

    def __iadd__(self, other):
        assert isinstance(other, self.__class__)
        self.hour += other.hour
        self.min += other.min
        return self

    __repr__ = __str__


class RandSeq():
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def __next__(self):
        return choice(self.data)


class AnyIter():
    def __init__(self, data, safe=False):
        self.iter = iter(data)
        self.safe = safe

    def __iter__(self):
        return self

    def __next__(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.__next__())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval



def run_attrs():
    ins = MyClass()
    print("hasattr(ins, 'foo'): ", hasattr(ins, 'foo'))
    print("getattr(ins, 'foo'): ", getattr(ins, 'foo'))
    print("hasattr(ins, 'bar'): ", hasattr(ins, 'bar'))
    print("getattr(ins, 'bar', 'default'): ", getattr(ins, 'bar', 'default'))
    print("setattr(ins, 'bar', 'my attr'): ", setattr(ins, 'bar', 'my attr'))
    print("getattr(ins, 'bar'): ", getattr(ins, 'bar'))

def run_roundfloat2():
    rfm = RoundFloat2(6.5689)
    print(rfm)

def run_time60():
    '''
    /usr/bin/python3.7 /home/liushan/PycharmProjects/python-exercise/main.py
    n1: 1:20
    n2: 13:30
    n1 + n2: 14:50
    id n1: 140596605179384
    n1 after n1 += n2: 14:50
    id n1: 140596605179384
    :return:
    '''
    n1 = Time60(1,20)
    n2 = Time60(13,30)
    print("n1:", n1)
    print("n2:", n2)
    print("n1 + n2:", n1 + n2)
    print('id n1:', id(n1))
    n1 += n2
    print("n1 after n1 += n2:", n1)
    print('id n1:', id(n1))


def run_randseq():
    myrand = RandSeq([1, 3, 5, 7, 9])
    n = 0
    for i in myrand:
        print(i)
        n += 1
        if n > 5:
            break


def run_any_iter():
    '''
    /usr/bin/python3.7 /home/liushan/PycharmProjects/python-exercise/main.py
    1 : [0]
    2 : [1, 2]
    3 : [3, 4, 5]
    4 : [6, 7, 8, 9]
    ----------
    [0]
    [1]
    [2]
    [3]
    ----------
    [0, 1]
    [2, 3, 4]
    [5, 6, 7, 8]
    [9, 10, 11, 12, 13]
    [14, 15, 16, 17, 18, 19]
    [20, 21, 22]

    Process finished with exit code 0
    :return:
    '''
    a = AnyIter(range(10))
    for j in range(1, 5):
        print(j, ':', a.__next__(j))
    print('-' * 10)
    b = AnyIter(range(4))
    for i in b:
        print(i)
    print('-' * 10)
    c = AnyIter(range(23), safe=True)
    i = 2
    while True:
        try:
            ret = c.__next__(i)
            if not ret:
                break
            else:
                print(ret)
        except StopIteration:
            print('haha')
            break
        i += 1

