# !/usr/bin/env python
# -*- coding: utf-8 -*-

from multipledispatch import dispatch

from assertpy.base import AbstractAssert
from assertpy.collection import DefaultCollectionAssert
from assertpy.dict import DefaultDictAssert
from assertpy.number import NumberAssert, DefaultNumberAssert
from assertpy.strings import StringAssert, DefaultStringAssert


class Assertions:
    @staticmethod
    def add_exception_convertor(code_type, convertor):
        AbstractAssert.add_exception_convertor(code_type, convertor)


@dispatch(object)
def assert_that(actual):
    pass


@dispatch(str)
def assert_that(actual):
    return DefaultStringAssert(actual)


@dispatch((int, float))
def assert_that(actual):
    return DefaultNumberAssert(actual)


@dispatch(bool)
def assert_that(actual):
    pass


@dispatch((list, tuple))
def assert_that(actual):
    return DefaultCollectionAssert(actual)


@dispatch(dict)
def assert_that(actual):
    return DefaultDictAssert(actual)
