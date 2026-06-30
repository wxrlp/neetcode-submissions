class Solution:
    def scoreOfString(self, s: str) -> int:
        accum = 0
        left = 0
        right = 1
        while right < len(s):
            inc = abs(ord(s[left]) - ord(s[right]))
            accum += inc
            left += 1
            right += 1
        return accum