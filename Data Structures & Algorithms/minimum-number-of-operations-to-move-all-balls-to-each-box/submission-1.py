class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # result = []

        # for i in range(len(boxes)):
        #     operations = 0

        #     for j in range(len(boxes)):
        #         if boxes[j] == '1':
        #             operations += abs(i - j)

        #     result.append(operations)

        # return result

        res = [0] * len(boxes)

        balls = 0
        moves = 0

        for i in range(len(boxes)):
            res[i] += moves
            if boxes[i] == "1":
                balls += 1
            moves += balls

        balls = 0
        moves = 0

        for i in range(len(boxes) - 1, -1, -1):
            res[i] += moves
            if boxes[i] == "1":
                balls += 1
            moves += balls
        
        return res
