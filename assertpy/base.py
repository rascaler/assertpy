# !/usr/bin/env python
# -*- coding: utf-8 -*-


from abc import ABCMeta, abstractmethod
from functools import singledispatch

class ExceptionConvertor(metaclass=ABCMeta):
    @abstractmethod
    def get_exception(obj):
        pass


class Assert(metaclass=ABCMeta):
    @abstractmethod
    def is_none():
        pass

    @abstractmethod
    def is_not_none():
        pass

    @abstractmethod
    def is_equal_to(expected):
        pass

    @abstractmethod
    def is_not_equal_to(expected):
        pass

    @abstractmethod
    def is_not_equal_to(expected):
        pass

    @abstractmethod
    def is_in(values):
        pass

    @abstractmethod
    def is_not_in(values):
        pass

    @abstractmethod
    def then_fail_throw(obj, format, arguments):
        pass
    
    @abstractmethod
    def add_exception_convertor(convertor):
        pass

class AbstractAssert(Assert):
    __exception_mapping = {}
    def __init__(self, actual) -> None:
        self.log = None
        self.actual = None
        self.passed = True

    def is_none(self):
        if (not self.passed):
            return self
        self.passed = self.actual is None
        return self    

    def is_not_none(self):
        if (not self.passed):
            return self
        self.passed = self.actual is not None
        return self

    def is_equal_to(self, expected):
        if (not self.passed):
            return self
        self.passed = self.actual == expected
        return self    

    def is_not_equal_to(self, expected):
        if (not self.passed):
            return self
        self.passed = not (self.actual == expected)
        return self

    def is_in(self, values):
        if (not self.passed):
            return self
        for value in values:
            if self.actual == value:
                self.passed = True
                return self
        self.passed = False
        return self        

    def is_not_in(self, values):
        if (not self.passed):
            return self
        for value in values:
            if self.actual == value:
                self.passed = False
                return self
        self.passed = True
        return self     

    @singledispatch
    def then_fail_throw(self, obj, format=None, arguments=None):
        pass

    @then_fail_throw.register(Exception)    
    def _then_fail_throw(self, obj, format=None, arguments=None):
        pass
    
    @then_fail_throw.register(str)
    @then_fail_throw.register(int)    
    def _then_fail_throw(self, obj, format=None, arguments=None):
        pass

    @staticmethod
    def add_exception_convertor(code_type, convertor):
        AbstractAssert.__exception_mapping[code_type] = convertor

    def get_result(self):
        return self.passed 