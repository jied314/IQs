# 1/15 - sort
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
# Try to solve it in linear time/space.
# Return 0 if the array contains less than 2 elements.
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
# Idea:
#   Bucket Sort
#   use min and max to decide bucket size, then assign values to each bucket
#   max_gap = min_current_bucket - max_prev_bucket (not empty bucket)
#   if max_gap == 0, number are evenly distributed, so max_gap = avg_gap.
import math


class Solution(object):
    # Test on LC - 68ms, 48%
    def max_gap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 2:
            return 0
        max_val = max(nums)
        min_val = min(nums)
        avg_gap = (max_val - min_val) * 1.0 / (len(nums) - 1)
        buckets = [[] for _ in range(0, len(nums) - 1)]
        for n in nums:
            bucket = self.hash(n, min_val, avg_gap)
            buckets[bucket].append(n)
        empty_count, max_gap, pre = 0, 0, min_val
        for i in range(0, len(buckets)):
            if buckets[i]:
                if len(buckets[i]) > 1:
                    max_gap = max(max_gap, min(buckets[i]) - pre)
                    pre = max(buckets[i])
                else:
                    max_gap = max(max_gap, buckets[i][0] - pre)
                    pre = buckets[i][0]
            else:
                empty_count += 1

        if max_gap == 0:
            return int(avg_gap)
        return max_gap

    def hash(self, n, base, gap):
        return int((n - base) / (gap + 0.01))

    # Test on LC - 76ms, 33%
    def maximum_gap(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if nums is None or len(nums) < 2:
                return 0

            # calculate bucket size
            max_val, min_val = max(nums), min(nums)
            avg_gap = (max_val - min_val) * 1.0 / (len(nums) - 1) + 0.01

            # only need to record the min and max for each bucket, store in two arrays
            buckets_min = [max_val+1] * (len(nums) - 1)
            buckets_max = [min_val-1] * (len(nums) - 1)
            for n in nums:
                bucket = self.hash(n, min_val, avg_gap)
                buckets_min[bucket] = min(buckets_min[bucket], n)
                buckets_max[bucket] = max(buckets_max[bucket], n)

            max_gap, pre = 0, min_val
            for i in range(0, len(nums) - 1):
                if buckets_min[i] > max_val and buckets_max[i] < min_val:  # empty bucket
                    continue
                max_gap = max(max_gap, buckets_min[i] - pre)
                pre = buckets_max[i]
            if max_gap == 0:
                return int(avg_gap)
            return max_gap

    # hash n into the right bucket according to base and gap
    def hash(self, n, base, gap):
        """
        :param n: int
        :param base: int
        :param gap: int
        :return: int
        """
        return int((n - base) / gap)

test = Solution()
print test.maximum_Gap([1,10000000])