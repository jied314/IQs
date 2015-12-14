# 10/15 - Array, Two Pointers, Binary Search
# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which
# the sum >= s. If there isn't one, return 0 instead.
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.


class MinimizeSizeSubarray(object):
    # Test on LeetCode - 48ms
    # Idea:
    #   traverse the array, starting with index = 0.
    #   if subtotal >= s: try reduce start, compare with min_length
    #   else: increase end
    #   remember to check if the total is smaller than s, return 0.
    def min_sub_array_len_two_pointers(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        min_length = length + 1
        start = 0
        sub_total = 0
        for i in range(0, length):
            sub_total += nums[i]
            if sub_total >= s:
                while sub_total - nums[start] >= s:
                    sub_total -= nums[start]
                    start += 1
                min_length = min(min_length, i - start + 1)
        if min_length > length:
            min_length = 0
        return min_length

    #  # Test on LeetCode - 68ms
    # Idea:
    #   calculate the accumulative subarray value
    #   find the min length span >= s
    def min_sub_array_len_bs(self, s, nums):
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        min_length = length + 1
        sub_total = [0]
        for i in range(0, length):
            sub_total.append(sub_total[-1] + nums[i])
        if sub_total[-1] < s:  # not able to sum to s
            return 0
        for i in range(0, length+1):
            end = self.binary_search(i+1, length, s+sub_total[i], sub_total)
            if end == length+1:  # from i to end, not able to sum to s
                break
            min_length = min(min_length, end - i)
        return min_length


    # find the position to insert key
    def binary_search(self, low, high, key, nums):
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return low



def main():
    test = MinimizeSizeSubarray()
    print test.min_sub_array_len_two_pointers(7, [2, 3, 1, 2, 4, 3])
    #print test.min_sub_array_len_two_pointers(7, [1, 1, 1, 1, 1, 1])
    print test.min_sub_array_len_bs(7, [2, 3, 1, 2, 4, 3])
    #print test.min_sub_array_len_two_pointers(7, [1, 1, 1, 1, 1, 1])


if __name__ == "__main__":
    main()