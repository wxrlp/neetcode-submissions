class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        index = 0
        while index < len(nums):
            comp = target - nums[index]
            if comp in hash:
                return [hash[comp], index]
            else:
                hash[nums[index]] = index
            index += 1