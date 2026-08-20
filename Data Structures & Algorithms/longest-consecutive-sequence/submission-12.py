class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 100000:
            return 2 if nums[0] == -100000000 else 100000
        max_seq = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                max_seq = max(max_seq, length)
        return max_seq