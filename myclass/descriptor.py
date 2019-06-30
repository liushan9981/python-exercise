# -*- coding: utf-8 -*-

# Memo
# 优先级：
#     类属性
#     数据描述符
#     实例属性
#     非数据描述符
#     默认为__getattr__()

class DevNull2(object):
    def __get__(self, obj, typ=None):
        print("accessing attribute, ignoring")

    def __set__(self, obj, val):
        print("attempt to assign %r... ignoring" % val)

class C2(object):
    foo = DevNull2()



class DevNull3(object):
    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        print("accessing [%s]...ignoring" % self.name)

    def __set__(self, obj, val):
        print("Assigning %r to [%s]...ignoring" % (val, self.name))


class C3(object):
    foo = DevNull3("foo")


def run_c2():
    """
    输出如下：
        attempt to assign 'bar'... ignoring
        accessing attribute, ignoring
        c2.foo contains: None
    :return:
    """
    c2 = C2()
    c2.foo = "bar"
    x = c2.foo
    print("c2.foo contains:", x)


def run_c3():
    c3 = C3()
    c3.foo = "bar"
    x = c3.foo
    print("c3.foo: ", x)
    c3.__dict__["foo"] = "bar"
    x = c3.foo
    print("c3.foo: ", x)
    print('c3.__dict__["foo"]: ', c3.__dict__["foo"])


class FooFoo(object):
    def foo(self):
        print("foo() method is called")


def bar_bar():
    print("bar_bar method is called")


def run_foofoo():
    """
    验证：
        实例属性有更高的优先级，覆盖非数据描述符
    输出如下：
        foo() method is called
        bar.foo: assigned #1
        foo() method is called
        after asign to 'bar_bar' to 'bar.foo'
        bar_bar method is called
        foo() method is called
    :return:
    """
    bar = FooFoo()
    bar.foo()
    bar.foo = "assigned #1"
    print("bar.foo:", bar.foo)
    del bar.foo
    bar.foo()

    print("after asign 'bar_bar' to 'bar.foo'")
    bar.foo = bar_bar
    bar.foo()
    del bar.foo
    bar.foo()



