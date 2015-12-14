# 6/25 - Binary Search Tree
# Given an array of integers, find out whether there are two distinct indices i and j 
# in the array such that the difference between nums[i] and nums[j] is at most t and 
# the difference between i and j is at most k.
#
class ContainDuplicate3:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}

    # Test on LeetCode - TLE
    def contains_nearby_almost_duplicate(self, nums, k, t):
        num_dict = self.get_num_dict(nums)
        print num_dict

        # contain duplicate - must be true
        if k > 0:
            for num in num_dict.keys():
                if len(num_dict[num]) > 1:
                    indexes = num_dict[num]
                    for i in range(0, len(indexes) - 1):
                        if indexes[i + 1] - indexes[i] <= k:
                            return True
            
        sorted_nums = sorted(num_dict.keys())  # O(lgn)
        print sorted_nums

        # obtain all possible nums[i] and nums[j]
        num_paris = []
        for i in range(0, len(sorted_nums) - 1):
            num = sorted_nums[i]
            for j in range(i + 1, len(sorted_nums)):
                next = sorted_nums[j]
                if abs(next - num) <= t:
                    num_paris.append([num, next])
        print num_paris

        if k >= len(nums):
            k = len(nums) - 1

        for pair in num_paris:
            num1 = pair[0]
            num2 = pair[1]
            for m in num_dict[num1]:
                for n in num_dict[num2]:
                    if abs(m - n) <= k:
                        return True

        return False

    # Time & Memory Complexity: O(n)
    def get_num_dict(self, nums):
        dict = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if dict.has_key(num):
                dict[num].append(i)
            else:
                dict[num] = [i]
        return dict


def main():
    test = ContainDuplicate3()
    #print test.contains_nearby_almost_duplicate([2, 1, 3, 4, 3, 2, 3, 1], 1, 2)
    print test.contains_nearby_almost_duplicate([1,3,1], 2, 1)


if __name__ == '__main__':
    main()

