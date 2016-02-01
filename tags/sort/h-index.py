# 9/24 - HashTable, Sort (E)
# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute
# the researcher's h-index.
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at
# least h citations each, and the other N - h papers have no more than h citations each."
# For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them
# had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each
# and the remaining two with no more than 3 citations each, his h-index is 3.
# Note:
#   If there are several possible values for h, the maximum one is taken as the h-index.
# Hint:
#    1. An easy approach is to sort the array first.
#    2. What are the possible values of h-index?
#    3. A faster approach is to use extra space.
#
# Similar to http://www.fgdsb.com/2015/01/07/find-h/
# Idea:
#   Find h for the array that there are h elements that are greater or equal to h.
#   1. sort, then count - easy, O(NlgN)
#   2. quick select, find the (N-h)th-element that - O(N) in average


class H_INDEX(object):
    # Test on LeetCode - 44ms
    # Idea:
    #   Not require sorting
    #   record appearance of numbers, if > than length, add to the tail
    #   count the number against its position backward
    def h_index_memory(self, citations):
        length = len(citations)
        if citations is None or length == 0:
            return 0
        array = [0] * (length + 1)
        for i in range(0, length):
            if citations[i] > length:
                array[length] += 1
            else:
                array[citations[i]] += 1
        t, result = 0, 0
        for i in range(length, -1, -1):
            t += array[i]
            if t >= i:
                return i
        return 0

    # Revisit - 12/24
    # Test on LeetCode - 48ms
    # Note: hIndex is restricted by len(citations)
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        length = len(citations)
        citations.qsort()
        for i in range(length, 0, -1):
            if citations[length-i] >= i:
                return i
        return 0

    # Test on LeetCode - 44ms
    # Idea:
    #   use quick-select
    def hIndex_quick_select(self, citations):
        if citations is None or len(citations) == 0:
            return 0
        return self.select(citations, 0, len(citations)-1)

    # adjust low and high to find the right h
    def select(self, nums, low, high):
        ret = 0
        while low <= high:
            pos = self.quick_select(nums, low, high)
            right_count = len(nums) - pos
            if nums[pos] > right_count:
                ret = max(ret, right_count)
                high = pos - 1
            elif nums[pos] < right_count:
                low = pos + 1
            else:
                return right_count
        return ret

    # same as partition for quick-sort
    def quick_select(self, nums, low, high):
        pivot = nums[low]
        pi = low+1
        for i in range(low+1, high+1):
            if nums[i] < pivot:
                nums[i], nums[pi] = nums[pi], nums[i]
                pi += 1
        nums[low], nums[pi-1] = nums[pi-1], pivot
        return pi-1

    # Nice Quick-Sort in Python
    def quick_sort(self, nums):
        less, equal, greater = [], [], []
        if len(nums) > 1:
            pivot = nums[0]
            for num in nums:
                if num < pivot:
                    less.append(num)
                elif num == pivot:
                    equal.append(num)
                else:
                    greater.append(num)
            return self.quick_sort(less) + equal + self.quick_sort(greater)
        else:
            return nums

def main():
    l1 = [3, 0, 6, 1, 5]
    l2 = [0, 1, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6]
    l3 = [11, 15]
    test = H_INDEX()
    print test.h_index_memory(l1)
    print test.hIndex_quick_select(l1)
    print test.hIndex_quick_select([1])
    print test.hIndex_quick_select(l3)


if __name__ == '__main__':
    main()
