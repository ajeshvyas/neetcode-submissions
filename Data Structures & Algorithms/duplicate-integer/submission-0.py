class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup = set()
        for n in nums:
            if n in dedup:
                return True
            dedup.add(n)
        return False