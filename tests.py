import unittest
from pancake import valid_pancake_case
from pancake import calculate_flips

class TestPancakeCases(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(valid_pancake_case(''), False)

    def test_large(self):
        self.assertEqual(valid_pancake_case('+' * 101), False)

    def test_string(self):
        self.assertEqual(valid_pancake_case('a1' * 50), False)

    def test_pass(self):
        self.assertEqual(valid_pancake_case('+' * 50), True)

    def test_flip_all_up(self):
        self.assertEqual(calculate_flips('+' * 50), 0)

    def test_flip_all_down(self):
        self.assertEqual(calculate_flips('+' * 50), 0)

    def test_flip_all_down(self):
        self.assertEqual(calculate_flips('-' * 11), 1)

    def test_flip_1(self):
        self.assertEqual(calculate_flips('-'), 1)

    def test_flip_2(self):
        self.assertEqual(calculate_flips('-+'), 1)

    def test_flip_3(self):
        self.assertEqual(calculate_flips('+-'), 2)

    def test_flip_4(self):
        self.assertEqual(calculate_flips('--+-'), 3)

    def test_flip_5(self):
        self.assertEqual(calculate_flips('-+-++----+++++---'), 7)
