import unittest
from 6-max_integer import max_integer

class TestTask_6(unittest.TestCase):

    test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 10, 0, 3, 90, 23, 90.01]), 90.01)
        self.assertEqual(max_integer(None), 0)
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3"])
        with assertRaises(TypeError):
            max_integer(1)
        with assertRaises(NameError):
            max_integer([1, 2, E])
