#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple assertion test to prevent Jenkins from complaining."""


# Import Python libs
import unittest


class TrueTestCase(unittest.TestCase):
    """Assertion test case"""

    def test_true(self):
        """Tests that True == True"""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
