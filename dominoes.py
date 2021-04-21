from itertools import chain
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
            random_domino = random.choice(stock)
            computer.append(random_domino)
            stock.remove(random_domino)
            random_domino = random.choice(stock)
            player.append(random_domino)
            stock.remove(random_domino)
        code = determine_first(computer, player)
    return code


def end_game_condition():
    print('======================================================================')
    print('Stock size:', len(stock))
    print(f'Computer pieces: {len(computer)}\n')
    if len(domino_snake) < 7:
        print(*domino_snake, '\n', sep='')
    else:
        print(domino_snake[0], domino_snake[1], domino_snake[2], '...',
              domino_snake[-3], domino_snake[-2], domino_snake[-1], '\n', sep='')
    print('Your pieces:')
    for index, domino in enumerate(player):
        print(f'{index + 1}:{domino}')

    if len(computer) == 0:
        print("\nStatus: The game is over. The computer won!")
        return True
    elif len(player) == 0:
        print("\nStatus: The game is over. You won!")
        return True
    elif domino_snake[0][0] == domino_snake[-1][-1]:
        first_digit = domino_snake[0][0]
        digit_counter = 0
        for snake in domino_snake:
            if first_digit in snake:
                digit_counter += 1
        if digit_counter == 7:
            print("\nStatus: The game is over. It's a draw!")
            return True
    if move_num == 0:
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
    else:
        print("\nStatus: It's your turn to make a move. Enter your command.")
    return False


def legal_move(move):
    if move == 0:
        return 0
    if move_num == 0 and abs(move) <= len(computer):
        if move < 0 and domino_snake[0][0] in computer[abs(move) - 1]:
            return 0
        elif move > 0 and domino_snake[-1][-1] in computer[abs(move) - 1]:
            return 0
        else:
            return -2
    if move_num == 1 and abs(move) <= len(player):
        if move < 0 and domino_snake[0][0] in player[abs(move) - 1]:
            return 0
        elif move > 0 and domino_snake[-1][-1] in player[abs(move) - 1]:
            return 0
        else:
            return -2
    return -1


def handle_move(move):
    try:
        move = int(move)
    except ValueError:
        return -1
    error_code = legal_move(move)
    if error_code == 0:
        if move_num == 0:
            if move == 0:
                if len(stock) != 0:
                    add_domino = random.choice(stock)
                    computer.append(add_domino)
                    stock.remove(add_domino)
                else:
                    return -3
            else:
                chosen_domino = computer[abs(move) - 1]
                if move < 0:
                    computer.remove(chosen_domino)
                    if domino_snake[0][0] != chosen_domino[-1]:
                        chosen_domino = [chosen_domino[1], chosen_domino[0]]
                    domino_snake.insert(0, chosen_domino)
                elif move > 0:
                    computer.remove(chosen_domino)
                    if domino_snake[-1][-1] != chosen_domino[0]:
                        chosen_domino = [chosen_domino[1], chosen_domino[0]]
                    domino_snake.append(chosen_domino)

        elif move_num == 1:
            if move == 0:
                if len(stock) != 0:
                    add_domino = random.choice(stock)
                    player.append(add_domino)
                    stock.remove(add_domino)
                else:
                    return -3
            else:
                chosen_domino = player[abs(move) - 1]
                if move < 0:
                    player.remove(chosen_domino)
                    if domino_snake[0][0] != chosen_domino[-1]:
                        chosen_domino = [chosen_domino[1], chosen_domino[0]]
                    domino_snake.insert(0, chosen_domino)
                elif move > 0:
                    player.remove(chosen_domino)
                    if domino_snake[-1][-1] != chosen_domino[0]:
                        chosen_domino = [chosen_domino[1], chosen_domino[0]]
                    domino_snake.append(chosen_domino)
    else:
        return error_code


def computer_turn():
    count_nums = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for num in chain(computer, domino_snake):
        count_nums[num[0]] += 1
        count_nums[num[1]] += 1
    scores = list()
    for index, domino in enumerate(computer):
        scores.append((count_nums[domino[0]] + count_nums[domino[1]], index, domino))
    scores.sort(key=lambda x: x[0], reverse=True)
    scores = [(x[1], x[2]) for x in scores]
    for i, turn in scores:
        if domino_snake[-1][-1] in turn:
            return i + 1
        if domino_snake[0][0] in turn:
            return -(i + 1)
    return 0


random.seed()
move_num, domino_snake = distribute()

if move_num == 0:
    computer.remove(domino_snake)
else:
    player.remove(domino_snake)

move_num = (move_num + 1) % 2
domino_snake = [domino_snake]

while not end_game_condition():
    if move_num == 1:
        code = handle_move(input())
        while code == -1 or code == -2:
            if code == -1:
                print("Invalid input. Please try again.")
            elif code == -2:
                print("Illegal move. Please try again.")
            code = handle_move(input())
    else:
        input()
        code = computer_turn()
        handle_move(code)
    move_num = (move_num + 1) % 2
