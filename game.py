from gameparts import Board

from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    game = Board()
    player = "X"
    print(f"Первый ходит {player}")
    game.display()
    running = True
    while running:
        print(f"Ходит {player}")
        while True:
            try:
                row = int(input("Введите значение строки: "))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                col = int(input("Введите значение колонки: "))
                if col < 0 or col >= game.field_size:
                    raise FieldIndexError
                if game.board[row][col] != " ":
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    f"Значение должно быть неотрицательным и меньше {game.field_size}."
                )
                print("Пожалуйста, введите значения для строки и столбца заново.")
                continue
            except ValueError as v:
                print(f"Значение должно быть целым целым числом. Ошибка: {v}")
                print("Пожалуйста, введите значения для строки и столбца заново.")
                continue
            except CellOccupiedError:
                print("Позиция занята, ходите в пустую клетку")
                continue
            else:
                break
        game.make_move(row, col, player)
        print("Ход сделан!")
        game.display()
        if game.check_win(player):
            print("Победил", player)
            running = False
        if game.is_board_full():
            print("Ничья.")
            running = False
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()
