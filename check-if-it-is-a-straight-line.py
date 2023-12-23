def getSlope(a, b):
    return (b[1] - a[1]) / (b[0] - a[0])

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        # if all Xs are the same, y = mx + b won't work
        # but it would still be True
        xs = set(map(lambda i: i[0], coordinates))
        if len(xs) == 1:
            return True
        try:
            m = getSlope(coordinates[1], coordinates[0])
            b = coordinates[0][1] - m * coordinates[0][0]
            for point in coordinates:
                if point[1] != m * point[0] + b:
                    return False
            return True
        except ZeroDivisionError:
            return False
        