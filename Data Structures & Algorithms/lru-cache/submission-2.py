class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.queue = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        node = self.key_map[key]
        self.queue.move_to_front(node)
        return node.value

        
    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.queue.move_to_front(node)
            return
        
        if len(self.key_map) == self.capacity:
            node = self.queue.remove_at_end()
            self.key_map.pop(node.key)
        
        node = self.queue.insert_at_front(key, value)
        self.key_map[key] = node


class Node:
    def __init__(self, key, value, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_front(self, node):
        if node is self.head:
            return

        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def remove_at_end(self):
        if not self.tail:
            return None

        node = self.tail
        prev_node = node.prev
        if prev_node:
            prev_node.next = None
        else:
            self.head = None
        self.tail = prev_node
        node.prev = None
        return node

    def insert_at_front(self, key, value):
        node = Node(key, value)
        if not self.head:
            self.head = self.tail = node
            return node

        node.next = self.head
        self.head.prev = node
        self.head = node
        return node


