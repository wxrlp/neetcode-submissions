class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        b = 0
        for a in s:
            if a == t[b]:
                b += 1
            if b == len(t):
                break
            
        remaining = t[b:len(t)]
        return len(remaining)
