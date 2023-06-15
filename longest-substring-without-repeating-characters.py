# yes this is slow but it works lol
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_max = 0
        for i in range(len(s)):
            known_chars = set(s[i])
            count = 1
            for j in range(i + 1, len(s)):
                if s[j] not in known_chars:
                    known_chars.add(s[j])
                    count += 1
                else:
                    break
            if count > current_max:
                current_max = count
        return current_max
                
