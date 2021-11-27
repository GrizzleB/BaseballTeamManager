from decimal import Decimal
from decimal import ROUND_HALF_UP
from db import read_players
from db import write_players

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def list_players(players):
    print()
    # formatting the header before the list is generated
    print(f"{'':4}{'Player':12} {'POS':4} {'AB':6} {'H':6} {'AVG'}")
    print("-" * 60)
    for i, player in enumerate(players, start=1):
        avg = Decimal(player[3]) / Decimal(player[2])
        avg = avg.quantize(Decimal("1.000"), ROUND_HALF_UP)
        print(f"{i:<3} {player[0]:12} {player[1]:4} {player[2]:6} {player[3]:6} {avg}")
    print()


def add_player(players):
    name = input("Name: ")
    while True:  # Ensure the position is legitimate
        position = input("Position: ").upper()
        if position in POSITIONS:
            break
        else:
            print("Invalid position. Please try again.")
    while True:  # Ensure they don't use negatives
        at_bats = input("At bats: ")
        if int(at_bats) >= 0:
            break
        else:
            print("Cannot be negative. Please try again.")
    while True:
        hits = input("Hits: ")
        if int(hits) >= 0:
            break
        else:
            print("Cannot be negative. Please try again.")
    player = [name, position, at_bats, hits]
    players.append(player)
    write_players(players)
    print(f"{name} was added.\n")


def remove_player(players):
    while True:
        index = int(input("Lineup number to be removed: "))
        if index < 1 or index > len(players):
            print("Invalid lineup number.\n")
        else:
            player = players.pop(index - 1)
            write_players(players)
            print(f"{player[0]} was removed.\n")


#  def edit_position(players):



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
        command = input("Menu option: ")
        if command == "1":
            list_players(players)
        elif command == "2":
            add_player(players)
        elif command == "3":
            remove_player(players)
        elif command == "7":
            break
        else:
            display_menu()
            print("Invalid menu option. Please try again.\n")
    print("\nTake care!")


if __name__ == "__main__":
    main()
