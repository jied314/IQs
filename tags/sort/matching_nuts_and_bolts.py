# 2/2 - Sort, DC
# Matching nuts and bolts problem can be stated as follows: "Given a collection of n nuts of distinct sizes and n bolts
# such that there is a one-to-one correspondence between the nuts and the bolts, find for each nut its corresponding bolt."
# We can only compare nuts to bolts i.e., we can neither compare nuts to nuts nor bolts to bolts.
# Idea:
#   Recursively do QuickSort on both arrays
#   O(NlgN)
from random import randint


class Solution(object):
    def sort_two_groups(self, a, b):
        """
        :param a: List[int]
        :param b: List[int]
        :return: void
        """
        if a is None or b is None or len(a) < 2 or len(b) < 2:
            return
        self.sort(a, b, 0, len(a)-1)

    # randomly choose a pivot from a to partition b, then use b[pi] to partition a
    # recursively apply this process until left >= right
    def sort(self, a, b, left, right):
        if left >= right:
            return
        pivot_b = a[randint(left, right)]
        pi = self.partition(b, left, right, pivot_b)
        pivot_a = b[pi]
        self.partition(a, left, right, pivot_a)
        self.sort(a, b, left, pi-1)
        self.sort(a, b, pi+1, right)

    # sort array[left:right+1] using the pivot - similar to sort colors
    def partition(self, nums, l, r, pivot):
        i = l
        while i <= r:
            if nums[i] < pivot:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:  # nums[i] == pivot
                i += 1
        return l
