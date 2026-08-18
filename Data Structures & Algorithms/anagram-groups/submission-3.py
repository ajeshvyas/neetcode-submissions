class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen_map = dict()

        for idx, s in enumerate(strs):
            s_sort = "".join(sorted(s))
            if seen_map.get(s_sort):
                seen_map.get(s_sort).append(s)
            else:
                seen_map[s_sort] = [s]

        return list(seen_map.values())