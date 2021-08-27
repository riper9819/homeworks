# -*- coding: utf-8 -*-

__author__ = 'sobolevn'

from utils import get_input_function


class Storage(object):  # storage = Storge()
    obj = None

    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading, done=False):
        self.heading = heading
        self.done = done

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()

    def setDone(self, done):
        self.done = done

    def doneCheck(self):
        return "- Done" if self.done is True else "- Undone"

class ToDoItem(BaseItem):
    def __str__(self):
        done = self.doneCheck()
        return 'ToDo: {} {}'.format(
            self.heading,
            done
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        return ToDoItem(heading)


class ToReadItem(BaseItem):
    def __init__(self, heading: str, url, done=False):
        super(ToReadItem, self).__init__(heading)
        self.url = url
        self.done = done

    def __str__(self):
        done = self.doneCheck()
        return 'ToRead: {} on {} {}'.format(
            self.heading,
            self.url,
            done
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        url = input_function('Input URL: ')
        return ToReadItem(heading, url)

class ToBuyItem(BaseItem):
    def __init__(self, heading, price, done=False):
        super(ToBuyItem, self).__init__(heading)
        self.price = price
        self.done = done

    def __str__(self):
        done = self.doneCheck()
        return 'ToBuy: {} for {} {}'.format(
            self.heading,
            self.price,
            done
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price)
