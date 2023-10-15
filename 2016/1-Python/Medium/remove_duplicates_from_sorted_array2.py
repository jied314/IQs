# 8/4 - Array, Two Pointers
# Follow up for "Remove Duplicates": What if duplicates are allowed at most twice?
#
class RemoveDuplicatesFromSortedArray2:
    # @param {integer[]} nums
    # @return {integer}
    # Test on LeetCode - 156ms
    def remove_duplicates(self, nums):
        if nums is None:
            return 0
        else:
            if len(nums) <= 2:
                return len(nums)
            i = 0
            repeat = 0
            for j in range(1, len(nums)):
                if nums[j] == nums[i]:
                    repeat += 1
                else:
                    repeat = min(1, repeat)
                    if repeat > 0:
                        nums[i+1] = nums[i]
                    i += repeat+1
                    nums[i] = nums[j]
                    repeat = 0
            if repeat > 0:
                i += 1
                nums[i] = nums[i-1]
            print nums
            return i+1

    def remove_duplicates_nice1(self, nums):
        if nums is None:
            return 0
        else:
            if len(nums) <= 2:
                return len(nums)
            i = 2
            for j in range(2, len(nums)):
                if nums[j] != nums[i-2]:
                    nums[i] = nums[j]
                    i += 1
            return i

    def remove_duplicates_nice2(self, nums):
        if nums is None:
            return 0
        else:
            if len(nums) <= 2:
                return len(nums)
            i = 0
            for j in range(2, len(nums)):
                if nums[j] != nums[i]:
                    nums[i+2] = nums[j]
                    i += 1
            return i+2


def main():
    test = RemoveDuplicatesFromSortedArray2()
    print test.remove_duplicates_nice2([1,2])
    print test.remove_duplicates_nice2([1,1,1,1,2,2,3])

if __name__ == '__main__':
    main()