# 8/21 - DFS, List
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ConvertSortedListToBST(object):
    cur = None

    # Test on LeetCode - 268ms
    # Idea:
    #   DFS: use length and keep track of the next List Node
    def sorted_list_to_BST(self, head):
        """
        :type head: ListNode
        :rtype:
        """
        if head is None:
            return None

        node = head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        ConvertSortedListToBST.cur = head
        return self.build(0, length-1)

    def build(self, start, end):
        if start <= end:
            mid = (start + end) / 2
            lc = self.build(start, mid-1)
            root = TreeNode(ConvertSortedListToBST.cur.val)
            ConvertSortedListToBST.cur = ConvertSortedListToBST.cur.next
            rc = self.build(mid+1, end)
            root.left = lc
            root.right = rc
            return root
        else:
            return None

    # 12/26 - Revisit
    # In each recursive call, traverse half of the list's length to find the middle element.
    # Time Complexity - O(N lg N), N - list length
    # At each level of recursive call, it requires a total of N/2 traversal steps in the list,
    # and there are a total of lg N number of levels (ie, the height of the balanced tree).
    # However, change the original ll
    def sorted_list_to_BST_NLGN(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return head
        if head.next is None:
            return TreeNode(head.val)
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        root = slow.next
        root_node = TreeNode(root.val)
        slow.next = None
        root_node.left = self.sorted_list_to_BST_NLGN(head)
        root_node.right = self.sorted_list_to_BST_NLGN(root.next)
        return root_node

    # 1/25 - revisit
    # not change the original ll
    def sorted_list_to_BST_nice(self, head):
        self.convert(head, None)

    def convert(self, begin, end):
        if begin is None or begin == end:
            return None
        if begin.next == end:
            return TreeNode(begin.val)
        mid = self.middle(begin, end)
        root = TreeNode(mid.val)
        root.left = self.convert(begin, mid)
        root.right = self.convert(mid.next, end)
        return root

    # start at the head
    def middle(self, begin, end):
        fast, slow = begin, begin
        while fast != end and fast.next != end:
            fast = fast.next.next
            slow = slow.next
        return slow

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five
test = ConvertSortedListToBST()
test.sorted_list_to_BST(one)