from colored import bg, attr

from main.setup.piece import Piece

black_empty_spot = '%s   %s' % (bg(0), attr(0))
red_empty_spot = '%s   %s' % (bg(124), attr(0))


def make_cpu_side():
    cpu_layout = [[], [], [], []]
    even_squares = range(0, 8, 2)
    odd_squares = range(1, 9, 2)
    side = 'cpu'

    for i in range(0, 4, 2):
        for j in odd_squares:
            piece = Piece(i + 1, chr(65 + j), side)
            cpu_layout[i].append(piece)
        for j in even_squares:
            cpu_layout[i].insert(j, red_empty_spot)

    for i in even_squares:
        piece = Piece(2, chr(65 + i), side)
        cpu_layout[1].append(piece)
    for i in odd_squares:
        cpu_layout[1].insert(i, red_empty_spot)

    for i in odd_squares:
        cpu_layout[3].insert(i, red_empty_spot)
    for i in even_squares:
        cpu_layout[3].insert(i, black_empty_spot)

    return cpu_layout


def make_player_side():
    player_layout = [[], [], [], []]
    even_squares = range(0, 8, 2)
    odd_squares = range(1, 9, 2)
    side = 'player'
    for i in odd_squares:
        player_layout[0].insert(i, black_empty_spot)
    for i in even_squares:
        player_layout[0].insert(i, red_empty_spot)

    for i in range(1, 4, 2):
        for j in even_squares:
            piece = Piece(i + 5, chr(65 + j), side)
            player_layout[i].append(piece)
        for j in odd_squares:
            player_layout[i].insert(j, red_empty_spot)

    for i in odd_squares:
        piece = Piece(7, chr(65 + i), side)
        player_layout[2].append(piece)
    for i in even_squares:
        player_layout[2].insert(i, red_empty_spot)

    return player_layout
