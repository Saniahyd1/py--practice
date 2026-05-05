from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                # No overlap
                prevEnd = end
            else:
                # Overlap
                res += 1
                prevEnd = min(end, prevEnd)

        return res


# -------- Driver Code --------
if __name__ == "__main__":
    n = int(input("Enter number of intervals: "))

    intervals = []
    print("Enter intervals (start end):")
    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append([start, end])

    sol = Solution()
    result = sol.eraseOverlapIntervals(intervals)

    print("Minimum intervals to remove:", result)