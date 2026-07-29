class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i,j = i+1,j+1
            else:
                j+=1
        if len(s)-i == 0:
            return True
        return False