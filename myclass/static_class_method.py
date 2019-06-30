# -*- coding: utf-8 -*-

class TestStaticMethod:
    # 静态方法
    def foo():
        print("calling static method foo()")
    foo = staticmethod(foo)


class TestClassMethod:
    # 类方法
    def foo(cls):
        print("calling class method foo()", cls.__name__)
    foo = classmethod(foo)


