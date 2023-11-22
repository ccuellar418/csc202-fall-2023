import unittest
from lab3 import *


class TestLab3(unittest.TestCase):
    def test_isBST_empty_tree(self):
        tree = BST()
        self.assertTrue(tree.isBST())

    def test_isBST_invalid_tree(self):
        tree = BST()
        tree.root = TreeNode(5)
        tree.root.left_child = TreeNode(10)
        tree.root.right_child = TreeNode(1)
        self.assertFalse(tree.isBST())

    def test_isBST_valid_tree(self):
        tree = BST()
        tree.root = TreeNode(5)
        tree.root.left_child = TreeNode(1)
        tree.root.right_child = TreeNode(10)
        self.assertTrue(tree.isBST())

    def test_convert_to_sorted_array_empty_tree(self):
        tree = BST()
        self.assertEqual(tree.convertToSortedArray(), [])

    def test_convert_to_sorted_array_valid_tree(self):
        tree = BST()
        tree.root = TreeNode(5)
        tree.root.left_child = TreeNode(1)
        tree.root.right_child = TreeNode(10)
        self.assertEqual(tree.convertToSortedArray(), [1, 5, 10])

    def test_convert_to_sorted_array_complex_tree(self):
        tree = BST()
        tree.root = TreeNode(5)
        tree.root.left_child = TreeNode(1)
        tree.root.right_child = TreeNode(10)
        tree.root.right_child.right_child = TreeNode(15)
        self.assertEqual(tree.convertToSortedArray(), [1, 5, 10, 15])

    def test_lowest_common_ancestor_empty_tree(self):
        tree = BST()
        self.assertEqual(tree.lowestCommonAncestor(), None)

    def test_lowest_common_ancestor_valid_tree(self):
        tree = BST()
        tree.root = TreeNode(5)
        tree.root.left_child = TreeNode(1)
        tree.root.right_child = TreeNode(10)
        self.assertEqual(tree.lowestCommonAncestor(), 5)

    def test_lowest_common_ancestor_different_level_nodes(self):
        tree = BST()
        tree.root = TreeNode(5)
        tree.root.left_child = TreeNode(1)
        tree.root.right_child = TreeNode(10)
        tree.root.right_child.right_child = TreeNode(15)
        self.assertEqual(tree.lowestCommonAncestor(), 5)

    def test_lowest_common_ancestor_one_node_ancestor(self):
        tree = BST()
        tree.root = TreeNode(5)
        tree.root.left_child = TreeNode(1)
        tree.root.right_child = TreeNode(10)
        tree.root.right_child.right_child = TreeNode(15)
        self.assertEqual(tree.lowestCommonAncestor(), 5)

    def test_lowest_common_ancestor_extreme_case(self):
        tree = BST()
        tree.root = TreeNode(5)
        tree.root.left_child = TreeNode(1)
        tree.root.right_child = TreeNode(10)
        tree.root.right_child.right_child = TreeNode(15)
        tree.root.right_child.right_child.right_child = TreeNode(20)
        self.assertEqual(tree.lowestCommonAncestor(), 5)

    def test_delete_tree_empty_tree(self):
        tree = BST()
        tree.deleteTree()
        self.assertEqual(tree.root, None)

    def test_delete_tree_valid_tree(self):
        tree = BST()
        tree.root = TreeNode(5)
        tree.root.left_child = TreeNode(1)
        tree.root.right_child = TreeNode(10)
        tree.deleteTree()
        self.assertEqual(tree.root, None)


if __name__ == "__main__":
    unittest.main()
