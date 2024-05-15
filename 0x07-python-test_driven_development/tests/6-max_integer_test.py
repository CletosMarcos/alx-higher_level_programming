import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([9, 8, 7, 6]), 9)

    def test_floats(self):
        self.assertEqual(max_integer([1, 10, 0, 3, 90, 23, 90.01]), 90.01)
        self.assertEqual(max_integer([1.1, 2.5, 5.001, 5.0001]), 5.0001)

    def test_ints_and_floats(self):
        self.assertEqual(maxx_integer([1, 2, 2.1, 6, 9.0, 9.1, 8], 9.1))

    def test_no_argument(self):
        self.assertIsNone(max_integer())


    def test_mix_values_and_strings(self)
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3"])

    def test_pass_a_number(self):
        with assertRaises(TypeError):
            max_integer(1)

    def test_undefined_variable(self):
        with assertRaises(NameError):
            max_integer([1, 2, E])

    def test_strings(self):
        self.assertEqual(max_integer("lsdfg9"))
