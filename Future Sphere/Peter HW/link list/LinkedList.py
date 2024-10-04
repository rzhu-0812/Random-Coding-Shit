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
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, index):
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if not current:
                raise IndexError("Index out of bounds")
            current = current.next
        if not current:
            raise IndexError("Index out of bounds") 
        new_node.next = current.next
        current.next = new_node
    
    def delete(self, data=None, index=None):
        if data and index:
            current = self.head
            if not current:
                return
            for _ in range(index - 1):
                if not current:
                    raise IndexError("Index out of bounds")
                current = current.next
            if not current or not current.next:
                raise IndexError("Index out of bounds")
            elif current.next.data != data:
                print("Data at index is incorrect")
            else:
                current.next = current.next.next
        elif data:
            current = self.head
            if current and current.data == data:
                self.head = current.next
                return
            if not current:
                return
            while current.next:
                if current.next.data == data:
                    current.next == current.next.next
                    return
                current = current.next
        elif index:
            if index == 0:
                self.head == self.head.next
                return
            current = self.head
            for _ in range(index - 1):
                if not current:
                    raise IndexError("Index out of bounds")
                current = current.next
            if not current:
                raise IndexError("Index out of bounds")
            current.next = current.next.next
            
            
    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == None:
                break
        return slow.data
    
    def remove_duplicates(self):
        if not self.head:
            return
        current = self.head
        while current:
            if current.data == current.next.data:
                current.next = current.next.next
            current = current.next
    

def merge_sorted_lists(list1, list2):
    dummy_node = Node(0)
    current = dummy_node
    
    pointer_1 = list1
    pointer_2 = list2

    while pointer_1 and pointer_2:
        if pointer_1.data <= pointer_2.data:
            current.next = pointer_1
            pointer_1 = pointer_1.next
        else:
            current.next = pointer_2
            pointer_2 = pointer_2.next
        current = current.next
    
    if pointer_1:   
        current.next = pointer_1
    if pointer_2:
        current.next = pointer_2
        
    return dummy_node.next