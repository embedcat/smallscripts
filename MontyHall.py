import random

NUM_GAMES = 1000000


def play(change=False):
    doors = [0, 0, 0]
    car = random.randint(0, 2)
    doors[car] = 1
    choice = random.randint(0, 2)
    if change:
        return False if choice is car else True
    else:
        return doors[choice] is 1


def play_match(num, change):
    result = []
    for _ in range(num):
        result.append(play(change))
    return result.count(True) / len(result)


if __name__ == "__main__":
    random.seed()
    print("Playing {} games...".format(NUM_GAMES))
    print("Winrate without choice change:", play_match(NUM_GAMES, False))
    print("Winrate with choice change:", play_match(NUM_GAMES, True))
