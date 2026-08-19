class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row in board:
        #     row_ele = []
        #     for ele in row:
        #         if ele.isnumeric():
        #             if ele in row_ele:
        #                 return False
        #             row_ele.append(ele)
        # for col in range(len(board)):
        #     col_ele = []
        #     for ele in range(len(board)):
        #         if board[ele][col].isnumeric():
        #             if board[ele][col] not in col_ele:
        #                 col_ele.append(board[ele][col])
        #             else:
        #                 return False
        # col_vector = 0
        # row_vector = 0
        # while row_vector < 9:
        #     box_ele = []
        #     for row in range(row_vector, row_vector + 3):
        #         for col in range(col_vector, col_vector + 3):
        #             value = board[row][col]
        #             if value.isnumeric():
        #                 if value in box_ele:
        #                     return False
        #                 box_ele.append(value)
        #     col_vector += 3
        #     if col_vector == 9:
        #         col_vector = 0
        #         row_vector += 3
        # return True

        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        for row in range(9):
            for col in range(9):

                value = board[row][col]

                if value == ".":
                    continue

                box = (row // 3) * 3 + (col // 3)

                if value in rows[row]:
                    return False

                if value in cols[col]:
                    return False

                if value in boxes[box]:
                    return False

                rows[row].append(value)
                cols[col].append(value)
                boxes[box].append(value)

        return True