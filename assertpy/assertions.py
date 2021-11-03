# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import overload, Union

from assertpy.base import AbstractAssert
from assertpy.booleans import BooleanAssert
from assertpy.collection import DefaultCollectionAssert, CollectionAssert
from assertpy.dict import DefaultDictAssert, DictAssert
from assertpy.number import NumberAssert, DefaultNumberAssert
from assertpy.objects import ObjectAssert
from assertpy.strings import StringAssert, DefaultStringAssert


class Assertions:
    @staticmethod
    def add_exception_convertor(code_type, convertor):
        AbstractAssert.add_exception_convertor(code_type, convertor)


@overload
def assert_that(actual: int) -> DefaultNumberAssert:
    ...


@overload
def assert_that(actual: float) -> DefaultNumberAssert:
    ...


@overload
def assert_that(actual: str) -> DefaultStringAssert:
    ...


@overload
def assert_that(actual: bool) -> BooleanAssert:
    ...


@overload
def assert_that(actual: list) -> DefaultCollectionAssert:
    ...


@overload
def assert_that(actual: tuple) -> DefaultCollectionAssert:
    ...


@overload
def assert_that(actual: set) -> DefaultCollectionAssert:
    ...


@overload
def assert_that(actual: dict) -> DefaultDictAssert:
    ...


@overload
def assert_that(actual: dict) -> ObjectAssert:
    ...


def assert_that(actual):
    if type(actual) in [int, float]:
        return DefaultNumberAssert(actual)
    elif isinstance(actual, str):
        return DefaultStringAssert(actual)
    elif isinstance(actual, bool):
        return BooleanAssert(actual)
    elif type(actual) in [list, tuple, set]:
        return DefaultCollectionAssert(actual)
    elif isinstance(actual, dict):
        return DefaultDictAssert(actual)
    else:
        return ObjectAssert(actual)
