class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = 0
        arr = arr[::-1]
        accum = []
        for a in arr:
            if a >= current_max:
                current_max = a
            accum.append(current_max)
        accum.pop()
        accum = accum[::-1]
        accum.append(-1)
        return accum
