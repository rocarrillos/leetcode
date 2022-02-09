class Solution:
    def addDigits(self, num: int) -> int:
        # if num < 10:
        #     return num
        # else:
        #     nums = map(lambda i: int(i), list(str(num)))
        #     return self.addDigits(sum(nums))
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
