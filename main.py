import csv
from decimal import Decimal
from decimal import ROUND_HALF_UP


FILENAME = "players.csv"


def read_players():
    players = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            players.append(row)
    return players


def write_players(players):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(players)


def list_players(players):
    print(f"{'':4}{'Player':12} {'POS':4} {'AB':6} {'H':6} {'AVG'}")
    print("-" * 60)

    for i, player in enumerate(players, start=1):
        avg = Decimal(player[3]) / Decimal(player[2])
        avg = avg.quantize(Decimal("1.000"), ROUND_HALF_UP)
        print(f"{i:<3} {player[0]:12} {player[1]:4} {player[2]:6} {player[3]:6} {avg}")


def display_menu():
    print("=" * 60)
    print(f"{'Baseball Team Manager':>40}")
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print("\nPOSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("=" * 60)


def main():
    display_menu()
    players = read_players()
    while True:
        command = input("Command: ")
        if command == "1":
            list_players(players)
        elif command == "7":
            break
        else:
            print("Invalid command. Please try again.")
    print("\nFarewell")


if __name__ == "__main__":
    main()
