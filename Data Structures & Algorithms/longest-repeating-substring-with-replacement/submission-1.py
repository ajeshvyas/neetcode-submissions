class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s_len = len(s)
        # max_length = 0

        # for i in range(s_len):
        #     frequency = {}

        #     for j in range(i, s_len):
        #         frequency[s[j]] = frequency.get(s[j], 0) + 1

        #         max_frequency = max(frequency.values())

        #         window_length = j - i + 1
        #         replacements = window_length - max_frequency

        #         if replacements <= k:
        #             max_length = max(max_length, window_length)

        # return max_length

        left = 0
        max_frequency = 0
        max_length = 0
        frequency = {}

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1

            max_frequency = max(max_frequency, frequency[s[right]])

            window_length = right - left + 1

            if window_length - max_frequency > k:
                frequency[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length