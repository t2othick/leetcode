# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        res = []
        current = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start > current.end:
                res.append(current)
                current = intervals[i]
            else:
                if intervals[i].end >= current.end:
                    current.end = intervals[i].end
        res.append(current)
        return res


def make_intervals(nums):
    res = []
    for start, end in nums:
        res.append(Interval(start, end))
    return res


def show_intervals(intervals):
    for x in intervals:
        print x.start, x.end


show_intervals(Solution().merge(make_intervals([[1,4],[4,5]])))