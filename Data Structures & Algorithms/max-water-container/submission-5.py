class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area = 0

        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j - i)
        #         max_area = max(max_area, area)

        # return max_area

        # left = 0
        # right = len(heights) - 1
        # max_area = 0

        # while left < right:
        #     width = right - left
        #     area = min(heights[left], heights[right]) * width
        #     max_area = max(area, max_area)
        #     if heights[left] > heights[right]:
        #         right -= 1
        #     else:
        #         left += 1
        # return max_area

        amount = 0
        l, r = 0, len(heights)-1

        for i in range(1, max(heights)+1):

            while heights[l] < i:
                l+=1
            
            while heights[r] < i:
                r-=1
            
            else:
                if i * (r - l) > amount:
                    amount = i * (r - l)
        return amount