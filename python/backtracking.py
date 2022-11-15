# Backtracking is used, when we have to explore possibilities incrementally
# and make a decision based on solution of partial subproblem if we should continue
#  exploring the possibility or not. In short, there are two fundamental properties:
# 1. No repetition and completion
# 2. Search Pruning - Make a decision incrementally
# Classic example - N-Queen Problem


# Check if move was safe
def isSafe(row, col):

    for i in range(n):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def place_queen(col):
    global board
    if col >= n:
        return True

    for row in range(n):
        # Search Pruning
        if isSafe(row, col):
            board[row][col] = 1
            result = place_queen(col + 1)
            if result:
                return True
            # Backtracking
            board[row][col] = 0

    return False


if __name__ == '__main__':
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    result = place_queen(0)
    if not result:
        print("No possible state")
    else:
        print(board)
