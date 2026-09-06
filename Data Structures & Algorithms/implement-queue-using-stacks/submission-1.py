class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        """
        push_stack = front [1, 2, 3, 4] <- top of stack aka back of queue

        on pop
        push = []
        pop_stack = back [4, 3, 2, 1] top of stack aka front of queue
        popped 1
        push 5, 6
        push = [5, 6] back
        the 5 should go before 4
        pop_stack = [4, 3, 2] front
        """

    def push(self, x: int) -> None:
        self.__move_to_pop_stack()
        self.push_stack.append(x)

    def pop(self) -> int:
        self.__move_to_pop_stack()
        return self.pop_stack.pop()

    def peek(self) -> int:
        self.__move_to_pop_stack()
        return self.pop_stack[-1]

    def empty(self) -> bool:
        self.__move_to_pop_stack()
        return not self.pop_stack
    
    def __move_to_pop_stack(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()