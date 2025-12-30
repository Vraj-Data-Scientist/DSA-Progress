from typing import List

class Solution:
    def merge_brute(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        list1 = []
        for i in range(0, n):
            if (list1 and list1[-1][1] >= intervals[i][1]):
                continue
            start = intervals[i][0]
            end = intervals[i][1]
            for j in range(i+1, n):
                if (intervals[j][0] <= end):
                    end = max(end, intervals[j][1])
                else:
                    break
            list1.append([start, end])
        return list1

    def merge_better(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        list1 = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, n):
            if (intervals[i][0] <= end):
                end = max(end, intervals[i][1])
            else:
                list1.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        list1.append([start, end])
        return list1

    def merge_optimal(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        list1 = []
        for interval in intervals:
            if not list1 or list1[-1][1] < interval[0]:
                list1.append(interval)
            else:
                list1[-1][1] = max(list1[-1][1], interval[1])
        return list1

print(Solution().merge_brute([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge_brute([[2,3],[4,5],[6,7],[8,9],[1,10]]))
print(Solution().merge_better([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge_better([[2,3],[4,5],[6,7],[8,9],[1,10]]))
print(Solution().merge_optimal([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge_optimal([[2,3],[4,5],[6,7],[8,9],[1,10]]))