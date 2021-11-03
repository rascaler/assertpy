# !/usr/bin/env python
# -*- coding: utf-8 -*-
from assertpy.base import AbstractAssert


class BooleanAssert(AbstractAssert):
    def __init__(self, actual):
        super(BooleanAssert, self).__init__(actual)

    def is_true(self):
        """
        :rtype: BooleanAssert
        """
        if not self.passed:
            return self
        self.passed = self.actual
        return self

    def is_false(self):
        """
        :rtype: BooleanAssert
        """
        if not self.passed:
            return self
        self.passed = not self.actual
        return self
