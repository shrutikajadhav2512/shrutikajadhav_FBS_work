# Print 1 to 100 in snakes and ladder pattern.
board = []

for row in range(10):
    start = row * 10 + 1
    end = start + 10

    if row % 2 == 0:
        board.append(list(range(start, end)))
    else:
        board.append(list(range(start, end))[::-1])

print(board)