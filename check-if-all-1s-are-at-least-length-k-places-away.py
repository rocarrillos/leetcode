class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_idx = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_idx is None:
                    last_idx = i
                else:
                    if i - last_idx <= k:
                        return False
                    else:
                        last_idx = i
        return True
