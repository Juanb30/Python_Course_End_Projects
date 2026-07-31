# This script runs a text-based adventure game where the player searches for treasure.

LINE = "=" * 48
DIVIDER = "-" * 48


def display_title():
    """Display the title screen."""

    print(f"\n{LINE}")
    print("              THE ADVENTURE GAME")
    print("          Find the Legendary Treasure")
    print("              Created by Juan Benitez")
    print(LINE)


def get_valid_choice(prompt):
    """Ask the player to enter either 1 or 2."""

    while True:
        choice = input(prompt).strip()

        if choice in ("1", "2"):
            return choice

        print("Invalid choice. Please enter 1 or 2.")


def start_game():
    """Display the introduction and collect the player's first choice."""

    display_title()

    player_name = input("\nWhat is your name? ").strip()

    while not player_name:
        print("Please enter a name.")
        player_name = input("What is your name? ").strip()

    print(f"\nWelcome, {player_name}!")
    print(DIVIDER)
    print("For centuries, explorers have searched for a legendary")
    print("treasure hidden deep within an ancient land.")
    print()
    print("Many have entered.")
    print("None have returned.")
    print()
    print("Today, your adventure begins.")
    print(DIVIDER)

    print("\nBefore you are two paths:")
    print("1. Enter the dark forest")
    print("2. Enter the mysterious cave")

    choice = get_valid_choice("\nChoose a path (1 or 2): ")

    return player_name, choice


def display_victory(player_name):
    """Display the winning message."""

    print(f"\n{LINE}")
    print("                 CONGRATULATIONS!")
    print()
    print(f"{player_name}, you discovered the legendary treasure.")
    print("Your name will be remembered for generations.")
    print(LINE)


def display_game_over():
    """Display the losing message."""

    print(f"\n{LINE}")
    print("                    GAME OVER")
    print()
    print("Your journey has come to an end.")
    print("Better luck next time.")
    print(LINE)


def forest_path(player_name):
    """Handle the player's choices in the forest."""

    print(f"\n{DIVIDER}")
    print(f"{player_name}, you enter the dark forest.")
    print(DIVIDER)
    print("The trees are tall, and the path disappears behind you.")
    print("You hear rushing water nearby and notice a tall tree.")

    print("\n1. Follow the river")
    print("2. Climb the tree")

    choice = get_valid_choice("\nChoose an action (1 or 2): ")

    if choice == "1":
        print("\nYou follow the river deeper into the forest.")
        print("The water leads you to a hidden waterfall.")
        print("Behind the waterfall, you discover a secret chamber.")
        print("Inside the chamber is the legendary treasure.")

        display_victory(player_name)
        return "Forest", "Victory"

    print("\nYou climb the tree to search for the treasure.")
    print("A branch breaks beneath you, and you fall to the ground.")

    display_game_over()
    return "Forest", "Defeat"


def cave_path(player_name):
    """Handle the player's choices in the cave."""

    print(f"\n{DIVIDER}")
    print(f"{player_name}, you enter the mysterious cave.")
    print(DIVIDER)
    print("The cave is cold, dark, and completely silent.")
    print("You find an old torch resting beside the cave wall.")

    print("\n1. Light the torch")
    print("2. Proceed in the dark")

    choice = get_valid_choice("\nChoose an action (1 or 2): ")

    if choice == "1":
        print("\nYou light the torch and discover ancient markings.")
        print("The markings guide you through a hidden passage.")
        print("At the end of the passage, you find the treasure.")

        display_victory(player_name)
        return "Cave", "Victory"

    print("\nYou continue through the cave without any light.")
    print("You cannot see a hidden pit ahead and fall into it.")

    display_game_over()
    return "Cave", "Defeat"


def display_summary(player_name, path, outcome):
    """Display a summary of the completed adventure."""

    print(f"\n{DIVIDER}")
    print("               ADVENTURE SUMMARY")
    print(DIVIDER)
    print(f"Player:  {player_name}")
    print(f"Path:    {path}")
    print(f"Outcome: {outcome}")
    print(DIVIDER)


def play_again():
    """Ask the player whether they want to restart the game."""

    print("\nWould you like to play another adventure?")
    print("1. Yes")
    print("2. No")

    choice = get_valid_choice("\nChoose 1 or 2: ")

    return choice == "1"


def main():
    """Run the game and restart it when requested."""

    playing = True

    while playing:
        player_name, choice = start_game()

        if choice == "1":
            path, outcome = forest_path(player_name)
        else:
            path, outcome = cave_path(player_name)

        display_summary(player_name, path, outcome)
        playing = play_again()

    print(f"\n{LINE}")
    print("       Thanks for playing the Adventure Game!")
    print(LINE)


if __name__ == "__main__":
    main()
