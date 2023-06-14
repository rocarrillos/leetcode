class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # rows are already given to us
        # columns need to be extracted
        pairs = 0
        columns = [[row[i] for row in grid] for i in range(len(grid))]
        for row in grid:
            for column in columns:
                if row == column:
                    pairs += 1
        return pairs