class Board:
    field_size = 3

    def __init__(self):
        self.board = [
            [" " for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player
        
    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def is_board_full(self):
        for row in range(self.field_size):
            for col in range(self.field_size):
                if self.board[row][col] == " ":
                    return False
        return True

    def check_win(self, player):
        for i in range(self.field_size):
            if all([self.board[i][j] == player for j in range(self.field_size)]) or all(
                [self.board[j][i] == player for j in range(self.field_size)]
            ):
                return True
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False

    def __str__(self):
        return f"Размер игрового поля ({self.field_size} X {self.field_size})"



