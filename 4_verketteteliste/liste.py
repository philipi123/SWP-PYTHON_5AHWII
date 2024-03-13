import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

if __name__ == "__main__":
    ll = LinkedList()
    for _ in range(5):
        ll.add_last(random.randint(1, 100))
    
    print("All elements in the list:")
    ll.print_list()
    
    print("Length of the list:", ll.length())
    
    print("Iterating through the list using iterator protocol:")
    for item in ll:
        print(item, end=" ")
    print()
