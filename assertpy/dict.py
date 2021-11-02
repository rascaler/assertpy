# !/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from assertpy.base import AbstractAssert
from assertpy.utils import CollectionUtils


class DictAssert(metaclass=ABCMeta):
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def is_not_empty(self):
        pass

    @abstractmethod
    def contains_key(self, key):
        pass

    @abstractmethod
    def contains_keys(self, keys):
        pass

    @abstractmethod
    def does_not_contain_key(self, key):
        pass

    @abstractmethod
    def does_not_contain_keys(self, keys):
        pass

    @abstractmethod
    def contains_value(self, value):
        pass

    @abstractmethod
    def contains_values(self, values):
        pass

    @abstractmethod
    def does_not_contain_value(self, value):
        pass

    @abstractmethod
    def does_not_contain_values(self, values):
        pass


class DefaultDictAssert(DictAssert, AbstractAssert):
    def __init__(self, actual):
        super(DefaultDictAssert, self).__init__(actual)

    def is_empty(self):
        if not self.passed:
            return self
        self.passed = self.passed is None or len(self.actual) == 0
        return self

    def is_not_empty(self):
        if not self.passed:
            return self
        self.passed = self.passed is not None and len(self.actual) > 0
        return self

    def contains_key(self, key):
        if not self.passed:
            return self
        self.passed = key in self.actual
        return self

    def contains_keys(self, keys):
        if not self.passed:
            return self
        self.passed = CollectionUtils.contains_all(self.actual.keys(), keys)
        return self

    def does_not_contain_key(self, key):
        if not self.passed:
            return self
        self.passed = not (key in self.actual)
        return self

    def does_not_contain_keys(self, keys):
        if not self.passed:
            return self
        self.passed = not CollectionUtils.contains_all(self.actual.keys(), keys)
        return self

    def contains_value(self, value):
        if not self.passed:
            return self
        self.passed = value in self.actual.values()
        return self

    def contains_values(self, values):
        if not self.passed:
            return self
        self.passed = CollectionUtils.contains_all(self.actual.values(), values)
        return self

    def does_not_contain_value(self, value):
        if not self.passed:
            return self
        self.passed = not (value in self.actual.values())
        return self

    def does_not_contain_values(self, values):
        if not self.passed:
            return self
        self.passed = not CollectionUtils.contains_all(self.actual.values(), values)
        return self
