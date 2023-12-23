# this was an Easy one

# initial naive solution
class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        sorted_arr = sorted(arr)
        delta = sorted_arr[1] - sorted_arr[0]
        for i in range(len(arr) - 1):
            if sorted_arr[i+1] - sorted_arr[i] != delta:
                return False
        return True
    
# smarter solution with sets
class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        known_nums = set()
        min_val = min(arr)
        max_val = max(arr)
        delta = (min_val - max_val) / (len(arr) - 1)
        if delta == 0:
            return True
        for item in arr:
            if (item - min_val) % delta != 0 or item in known_nums:
                return False
            else:
                known_nums.add(item)
        return True