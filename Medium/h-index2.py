# 11/27 - Binary Search
# Follow up for H-Index: What if the citations array is sorted in ascending order? 
# Could you optimize your algorithm?
class H_INDEX2(object):
    # Test on LeetCode - 140ms
    # Binary Search - find the mid that citations[mid] >= length - mid
    def h_index(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        h_index = 0
        length = len(citations)
        low, high = 0, length - 1
        while low <= high:
            mid = low + (high - low) / 2
            if citations[mid] >= (length - mid):
                h_index = length - mid
                high = mid - 1
            else:
                low = mid + 1
        return h_index

def main():
    l1 = [3, 0, 6, 1, 5]
    test = H_INDEX2()
    print test.h_index(l1)


if __name__ == '__main__':
    main()