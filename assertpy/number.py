# !/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, ABC

from assertpy.base import AbstractComparableAssert


class NumberAssert(metaclass=ABCMeta):
    @abstractmethod
    def is_zero(self):
        pass

    @abstractmethod
    def is_zero(self):
        pass

    @abstractmethod
    def is_not_zero(self):
        pass

    @abstractmethod
    def is_one(self):
        pass

    @abstractmethod
    def is_not_one(self):
        pass

    @abstractmethod
    def is_positive(self):
        pass

    @abstractmethod
    def is_negative(self):
        pass

    @abstractmethod
    def is_not_negative(self):
        pass

    @abstractmethod
    def is_not_positive(self):
        pass


class AbstractNumberAssert(NumberAssert, AbstractComparableAssert, ABC):
    def __init__(self, actual):
        super(AbstractNumberAssert, self).__init__(actual)

    def is_zero(self):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, 0) == 0
        return self

    def is_not_zero(self):
        if not self.passed:
            return self
        self.passed = not (self.compare(self.actual, 0) == 0)
        return self

    def is_one(self):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, 1) == 0
        return self

    def is_not_one(self):
        if not self.passed:
            return self
        self.passed = not (self.compare(self.actual, 1) == 0)
        return self

    def is_positive(self):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, 0) > 0
        return self

    def is_negative(self):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, 0) < 0
        return self

    def is_not_negative(self):
        if not self.passed:
            return self
        self.passed = not (self.compare(self.actual, 0) < 0)
        return self

    def is_not_positive(self):
        if not self.passed:
            return self
        self.passed = not (self.compare(self.actual, 0) > 0)
        return self


class DefaultNumberAssert(AbstractNumberAssert):
    def __init__(self, actual):
        super(DefaultNumberAssert, self).__init__(actual)

    def compare(self, left, right) -> int:
        return left - right

