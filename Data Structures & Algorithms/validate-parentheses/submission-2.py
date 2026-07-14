class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{',']':'[',')':'('}
        for ch in s:
            if ch in mapping:
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        if len(stack) == 0:
            return True
        else:
            return False