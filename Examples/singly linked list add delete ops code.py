from dataclasses import dataclass

@dataclass
class Node: # Data defination of Node
    value: int
    next_node: 'Node' = None # By using the type hint 'Node', it indicates that the next_node attribute is expected to be either a reference
    # to another Node object or None to indicate the end of the linked list.
@dataclass
class LinkedList:
    head: 'Node' = None # This refers to the Node class, indicating that the head attribute is expected to be an instance of the Node class.

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def traverse(self):
        if self.head==None:
            print("Linked List is empty")
        else:
         current_node = self.head
        while current_node is not None:
            print("\n",current_node.value)
            current_node = current_node.next_node


    def add_begin(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def add_last(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def add_in_between(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            current_position = 0
            while current_node is not None:
                if current_position == position - 1:
                    new_node.next_node = current_node.next_node
                    current_node.next_node = new_node
                    break
                current_node = current_node.next_node
                current_position += 1

    def delete_first_node(self):
        if self.head is not None:
            self.head = self.head.next_node

    def delete_last_node(self):
        if self.head is None:
            print("The Linked List is empty")
        if self.head.next_node is None:
            self.head = None
            print("The Linked List has only one node ")
        else:
            current_node = self.head
        while current_node.next_node.next_node is not None: # Checking two positions ahead of a current node unless we find second last node
            current_node = current_node.next_node

        current_node.next_node = None

    def delete_in_between(self, value):
        if self.head is None:
           print("Linked List is empty")

        elif self.head.value == value:
            self.head = self.head.next_node # if targeted value is the head value

        else:
             current_node = self.head
        while current_node.next_node is not None:
            if current_node.next_node.value == value:
                current_node.next_node = current_node.next_node.next_node
                return
            current_node = current_node.next_node


    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next_node



linked_list = LinkedList()
linked_list.append(23)
linked_list.append(54)
linked_list.append(78)
linked_list.append(90)

#linked_list.add_begin(20)
#linked_list.add_last(10)
#linked_list.add_in_between(30,3)


#linked_list.delete_first_node()
#linked_list.delete_last_node()
#linked_list.delete_in_between(30)

linked_list.display()
#linked_list.traverse()
