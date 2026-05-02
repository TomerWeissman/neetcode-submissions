class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')', '[':']', '{':'}'}
        tracker = []

        for c in s:
            if c in mapping:
                tracker.append(mapping[c])
            
            if c in mapping.values():
                if not tracker or tracker[-1] != c:
                    return False
                else:
                    tracker.pop()
        
        if len(tracker) == 0:
            return True
        else:
            return False

        