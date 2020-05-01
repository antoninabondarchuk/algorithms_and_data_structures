def isValidSudoku(board) -> bool:
    met_nums = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                continue
            if not board[i][j] in met_nums:
                met_nums[board[i][j]] = [(i, j), ]
                continue
            for coordinates in met_nums[board[i][j]]:
                if i == coordinates[0] or j == coordinates[1]:
                    return False
                if (i // 3 == coordinates[0] // 3) and (j // 3 == coordinates[1] // 3):
                    return False
            met_nums[board[i][j]].append((i, j))
    return True


if __name__ == '__main__':
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    result1 = isValidSudoku(board)
    print(result1)
