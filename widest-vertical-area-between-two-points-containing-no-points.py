# this was a soft medium
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        delta = 0
        xcoords = sorted([point[0] for point in points])
        for i in range(1, len(xcoords) - 1):
            new_delta = xcoords[i] - xcoords[i - 1]
            if new_delta > delta:
                delta = new_delta
        return delta