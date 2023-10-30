import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):
    def test_simple(self):
        t_list = doubly_Ordered_List(None, None)
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_complex(self):
        complex_list = doubly_Ordered_List(None, None)
        complex_list.add(10)
        complex_list.add(20)
        complex_list.add(30)
        complex_list.add(40)
        complex_list.add(50)
        self.assertEqual(complex_list.python_list(), [10, 20, 30, 40, 50])
        self.assertEqual(complex_list.index(30), 2)
        self.assertTrue(complex_list.search(30))
        self.assertFalse(complex_list.is_empty())
        self.assertEqual(complex_list.python_list_reversed(), [50, 40, 30, 20, 10])
        self.assertTrue(complex_list.remove(10))
        complex_list.add(10)
        self.assertEqual(complex_list.pop(0), 10)
        self.assertEqual(complex_list.size(), 5)


if __name__ == "__main__":
    unittest.main()
