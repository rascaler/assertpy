# !/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta

from assertpy.base import AbstractAssert


class StringAssert(metaclass=ABCMeta):

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def is_not_empty(self):
        pass

    @abstractmethod
    def is_blank(self):
        pass

    @abstractmethod
    def is_not_blank(self):
        pass

    @abstractmethod
    def starts_with(self, prefix):
        pass

    @abstractmethod
    def does_not_start_with(self, prefix):
        pass

    @abstractmethod
    def ends_with(self, suffix):
        pass

    @abstractmethod
    def does_not_end_with(self, suffix):
        pass

    @abstractmethod
    def contains(self, search_str):
        pass

    @abstractmethod
    def does_not_contain(self, search_str):
        pass

    @abstractmethod
    def is_all_Lower_case(self):
        pass

    @abstractmethod
    def is_all_upper_case(self):
        pass

    @abstractmethod
    def is_number_creatable(self):
        pass


class DefaultStringAssert(StringAssert, AbstractAssert):
    def __init__(self, actual):
        super(DefaultStringAssert, self).__init__(actual)

    def is_empty(self):
        if not self.passed:
            return self
        self.passed = self.passed is None or self.passed == ""
        return self

    def is_not_empty(self):
        if not self.passed:
            return self
        self.passed = self.passed is not None and self.passed != ""
        return self

    def is_blank(self):
        if not self.passed:
            return self
        self.passed = not (self.actual and self.actual.strip())
        return self

    def is_not_blank(self):
        if not self.passed:
            return self
        self.passed = self.actual and self.actual.strip()
        return self

    def starts_with(self, prefix):
        if not self.passed:
            return self
        self.passed = self.actual.startswith(prefix)
        return self

    def does_not_start_with(self, prefix):
        if not self.passed:
            return self
        self.passed = not self.actual.startswith(prefix)
        return self

    def ends_with(self, suffix):
        if not self.passed:
            return self
        self.passed = self.actual.endswith(suffix)
        return self

    def does_not_end_with(self, suffix):
        if not self.passed:
            return self
        self.passed = not self.actual.endswith(suffix)
        return self

    def contains(self, search_str):
        if not self.passed:
            return self
        self.passed = search_str in self.actual
        return self

    def does_not_contain(self, search_str):
        if not self.passed:
            return self
        self.passed = not (search_str in self.actual)
        return self

    def is_all_Lower_case(self):
        if not self.passed:
            return self
        self.passed = self.actual.islower()
        return self

    def is_all_upper_case(self):
        if not self.passed:
            return self
        self.passed = self.actual.isupper()
        return self

    def is_number_creatable(self):
        if not self.passed:
            return self
        try:
            float(self.actual)
            self.passed = True
            return self
        except ValueError:
            self.passed = False
            return self
