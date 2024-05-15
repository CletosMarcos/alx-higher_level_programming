import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    test_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([9, 8, 7, 6]), 9)

    test_floats(self):
        self.assertEqual(max_integer([1, 10, 0, 3, 90, 23, 90.01]), 90.01)
        self.assertEqual(max_integer([1.1, 2.5, 5.001, 5.0001]), 5.0001)

    test_ints_and_floats(self):
        self.assertEqual(maxx_integer([1, 2, 2.1, 6, 9.0, 9.1, 8], 9.1))

    test_no_argument(self):
        self.assertIsNone(max_integer())


    test_mix_values_and_strings(self)
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3"])

    test_pass_a_number(self):
        with assertRaises(TypeError):
            max_integer(1)

    test_undefined_variable(self):
        with assertRaises(NameError):
            max_integer([1, 2, E])

    test_strings(self):
        self.assertEqual(max_integer("lsdfg9"))
