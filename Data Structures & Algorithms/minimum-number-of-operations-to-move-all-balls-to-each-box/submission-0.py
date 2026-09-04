class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []

        for i in range(len(boxes)):
            operations = 0

            for j in range(len(boxes)):
                if boxes[j] == '1':
                    operations += abs(i - j)

            result.append(operations)

        return result