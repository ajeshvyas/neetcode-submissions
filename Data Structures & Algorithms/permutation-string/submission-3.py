class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force
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

        # Using Sorted
        # left = 0
        # right = len(s1)
        # while right <= len(s2):
        #     if sorted(s2[left:right]) == sorted(s1):
        #         return True
        #     left += 1
        #     right += 1

        # return False

        # Best case
        count1 = {}
        count2 = {}

        for char in s1:
            count1[char] = count1.get(char, 0) + 1

        for char in s2[:len(s1)]:
            count2[char] = count2.get(char, 0) + 1

        left = 0
        right = len(s1)

        while right < len(s2):
            if count1 == count2:
                return True

            char = s2[left]
            count2[char] -= 1

            if count2[char] == 0:
                del count2[char]

            char = s2[right]
            count2[char] = count2.get(char, 0) + 1

            left += 1
            right += 1

        return count1 == count2