# Array, HashTable - Contain Duplicate
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice
# in the array, and it should return false if every element is distinct.
# Note:
#   try different data structures and be aware of time complexity of different operations
#
class ContainsDuplicate:
    # @param {integer[]} nums
    # @return {boolean}

    # test on LeetCode - 56ms
    # python set internal implementation uses hashing
    def containsDuplicate_set1(self, nums):
        """set operation time complexity - O(n), len() function time complexity - O(1)"""
        return len(nums) != len(set(nums))

    # test on LeetCode - 52ms
    # python set internal implementation uses hashing
    def containsDuplicate_set2(self, nums):
        """set.contain() - O(1), Time Complexity - O(n)"""
        visited = set()
        for element in nums:
            if element in visited:
                return True
            visited.add(element)
        return False

    # test on LeetCode - 68ms
    def containsDuplicate_dictionary(self, nums):
        """dictionary.contain() - O(1), Time Complexity - O(n)"""
        visited = {}
        for element in nums:
            if visited.has_key(element):
                return True
            visited[element] = element
        return False

    # test on LeetCode - Time Limit Exceeded
    def containsDuplicate_list(self, nums):
        """list.contain() - O(n), Time Complexity - O(n * n)"""
        visited = []
        for element in nums:
            if element in visited:
                return True
            visited.append(element)
        return False

def main():
    test = ContainsDuplicate()
    print test.containsDuplicate_list([1, 2, 3, 4, 1])
    print test.containsDuplicate_dictionary([1, 2, 3, 4, 0])
    print test.containsDuplicate_set2([1, 2, 3, 4, 1])

if __name__ == '__main__':
    main()
