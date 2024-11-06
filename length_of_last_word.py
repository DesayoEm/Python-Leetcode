class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list=s.rstrip().split()
        return len(str_list[-1])