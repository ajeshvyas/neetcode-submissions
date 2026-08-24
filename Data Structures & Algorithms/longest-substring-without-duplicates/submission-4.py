class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = dict()
        left = 0

        for right in range(len(s)):
            char = s[right]
            if char in seen:
                left = max(left, seen[char] + 1)
            seen[char] = right
            longest = max(longest, right - left + 1)

        return longest