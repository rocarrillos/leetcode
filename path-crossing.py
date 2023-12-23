def move(direction: str, coords: tuple):
    if direction == "N":
        return (coords[0], coords[1] + 1)
    elif direction == "S":
        return (coords[0], coords[1] - 1)
    elif direction == "E":
        return (coords[0] + 1, coords[1])
    elif direction == "W":
        return (coords[0] - 1, coords[1])
    else:
        raise Exception("invalid input")

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coords = (0, 0)
        visited_coords = set()
        visited_coords.add(coords)
        for step in path:
            coords = move(step, coords)
            if coords in visited_coords:
                return True
            else:
                visited_coords.add(coords)
        return False
