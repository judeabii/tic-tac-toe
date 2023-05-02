replay = "Y"
while replay == "Y":
    board = [[[' '], [' '], [' ']],
             [[' '], [' '], [' ']],
             [[' '], [' '], [' ']]]

    for row in range(0, 3):
        for column in range(0, 3):
            board[row][column] = " "

    values = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}

    print("POSITIONS")
    print("-------------------")
    print("    1 | 2  | 3 ")
    print("-------------------")
    print("    4 | 5  | 6 ")
    print("-------------------")
    print("    7 | 8  | 9 ")
    print("\n")


    def print_board():
        print(f"    {board[0][0]} | {board[0][1]}  | {board[0][2]} ")
        print("-------------------")
        print(f"    {board[1][0]} | {board[1][1]}  | {board[1][2]} ")
        print("-------------------")
        print(f"    {board[2][0]} | {board[2][1]}  | {board[2][2]} ")


    def insert_value(num, value):
        if num == 1:
            board[0][0] = value
        elif num == 2:
            board[0][1] = value
        elif num == 3:
            board[0][2] = value
        elif num == 4:
            board[1][0] = value
        elif num == 5:
            board[1][1] = value
        elif num == 6:
            board[1][2] = value
        elif num == 7:
            board[2][0] = value
        elif num == 8:
            board[2][1] = value
        elif num == 9:
            board[2][2] = value
        values[num] = True


    def check_winner():
        for item in range(0, 3):
            # print(item)
            # print(board[item][0] == board[item][1] == board[item][2])
            if board[item][0] == board[item][1] == board[item][2] and board[item][0] != " " \
                    and board[item][1] != " " and board[item][2] != " ":
                #  print(board[item][0] == board[item][1] == board[item][2])
                return False
            # print(board[0][item] == board[1][item] == board[2][item])
            if board[0][item] == board[1][item] == board[2][item] and board[0][item] != " " and board[1][item] != " " and \
                    board[2][item] != " ":
                return False
            if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " " and board[1][1] != " " \
                    and board[2][2] != " ":
                return False
            if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " " and board[1][1] != " " \
                    and board[2][0] != " ":
                return False
        return True


    def check_draw():
        available_places = 0
        for row in range(0, 3):
            for column in range(0, 3):
                #  print(board[row][column])
                if board[row][column] == " ":
                    available_places += 1
        if available_places >= 1:
            return False
        else:
            return True


    def check_overwrite(position):
        return values[position]


    def player():
        '''p1_position = int(input("Enter the position for X\n"))
        insert_value(p1_position, "X")
        print_board()
        p2_position = int(input("Enter the position for O\n"))
        insert_value(p2_position, "O")
        print_board()'''

        while check_winner() is True:
            p1_position = int(input("Enter the position for X\n"))
            while check_overwrite(p1_position) is True:
                p1_position = int(input("This position is already taken, enter another position for X\n"))
            insert_value(p1_position, "X")
            print_board()

            if check_winner() is False:
                print("Congrats! X is the winner")
                break

            if check_draw() is True:
                print("It's a draw!")
                break

            p2_position = int(input("Enter the position for O\n"))
            while check_overwrite(p2_position) is True:
                p2_position = int(input("This position is already taken, enter another position for O\n"))
            insert_value(p2_position, "O")
            print_board()

            if check_winner() is False:
                print("Congrats! O is the winner")
                break

            if check_draw() is True:
                print("It's a draw!")
                break


    player()
    replay = input("Do you want to play again? (Y/N)").upper()
print("Thanks for playing!")