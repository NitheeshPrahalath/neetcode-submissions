class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_str =defaultdict(list)
        for i in strs:
            val ="".join(sorted(i))
            if val in map_str:
                map_str[val].append(i)
            else:
                map_str[val] = [i]
        return list(map_str.values())