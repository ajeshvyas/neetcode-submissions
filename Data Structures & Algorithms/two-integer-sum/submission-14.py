class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for idx, i in enumerate(nums):
            needed = target - i
            if needed in seen:
                return [seen[needed], idx]
            seen[i] = idx