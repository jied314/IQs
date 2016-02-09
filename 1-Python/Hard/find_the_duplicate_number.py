# 1/12 - Array, Two Pointers, Binary Search
class Solution(object):
    # Test on LC - 80ms, 23%
    # Idea:
    #   similar to the partitioning in QuickSort
    #   instead of update the array, update the pivot value
    # pivot = k. if no duplicate, small_count = k - 1, large_count = n - k
    def find_duplicate_bs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high, max_val = 1, len(nums)-1, len(nums)-1
        while low < high:
            pivot = low + (high - low) / 2
            small_count, large_count = 0, 0
            for n in nums:
                if n < pivot:
                    small_count += 1
                elif n > pivot:
                    large_count += 1
            if small_count > pivot-1:  # search left
                high = pivot - 1
            elif large_count > max_val - pivot:  # search right
                low = pivot + 1
            else:
                return pivot
        return low

    # Test on LC - 76ms, 27%
    # Idea:
    #   similar to above, only need one variable to store count.
    def find_duplicate_bs_nice(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums)-1

        while low < high:
            mid = low+(high-low)/2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:  # search right
                low = mid+1
            else:  # search left
                high = mid
        return low

    # Test on LC - 52ms, 62%
    # Idea:
    #   similar to find cycles in ll (turtle & hare problem)
    #   array, not knowing how cycle links, use nums[index] as the linking function
    #   slow = f(slow)
    #   fast = f(f(fast))
    #   http://keithschwarz.com/interesting/code/?dir=find-duplicate
    def find_duplicate_two_pointers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        # find intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # find the starting point of the cycle
        start = 0
        while start != slow:
            slow = nums[slow]
            start = nums[start]
        return slow