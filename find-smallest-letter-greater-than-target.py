class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        index_to_chop = 0
        for i in range(len(letters)):
            if letters[i] <= target:
                index_to_chop = i + 1
        survivors = letters[index_to_chop:]
        if len(survivors):
            return survivors[0]
        return letters[0]
