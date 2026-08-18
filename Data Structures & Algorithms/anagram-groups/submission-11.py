# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         seen_map = dict()

#         for idx, s in enumerate(strs):
#             s_sort = "".join(sorted(s))
#             if seen_map.get(s_sort):
#                 seen_map.get(s_sort).append(s)
#             else:
#                 seen_map[s_sort] = [s]

#         ans = []
#         for group in seen_map.values():
#             ans.append(group)
#         return ans

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups: dict[str, List[str]] = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in anagram_groups:
                anagram_groups[sorted_string].append(string)
            else:
                anagram_groups[sorted_string] = [string]
        ans = []
        for group in anagram_groups.values():
            ans.append(group)
        return ans