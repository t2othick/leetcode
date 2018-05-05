class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(0, len(board)):
            nums = set()
            for j in range(0, len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in nums:
                    return False
                nums.add(board[i][j])

        for i in range(0, len(board)):
            nums = set()
            for j in range(0, len(board[i])):
                if board[j][i] == '.':
                    continue
                if board[j][i] in nums:
                    return False
                nums.add(board[j][i])

        i = 0
        while i <= 6:
            j = 0
            while j <= 6:
                nums = set()
                for k in range(0, 3):
                    for m in range(0, 3):
                        if board[i + k][j + m] == '.':
                            continue
                        if board[i + k][j + m] in nums:
                            return False
                        nums.add(board[i + k][j + m])
                j += 3
            i += 3

        return True
