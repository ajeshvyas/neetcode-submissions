class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        for _ in range(len(numbers)):
            if left >= right:
                break
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current < target:
                left += 1
            else:
                right -= 1