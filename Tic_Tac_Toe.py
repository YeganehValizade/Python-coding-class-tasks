def show():
    for row in game:
        for cel in row:
            print(cel, end = " ")
        print()

def check_game():
    flag = 0
    if game[0][0] == "X" and game[0][1] == "X" and game[0][2] == "X":
        print("player2 win!")
        flag = 1
    if game[0][0] == "O" and game[0][1] == "O" and game[0][2] == "O":
        print("player1 win!")
        flag = 1

game = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]
show()
while True:
    print("player1")
    while True:
        row = int(input("enter row:"))
        cel = int(input("enter cel:"))
        if 0 <= row <= 2 and 0 <= cel <= 2:
            if game[row][cel] == "-":
                game[row][cel] = "O"
                show()
                check = check_game()
                break
            else: print("choose another cel")
        else:
            print("choose between 0 and 2")
    if check == 1:
     break

    print("player2")
    while True:
            row = int(input("enter row: "))
            cel = int(input("enter cel: "))
            if 0 <= row <= 2 and 0 <= cel <= 2:
                if game[row][cel] == "-":
                    game[row][cel] = "X"
                    show()
                    check_game()
                    break
                else: print("choose another cel")
            else:
                print("choose between 0 and 2")            
    if check == 1:
     break
