class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self, node):
        self.head = node
        self.size = 1
    
    def get_size(self):
        return f"Size: {self.size}"
    
    def append(self, value):
        current_node = self.head
        previous_node = None
        while current_node:
            previous_node = current_node
            current_node = current_node.next
        current_node = Node(value)
        previous_node.next = current_node
        self.size += 1

    def delete(self, value):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.value == value:
                previous_node.next = current_node.next
                break
            previous_node = current_node
            current_node = current_node.next
    
    def print_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

n1 = Node(5)
sll = SinglyLinkedList(n1)
sll.append(10)
sll.append(15)
sll.delete(10)
print(sll.print_nodes())