def recursePalindrome(numstr):
    if len(numstr) > 1:
        if numstr[0] != numstr[-1]:
            return False
        else:
            return True and recursePalindrome(numstr[1:-1])
    return True
    

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # cast number to string first
        numstr = str(x)
        return numstr == numstr[::-1] #recursePalindrome(numstr)
