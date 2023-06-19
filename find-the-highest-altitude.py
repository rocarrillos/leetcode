class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0
        for point in gain:
            current_altitude += point
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude