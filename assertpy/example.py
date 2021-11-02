# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from assertpy.assertion import assert_that
from assertpy.base import AbstractAssert

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

    assert_that(1).is_not_none().is_one().then_fail_throw()
    n = {'a': 1}
    print(len(n))

