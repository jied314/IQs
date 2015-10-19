# 6/17 - Divide and Conquer, Array, Bit Manipulation (E)
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than floor n/2  times.
# You may assume that the array is non-empty and the majority element always exist in the array.


class MajorityElement:
    # @param {integer[]} nums
    # @return {integer}
    # Test on LeetCode - 79ms
    def majority_element_hashtable(self, nums):
        """use HashTable - Running Time: O(n), Space: O(n)"""
        frequency = {}
        goal = len(nums) / 2
        for num in nums:
            if frequency.has_key(num):
                frequency[num] += 1
            else:
                frequency[num] = 1
            if frequency[num] > goal:
                return num

    # sort the list, the n/2th element must be the majority element - Running Time: O(nlgn)
    def majority_element_sort(self, nums):
        nums.reverse()
        return nums[len(nums) / 2]

    # Test on LeetCode - 52ms
    # Idea:
    #   use two variables to store count and candidate
    #   traverse the array: if count = 0, assign num to candidate; if num == candidate, count++; else, count--;
    #   since the majority element has to be more than floor n/2, the final count has to be more than 0.
    #   verify - traverse the array the second time to count the frequency of the majority element
    def majority_element_Boyer_Moore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, candidate = 0, 1.1
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        # assume the majority element always exists - no need to check count > 0
        return candidate
        

def main():
    test = MajorityElement()
    print test.majority_element_hashtable([1, 2, 2, 2, 1])
    print test.majority_element_sort([1, 2, 2, 2, 1])
    print test.majority_element_Boyer_Moore([1, 2, 2, 2, 1])

if __name__ == '__main__':
    main()