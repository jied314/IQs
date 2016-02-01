# 1/19 - Sort
# Given a collection of intervals, merge all overlapping intervals.
# For example,
#   Given [1,3],[2,6],[8,10],[15,18], return [1,6],[8,10],[15,18].
# Idea:
#   sort intervals by its start position, then merge. O(N*lgN)

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    # Test on LC - 80ms, 88%
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) < 2:
            return intervals
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        ret = []
        start, end = sorted_intervals[0].start, sorted_intervals[0].end
        for interval in sorted_intervals:
            if interval.start <= end:  # overlap
                end = max(end, interval.end)
            else:  # no overlap
                ret.append(Interval(start, end))
                start, end = interval.start, interval.end
        ret.append(Interval(start, end))
        return ret