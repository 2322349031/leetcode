#56.合并区间

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        output = []
        for x in sorted(intervals,key=lambda x:x.start):
            if output and x.start <= output[-1].end:
                output[-1].end = max(x.end,output[-1].end)
            else:
                output.append(x)
        return output

