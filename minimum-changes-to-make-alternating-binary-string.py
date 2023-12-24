def getOps(spl):
    ops = 0
    for i in range(1, len(spl)):
        if spl[i] == spl[i - 1]:
            ops += 1
            if spl[i - 1] == "0":
                spl[i] = "1"
            else:
                spl[i] = "0"
    return ops

def switchFirst(spl):
    if spl[0] == '1':
        spl[0] = '0'
    else:
        spl[0] = "1"
    return spl

class Solution:
    def minOperations(self, s: str) -> int: 
        if len(s) == 1:
            return 0

        st = [i for i in s]
        st2 = switchFirst(st[:])

        ops1 = getOps(st)
        ops2 = getOps(st2) + 1
        return min(ops1, ops2) 
