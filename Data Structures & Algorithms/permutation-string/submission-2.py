class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # left = 0
        # right = len(s1)
        # check = True

        # while right <= len(s2):
        #     if s2[left] in s1 and s2[right - 1] in s1:
        #         dup_s1 = list(s1)
        #         for char in s2[left : right]:
        #             if char in dup_s1:
        #                 dup_s1.remove(char)
        #         if len(dup_s1) == 0:
        #             return True
        #     left += 1
        #     right += 1
        # return False


        left = 0
        right = len(s1)
        while right <= len(s2):
            if sorted(s2[left:right]) == sorted(s1):
                return True
            left += 1
            right += 1

        return False