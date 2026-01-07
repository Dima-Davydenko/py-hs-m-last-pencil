import random

pencils_visual = "|"
players_names = ["John", "Jack"]


def get_pencils_number():
    while True:
        try:
            pencils_num = int(input())
            if pencils_num == 0:
                print("The number of pencils should be positive")
                continue
            if pencils_num < 0:
                raise ValueError
        except ValueError:
            print("The number of pencils should be numeric")
        else:
            return pencils_num


def get_first_player(players):
    print(f"Who will be the first ({players[0]}, {players[1]}):")
    while True:
        name = input()
        if name in players:
            return name
        else:
            print(f"Choose between {players[0]} and {players[1]}")


def remove_pencils(pencils):
    possible_values = "123"
    while True:
        pencils_to_remove = input()
        if pencils_to_remove not in possible_values:
            print("Possible values: '1', '2' or '3'")
        elif int(pencils_to_remove) > pencils:
            print("Too many pencils were taken")
        else:
            break
    return pencils - int(pencils_to_remove)


def bot_move(pencils):
    win_limit = 4
    if pencils == 1:
        pencils_to_remove = 1
    elif pencils % win_limit == 0:
        pencils_to_remove = 3
    elif pencils % win_limit == 1:
        pencils_to_remove = random.randint(1, 3)
    elif pencils % win_limit == 2:
        pencils_to_remove = 1
    else:
        pencils_to_remove = 2
    print(pencils_to_remove)
    return pencils - pencils_to_remove


def run_game(pencils, player1, player2):
    turn = 0
    while pencils > 0:
        turn += 1
        current_player = player1 if turn % 2 == 1 else player2
        print(f"{current_player}'s turn:")
        if current_player == "Jack":
            pencils = bot_move(pencils)
        else:
            pencils = remove_pencils(pencils)
        print(pencils_visual * pencils)
    winner = player2 if turn % 2 == 1 else player1
    print(f"{winner} won!")


def main_logic():
    print("How many pencils would you like to use?")
    pencils = get_pencils_number()
    first_player = get_first_player(players_names)
    players_names.remove(first_player)
    second_player = players_names[0]
    print(pencils_visual * pencils)
    run_game(pencils, first_player, second_player)


main_logic()
