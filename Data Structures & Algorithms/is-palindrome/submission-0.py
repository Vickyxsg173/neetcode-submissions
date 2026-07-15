class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for i in s:
            if i.isalnum():
                text+=i.lower()
        return text == text[::-1]