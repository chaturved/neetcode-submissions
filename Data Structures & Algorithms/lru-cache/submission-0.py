class Node:
    def __init__(self, val, prev: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_front(self, node: Node) -> None:
        if node == self.head:
            return
        self.remove(node)
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_front(self, val) -> Node:
        node = Node(val, next=self.head)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            return node
        self.head.prev = node
        self.head = node
        return node

    def remove_at_back(self) -> None:
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def remove(self, node: Node) -> None:
        if node == self.head:
            self.remove_at_front()
            return
        if node == self.tail:
            self.remove_at_back()
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_at_front(self) -> None:
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def peek_back(self):
        return self.tail.val if self.tail else None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_lst = LinkedList()
        self.key_node: dict[int, Node] = {}

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1

        node = self.key_node[key]
        self.lru_lst.move_to_front(node)
        return node.val[1]

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            node.val[1] = value
            self.lru_lst.move_to_front(node)
            return

        if len(self.key_node) == self.capacity:
            evicted_key = self.lru_lst.peek_back()[0]
            self.lru_lst.remove_at_back()
            del self.key_node[evicted_key]

        new_node = self.lru_lst.insert_at_front([key, value])
        self.key_node[key] = new_node