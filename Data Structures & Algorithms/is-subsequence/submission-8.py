class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # t_map = dict()
        # for char in t:
        #     t_map[char] = t_map.get(char, 0)+1
        
        # for char in s:
        #     if t_map.get(char, None) and t_map[char] > 0:
        #         t_map[char] -= 1
        #     else:
        #         return False
        # return True

        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)