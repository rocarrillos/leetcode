class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        current_greatest = max(candies)
        # return list(map(lambda x: (x + extraCandies) >= current_greatest, candies))
        # apparently list comprehension is faster than lambda
        return [x + extraCandies >= current_greatest for x in candies]
