# !/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, ABC

from assertpy.base import AbstractAssert, Comparator


class CalendarAssert(metaclass=ABCMeta):
    @abstractmethod
    def is_equal_to(self, expected):
        pass

    @abstractmethod
    def is_before(self, boundary):
        pass

    @abstractmethod
    def is_before_or_equal_to(self, boundary):
        pass

    @abstractmethod
    def is_after(self, boundary):
        pass

    @abstractmethod
    def is_after_or_equal_to(self, boundary):
        pass

    @abstractmethod
    def is_between(self, start_inclusive_boundary, end_inclusive_boundary):
        pass

    @abstractmethod
    def is_strictly_between(self, start_exclusive_boundary, end_exclusive_boundary):
        pass

    @abstractmethod
    def is_start_inclusive_between(self, start_inclusive_boundary, end_exclusive_boundary):
        pass

    @abstractmethod
    def is_end_inclusive_between(self, start_exclusive_boundary, end_inclusive_boundary):
        pass


class AbstractCalendarAssert(CalendarAssert, AbstractAssert, Comparator, ABC):
    def __init__(self, actual):
        super(AbstractCalendarAssert, self).__init__(actual)

    def is_equal_to(self, expected):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, expected) == 0
        return self

    def is_before(self, boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, boundary) < 0
        return self

    def is_before_or_equal_to(self, boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, boundary) <= 0
        return self

    def is_after(self, boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, boundary) > 0
        return self

    def is_after_or_equal_to(self, boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, boundary) >= 0
        return self

    def is_between(self, start_inclusive_boundary, end_inclusive_boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, start_inclusive_boundary) >= 0 and self.compare(self.actual,end_inclusive_boundary) <= 0
        return self

    def is_strictly_between(self, start_exclusive_boundary, end_exclusive_boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, start_exclusive_boundary) > 0 and self.compare(self.actual, end_exclusive_boundary) < 0
        return self

    def is_start_inclusive_between(self, start_inclusive_boundary, end_exclusive_boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, start_inclusive_boundary) >= 0 and self.compare(self.actual, end_exclusive_boundary) < 0
        return self

    def is_end_inclusive_between(self, start_exclusive_boundary, end_inclusive_boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, start_exclusive_boundary) > 0 and self.compare(self.actual, end_inclusive_boundary) <= 0
        return self


class DefaultCalendarAssert(AbstractCalendarAssert):
    def __init__(self, actual):
        super(DefaultCalendarAssert, self).__init__(actual)

    def compare(self, left, right) -> int:
        if left > right:
            return 1
        elif left < right:
            return -1
        else:
            return 0
