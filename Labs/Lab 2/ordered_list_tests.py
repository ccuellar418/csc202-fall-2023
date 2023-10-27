import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):
    def test_simple(self):
        t_list = doubly_Ordered_List(None, None)
        t_list.add(10, t_list.head)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10, t_list.head))
        self.assertEqual(t_list.size(), 0)
        self.assertFalse(t_list.is_empty())
        t_list.add(10, t_list.head)
        self.assertEqual(t_list.pop(0), 10)

    def test_ronan(self):
        t_list = doubly_Ordered_List(None, None)
        t_list.add(2, t_list.head)
        t_list.add(1, t_list.head)
        t_list.add(107, t_list.head)
        t_list.add(55, t_list.head)
        t_list.add(32, t_list.head)
        t_list.remove(2, t_list.head)
        t_list.remove(107, t_list.head)
        t_list.remove(108, t_list.head)
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.head.value, 1)
        self.assertEqual(t_list.head.next_node.value, 32)
        self.assertEqual(t_list.head.next_node.next_node.value, 55)

    def test_complex(self):
        complex_list = doubly_Ordered_List(None, None)
        complex_list.add(10, complex_list.head)
        complex_list.add(20, complex_list.head)
        complex_list.add(30, complex_list.head)
        complex_list.add(40, complex_list.head)
        complex_list.add(50, complex_list.head)
        self.assertEqual(complex_list.python_list(), [10, 20, 30, 40, 50])
        self.assertEqual(complex_list.size(), 5)
        self.assertEqual(complex_list.index(30), 2)
        self.assertTrue(complex_list.search(30))
        self.assertFalse(complex_list.is_empty())
        self.assertEqual(complex_list.python_list_reversed(), [50, 40, 30, 20, 10])
        self.assertTrue(complex_list.remove(10))
        complex_list.add(10)
        self.assertEqual(complex_list.pop(0), 10)


if __name__ == "__main__":
    unittest.main()
