class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.lst = LinkedList()

    def enQueue(self, value: int) -> bool:
        if self.lst.size == self.capacity:
            return False
        return self.lst.insert(value)

    def deQueue(self) -> bool:
        if self.lst.size == 0:
            return False
        return self.lst.remove()

    def Front(self) -> int:
        if not self.lst.head:
            return -1
        return self.lst.head.val

    def Rear(self) -> int:
        if not self.lst.tail:
            return -1
        return self.lst.tail.val

    def isEmpty(self) -> bool:
        return self.lst.size == 0

    def isFull(self) -> bool:
        return self.lst.size == self.capacity


class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, val):
        self.size += 1
        new_node = ListNode(val)
        if not self.head:
            self.head = self.tail = new_node
            return True

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        return True

    def remove(self):
        if not self.head:
            return False

        self.size -= 1
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return True