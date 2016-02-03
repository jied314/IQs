# 2/1 - Sort
# Given a set of n jobs with [start time, end time, cost], find a subset of jobs that that no 2 jobs overlap
# and the cost is maximum.
#
# Solution:
# DP + BS:
#   Sort the intervals based on end time
#   define p(i) for each interval, giving the biggest end point which is smaller than the start point of i-th interval.
# Use binary search to obtain nlogn.
#   define d[i] = max(w(i) + d[p(i)], d[i-1]), d[0] = 0
#   The result will be in d[n] n is the number of intervals.
#   Overall complexity O(NlgN)


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0, c=0):
        self.start = s
        self.end = e
        self.cost = c


class IntervalNode(object):
    def __init__(self, interval):
        self.interval = interval
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_cost = 0

    # Idea:
    #   sort by weight, then construct tree to separate intervals
    def getBestCombination(self, intervals):
        """
        :param intervals: List[Interval]
        :return: int
        """
        sorted_intervals = sorted(intervals, key=lambda interval: interval.cost, reverse=True)
        root = IntervalNode(sorted_intervals[0])
        for i in range(1, len(sorted_intervals)):
            interval = sorted_intervals[i]
            self.insert(interval, root)
        return self.max_cost

    #
    def insert(self, interval, node):
        if self.is_overlap(interval, node.interval):  # overlap, insert node
            if interval.start <= node.interval.start <= interval.end:  # interval covers node's interval
                return
            elif interval.start < node.interval.start or interval.start == node.interval.start and interval.end < node.interval.end:
                # overlap on the left side, insert to left
                if node.left is not None:
                    self.insert(interval, node.left)
                else:
                    node.left = IntervalNode(interval)
            else:  # overlap on the right side, insert to right
                if node.right is not None:
                    self.insert(interval, node.right)
                else:
                    node.right = IntervalNode(interval)
        else:  # non_overlap, update max_cost
            self.max_cost = max(self.max_cost, node.interval.cost + interval.cost)


    def is_overlap(self, interval1, interval2):
        return interval1.start <= interval2.start < interval1.end or interval2.start <= interval1.start < interval2.end

    # sort by end time, then use dp & bs
    # similar to brute force, for each interval, find all non-overlapping interval and update max_cost if necessary
    def get_best_combinations(self, intervals):
        if intervals is None or len(intervals) == 0:
            return 0
        sorted_intervals = sorted(intervals, key=lambda interval: interval.end)
        return self.find_best_combination(sorted_intervals)

    def find_best_combination(self, intervals):
        """
        :param intervals:  List[Interval]
        :return: int
        """
        length = len(intervals)
        dp = [0] * (length + 1)
        for i in range(1, length+1):
            interval = intervals[i-1]
            pi = self.find(intervals, interval.start, 0, len(intervals)-1)
            dp[i] = max(dp[pi+1] + interval.cost, dp[i-1])
        return dp[length]

    # bs on end time
    def find(self, intervals, target, left, right):
        if left > right:
            return right
        else:
            mid = (left + right) / 2
            if intervals[mid].end == target:
                return mid
            elif intervals[mid].end > target:
                return self.find(intervals, target, left, mid-1)
            else:
                return self.find(intervals, target, mid+1, right)


test = Solution()
intervals = [Interval(0, 5, 1), Interval(1, 4, 100), Interval(6, 8, 2)]
print test.getBestCombination(intervals)
intervals = [Interval(0, 5, 1), Interval(1, 4, 100), Interval(6, 8, 2)]
print test.get_best_combinations(intervals)