class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}

        for ch in s:
            s_freq[ch] = s_freq.get(ch,0) + 1

        for ch in t:
            if ch not in s_freq:
                return False
            s_freq[ch] -= 1
            if s_freq[ch] < 0:
                return False
        
        return True
        