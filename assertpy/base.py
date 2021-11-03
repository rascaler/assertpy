# !/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, ABC


class ExceptionConvertor(metaclass=ABCMeta):

    @abstractmethod
    def get_exception(self, obj):
        pass


class Comparator(metaclass=ABCMeta):
    @abstractmethod
    def compare(self, left, right) -> int:
        pass


class Assert(metaclass=ABCMeta):
    @abstractmethod
    def is_none(self):
        pass

    @abstractmethod
    def is_not_none(self):
        pass

    @abstractmethod
    def is_equal_to(self, expected):
        pass

    @abstractmethod
    def is_in(self, values):
        pass

    @abstractmethod
    def is_not_in(self, values):
        pass

    @abstractmethod
    def then_fail_throw(self, obj, format_msg, arguments):
        pass


class ComparableAssert(metaclass=ABCMeta):
    @abstractmethod
    def is_equal_to(self, expected):
        pass

    @abstractmethod
    def is_less_than(self, boundary):
        pass

    @abstractmethod
    def is_less_than_or_equal_to(self, boundary):
        pass

    @abstractmethod
    def is_greater_than(self, boundary):
        pass

    @abstractmethod
    def is_greater_than_or_equal_to(self, boundary):
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


class SizeComparableAssert(metaclass=ABCMeta):
    @abstractmethod
    def has_one_size(self):
        pass

    @abstractmethod
    def has_more_than_one_size(self):
        pass

    @abstractmethod
    def is_size_equal_to(self, boundary):
        pass

    @abstractmethod
    def is_size_less_than(self, boundary):
        pass

    @abstractmethod
    def is_size_less_than_or_equal_to(self, boundary):
        pass

    @abstractmethod
    def is_size_greater_than(self, boundary):
        pass

    @abstractmethod
    def is_size_greater_than_or_equal_to(self, boundary):
        pass

    @abstractmethod
    def is_size_between(self, start_inclusive_boundary, end_inclusive_boundary):
        pass

    @abstractmethod
    def is_size_strictly_between(self, start_exclusive_boundary, end_exclusive_boundary):
        pass

    @abstractmethod
    def is_size_start_inclusive_between(self, start_inclusive_boundary, end_exclusive_boundary):
        pass

    @abstractmethod
    def is_size_end_inclusive_between(self, start_exclusive_boundary, end_inclusive_boundary):
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

    def is_not_none(self):
        if not self.passed:
            return self
        self.passed = self.actual is not None
        return self

    def is_equal_to(self, expected):
        if not self.passed:
            return self
        self.passed = self.actual == expected
        return self

    def is_not_equal_to(self, expected):
        if not self.passed:
            return self
        self.passed = not (self.actual == expected)
        return self

    def is_in(self, values):
        if not self.passed:
            return self
        for value in values:
            if self.actual == value:
                self.passed = True
                return self
        self.passed = False
        return self

    def is_not_in(self, values):
        if not self.passed:
            return self
        for value in values:
            if self.actual == value:
                self.passed = False
                return self
        self.passed = True
        return self

    def then_fail_throw(self, obj, format_msg=None, arguments=None):
        if self.passed:
            return self
        self._write_custom_log(format_msg, arguments)
        if isinstance(obj, Exception):
            raise obj
        convertor = AbstractAssert._exception_mapping[type(obj)]
        raise convertor.get_exception(obj)

    def _write_custom_log(self, format_msg=None, arguments=None):
        if not format_msg:
            return
        if not arguments:
            print(format_msg)
        print(format_msg % arguments)

    @staticmethod
    def add_exception_convertor(code_type, convertor):
        if code_type in AbstractAssert._exception_mapping:
            raise Exception('convertor for %s has already existed' % code_type)
        AbstractAssert._exception_mapping[code_type] = convertor

    def get_result(self):
        return self.passed


class AbstractComparableAssert(ComparableAssert, AbstractAssert, Comparator, ABC):
    def __init__(self, actual):
        super(AbstractComparableAssert, self).__init__(actual)

    def is_equal_to(self, expected):
        if not self.passed:
            return self
        self.passed = self.actual == expected
        return self

    def is_less_than(self, boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, boundary) < 0
        return self

    def is_less_than_or_equal_to(self, boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, boundary) <= 0
        return self

    def is_greater_than(self, boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, boundary) > 0
        return self

    def is_greater_than_or_equal_to(self, boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, boundary) >= 0
        return self

    def is_between(self, start_inclusive_boundary, end_inclusive_boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.actual, start_inclusive_boundary) >= 0 and self.compare(self.actual, end_inclusive_boundary) <= 0
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


class AbstractSizeComparableAssert(SizeComparableAssert, AbstractAssert, Comparator, ABC):
    def __init__(self, actual):
        super(AbstractSizeComparableAssert, self).__init__(actual)

    @abstractmethod
    def size(self):
        pass

    def has_one_size(self):
        if not self.passed:
            return self
        self.passed = self.size() == 1
        return self

    def has_more_than_one_size(self):
        if not self.passed:
            return self
        self.passed = self.size() > 1
        return self

    def is_size_equal_to(self, other):
        if not self.passed:
            return self
        self.passed = self.size() == other
        return self

    def is_size_less_than(self, other):
        if not self.passed:
            return self
        self.passed = self.compare(self.size(), other) < 0
        return self

    def is_size_less_than_or_equal_to(self, other):
        if not self.passed:
            return self
        self.passed = self.compare(self.size(), other) <= 0
        return self

    def is_size_greater_than(self, other):
        if not self.passed:
            return self
        self.passed = self.compare(self.size(), other) > 0
        return self

    def is_size_greater_than_or_equal_to(self, other):
        if not self.passed:
            return self
        self.passed = self.compare(self.size(), other) >= 0
        return self

    def is_size_between(self, start_inclusive_boundary, end_inclusive_boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.size(), start_inclusive_boundary) >= 0 and self.compare(self.size(), end_inclusive_boundary) <= 0
        return self

    def is_size_strictly_between(self, start_exclusive_boundary, end_exclusive_boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.size(), start_exclusive_boundary) > 0 and self.compare(self.size(), end_exclusive_boundary) < 0
        return self

    def is_size_start_inclusive_between(self, start_inclusive_boundary, end_exclusive_boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.size(), start_inclusive_boundary) >= 0 and self.compare(self.size(), end_exclusive_boundary) < 0
        return self

    def is_size_end_inclusive_between(self, start_exclusive_boundary, end_inclusive_boundary):
        if not self.passed:
            return self
        self.passed = self.compare(self.size(), start_exclusive_boundary) > 0 and self.compare(self.size(), end_inclusive_boundary) <= 0
        return self

    def compare(self, left, right):
        return left - right


