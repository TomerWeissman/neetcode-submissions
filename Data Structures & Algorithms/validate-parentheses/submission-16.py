class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {'{':'}', '[':']', '(':')'}
        stack = []

        for c in s:
            if c in hashmap:
                stack.append(hashmap[c])
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr != c:
                    return False
        
        
        return True if not stack else False