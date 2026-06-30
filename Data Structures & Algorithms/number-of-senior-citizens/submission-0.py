class Solution:
    def countSeniors(self, details: List[str]) -> int:
        accum = 0
        for code in details:
            age = int(code[11:13])
            if age > 60:
                accum += 1
        return accum
