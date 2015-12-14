# 9/24 - Array
# Given a sorted integer array without duplicates, return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class SummaryRanges(object):

    # Test on LeetCode - 48ms
    # Idea:
    #     while traversing the array, exhaust current range
    def summary_ranges_nice(self, nums):
        result = []
        if nums is None:
            return result

        length = len(nums)
        i = 0
        while i < length:
            start, end = i, i
            while end + 1 < length and nums[end + 1] == nums[end] + 1:  # exhaust current range
                end += 1
            if end == start:
                result.append(str(nums[start]))
            else:
                result.append("{0}->{1}".format(nums[start], nums[end]))
            i = end + 1
        return result

    # Test on LeetCode - 48ms
    # Idea:
    #   linearly traverse the array and report range
    #   need special treatment for end of array
    def summary_ranges_long(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if nums is None:
            return result

        length = len(nums)
        range_start = 0
        for i in range(0, length):
            if nums[i] - nums[range_start] > (i - range_start):  # not continuous
                if range_start < i - 1:
                    start, end = str(nums[range_start]), str(nums[i-1])
                    result.append("{0}->{1}".format(start, end))
                else:
                    result.append(str(nums[range_start]))
                range_start = i
            if i == length - 1:  # end of list
                if range_start == i:
                    result.append(str(nums[range_start]))
                else:
                    start, end = str(nums[range_start]), str(nums[i])
                    result.append("{0}->{1}".format(start, end))
                break
        return result

    # Test on LeetCode
    # Idea:
    #   linearly traverse the array and report range
    #   add dummy tail to the array
    def summary_ranges_modify(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if nums is None:
            return result
        nums.append(nums[-1] + 2)
        length = len(nums)
        range_start = 0
        for i in range(1, length):
            if nums[i] - nums[range_start] > (i - range_start):  # not continuous
                if range_start < i - 1:
                    start, end = str(nums[range_start]), str(nums[i-1])
                    result.append("{0}->{1}".format(start, end))
                else:
                    result.append(str(nums[range_start]))
                range_start = i
        return result

def main():
    l1 = [0, 1, 2, 4, 5, 7]
    l2 = [1, 3, 4, 7, 8]
    test = SummaryRanges()
    print test.summary_ranges_nice(l1)
    print test.summary_ranges_nice(l2)
    print test.summary_ranges_modify([1])
    print test.summary_ranges_modify(l2)


if __name__ == '__main__':
    main()
