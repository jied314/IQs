# 6/26 - Hash Table, Bit Manipulation
# Given an array of integers, every element appears twice except for one. Find that single one.
# Linear Running Time, O(1) Memory
# Two Solutions:
#   1. HashTable - store seen numbers
#   2. use bit operator XOR
class SingleNumber:
    # @param {integer[]} nums
    # @return {integer}
    # Use HashMap, Test on LeetCode - 68ms
    # Time - O(N), Memory - O(N/2)
    def single_number_hashmap(self, nums):
        values = set()
        for num in nums:
            if num in values:
                values.remove(num)
            else:
                values.add(num)
        return list(values)[0]

    # Use Bit Manipulation, XOR operator (A^A = 0, A^B^A = B)
    def single_number_bit(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result


def main():
    test = SingleNumber()
    # print test.single_number_hashmap([1, 2, 3, 1, 2])
    print test.single_number_bit([1, 2, 3, 1, 2])


if __name__ == '__main__':
    main()