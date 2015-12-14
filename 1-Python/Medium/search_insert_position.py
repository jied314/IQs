# 6/30 - Array, Binary Search
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
#
class SearchInsertPosition:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}

    # Test on LeetCode - 40ms
    def search_insert(self, nums, target):
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = (low + high) / 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low

    def search_insert_error(self, nums, target):
        position = 0
        if nums:
            low = 0
            high = len(nums) - 1
            while high >= low:
                if high == low:  # able to lock a position
                    position = high if nums[high] >= target else high + 1
                    break
                mid = (low + high) / 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    position = mid
                    break
        return position


def main():
    test = SearchInsertPosition()
    print test.search_insert([1, 3, 5, 6], 5)
    print test.search_insert([1, 3, 5, 6], 2)
    print test.search_insert([1, 3, 5, 6], 7)
    print test.search_insert([3, 5, 7, 9, 10], 8)


if __name__ == "__main__":
    main()