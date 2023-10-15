# 7/8 - Array, Binary Search
# Note: O(lgn)
class FindPeakElement:
    # @param nums, an integer[]
    # @return an integer

    # Test on LeetCode - 60ms
    def find_peak_element(self, nums):
        if nums:
            if len(nums) > 1:
                length = len(nums)
                if nums[0] > nums[1]:
                    return 0
                if nums[length-1] > nums[length-2]:
                    return length-1
                index = 1
                while index < length-1:
                    if nums[index] > nums[index-1] and nums[index] > nums[index+1]:
                        # not necessary to check left and right since only need to find one peak
                        return index
                    else:
                        index += 1
            else:
                return 0

    def find_peak_element_sequential(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums)-1

    # Test on LeetCode - 52ms
    # Use binary serach - O(lgn)
    def find_peak_element_binary_search_recursive(self, nums):
        return self.find(0, len(nums)-1, nums)

    def find(self, low, high, nums):
        if low == high:
            return low
        else:
            mid1 = (low + high) / 2
            mid2 = mid1 + 1
            if nums[mid1] > nums[mid2]:
                return self.find(low, mid1, nums)
            else:
                return self.find(mid2, high, nums)

    # Test on LeetCode - 52ms
    def find_peak_element_binary_search_iterative(self, nums):
        low, high = 0, len(nums)-1
        while low < high:
            mid1 = (low + high) / 2
            mid2 = mid1 + 1
            if nums[mid1] > nums[mid2]:
                high = mid1
            else:
                low = mid2
        return low

def main():
    test = FindPeakElement()
    print test.find_peak_element_binary_search_iterative([1,2,3,4,5])


if __name__ == '__main__':
    main()

