# 1/25 - LL
# Convert BST to Sorted Doubly-Linked List


# Definition for doubly-linked list.
class DoublyListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.prev = None

class Solution(object):
    # used to track current processed node
    dummy = DoublyListNode(-1)
    cur = dummy

    def bst_to_list_nice(self, root):
        if root is None:
            return None
        self.dfs(root)
        if Solution.dummy.next is not None:
            Solution.dummy.next.prev = None
        return Solution.dummy.next

    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.left)
        new_node = DoublyListNode(node.val)
        Solution.cur.next = new_node
        new_node.prev = Solution.cur
        Solution.cur = new_node
        self.dfs(node.right)