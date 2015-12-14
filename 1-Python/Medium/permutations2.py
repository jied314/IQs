# 10/15 - BackTracking (M)
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# For example,
#   [1,1,2] have the following unique permutations: [1,1,2], [1,2,1], and [2,1,1].
# check next_permutation.py


class Permutations2(object):
    # Test on LeetCode - 140ms
    # Idea:
    # sort the array
    # traverse: if not duplicate, insert into every position; else, insert until reaching the duplicate.
    # e.g. [1, 1, 2, 2]
    # [1] -> [1, 1] -> [1, 1, 2] -> [1, 1, 2, 2]
    #                  [1, 2, 1] -> [1, 2, 1, 2], [1, 2, 2, 1]
    #                  [2, 1, 1] -> [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]
    def permute_unique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.reverse()
        length = len(nums)
        ret = [[]]
        num = None
        for i in range(0, length):
            temp = []
            cur = nums[i]
            if cur != num:  # insert to every position
                while len(ret) > 0:
                    e = ret.pop()
                    for j in range(0, i + 1):
                        copy_e = list(e)
                        copy_e.insert(j, cur)
                        temp.append(copy_e)
            else:  # insert until the last duplicate
                while len(ret) > 0:
                    e = ret.pop()
                    for j in range(0, i):
                        copy_e = list(e)
                        copy_e.insert(i - j, cur)
                        temp.append(copy_e)
                        if e[i - j - 1] == num:
                            break
            num = cur
            ret = temp
        return ret

    # borrow idea from next permutation
    # [1, 2, 3, 4] -> find the next greater one [1, 2, 4, 3]
    # find all the next permutations until index == 0 (reach the end [4, 3, 2, 1]
    def permute_unique2(self, nums):
        print 1


def main():
    test = Permutations2()
    print test.permute_unique([])
    print test.permute_unique([1])
    print test.permute_unique([1, 1])
    print test.permute_unique([1, 1, 2])
    print test.permute_unique([1, 1, 2, 2])


if __name__ == '__main__':
    main()
