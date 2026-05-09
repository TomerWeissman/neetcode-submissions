class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs:
            output += str(len(s)) + '#' + s

        return output            

    def decode(self, s: str) -> List[str]:
        
        output = []
        i = 0

        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            print(length)
            j = int(length)
            end = i + 1 + j
            output.append(s[i+1:end])
            i = end
            
        return output
    