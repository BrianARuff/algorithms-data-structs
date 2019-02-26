# Why linked list?
# 1. Array size is fixed to the upper limit
# 2. inserting new elements into arrays is expensive because of item shifting depending on where it's inserted at
# 3. Dynamic size
# 4. Ease of insertion and deletion

# Drawbacks
# 1. Random access is not allowed. Sequential access only starting from the first node. No binary searching!
# 2. Extra memory space for the pointer
# 3. WHAT IS LOCALITY OF REFERENCE??

# Representation
# 1. represented by a pointer to the first node of the linked list (the head).
    # a. If the LL is empty then the value of the head is NULL.
# 2. Each node consist of two parts
    # a. data
    # b. pointer to the next node
# 3. class Node && class LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # next starts as None

    def __repr__(self):
        return f"{self.data}"

class LinkedList:
    def __init__(self, head):
        self.head = Node(head)
        self.length = 1
    
    def print_all(self):
        current = self.head
        print(current.data)
        while current.next != None:
            current = current.next
            print(current.data)
    
    def append(self, value):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(value)
        self.length += 1
    
    def delete(self, value):
        current = self.head
        while current.next != None:
            current = current.next
            if current.data == value:
                current.data = None

    def replace_next(self, curr_value, value):
        current = self.head
        found = False
        while current != None:
            tmp = 0
            if current.data == curr_value:
                tmp = current
                current = current.next
                current.data = value
            current = current.next
        current = tmp


    def size(self):
        return f"Length: {self.length}"
            
            

if __name__ == "__main__":
    ll = LinkedList(5)
    ll.append(10)
    ll.delete(10)
    ll.append(15)
    ll.replace_next(5, 10)
    ll.replace_next(5, 12.5)
    ll.print_all()
    