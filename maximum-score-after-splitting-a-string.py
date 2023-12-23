# naive solution
class Solution:
    def maxScore(self, s: str) -> int:
        scores = []
        for i in range(1, len(s)):
            left = list(filter(lambda x: x == '0', s[0:i]))
            right = list(filter(lambda x: x == '1', s[i:]))
            scores.append(len(left) + len(right))
        return max(scores)