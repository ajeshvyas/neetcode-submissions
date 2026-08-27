class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        # if len(s) == len(t):
        #     if sorted(s) == sorted(t):
        #         return s
        #     else:
        #         return ""
        
        # need = {}

        # for char in t:
        #     need[char] = need.get(char, 0) + 1

        # min_length = float("inf")
        # answer = ""

        # print(min_length)

        # for i in range(len(s)):
        #     window = {}
        #     for j in range(i, len(s)):
        #         char = s[j]
        #         if char in need:
        #             window[char] = window.get(char, 0) + 1
        #         valid = True
        #         for char in need:
        #             if window.get(char, 0) < need[char]:
        #                 valid = False
        #                 break
        #         if valid:
        #             if j - i + 1 < min_length:
        #                 min_length = j - i + 1
        #                 answer = s[i:j + 1]

        # return answer

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        left = 0
        have = 0
        required = len(need)

        min_length = float("inf")
        start = 0

        for right in range(len(s)):

            # Expand window
            char = s[right]

            if char in need:
                window[char] = window.get(char, 0) + 1

                if window[char] == need[char]:
                    have += 1

            # Shrink window
            while have == required:

                # Current window is valid
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                # Remove left character
                char = s[left]

                if char in need:
                    window[char] -= 1

                    if window[char] < need[char]:
                        have -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[start:start + min_length]