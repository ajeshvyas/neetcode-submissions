class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # valid = {
        #     "{": 0,
        #     "(": 0,
        #     "[": 0
        # }
        # check_against = {"}", ")", "]"}

        # for char in s:
        #     if char in valid or char in check_against:
        #         if char in valid:
        #             valid[char] += 1
        #         if char in check_against:
        #             valid[char] -= 1
        # for key, value in valid
        res = []
        cnt = 0  # extra ( parentheses
        for c in s:
            if c == "(":
                res.append(c)
                cnt += 1
            elif c == ")" and cnt > 0:
                res.append(c)
                cnt -= 1
            elif c != ")":
                res.append(c)

        filtered = []
        for c in reversed(res):
            if c == "(" and cnt > 0:
                cnt -= 1
            else:
                filtered.append(c)
        return "".join(reversed(filtered))