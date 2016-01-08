# 9/24 - HashTable, Sort (E)
# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute
# the researcher's h-index.
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at
# least h citations each, and the other N - h papers have no more than h citations each."
# For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them
# had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each
# and the remaining two with no more than 3 citations each, his h-index is 3.
# Note:
#   If there are several possible values for h, the maximum one is taken as the h-index.
# Hint:
#    1. An easy approach is to sort the array first.
#    2. What are the possible values of h-index?
#    3. A faster approach is to use extra space.
# Revisit 11/20,


class H_INDEX(object):
    # Test on LeetCode - 48ms
    # Idea:
    #   sort the array, then from tail to start, find the right h-index
    # Note: insert 0 to the beginning to avoid case like [11, 13] -> 2, not 0.
    def h_index_sort(self, citations):
        h_index = 0
        if citations is None or len(citations) == 0:
            return h_index
        citations.append(0)
        sorted_c = sorted(citations)
        length = len(citations)
        i = length - 1
        num_visited = 1
        while i >= 0:
            if sorted_c[i] < num_visited:
                break
            if sorted_c[i-1] <= num_visited:
                h_index = num_visited
            num_visited += 1
            i -= 1
        citations.pop(0)
        return h_index

    # Test on LeetCode - 44ms
    # Idea:
    #   Not require sorting
    #   record appearance of numbers, if > than length, add to the tail
    #   count the number against its position backward
    def h_index_memory(self, citations):
        length = len(citations)
        if citations is None or length == 0:
            return 0
        array = [0] * (length + 1)
        for i in range(0, length):
            if citations[i] > length:
                array[length] += 1
            else:
                array[citations[i]] += 1
        t, result = 0, 0
        for i in range(length, -1, -1):
            t += array[i]
            if t >= i:
                return i
        return 0

    # Revisit - 12/24
    # Test on LeetCode - 48ms
    # Note: hIndex is restricted by len(citations)
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        length = len(citations)
        citations.qsort()
        for i in range(length, 0, -1):
            if citations[length-i] >= i:
                return i
        return 0


def main():
    l1 = [3, 0, 6, 1, 5]
    l2 = [0, 1, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6]
    l3 = [11, 15]
    test = H_INDEX()
    print test.h_index_memory(l1)
    print test.h_index_sort(l2)
    print test.h_index_sort([2, 2, 2])
    print test.h_index_sort(l3)


if __name__ == '__main__':
    main()
