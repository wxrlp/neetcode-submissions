class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answers = set()
        for num in nums:
            if num not in answers:
                answers.add(num)
            else:
                return True
        return False