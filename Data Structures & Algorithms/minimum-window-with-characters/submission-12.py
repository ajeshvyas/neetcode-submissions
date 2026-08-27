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

        smallest_s = ""
        freq = defaultdict(int)
        need = 0
        for c in t:
            freq[c] += 1
            need += 1 
        
        window = defaultdict(int)
        l, r = 0, len(s) - 1
        for c in s:
            window[c] += 1
        
        # check if a valid window even exists
        for key in freq.keys():
            if window[key] < freq[key]:
                return ""

        # shrink window back until it is valid
        valid = True
        while valid:
            if window[s[r]] - 1 >= freq[s[r]]:
                window[s[r]] -= 1
                r -= 1
            else:
                valid = False
        smallest_window = s[l:r+1]

        if l == r:
            return smallest_window

        have = need
        while True:
            # pop of the left side to see if we can make a smaller window
            window[s[l]] -= 1
            if window[s[l]] < freq[s[l]]:
                have -= 1
            l += 1
            # extend window rightward until valid
            while have != need and r != len(s) - 1:
                r += 1
                window[s[r]] += 1
                if window[s[r]] ==  freq[s[r]]:
                    have += 1
            # if window hit the end and the window isn't valid, return
            if r == len(s) - 1 and have != need:
                return smallest_window
            # if we reach a valid window, pop off left amap
            while True:
                if window[s[l]] == freq[s[l]]:
                    break
                else:
                    window[s[l]] -= 1
                    l += 1
            if len(smallest_window) > len((s[l:r+1])):
                smallest_window = s[l:r+1]
        return smallest_window