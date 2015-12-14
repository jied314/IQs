# 10/19 - Array (M)
# Given an integer array of size n, find all elements that appear more than floor n/3 times. The algorithm should
# run in linear time and in O(1) space.
# Note:
#   check Easy/majority_element.py
#   use Boyer-Moore algorithm


class MajorityElement2(object):
    # Test on LeetCode - 52ms
    # Idea:
    #
    def majority_element_boyer_moore(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        if nums is None or len(nums) < 1:
            return ret
        count1, count2, candidate1, candidate2 = 0, 0, 1.1, 1.1
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        if count1 > 0 and self.verify_majority_element(candidate1, nums):
            ret.append(candidate1)
        if count2 > 0 and self.verify_majority_element(candidate2, nums):
            ret.append(candidate2)
        return ret

    def verify_majority_element(self, candidate, nums):
        length = len(nums)
        min_majority_frequency = length / 3 + 1
        return nums.count(candidate) >= min_majority_frequency


def main():
    test = MajorityElement2()
    print test.majority_element_boyer_moore([3])
    print test.majority_element_boyer_moore([3, 2])
    print test.majority_element_boyer_moore([3, 2, 3])
    print test.majority_element_boyer_moore([2, 2, 1, 3])
    # print test.verify_majority_element(2, [2, 2, 1, 3])


if __name__ == "__main__":
    main()
