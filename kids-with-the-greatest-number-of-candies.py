class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_greatest = max(candies)
        return list(map(lambda x: (x + extraCandies) >= current_greatest, candies))
