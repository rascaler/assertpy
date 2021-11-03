# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from abc import ABCMeta, abstractmethod

from assertpy.assertions import assert_that
from assertpy.base import AbstractAssert
from assertpy.collection import DefaultCollectionAssert


class Assert(metaclass=ABCMeta):
    @abstractmethod
    def is_none(self):
        pass


class AbstractAssert(Assert):
    _exception_mapping = {}

    def __init__(self, actual) -> None:
        self.log = None
        self.actual = actual
        self.passed = True

    def is_none(self):
        if not self.passed:
            return self
        self.passed = self.actual is None
        return self


class NumberAssert(metaclass=ABCMeta):
    @abstractmethod
    def is_zero(self):
        pass


class AbstractNumberAssert(NumberAssert, AbstractAssert):
    def __init__(self, actual):
        super(AbstractNumberAssert, self).__init__(actual)

    def is_zero(self):
        if not self.passed:
            return self
        self.passed = self.actual == 0
        return self


class DefaultNumberAssert2(AbstractNumberAssert):
    def __init__(self, actual):
        super(DefaultNumberAssert2, self).__init__(actual)
