# -*- coding: utf-8 -*-

from myclass.myclass import C
from myclass.static_class_method import TestClassMethod, TestStaticMethod
from myclass.composition import NewAddrBookEntry
from myclass.subclass import Child, SubA, SubB, SubC, SubD, SubE, ChildMethod, RoundFloat, SortedKeyDict, \
    run_attrs, run_roundfloat2, run_time60, run_randseq, run_any_iter

from myclass.wrap import run_wrap, run_wrap2
from myclass.descriptor import run_c2, run_c3, run_foofoo
from myclass.myproperty import run_hidex1, run_celsius

from myre import retest


from mythread.test_thread_func import test_main_thread_func
from mythread.test_thread_func import test_main_thread_obj
from mythread.test_thread_func import test_main_thread_subobj

from mythread.test_queue import testqueue
from tools.mysubprocess import test_subprocess

def run_myclass_c():
    """
    实例属性和类属性是不同的东西，self.name是实例属性，引用"实例.foo"时，如果该实例空间没有foo属性，则从类空间查找
    python中，创建一个类，相当于创建一个新的数据类型
    :return:
    """
    c = C()
    print(c.foo, C.foo)
    c.foo += 2
    print(c.foo, C.foo)
    c1 = C()
    C.foo += 5
    print(c.foo, c1.foo, C.foo)
    print(C.__dict__)
    print(c.__dict__)
    print(c1.__dict__)


def run_static_class_method():
    tsm = TestClassMethod()
    tsm.foo()

    tcm = TestStaticMethod()
    tcm.foo()

    TestStaticMethod.foo()
    TestClassMethod.foo()


def run_composition():
    cm = NewAddrBookEntry("liushan", "171")


def run_subclass():
    child = Child()
    child.child_method()
    child.parent_method()

    print('inherit')
    print(SubA.__bases__)
    print(SubB.__bases__)
    print(SubC.__bases__)
    print(SubD.__bases__)
    print(SubE.__bases__)
    print("rewrite method")
    c = ChildMethod()
    c.foo()
    print("rewrite type")
    print(RoundFloat(1.5994))
    print(RoundFloat(1.5994))
    print(RoundFloat(1.5994))
    d = SortedKeyDict((("zhengcai", 68), ("hejin", 56), ("xinxi", 76)))
    print([key for key in d])
    print(d.keys())







def main():
    # run_myclass_c()
    # run_static_class_method()
    # run_subclass()
    # run_attrs()
    # run_roundfloat2()
    # run_time60()
    # run_randseq()
    # run_any_iter()
    # wrappedComplex = wrap.WrapMe(3.5 + 4.2j)
    # wrappedComplex
    # run_wrap()
    # run_wrap2()
    # run_c2()
    # run_c3()
    # run_foofoo()
    # run_hidex1()

    # retest.test1()
    # testqueue()
    test_subprocess()




if __name__ == '__main__':
    main()


