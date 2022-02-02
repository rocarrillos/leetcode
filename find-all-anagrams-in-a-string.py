class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pmap = [0] * 26
        indices = []
        for l in p:
            pmap[ord(l) - ord("a")] += 1
        runmap = [0] * 26
        for i in range(len(s)):
            runmap[ord(s[i]) - ord("a")] += 1 
            if i >= len(p):
                runmap[ord(s[i-len(p)]) - ord("a")] -= 1
            if runmap == pmap:
                indices.append(i - len(p) + 1)
                
        return indices
                
