# Setting player as None initially
class Gamer:
    player = None
    ai = None


#  Setting variables
O = '0'
X = 'X'
player_moves = []
ai_moves = []
width = 3
height = 3
center = (1, 1)
corner = [(0, 0), (2, 0), (0, 2), (2, 2)]
edges = [(1, 0), (0, 1), (2, 1), (1, 2)]


class Game_over:
    lost = False
    game_over = False


# Checking if winning pattern could be made
def checking_line(item_dup, moves):
    row_count = {0: 0, 1: 0, 2: 0}
    column_count = {0: 0, 1: 0, 2: 0}
    diagonal_up_count = 0
    diagonal_down_count = 0
    moves_dup = moves.copy()
    moves_dup.append(item_dup)

    for (i, j) in moves_dup:
        row_count[j] += 1
        column_count[i] += 1
        if i == j:
            diagonal_down_count += 1
        if (width - 1 - i) == j:
            diagonal_up_count += 1

    for i in range(0, width):
        if row_count[i] == 3 or column_count[i] == 3:
            return 1
        elif diagonal_down_count == 3 or diagonal_up_count == 3:
            return 1
    return 0


def actions():
    action = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if (i, j) in player_moves or (i, j) in ai_moves:
                continue
            action.add((i, j))
    return action


def tricks():
    if Gamer.ai == X:
        if center not in ai_moves:
            return center
        for row in corner:
            if row not in ai_moves and row not in player_moves:
                (i, j) = row
                if (i + 1, j) not in player_moves and (i, j + 1) not in \
                        player_moves and (i - 1, j) not in player_moves and (
                        i, j - 1) not in player_moves:
                    return row
        return 0
    elif Gamer.ai == O:
        if center not in ai_moves and center not in player_moves:
            return center
        if center in ai_moves:
            for row in edges:
                if row not in ai_moves and row not in player_moves:
                    return row
        else:
            for row in corner:
                if row not in ai_moves and row not in player_moves:
                    return row
        return 0


def ai_perfomance():
    available_actions = actions()

    for item in available_actions:
        if checking_line(item, ai_moves):
            Game_over.lost = True
            return item

    for item in available_actions:
        if checking_line(item, player_moves):
            return item

    clue = tricks()
    if clue:
        return clue
    else:
        return available_actions.pop()
