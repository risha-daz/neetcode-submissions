class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in [']', '}', ')']:
                if not stack: return False
                j = stack.pop()
                if ((i==']' and j!='[') or
                    (i==')' and j!='(') or
                    (i=='}' and j!='{')):
                    return False
            else: stack.append(i)
        return len(stack) == 0