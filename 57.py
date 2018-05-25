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
        # intervals = sorted(intervals, key=lambda x: x.start)
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

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        while i < len(intervals):
            if intervals[i].start >= newInterval.start:
                break
            i += 1
        intervals.insert(i, newInterval)
        return self.merge(intervals)


def make_intervals(nums):
    res = []
    for start, end in nums:
        res.append(Interval(start, end))
    return res


def show_intervals(intervals):
    for x in intervals:
        print x.start, x.end


intervales = make_intervals([[1,3],[6,9]])
show_intervals(Solution().insert(intervales, Interval(2, 5)))