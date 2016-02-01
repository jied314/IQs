# 1/27 - Sort
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
# Example 1:
#   Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
# Example 2:
#   Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
#   This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @classmethod
    def construct(self, l):
        ret = []
        for e in l:
            ret.append(Interval(e[0], e[1]))
        return ret

    @classmethod
    def output(self, intervals):
        ret = []
        for interval in intervals:
            ret.append([interval.start, interval.end])
        return ret


class Solution(object):
    # Test on LC - 76ms, 86%
    # Idea (three steps):
    #   1. find insertion position
    #   2. insert or merge with the left
    #   3. merge with the right if necessary
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals is None:
            return [newInterval]

        # find the insertion place
        i = 0
        while i < len(intervals) and newInterval.start > intervals[i].start:
            i += 1

        # merge or insert with the left part
        left = intervals[:i]
        if i == 0 or newInterval.start > left[-1].end:  # insert
            left.append(newInterval)
        else:  # overlap
            left[-1].end = max(left[-1].end, newInterval.end)

        # merge or insert with the right part
        j = i
        while j < len(intervals):
            if intervals[j].start <= left[-1].end:
                left[-1].end = max(left[-1].end, intervals[j].end)
            else:
                return left + intervals[j:]
            j += 1
        return left

    # borrow from Yanxing
    # 3 steps:
    #   1. find the left non-overlapping
    #   2. merge the overlapping ones
    #   3. copy the rest
    def insert_nice(self, intervals, newInterval):
        i = 0
        ret = []
        while i < len(intervals) and intervals[i].end < newInterval.start:
            ret.append(intervals[i])
            i += 1
        while i < len(intervals) and newInterval.end >= intervals[i].start:
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[i].end)
            i += 1
        ret.append(newInterval)
        return ret + intervals[i:]

test = Solution()
intervals = Interval.construct([[2,4],[5,7],[8,10],[11,13]])
print Interval.output(test.insert(intervals, Interval(3, 8)))
print Interval.output(test.insert_nice(intervals, Interval(3, 8)))
