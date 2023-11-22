from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int = None
    left_child: "TreeNode" = None
    right_child: "TreeNode" = None


@dataclass
class BST:
    root: TreeNode = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child is not None:
                self._insert_recursive(current_node.left_child, value)
            else:
                current_node.left_child = TreeNode(value)
        elif value > current_node.value:
            if current_node.right_child is not None:
                self._insert_recursive(current_node.right_child, value)
            else:
                current_node.right_child = TreeNode(value)
        else:
            # Value already exists in the tree, handle as per your requirement.
            pass

    def pre_order_traversal(self):
        self._pre_order_recursive(self.root)
        print()

    def _pre_order_recursive(self, current_node):
        if current_node is not None:
            print(current_node.value, end=" ")
            self._pre_order_recursive(current_node.left_child)
            self._pre_order_recursive(current_node.right_child)

    def in_order_traversal(self):
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, current_node):
        if current_node is not None:
            self._in_order_recursive(current_node.left_child)
            print(current_node.value, end=" ")
            self._in_order_recursive(current_node.right_child)

    def post_order_traversal(self):
        self._post_order_recursive(self.root)
        print()

    def _post_order_recursive(self, current_node):
        if current_node is not None:
            self._post_order_recursive(current_node.left_child)
            self._post_order_recursive(current_node.right_child)
            print(current_node.value, end=" ")

    def isBST(self) -> bool:
        return self._isBST(self.root)

    def _isBST(self, current_node) -> bool:
        if current_node is not None:
            if current_node.left_child is not None:
                if current_node.left_child.value > current_node.value:
                    return False
                else:
                    self._isBST(current_node.left_child)
            if current_node.right_child is not None:
                if current_node.right_child.value < current_node.value:
                    return False
                else:
                    self._isBST(current_node.right_child)
            return True
        else:
            return True

    def convertToSortedArray(self) -> list:
        return self._convertToSortedArray(self.root, [])

    def _convertToSortedArray(self, current_node, sorted_array) -> list:
        if current_node is None or sorted_array is None:
            return []
        else:
            if current_node.left_child is not None:
                self._convertToSortedArray(current_node.left_child, sorted_array)
            sorted_array.append(current_node.value)
            if current_node.right_child is not None:
                self._convertToSortedArray(current_node.right_child, sorted_array)
            return sorted_array

    def lowestCommonAncestor(self) -> int:
        return self._lowestCommonAncestor(self.root)

    def _lowestCommonAncestor(self, current_node) -> int:
        if current_node is not None:
            if current_node.left_child is not None:
                self._lowestCommonAncestor(current_node.left_child)
            if current_node.right_child is not None:
                self._lowestCommonAncestor(current_node.right_child)
            return current_node.value
        else:
            return None

    def deleteTreeRecursive(self, node):
        if node:
            self.deleteTreeRecursive(node.left_child)
            self.deleteTreeRecursive(node.right_child)

            node.left_child = None
            node.right_child = None
        else:
            self.root = None

    def deleteTree(self):
        self.deleteTreeRecursive(self.root)
