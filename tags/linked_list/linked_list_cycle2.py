# 7/8 - Linked List, Two-Pointers
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# Solutions:
#   Length of head to cycle start: x
#   Length of the cycle: y
#   while both of them entered the cycle, the hare is definitely to overlap the tortoise at some node,
#   we define it as m.
#   The hare totally runs: x + ky + m, The tortoise totally runs: x + ty + m.
#   Thus, ky = 2ty + x + m, we have (x + m) % y = 0.
#   We can conclude that if the hare run more x steps, it will reach the cycle's starting node.


class LinkedListCycle2:
    # @param head, a ListNode
    # @return a list node

    # Test on LeetCode - 184ms
    def detect_cycle(self, head):
        if head is None:
            return None
        hare, turtle = head, head
        while hare is not None:
            turtle = turtle.next
            hare = hare.next
            if hare is None:  # no cycle
                return None
            hare = hare.next
            if hare == turtle:  # has cycle
                turtle = head
                while turtle != hare:
                    hare = hare.next
                    turtle = turtle.next
                return hare
        return None
