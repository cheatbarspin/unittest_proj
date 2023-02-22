import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get_equals(self):
        self.assertEqual(arrs.get([1, 2, 3], 2, default="test"), 3)

    def test_get_raises(self):
        with self.assertRaises(IndexError):
            self.assertEqual(arrs.get([], 0, default="test"), "test")

    def test_get_default(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, default="test"), 'test')

    def test_slice_1(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])

    def test_slice_2(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_3(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -5, 3), [1, 2, 3])

    def test_slice_4(self):
        self.assertEqual(arrs.my_slice([], 1, 3), [])

    def test_slice_5(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2, 4), [3, 4])
