class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bracket = dict()
        i =0
        while i < len(nums):
            diff = target -nums[i]
            if diff in bracket:
                return [bracket[diff], i]
            bracket[nums[i]] = i
            i +=1
        return []