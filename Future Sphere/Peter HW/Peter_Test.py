class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next
        
        current.next = new_node

    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None

        for _ in range(index):
            if not current:
                print("Index out of bounds")
                return
            prev = current
            current = current.next
        
        if not current:
            print("Index out of bounds")
            return
        
        prev.next = current.next
    
    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(index - 1):
            if not current:
                print("Index out of bounds")
                return
            current = current.next
        
        if not current:
            print("Index out of bounds")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def print_list(self):
        ll_list = []
        current = self.head

        while current is not None:
            ll_list.append(current.data)
            current = current.next
        
        return ll_list
    
    def search(self, data):
        current = self.head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1

    def get(self, index):
        if index == 0:
            return self.head.data
        
        current = self.head

        for _ in range(index):
            if not current:
                print("Index out of bounds")
                return
            current = current.next
        
        if not current:
            print("Index out of bounds")
            return
        
        return current.data
    
    def update(self, index, data):
        if index == 0:
            self.head.data = data
        
        current = self.head

        for _ in range(index):
            if not current:
                print("Index out of bounds")
                return
            current = current.next
        
        if not current:
            print("Index out of bounds")
            return
        
        current.data = data

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.prepend(0)
ll1.insert(4, 4)
ll1.delete(3)
print(ll1.search(3))
print(ll1.get(1))
ll1.update(1, 100)
print(ll1.print_list())
