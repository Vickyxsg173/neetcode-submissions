class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        maps = set({'+',"-","*","/"})
        for i in tokens:
            if i not in maps:
                stack.append(int(i))
            elif i == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif i == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif i == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(y*x)
            elif i == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x))
        return stack[-1]

