class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values =dict()
        j =0
        while j < len(nums):
            if nums[j] not in values:
                values[nums[j]] = 1
            else:
                values[nums[j]] +=1
            j +=1
        result = list()

        sorted_items = sorted(values.items(), key=lambda x:x[1], reverse = True)
        for i in range(k):
            result.append(sorted_items[i][0])
        return result
            