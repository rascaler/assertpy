# !/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta, ABC

from assertpy.base import AbstractAssert, AbstractSizeComparableAssert, Assert, SizeComparableAssert
from assertpy.utils import CollectionUtils


class CollectionAssert(metaclass=ABCMeta):
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def is_not_empty(self):
        pass

    @abstractmethod
    def has_empty_element(self):
        pass

    @abstractmethod
    def contains_all(self, values):
        pass

    @abstractmethod
    def contains_any(self, values):
        pass

    @abstractmethod
    def contains_none(self, values):
        pass

    @abstractmethod
    def has_any_in(self, values):
        pass

    @abstractmethod
    def is_all_in(self, values):
        pass

    @abstractmethod
    def has_none_in(self, values):
        pass


class AbstractCollectionAssert(CollectionAssert, AbstractSizeComparableAssert, AbstractAssert, ABC):
    def __init__(self, actual):
        super(AbstractCollectionAssert, self).__init__(actual)

    @abstractmethod
    def get(self, index):
        pass

    def is_empty(self):
        if not self.passed:
            return self
        self.passed = self.actual is None or self.size() == 0
        return self

    def is_not_empty(self):
        if not self.passed:
            return self
        self.passed = self.actual is not None and self.size() > 0
        return self

    def has_empty_element(self):
        if not self.passed:
            return self
        for obj in self.actual:
            if obj is None:
                self.passed = True
                return self
        self.passed = False
        return self

    def contains_all(self, values):
        if not self.passed:
            return self
        self.passed = CollectionUtils.contains_all(self.actual, values)
        return self

    def contains_any(self, values):
        if not self.passed:
            return self
        if self.size() < len(values):
            if self._any_in(values):
                self.passed = True
                return self
        else:
            for coll2 in values:
                if self._contains(coll2):
                    self.passed = True
                    return self
        self.passed = False
        return self

    def contains_none(self, values):
        if not self.passed:
            return self
        if self.size() < len(values):
            if self._any_in(values):
                self.passed = False
                return self
        else:
            for coll2 in values:
                if self._contains(coll2):
                    self.passed = False
                    return self
        self.passed = True
        return self

    def has_any_in(self, values):
        if not self.passed:
            return self
        self.passed = self._any_in(values)
        return self

    def is_all_in(self, values):
        if not self.passed:
            return self
        if self.actual is None or self.size() == 0:
            self.passed = True
            return self
        elements_already_seen = set()
        for i in range(self.size()):
            next_element = self.get(i)
            if next_element in elements_already_seen:
                continue
            found_current_element = False
            for p in values:
                elements_already_seen.add(p)
                if p is None if next_element is None else next_element == p:
                    found_current_element = True
                    break
            if not found_current_element:
                self.passed = False
                return self
        self.passed = True
        return self

    def has_none_in(self, values):
        if not self.passed:
            return self
        self.passed = not self._any_in(values)
        return self

    def _contains(self, value_to_find):
        for i in range(self.size()):
            next_value = self.get(i)
            if next_value == value_to_find:
                return True
        return False

    def _any_in(self, values):
        for i in range(self.size()):
            next_value = self.get(i)
            if next_value in values:
                return True
        return False


class DefaultCollectionAssert(AbstractCollectionAssert):
    def __init__(self, actual):
        super(AbstractCollectionAssert, self).__init__(actual)

    def get(self, index):
        return self.actual[index]

    def size(self):
        return len(self.actual)