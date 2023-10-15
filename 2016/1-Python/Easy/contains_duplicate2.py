# Array, HashTable - Contain Duplicate2
# Given an array of integers and an integer k, find out whether there
# are two distinct indices i and j in the array such that nums[i] = nums[j]
# and the difference between i and j is at most k.
#
class ContainDuplicate2:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    # test on LeetCode - 56ms
    def containsNearbyDuplicate(self, nums, k):
        visited = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if visited.has_key(num):
                if i - visited[num] <= k:
                    return True
                visited[num] = i
            visited[num] = i
        return False

    def contains_nearby_duplicate_window(self, nums, k):
        if nums is None or len(nums) < 2:
            return False
        window = set()
        for i in range(0, len(nums)):
            if i > k:
                window.remove(nums[i-k-1])
            if nums[i] in window:
                return True
            else:
                window.add(nums[i])
        return False

def main():
    test = ContainDuplicate2()
    print test.containsNearbyDuplicate([1, 2, 3, 1, 1], 1)


if __name__ == '__main__':
    main()
