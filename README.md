# tic-tac-toe
Simulation of the tic tac toe game in the console while making use of 2-dimensional lists and dictionaries Python

## Code Explanation:
Creating the empty tic tac toe board using a 2D list
```commandline
    board = [[[' '], [' '], [' ']],
             [[' '], [' '], [' ']],
             [[' '], [' '], [' ']]]

    for row in range(0, 3):
        for column in range(0, 3):
            board[row][column] = " "
```

Function to check if a user is a winner, at any given time

```commandline
    def check_winner():
        for item in range(0, 3):
            if board[item][0] == board[item][1] == board[item][2] and board[item][0] != " " \
                    and board[item][1] != " " and board[item][2] != " ":
                return False          
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
```

Check if there is a draw - If the empty spaces on the board is more than or equal to 1, the game can continue, else it is called as a draw.
```commandline
    def check_draw():
        available_places = 0
        for row in range(0, 3):
            for column in range(0, 3):
                if board[row][column] == " ":
                    available_places += 1
        if available_places >= 1:
            return False
        else:
            return True
```
A dictionary is used to make sure that the values are not overwritten in the board
```commandline
values = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}
```
Whenever a user enters a value in a location, the corresponding value changes from _False_ to _True_.