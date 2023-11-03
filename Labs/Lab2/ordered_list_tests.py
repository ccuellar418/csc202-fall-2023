import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):
    def test_add_function(self):
        t_list = doubly_Ordered_List(None, None)
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(30))
        self.assertTrue(t_list.add(40))
        self.assertTrue(t_list.add(50))
        self.assertFalse(t_list.add(10))

    def test_remove_function(self):
        t_list = doubly_Ordered_List(None, None)
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(30))
        self.assertTrue(t_list.add(40))
        self.assertTrue(t_list.add(50))
        self.assertTrue(t_list.remove(10))
        self.assertTrue(t_list.remove(20))
        self.assertTrue(t_list.remove(30))
        self.assertTrue(t_list.remove(40))
        self.assertTrue(t_list.remove(50))
        self.assertFalse(t_list.remove(10))
        self.assertFalse(t_list.remove(20))
        self.assertFalse(t_list.remove(30))
        self.assertFalse(t_list.remove(40))
        self.assertFalse(t_list.remove(50))

    def test_index_function(self):
        t_list = doubly_Ordered_List(None, None)
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(30))
        self.assertTrue(t_list.add(40))
        self.assertTrue(t_list.add(50))
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(20), 1)
        self.assertEqual(t_list.index(30), 2)
        self.assertEqual(t_list.index(40), 3)
        self.assertEqual(t_list.index(50), 4)

    def test_pop_function(self):
        t_list = doubly_Ordered_List(None, None)
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(30))
        self.assertTrue(t_list.add(40))
        self.assertTrue(t_list.add(50))
        self.assertEqual(t_list.pop(0), 10)
        self.assertEqual(t_list.pop(0), 20)
        self.assertEqual(t_list.pop(0), 30)
        self.assertEqual(t_list.pop(0), 40)
        self.assertEqual(t_list.pop(0), 50)

    def test_search_function(self):
        t_list = doubly_Ordered_List(None, None)
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(30))
        self.assertTrue(t_list.add(40))
        self.assertTrue(t_list.add(50))
        self.assertTrue(t_list.search(10))
        self.assertTrue(t_list.search(20))
        self.assertTrue(t_list.search(30))
        self.assertTrue(t_list.search(40))
        self.assertTrue(t_list.search(50))
        self.assertFalse(t_list.search(60))
        self.assertFalse(t_list.search(70))
        self.assertFalse(t_list.search(80))
        self.assertFalse(t_list.search(90))
        self.assertFalse(t_list.search(100))

    def test_python_list_function(self):
        t_list = doubly_Ordered_List(None, None)
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(30))
        self.assertTrue(t_list.add(40))
        self.assertTrue(t_list.add(50))
        self.assertEqual(t_list.python_list(), [10, 20, 30, 40, 50])

    def test_python_list_reversed_function(self):
        t_list = doubly_Ordered_List(None, None)
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(30))
        self.assertTrue(t_list.add(40))
        self.assertTrue(t_list.add(50))
        self.assertEqual(t_list.python_list_reversed(), [50, 40, 30, 20, 10])

    def test_size_function(self):
        t_list = doubly_Ordered_List(None, None)
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(30))
        self.assertTrue(t_list.add(40))
        self.assertTrue(t_list.add(50))
        self.assertEqual(t_list.size(), 5)

    def test_combined(self):
        t_list = doubly_Ordered_List(None, None)
        self.assertTrue(t_list.add(10))
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertEqual(t_list.pop(0), 10)


if __name__ == "__main__":
    unittest.main()
