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
        result = ""
        balance = 0

        for char in s:

            if char == '(':
                balance += 1
                result += char

            elif char == ')':

                if balance > 0:
                    balance -= 1
                    result += char

            else:
                result += char

        while balance > 0:
            index = result.rfind('(')
            result = result[:index] + result[index + 1:]
            balance -= 1

        return result