class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict = dict()
        for i in range(len(nums)):
            numsdict[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numsdict and numsdict[comp] != i:
                return [i, numsdict[comp]]
