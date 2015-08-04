# 8/1 - Array, Two Pointers
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional
# elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
# Note:
#   1. head -> tail, need to shift memory
#   2. tail -> head, no need to shift
#
import sys
class MergeSortedArrays:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        nums1.append(sys.maxint)
        nums2.append(sys.maxint)
        i = 0
        j = 0
        for index in range(0, m+n):
            if nums1[i] > nums2[j]:  # insert
                self.shift_insert(i, nums1, nums2[j])
                j += 1
            i += 1
        nums1.pop()
        return nums1

    def shift_insert(self, start, array, num):
        array.append(0)
        for i in range(len(array)-2, start-1, -1):
            array[i+1] = array[i]
        array[start] = num

    # Test on LeetCode - 56ms
    # update nums1 from tail to head, no need to shift array
    def merge_nice(self, nums1, m, nums2, n):
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        print nums1


def main():
    test = MergeSortedArrays()
    print test.merge_nice([1,0], 1, [2], 1)

if __name__ == '__main__':
    main()
