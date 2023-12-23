class Solution:
    # there's definitely more clever solutions
    # but the naive one isn't bad in this case
    def countNegatives(self, grid: list[list[int]]) -> int:
        negatives = 0
        for row in grid:
            for column in row:
                if column < 0:
                    negatives += 1
        return negatives