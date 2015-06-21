# Data Structure - Implement Stack using Queues
# Implement the following operations of a stack using queues.
#   push(x) -- Push element x onto stack.
#   pop() -- Removes the element on top of the stack.
#   top() -- Get the top element.
#   empty() -- Return whether the stack is empty.
# Note: 
#   can use 'push to back, peek/pop from front, size, and is empty' methods
#
from collections import deque

# Test on LeetCode - 36ms
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self._stack = deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self._stack.append(x)

    # can use len() method
    # @return nothing
    def pop(self): 
        if len(self._stack) == 1:
            self._stack.popleft()
        else:           
            top = self._stack.popleft()
            self._stack.append(top)
            while True:
                first = self._stack.popleft()
                if self._stack[0] is not top:
                    self._stack.append(first)
                else:
                    break

    # @return an integer
    def top(self):
        if len(self._stack) == 1:
            return self._stack[0]
        else:           
            top = self._stack.popleft()
            self._stack.append(top)
            while True:
                first = self._stack.popleft()
                self._stack.append(first)
                if self._stack[0] is top:
                    return first

    # @return an boolean
    def empty(self):
        return len(self._stack) == 0


def main():
    test = Stack()
    print test.empty()
    test.push(1)
    test.push(2)
    test.push(3)
    print test.top()
    test.pop()
    print test.top()


if __name__ == '__main__':
    main()

