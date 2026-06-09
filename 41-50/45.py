def chessboard(size):
    for row in range (size):
        line = ""
        for col in range(size):
            line += str((col+row)%2)
        print(line)
x = int(input("Size:"))
chessboard(x)