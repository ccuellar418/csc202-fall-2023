from dataclasses import dataclass
@dataclass
class Node:
    value: int
    left_child: 'Node' = None
    right_child: 'Node' = None


@dataclass
class BinaryTree:
    root: Node = None  # top of the tree

    def isBST(self, root):
        if root != None:
            if root.left_child.value > root.value or root.right_child.value < root.value:
                return False
            else:
                left_child = root.left_child.value
                self.isBST(self, left_child)
                right_child = root.right_child
                self.isBST(self, right_child)
                return self.isBST(root.left_child) and self.isBST(root.right_child)

    #2. Implement the convertToSortedArray() method to convert
    #the BST into a sorted array.
    def convertToSortedArray(self,root):
        sorted_values = []
        if root != None:
            in_order_traversal(root, sorted_values)
            current_node = self.head
            return(self.recursive_convertToSortedArray(self, current_node))
    def recursive_convertToSortedArray(self,node):
        if node != None:
            self.recursive_convertToSortedArray(self, node.left_child)

'''    def in_order_traversal(node):
        if node is not None:
            in_order_traversal(node.left_child)
            yield node.value
            in_order_traversal(node.right_child)

    def convertToSortedArray(root):
        sorted_values = []
        for value in in_order_traversal(root):
            sorted_values.append(value)

        return sorted_values
'''
    def in_order_traversal(self,node,sorted_values):
        if node is not None:
            in_order_traversal(node.left_child)
            sorted_values.append(node.value)
            in_order_traversal(node.right_child)

    in_order_traversal(root)

    return sorted_array

    def insert(self, value):
        if not self.root:
            self.root = Node(value)  # if the tree is empty, it creates a new node as the root
        else:  # but if it isn't empty, it calls the recursive insertion function
            self._insert_recursive(self.root,
                                   value)  # recursive function that will keep going through the Binary Tree until the value is in a position that it should be and then inserts it

    # If the value is smaller, it checks if the current node has a left child. If it does, it recursively
    # calls itself with the left child as the new current node. If not, it creates a new node with the given
    # value and assigns it as the left child of the current node.
    # and it does the same with the right side

    def _insert_recursive(self, current_node, value):  # THIS HAS TO DO WIHT THE INSERT FUNCTION
        if value < current_node.value:  # this makes sense to me, basically saying if the one you are inserting is less than the one we are checking
            if current_node.left_child is not None:
                self._insert_recursive(current_node.left_child,
                                       value)  # go down the left of the subtree (go down and make left_child the root of the new subtree)
            else:
                current_node.left_child = Node(value)  # if not, create a new node as the left child
        elif value > current_node.value:  # if what we are trying to insert is greater than the bubble we are looking at
            if current_node.right_child is not None:
                self._insert_recursive(current_node.right_child,
                                       value)  # then we go down the right side of the subtree(go down and make right_child the root of the new subtree
            else:
                current_node.right_child = Node(value)  # If not, create a new node as the right_child
        else:
            # Value already exists in the tree, handle as per your requirement.
            pass

    def search(self,
               value):  # recursively compares the target value (the value we are looking to see if it is in the tree or not, then returns true or false)
        return self._search_recursive(self.root, value)  # where the recursion occurs

    def _search_recursive(self, current_node, value):  # the recursion function
        if not current_node:  # checks if there is even nodes in the tree
            return False
        if current_node.value == value:  # if it finds the value it was searching for, it returns true
            return True
        elif value < current_node.value:  # if the value we are searching for is less than the current_node (the node we are looking at that is apart of the tree), it will go to the left and call the recursive function
            return self._search_recursive(current_node.left_child, value)
        else:
            return self._search_recursive(current_node.right_child,
                                          value)  # otherwise the only other option is that the value we are searching for is greater than the current_node (the node we are looking at that is apart of the tree), it will go to the right and call the recursive function.

    def delete(self, value):  # calls the delete_recursive function
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):  # this is the recursion function
        if current_node is None:  # if there are no nodes in the tree, it will return the current_node, which is showing there is nothing to delete
            return current_node  # If the tree is empty or the node is not found, return None.
        # Recursive calls for ancestors of the node to be deleted.

        if value < current_node.value:  # if the value we are trying to delete is less than the current_node we are looking at on the tree, it will go down the left side of the subtree, and call itself recursively
            current_node.left_child = self._delete_recursive(current_node.left_child,
                                                             value)  # Recur down the left subtree if the value is smaller.
        elif value > current_node.value:  # if the value we are trying to delete is greater than the current_node we are looking at on the tree, it will go down the right side of the subtree, and call itself recursively
            current_node.right_child = self._delete_recursive(current_node.right_child,
                                                              value)  # Recur down the left subtree if the value is greator.
        else:
            # Node with only one child or no child
            if current_node.left_child is None:  # If no left child, replace with the right child (?)
                temp_node = current_node.right_child
                del current_node
                return temp_node
            elif current_node.right_child is None:  # if no right child, replace with the left child (?)
                temp_node = current_node.left_child
                del current_node
                return temp_node

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            current_node.value = self._find_min_value(
                current_node.right_child)  # replace node's value with inorder successor (?)

            # Delete the inorder successor
            current_node.right_child = self._delete_recursive(current_node.right_child,
                                                              current_node.value)  # deletes the nodes' successor node (????)

        return current_node

    def _find_min_value(self, node):
        current = node
        while current.left_child is not None:  # if there is a left_child
            current = current.left_child  # make the current = to the left_child (bc the left child will be less than the right, and also less than the current_node)
        return current.value  # return it


# Example usage:
if __name__ == "__main__":
    binary_tree = BinaryTree()
    elements = [44, 17, 88, 8, 32, 65, 97, 54, 82, 93, 78, 80]

    for element in elements:
        binary_tree.insert(element)

    print(binary_tree.search(65))  # Output: True
    print(binary_tree.search(9))  # Output: False
    print("Original Binary Search Tree:")
    print(binary_tree.search(65))  # Output: True

    # Deleting a node with one child
    binary_tree.delete(65)
    print("Binary Search Tree after deleting 65:")
    print(binary_tree.search(65))  # Output: False

    # Deleting a node with no children
    binary_tree.delete(8)
    print("Binary Search Tree after deleting 8:")
    print(binary_tree.search(8))  # Output: False

    # Deleting a node with two children
    binary_tree.delete(88)
    print("Binary Search Tree after deleting 88:")
    print(binary_tree.search(88))  # Output: False