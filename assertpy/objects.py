# !/usr/bin/env python
# -*- coding: utf-8 -*-
from assertpy.base import AbstractAssert


class ObjectAssert(AbstractAssert):
    def __init__(self, actual):
        super(ObjectAssert, self).__init__(actual)
