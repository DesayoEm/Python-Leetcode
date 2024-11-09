class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count=0
        for word in words:
            if any(char not in allowed for char in word):
                pass
            else:
                count+=1
        return count