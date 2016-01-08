# 12/29 - Hash Table, String
# Given an array of strings, group anagrams together.
#   For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
#   Return:
#   [ ["ate", "eat","tea"], ["nat","tan"], ["bat"] ]
# Note:
#   For the return value, each inner list's elements must follow the lexicographic order.
#   All inputs will be in lower-case.


class solution:
    def group_anagrams_tle(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        ret_dict = {}
        ret = []
        for s in strs:
            anagram_array = self.get_anagram_array(s)
            is_existed = False
            for key, val in dict.iteritems():
                if val == anagram_array:
                    ret_dict[key].append(s)
                    is_existed = True
            if not is_existed:
                dict[s] = anagram_array
                ret_dict[s] = [s]
        for key in ret_dict:
            ret_dict[key].qsort()
            ret.append(ret_dict[key])
        return ret

    def get_anagram_array(self, s):
        ret = [0] * 26
        for char in s:
            ret[ord(char) - ord('a')] += 1
        return ret

    # Test on LC - 260ms
    # Idea:
    #   sort strs first, in lexicographic order
    #   sort each string, store it as the key and index as value
    #   output the dictionary
    def group_anagrams_nice(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ana_dict = {}
        ret = []
        length = len(strs)
        strs.qsort()
        for i in range(0, length):
            s = strs[i]
            sorted_s = ''.join(sorted(s))
            if sorted_s not in ana_dict:
                ana_dict[sorted_s] = []
            ana_dict[sorted_s].append(i)
        for key in ana_dict:
            ret.append([])
            for index in ana_dict[key]:
                ret[-1].append(strs[index])
        return ret

test = solution()
test.group_anagrams_tle(["eat", "tea", "tan", "ate", "nat", "bat"])
