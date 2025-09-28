class Solution:
    def lengthOfLastWord(self, s: str) -> int:
     lengthofLastWord= s.split()[-1]
     return len(lengthofLastWord)
