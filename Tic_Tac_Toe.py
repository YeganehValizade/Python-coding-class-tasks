game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
for row in game_board:
    for cel in row:
        print(cel, end=" ")
    print()

#player1 => X
print("player1")
row = int(input("enter row: "))
cel = int(input("enter cel:"))
game_board[row][cel] = "X"
for row in game_board:
    for cel in row:
        print(cel, end = " ")
    print()

#player2 => O
print("player2")
row = int(input("enter row: "))
cel = int(input("enter cel:"))
game_board[row][cel] = "O"
for row in game_board:
    for cel in row:
        print(cel, end = " ")
    print()
