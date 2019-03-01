class BinarySearchTree:
    def __init__(self, value=0, left=None, right=None, items=None):
        self.value = value
        self.left = left
        self.right = right
        self._size = 1
        self.items = set()
    
    def print_tree(self):
        old_current = self
        current_node = self
        self.items.add(current_node.value)
        while current_node:
            if current_node.right: self.items.add(current_node.right.value)
            if current_node.left: self.items.add(current_node.left.value)
            current_node = current_node.left
        while old_current:
            if old_current.right: self.items.add(old_current.right.value)
            if old_current.left: self.items.add(old_current.left.value)
            old_current = old_current.right
        print(sorted(list(self.items)))
        

    def size(self):
        return self._size
    
    def insert(self, value):
        new_node = BinarySearchTree(value)
        current_node = self
        if new_node.value < current_node.value:
            if current_node.left == None:
                current_node.left = new_node
            else:
                current_node = current_node.left
                return current_node.insert(new_node.value)
        if new_node.value > current_node.value:
            if current_node.right == None:
                current_node.right = new_node
            else:
                current_node = current_node.right
                return current_node.insert(new_node.value)
        self._size += 1

    def contains(self, value):
        current_node = self
        if current_node.value == value: 
            return True
        if value < current_node.value:
            if current_node.left:
                current_node = current_node.left
                return current_node.contains(value)
        if value > current_node.value:
            if current_node.right:
                current_node = current_node.right
                return current_node.contains(value)
        return False
            

bst = BinarySearchTree(20)
bst.insert(25)
bst.insert(33)
bst.insert(27)
bst.insert(10)
bst.insert(5)
bst.insert(2.5)
bst.insert(15)
bst.insert(1.25)
bst.insert(7)
bst.print_tree()
print("COUNT", bst.size())
print(bst.contains(15))