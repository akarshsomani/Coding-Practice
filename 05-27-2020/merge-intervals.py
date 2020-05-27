# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        l = len(intervals)
        intervals.sort()
        
        # print(intervals)
        if(intervals == []):
            return([])
        
        final = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,l):
            if intervals[i][0] <= end: 
                if intervals[i][1] >= end:
                    end = intervals[i][1]
            else:
                final.append([start,end])
                
                start = intervals[i][0]
                end = intervals[i][1]

        final.append([start,end])
        
        return(final)
