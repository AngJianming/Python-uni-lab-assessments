def get_player_data():
    players = []
    while True:
        name = input("Enter player's name or 'done' to finish: ")
        if name.lower() == 'done':
            break
        while True:
            score = input(f"Enter {name}'s golf score: ")
            if score.isdigit():
                score = int(score)
                break
            else:
                print("Invalid input. Please enter a numeric value for the golf score.")
        players.append((name, score))
    return players


def save_to_file(filename, players):
    with open(filename, 'w') as file:
        for player in players:
            file.write(f"{player[0]}, {player[1]}\n")


def read_from_file(filename):
    players = []
    with open(filename, 'r') as file:
        for line in file:
            name, score = line.strip().split(", ")
            players.append((name, int(score)))
    return players


def main():
    filename = "golf.txt"
    players = get_player_data()
    save_to_file(filename, players)
    players = read_from_file(filename)
    players.sort(key=lambda x: x[1])
    print("\nPlayer Scores (sorted):")
    for player in players:
        print(f"{player[0]}: {player[1]}")


if __name__ == "__main__":
    main()