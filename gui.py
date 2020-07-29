import pygame
import sys
from my_tic_tac_toe import *
import time

# Initialising pygame
pygame.init()

# Setting initial values
player_option = True
player_turn = False

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setting screen, name and icon
size = (width, height) = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TicTacToe')

# Setting Font
my_font = 'OpenSans-Regular.ttf'
small_font = pygame.font.Font(my_font, 20)
medium_font = pygame.font.Font(my_font, 28)
large_font = pygame.font.Font(my_font, 40)


def game_decider(text):
    game_decision = large_font.render(text, True, WHITE)
    game_decision_rect = game_decision.get_rect()
    game_decision_rect.center = (width / 2, height / 7)
    screen.blit(game_decision, game_decision_rect)


# Play again box
def play_again():
    play_agan = medium_font.render('PLAY AGAIN', True, BLACK)
    pla_again_rect = play_agan.get_rect()
    play_again_box = pygame.Rect(width / 4, height * (6 / 7) - 20,
                                 width / 2, 50)
    pygame.draw.rect(screen, WHITE, play_again_box)
    pla_again_rect.center = play_again_box.center
    screen.blit(play_agan, pla_again_rect)

    # Checking of play game box is pressed
    click, _, _ = pygame.mouse.get_pressed()
    if click == 1:
        coordinate = pygame.mouse.get_pos()
        if play_again_box.collidepoint(coordinate[0], coordinate[1]):
            ai_moves.clear()
            player_moves.clear()
            Game_over.lost = False
            Game_over.game_over = False


while True:

    # Setting bg color
    screen.fill(BLACK)

    # To end the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if player_option:
        # Setting instruction text
        instruction_text = large_font.render('Play Tic-Tac-Toe', True, WHITE)
        instruction_text_rect = instruction_text.get_rect()
        instruction_text_rect.center = (width / 2, height / 4)
        screen.blit(instruction_text, instruction_text_rect)

        # Setting player button
        fp_sentence_x = medium_font.render('Play as X', True, BLACK)
        fp_sentence_0 = medium_font.render('Play as 0', True, BLACK)
        fp_sentence_x_rect = fp_sentence_x.get_rect()
        fp_sentence_0_rect = fp_sentence_0.get_rect()
        fp_sentence_x_box = pygame.Rect(70, height * (2 / 4), 200, 70)
        fp_sentence_0_box = pygame.Rect(width - 270, height * (2 / 4), 200, 70)
        fp_sentence_x_rect.center = fp_sentence_x_box.center
        fp_sentence_0_rect.center = fp_sentence_0_box.center

        pygame.draw.rect(screen, WHITE, fp_sentence_x_box)
        pygame.draw.rect(screen, WHITE, fp_sentence_0_box)
        screen.blit(fp_sentence_x, fp_sentence_x_rect)
        screen.blit(fp_sentence_0, fp_sentence_0_rect)

        # Checking if buttons are pressed
        mouse = pygame.mouse.get_pressed()
        left, _, _ = mouse

        # Checking which button is pressed
        if left == 1:
            position = pygame.mouse.get_pos()
            if fp_sentence_0_box.collidepoint(position[0], position[1]):
                Gamer.player = O
                Gamer.ai = X
                player_option = False
                time.sleep(0.3)
            elif fp_sentence_x_box.collidepoint(position[0], position[1]):
                Gamer.player = X
                Gamer.ai = O
                player_turn = True
                player_option = False
                time.sleep(0.3)
        pygame.display.update()
        continue

    # Setting board origin
    board_origin = (width * (1 / 3), height * (2 / 7))

    # Setting X and O
    player_rep = large_font.render(Gamer.player, True, WHITE)
    player_rep_rect = player_rep.get_rect()
    ai_rep = large_font.render(Gamer.ai, True, WHITE)
    ai_rep_rect = ai_rep.get_rect()

    # Setting cells
    cells = dict()
    cell_size = (int(width / 9), height * (1 / 7))
    for i in range(0, 3):
        for j in range(0, 3):
            cells[(i, j)] = pygame.Rect(board_origin[0] + i * cell_size[0],
                                        board_origin[1] + j * cell_size[1],
                                        cell_size[0], cell_size[1])
            pygame.draw.rect(screen, WHITE, cells[(i, j)], 1)

            if (i, j) in player_moves:
                player_rep_rect.center = cells[(i, j)].center
                screen.blit(player_rep, player_rep_rect)
            elif (i, j) in ai_moves:
                ai_rep_rect.center = cells[(i, j)].center
                screen.blit(ai_rep, ai_rep_rect)

    # Checking if the game is lost
    if Game_over.lost:
        Game_over.game_over = True
        # Printing Game position
        game_decider('YOU LOST THE GAME')
        play_again()
        if Gamer.player == X:
            player_turn = True
        else:
            player_turn = False

    # Checking if all the cells are taken
    elif len(ai_moves) + len(player_moves) >= 9:
        Game_over.game_over = True
        game_decider('TIE')
        play_again()
        if Gamer.player == X:
            player_turn = True
        else:
            player_turn = False

    # Taking turns
    if not Game_over.game_over:
        if player_turn:
            game_decider('Your Turn')
            # Checking for mouse action
            left, _, _ = pygame.mouse.get_pressed()
            if left == 1:
                position = pygame.mouse.get_pos()

                # Checking which cell is clicked
                for key in cells.keys():
                    if key in player_moves or key in ai_moves:
                        continue
                    if cells[key].collidepoint(position[0], position[1]):
                        player_moves.append(key)
                        player_turn = False
                        break
        # Transferring the game to AI
        else:
            game_decider('Computer Thinking....')
            current_time = pygame.time.get_ticks()
            exit_time = current_time + 0.4

            if pygame.time.get_ticks() >= exit_time:
                cell = ai_perfomance()
                ai_moves.append(cell)
                player_turn = True

    # Updating the screen
    pygame.display.update()
