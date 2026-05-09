class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')', '[':']', '{':'}'}
        stack = []

        for c in s:
            if c in mapping:
                stack.append(mapping[c])
            else:
                if not stack or c != stack.pop():
                    return False
        
        if len(stack) == 0:
            return True
        
        return False

        
