class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = dict()
        n = dict()
        for i in s:
            if i in m:
                m[i] +=1
            else:
                m[i] = 1
        for j in t:
            if j in n:
                n[j] +=1
            else:
                n[j] =1
        if m == n:
            return True
        return False
