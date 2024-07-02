#!/usr/bin/python3
"""Defines unittests for models/base.py"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_no_arg(self):
        r = Base()
        r1 = r.id
        self.assertIsInstance(r1, int)

    def test_one_arg(self):
        r = Base(12)
        r1 = r.id
        self.assertIsInstance(r1, int)

    def test_one_val(self):
        r =Base(10)
        self.assertEqual(r.id, 10)
