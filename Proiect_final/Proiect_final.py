import pygame
import sys

# Iniț
pygame.init()

# ecr
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("X și O")


white = (255, 255, 255)
black = (0, 0, 0)
line_color = (0, 0, 0)


cell_size = 100
line_width = 15


board = [['' for _ in range(3)] for _ in range(3)]



def draw_board():
    screen.fill(white)

    for i in range(1, 3):

        pygame.draw.line(screen, line_color, (i * cell_size, 0), (i * cell_size, height), line_width)


        pygame.draw.line(screen, line_color, (0, i * cell_size), (width, i * cell_size), line_width)

    for row in range(3):
        for col in range(3):

            if board[row][col] == 'X':
                pygame.draw.line(screen, line_color, (col * cell_size, row * cell_size),
                                 ((col + 1) * cell_size, (row + 1) * cell_size), line_width)
                pygame.draw.line(screen, line_color, ((col + 1) * cell_size, row * cell_size),
                                 (col * cell_size, (row + 1) * cell_size), line_width)

            elif board[row][col] == 'O':
                pygame.draw.circle(screen, line_color, (int((col + 0.5) * cell_size), int((row + 0.5) * cell_size)),
                                   int(cell_size / 2) - line_width, line_width)



def check_winner():

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]


    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]

    return None



def is_board_full():
    for row in board:
        if '' in row:
            return False
    return True



current_player = 'X'
game_over = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // cell_size
            clicked_col = mouseX // cell_size


            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = current_player


                winner = check_winner()
                if winner:
                    print(f'Player {winner} a câștigat!')
                    game_over = True
                elif is_board_full():
                    print('Jocul s-a terminat. Egal!')
                    game_over = True
                else:

                    current_player = 'O' if current_player == 'X' else 'X'


    draw_board()


    pygame.display.flip()
