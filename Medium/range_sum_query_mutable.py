# 12/5 - Segment Tree, Binary Indexed Tree
# Check: http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
# Solutions:
#   1. Update in place O(1), traver array to calculate sum O(N)
#   2. Use DP to store sum_so_far. Good for frequent sum O(1) and infrequent updates O(N).
#   3. use Segment Tree. Update O(lgN), Sum O(lgN)
# Finished on 12/13
class NumArrayTLE(object):
    # use DP to calculate sum_so_far for the array
    # Time Complexity - O(N)
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        length = len(nums)
        self.sum_dp = [0] * (length+1)
        self.sum_dp[length] = 0
        if length > 0:
            for i in range(length-1, -1, -1):
                self.sum_dp[i] = self.sum_dp[i+1] + nums[i]
        
    # Time Complexity - O(N)
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        length = len(self.sum_dp) - 1
        if i < 0 or i >= length:
            return -1
        cur = self.sum_dp[i]
        prev = self.sum_dp[i+1]
        diff = cur - prev - val
        for index in range(0, i+1):
            self.sum_dp[index] -= diff
        return 1

    # Time Complexity - O(1)
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        length = len(self.sum_dp) - 1
        if i < 0:
            i = 0
            if j < 0:
                j = 0
        if j >= length:
            j = length - 1
            if i >= length:
                i = length - 1
        return self.sum_dp[i] - self.sum_dp[j+1]

# Your NumArray object will be instantiated and called as such:
"""nums = [7, -2, 3, -5, 1]
numArray = NumArrayTLE(nums)
print numArray.sumRange(0, 1)
print numArray.update(1, 0)
print numArray.sumRange(0, 1)"""


# Use Segment Tree
# Representation of Segment trees
#   1. Leaf Nodes are the elements of the input array.
#   2. Each internal node represents some merging of the leaf nodes.
#     The merging may be different for different problems. For this problem, merging is sum of leaves under a node.
#
# Test on LeetCode - 756ms
class NumArraySegmentTree(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.root = self.build_sum_segment_tree(0, len(nums)-1)

    def build_sum_segment_tree(self, l, r):
        if l > r:  # need to check boundary
            return None
        if l == r:  # return node itself
            node = TreeNode(self.nums[l])
            node.range = [l, r]
        else:
            mid = l + (r - l) / 2
            left = self.build_sum_segment_tree(l, mid)
            right = self.build_sum_segment_tree(mid+1, r)
            node = TreeNode(left.val + right.val)
            node.left = left
            node.right = right
            node.range = [left.range[0], right.range[1]]
        return node


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if i < 0 or i >= len(self.nums):
            return
        diff = val - self.nums[i]
        if diff == 0:
            return
        self.nums[i] = val
        self.update_tree(i, diff, self.root)

    def update_tree(self, i, diff, node):
        if node is None:
            return
        if self.is_within_range(i, node.range):
            node.val += diff
            self.update_tree(i, diff, node.left)
            self.update_tree(i, diff, node.right)


    def is_within_range(self, i, range):
        return range[0] <= i <= range[1]


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if j < i:
            return 0
        length = len(self.nums)
        i, j = max(i, 0), max(j, 0)
        i, j = min(i, length-1), min(j, length-1)
        if i == j:
            return self.nums[i]
        return self.sumRange_helper(i, j, self.root)

    def sumRange_helper(self, i, j, node):
        if node is None:
            return 0
        range = node.range
        # node range is within the search range
        if i <= range[0] and j >= range[1]:
            return node.val
        # node range is outside the search range
        if i > range[1] or j < range[0]:
            return 0
        # overlap
        return self.sumRange_helper(i, j, node.left) + self.sumRange_helper(i, j, node.right)


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.range = None



# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5, 7, 9, 11]
numArray = NumArraySegmentTree(nums)
print numArray.sumRange(0, 1)
numArray.update(1, 10)
print numArray.sumRange(1, 2)


