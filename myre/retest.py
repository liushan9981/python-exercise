# -*- coding: utf-8 -*-
import re

def test1():
    line_split = '-' * 10

    '''
    输出如下：
        abc-123
        abc
        123
        ('abc', '123')
    '''
    m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
    print(line_split)
    # 不使用分组时
    '''
    输出如下：
        abc-123
        ()
    '''
    m = re.match('\w\w\w-\d\d\d', 'abc-123')
    print(m.group())
    print(m.groups())
    print(line_split)
    # 搜索，可以不从第一个字符开始
    '''
    输出如下：
        abc-123
        abc
        123
        ('abc', '123')
    '''
    m = re.search('(\w\w\w)-(\d\d\d)', '# abc-123')
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
    print(line_split)

    # 匹配，必须从第一个字符开始
    m = re.match('(\w\w\w)-(\d\d\d)', '# abc-123')
    if m:
        print(m.group())
        print(m.group(1))
        print(m.group(2))
        print(m.groups())


def test2():
    mystr = 'liushan is Liushan'
    print(re.findall(r'[Ll]iushan', mystr))

    print(re.sub(r'[Ll]iushan', 'fanfan', mystr))

    print(re.split(r'[Ll]iu', mystr))
    # 原始字符串
    print('liushan\n')
    print(r'liushan\n')

