class Solution:
    # not super fast but same idea as the fast solutions
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        ranges = []
        lower = None
        upper = None
        for i in range(len(nums)):
            if i == 0:
                # begin
                lower = nums[i]
                upper = nums[i]
            else:
                if nums[i] == upper + 1:
                    upper = nums[i]
                else:
                    if lower == upper:
                        ranges.append(str(lower))
                    else:
                        ranges.append(str(lower) + "->" + str(upper))
                    lower = nums[i]
                    upper = nums[i]
        if lower == upper:
            ranges.append(str(lower))
        else:
            ranges.append(str(lower) + "->" + str(upper))
        return ranges