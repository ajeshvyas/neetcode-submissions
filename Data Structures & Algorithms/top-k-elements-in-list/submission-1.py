class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        res = []

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        for i in range(k):
            key = max(seen, key=seen.get)
            res.append(key)
            seen.pop(key)
        return res
