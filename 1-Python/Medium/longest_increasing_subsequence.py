# 11/28 - DP, BS
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
# Note that there may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?
#
# Initial Idea:
#   Traverse array backward, count LIS for each element
#   Problem: Use max_val + 1 or index of the next greater
#   e.g. [10, 9, 2, 5, 3, 4, 7, 101, 18]
#        [ 2, 2, ?, 3, 4, 3, 2,  1,  1] -> for 2, use value of 5 (next greater) or 3 (max_val)?
#        [1, 3, 6, 7, 9, 4, 10, 5, 6]
#        [6, 5, 4, ?, 2, 3, 1, 2, 1] -> for 2, use value of 9 (next greater) or 4 (max_val)?
# Solution:
#   DP - dp[i] need to try all dp[j] for j < i and nums[j] < nums[i]
#   see http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
#
# 11/28 First Trial - Fails
class LongestIncreasingSubsequence(object):
    # This attemps for O(N) solution - Impossible!
    def length_of_LIS_Wrong(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        length = len(nums)
        ret_array = [0] * length
        ret_array[-1] = 1
        max_val = 1
        for i in range(length - 2, -1, -1):
            if nums[i] == nums[i + 1]:
                ret_array[i] = ret_array[i+1]
            else:
                if nums[i] > nums[i + 1]:
                    temp = nums[i]
                    new_position = self.find_insert_position(temp, i+1, nums)
                    nums.insert(new_position, temp)
                    ret_array.insert(new_position, 0)
                    nums.pop(i)
                    ret_array.pop(i)
                    i = new_position - 1
                    if i == length - 1:
                        ret_array[i] = 1
                    else:
                        ret_array[i] = ret_array[i+1] + 1
                else:
                    ret_array[i] = max_val + 1
            max_val = max(max_val, ret_array[i])
        return max_val

    # Find the insert position of key in the sorted array
    # Note: this version also works for array having duplicates
    #       if no duplicate, no need for nums[mid] == key
    def find_insert_position(self, key, start, end, nums):
        low, high = start, end
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] < key:
                low = mid + 1
            elif nums[mid] > key:
                high = mid - 1
            else:
                return mid
        return low

    # dp[i] = max(dp[i], dp[j] + 1) for all j < i and nums[j] < nums[i]
    # Complexity - O(N * N)
    # Test on LeetCode - 1656ms
    def length_of_LIS_NN(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        dp = [1] * length
        ret = 1
        for i in range(1, length):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ret = max(ret, dp[i])
        return ret

    # Test on LeetCode - 44ms
    # keep track of tails of all possible LIS so far, tails is a sorted array
    # us bs to search for the smallest element in tails that is >= nums[i]
    # Note: duplicate in the array
    def length_of_LIS_NLOGN(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        tails = [nums[0]]  # keep track of tails of all possible LIS
        for i in range(1, length):
            if nums[i] <= tails[0]:
                tails[0] = nums[i]  # start a new LIS
            elif nums[i] > tails[-1]:
                tails.append(nums[i])  # clone and append
            else:  # find the smallest tail that is >= nums[i]
                tails[self.find_insert_position(nums[i], 0, len(tails)-1, tails)] = nums[i]
        return len(tails)



def main():
    test = LongestIncreasingSubsequence()
    print test.length_of_LIS_NN([2, 2])
    print test.length_of_LIS_NLOGN([2, 2])
    print test.length_of_LIS_NN([10, 9, 2, 5, 3, 4, 7, 101, 18])
    print test.length_of_LIS_NLOGN([10, 9, 2, 5, 3, 4, 7, 101, 18])
    print test.length_of_LIS_NN([1,3,6,7,9,4,10,5,6])
    print test.length_of_LIS_NLOGN([1,3,6,7,9,4,10,5,6])
    print test.length_of_LIS_NN([10,22,9,33,21,50,41,60,80])
    print test.length_of_LIS_NLOGN([10,22,9,33,21,50,41,60,80])


if __name__ == "__main__":
    main()