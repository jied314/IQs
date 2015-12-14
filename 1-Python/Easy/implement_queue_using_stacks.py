# 7/30 - Stack, Data Structure
# Implement the following operations of a queue using stacks.
#   push(x) -- Push element x to the back of queue.
#   pop() -- Removes the element from in front of queue.
#   peek() -- Get the front element.
#   empty() -- Return whether the queue is empty.
#
# Test on LeetCode - 52ms
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self._queue = []


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self._queue.append(x)

    # @return nothing
    def pop(self):
        length = len(self._queue)
        temp = []
        while length > 1:
            temp.append(self._queue.pop())
            length -= 1
        self._queue.pop()
        while temp:
            self._queue.append(temp.pop())


    # @return an integer
    def peek(self):
        length = len(self._queue)
        temp = []
        while length > 0:
            temp.append(self._queue.pop())
            length -= 1
        top = temp[-1]
        while temp:
            self._queue.append(temp.pop())
        return top

    # @return an boolean
    def empty(self):
        return len(self._queue) == 0


# Test on LeetCode - 48ms
# Idea:
#   Use two stacks, one for push, one for pop
class Queue_two_stacks:
    # initialize your data structure here.
    def __init__(self):
        self._in = []
        self._out = []


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self._in.append(x)


    # @return nothing
    def pop(self):
        self.peek()
        self._out.pop()


    # @return an integer
    def peek(self):
        if len(self._out) == 0:
            length = len(self._in)
            while length > 0:
                self._out.append(self._in.pop())
                length -= 1
        return self._out[-1]

    # @return an boolean
    def empty(self):
        return len(self._in) == 0 and len(self._out) == 0