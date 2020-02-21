from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        
    def pop(self):
        if not self.storage.head:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if not self.storage.head:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size