# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from assertpy.assertions import assert_that
from assertpy.base import AbstractAssert
from assertpy.collection import DefaultCollectionAssert

if __name__ == "__main__":
    a = AbstractAssert(None)
    # a.is_not_none().then_fail_throw(Exception('失败'))
    # a.then_fail_throw('sss', 'adfaf')
    # m = {'a': 1}
    # print(1 in m)
    a = (1, 2)
    t1 = time.time()
    time.sleep(2)
    t2 = time.time()
    print(t1 < t2)

    m = "1.9"
    print("a1" in "aaa")

    print(m.isdigit())

    n = {'a': 1}
    print(len(n))
    assert_that((1)).has_one_size().then_fail_throw(Exception('失败'))
    pass
