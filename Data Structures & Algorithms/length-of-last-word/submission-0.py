class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversed = s[::-1]
        reversed = reversed.strip()
        accum = 0
        for x in reversed:
            if x != " ":
                accum += 1
            else:
                return accum
        return accum