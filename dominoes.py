import random


stock = list()
computer = list()
player = list()


def determine_first(computer_pieces, player_pieces):
    for i in range(6, -1, -1):
        if [i, i] in computer_pieces:
            return 0, [i, i]
        elif [i, i] in player_pieces:
            return 1, [i, i]
    return -1


def distribute():
    global stock
    code = determine_first(computer, player)
    while code == -1:
        stock = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
                 [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2],
                 [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5],
                 [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]
        for _ in range(7):
            domino = random.choice(stock)
            computer.append(domino)
            stock.remove(domino)
            domino = random.choice(stock)
            player.append(domino)
            stock.remove(domino)
        code = determine_first(computer, player)
    return code


random.seed()

first_player, domino_snake = distribute()

print('======================================================================')
print('Stock size:', len(stock))
print(f'Computer pieces: {len(computer)}\n')
print(domino_snake, '\n')

if first_player == 0:
    computer.remove(domino_snake)
    print('Your pieces:')
    for index, domino in enumerate(player):
        print(f'{index + 1}:{domino}')
    print("\nStatus: It's your turn to make a move. Enter your command.")
else:
    player.remove(domino_snake)
    print('Your pieces:')
    for index, domino in enumerate(player):
        print(f'{index + 1}:{domino}')
    print("\nStatus: Computer is about to make a move. Press Enter to continue...")
