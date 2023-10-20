from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left_child: 'Node' = None
    right_child: 'Node' = None

@dataclass
class BinaryTree:
    root: Node = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child is not None:
                self._insert_recursive(current_node.left_child, value)
            else:
                current_node.left_child = Node(value)
        elif value > current_node.value:
            if current_node.right_child is not None:
                self._insert_recursive(current_node.right_child, value)
            else:
                current_node.right_child = Node(value)
        else:
            # Value already exists in the tree, handle as per your requirement.
            pass

    def pre_order_traversal(self):
        self._pre_order_recursive(self.root)
        print()

    def _pre_order_recursive(self, current_node):
        if current_node is not None:
            print(current_node.value, end=' ')
            self._pre_order_recursive(current_node.left_child)
            self._pre_order_recursive(current_node.right_child)

    def in_order_traversal(self):
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, current_node):
        if current_node is not None:
            self._in_order_recursive(current_node.left_child)
            print(current_node.value, end=' ')
            self._in_order_recursive(current_node.right_child)

    def post_order_traversal(self):
        self._post_order_recursive(self.root)
        print()

    def _post_order_recursive(self, current_node):
        if current_node is not None:
            self._post_order_recursive(current_node.left_child)
            self._post_order_recursive(current_node.right_child)
            print(current_node.value, end=' ')

# Example usage:
if __name__ == "__main__":
    bt = BinaryTree()
    elements = [44, 17, 88, 8, 32, 65, 97,28,54,82,93,29,78,80]
    for elem in elements:
        bt.insert(elem)

    print("Pre-order Traversal:")
    bt.pre_order_traversal()

    print("In-order Traversal:")
    bt.in_order_traversal()

    print("Post-order Traversal:")
    bt.post_order_traversal()
