# 8/3 - LL, Sort
# Note:
#   use dummy_head, but not add head initially. Need to init tail as None
#   initially, pre.next = None. with node.next = pre.next, successfully init tail as None.
#   no need to use index to avoid passing current node
class InsertionSortList:
    # @param {ListNode} head
    # @return {ListNode}
    def insertion_sort_list_correct(self, head):
        if head is None:
            return head
        helper = ListNode(0)
        cur = head
        pre = helper
        while cur is not None:
            next = cur.next
            # find the right place to insert
            while pre.next is not None and pre.next.val < cur.val:
                pre = pre.next
            # insert between pre and pre.next
            cur.next = pre.next
            pre.next = cur
            pre = helper
            cur = next
        self.traverse(helper.next)
        return helper.next

    def traverse(self, head):
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        print result


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def main():
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    three.next = two
    two.next = four
    l = three
    test = InsertionSortList()
    test.insertion_sort_list_correct(l)

if __name__ == '__main__':
    main()

