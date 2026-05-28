class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if sorted(list(set(nums))) == sorted(nums):
            return False
        return True