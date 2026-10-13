class Solution:
    def isValid(self, s: str) -> bool:
        seen = {"}": "{", 
        "]": "[",
        ")": "("}
        stack = []
        for i in s:
            if i in seen and len(stack) >= 1 and seen.get(i) == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False