# -*- coding: utf-8 -*-

class Name():
    def __init__(self, name):
        pass


class Phone():
    def __init__(self, phone):
        pass


class NewAddrBookEntry():
    def __init__(self, nm, ph):
        # 该类中，同时包含Name Phone类的实例
        self.name = Name(nm)
        self.phone = Phone(ph)
        print("create instance for:", self.name)
