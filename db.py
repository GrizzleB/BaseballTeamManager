import csv


FILENAME = "players.csv"


def read_players():
    players = []
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                players.append(row)
        return players
    except OSError:
        print(f"\nThe file '{FILENAME}' could not be found.\nPlease fix the file and reload program.")
        exit()


def write_players(players):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(players)