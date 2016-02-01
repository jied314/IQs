# 1/31 - Sort
# Sort the given strings according to the given letter order
# e.g. given strings { 'face', 'ball', 'apple', 'art', 'ah' } and the order "htarfbp...",
# should return {'ah', 'art', 'apple', 'face', 'ball'}


class Solution(object):
    def __init__(self):
        self.dict = {}

    def str_sort(self, strs, str_dict):
        """
        :param strs: List[str]
        :param str_dict: string
        :return:
        """
        for idx, val in enumerate(str_dict):
            self.dict[val] = idx
        return sorted(strs, cmp=self.mycmp1)

    def mycmp(self, s1, s2):
        return self.mycmp_helper(s1, s2, 0, 0)

    def mycmp_helper(self, s1, s2, i, j):
        if i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                return self.mycmp_helper(s1, s2, i+1, j+1)
            return self.dict[s1[i]] - self.dict[s2[j]]
        if i < len(s1):
            return 1
        else:
            return -1

    def mycmp1(self, s1, s2):
        min_length = min(len(s1), len(s2))
        i = 0
        for i in range(0, min_length):
            diff = self.dict[s1[i]] - self.dict[s2[i]]
            if diff != 0:
                return diff
        if i < len(s1):
            return 1
        else:
            return -1

test = Solution()
print test.str_sort(['face', 'ball', 'apple', 'art', 'ah'], "htarfbpcl")