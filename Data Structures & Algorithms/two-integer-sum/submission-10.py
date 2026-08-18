class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        second = 1
        while first <= len(nums) - 2:
            if nums[first] + nums[second] == target:
                return [first, second]
            if second == len(nums) - 1:
                first += 1
                second = first + 1
            else:
                second += 1
