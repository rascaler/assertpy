# !/usr/bin/env python
# -*- coding: utf-8 -*-
class CollectionUtils:

    @staticmethod
    def is_empty(coll):
        return coll is None or len(coll) == 0

    @staticmethod
    def contains_all(coll1, coll2):
        if CollectionUtils.is_empty(coll2):
            return True
        elements_already_seen = set()
        for next_element in coll2:
            if next_element in elements_already_seen:
                continue
            found_current_element = False
            for p in coll1:
                elements_already_seen.add(p)
                if p is None if next_element is None else next_element == p:
                    found_current_element = True
                    break
            if not found_current_element:
                return False
        return True
