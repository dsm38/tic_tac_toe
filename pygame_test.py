import pygame
from gameparts import Board

pygame.init()

CELL_SIZE = 100
BOARD_SIZE = 3
WEIGHT = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

screen = pygame.display.set_mode((WEIGHT, HEIGHT))
pygame.display.set_caption("Крестики-нолики")
screen.fill(BG_COLOR)


def save_result(result):
    file = open("result.txt", "a", encoding="utf-8")
    file.write(result + "\n")
    file.close()


def draw_lines():
    for row in range(1, BOARD_SIZE):
        for col in range(1, BOARD_SIZE):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, row * CELL_SIZE),
                (WEIGHT, row * CELL_SIZE),
                LINE_WIDTH,
            )
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (col * CELL_SIZE, 0),
                (col * CELL_SIZE, HEIGHT),
                LINE_WIDTH,
            )


def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == "X":
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE,
                    ),
                    X_WIDTH,
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE),
                    (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE),
                    X_WIDTH,
                )
            elif board[row][col] == "O":
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2,
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH,
                )


def main():
    game = Board()
    player_current = "X"
    running = True
    draw_lines()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            clicked_row = mouse_y // CELL_SIZE
            clicked_col = mouse_x // CELL_SIZE
            if game.board[clicked_row][clicked_col] == " ":
                game.make_move(clicked_row, clicked_col, player_current)
                if game.check_win(player_current):
                    result = f"Победил {player_current}!"
                    save_result(result)
                    print(result)
                    running = False
                if game.is_board_full():
                    result = "Ничья"
                    save_result(result)
                    print(result)
                    running = False
                player_current = "O" if player_current == "X" else "X"
                draw_figures(game.board)

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
