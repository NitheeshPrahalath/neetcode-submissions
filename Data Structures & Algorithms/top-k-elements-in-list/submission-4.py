class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values =dict()
        for num in nums:
            values[num] = values.get(num, 0) + 1

        return [num for num, count in sorted(values.items(), key = lambda x:x[1], reverse = True)[:k]]
         