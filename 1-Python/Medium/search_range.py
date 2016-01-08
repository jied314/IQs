class SearchRange(object):
    # Test on LeetCode - 52ms
    # Idea:
    #   first locate target position as fast as possible
    #   search left side for the min index
    #   search right side for the max index
    def search_range(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        if nums is None:
            return result
        length = len(nums)
        if length == 0:
            return result
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                result = [self.search_l(nums, target, low, mid - 1), self.search_h(nums, target, mid + 1, high)]
                break
        return result

    # find the minimum index that equals to target
    # numbers with l and h are less or equal to target
    def search_l(self, nums, target, l, h):
        low = l
        high = h
        min_l = h + 1
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                min_l = mid
                high = mid - 1
            else:  # nums[mid] < target
                low = mid + 1
        return min_l

    # find the maximum index that equals to target
    # numbers with l and h are greater or equal to target
    def search_h(self, nums, target, l, h):
        low = l
        high = h
        max_h = l - 1
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                max_h = mid
                low = mid + 1
            else:  # nums[mid] > target
                high = mid - 1
        return max_h

    # 12/27 - Revisit
    # Test on LeetCode - 42ms
    # Idea:
    #   normal BS, if target == nums[mid], adjust low and high accordingly
    def search_range_revisit(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return [-1, -1]
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:  # adjust low and high based on whether equal to target
                if nums[low] == nums[high]:
                    return [low, high]
                if nums[low] != target:
                    low += 1
                if nums[high] != target:
                    high -= 1
        return [-1, -1]

def main():
    test = SearchRange()
    print test.search_range([1], 0)
    print test.search_range([1], 1)
    print test.search_range([5, 7, 7, 8, 8, 10], 8)
    print test.search_range([5, 7, 7, 8, 8, 10], 7)

if __name__ == '__main__':
    main()

