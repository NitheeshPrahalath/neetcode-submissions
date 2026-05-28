class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        m = dict()
        for i in s:
            m[i] = m.get(i, 0) + 1
            
        for j in t:
            if j in m and m[j]>= 1:
                m[j] -=1
            
            else:
                return False
        return True
