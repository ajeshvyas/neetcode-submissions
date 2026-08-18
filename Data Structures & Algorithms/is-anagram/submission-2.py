class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = dict()
        for i in s:
            dic_s[i] = dic_s.get(i, 0) + 1
        dic_t = dict()
        for i in t:
            dic_t[i] = dic_t.get(i, 0) + 1
        return dic_s == dic_t