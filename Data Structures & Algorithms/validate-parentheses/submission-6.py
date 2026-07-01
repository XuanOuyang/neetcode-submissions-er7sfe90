class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0: return False

        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if not stack:
                    return False
                k = stack.pop()
                if (k == '(' and i == ')') or (k == '[' and i == ']') or (k == '{' and i == '}'):
                    continue
                else:
                     return False
        if stack != []:
            return False
        else:
            return True