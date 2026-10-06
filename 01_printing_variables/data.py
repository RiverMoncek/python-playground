# --------------------------------------------------
# LESSON 1: Printing, Variables & Data Types
# --------------------------------------------------

# 1. Outputting Text
# The print() function displays whatever is inside the parentheses to the screen.
print("=== In a galaxy far far away... ===")
print("Hello there, StarWars World!")


# 2. Variables & Data Types
# Variables store values. Python automatically determines the data type.

player_name = "MasterRiver"    # String (str): Plain text inside quotes
level = 99            # Integer (int): Whole numbers
energy_percent = 99.8    # Float (float): Decimal numbers
is_active = True         # Boolean (bool): True or False


# 3. Formatted Strings (f-strings)
# Put an 'f' before quotes to add variables directly inside {curly_braces}.
print(f"Player: {player_name}")
print(f"Level: {level} | Energy: {energy_percent}% | Active: {is_active}")


# 4. Interactive Input
# input() pauses the script and waits for keyboard input from the user.
favorite_topic = input("What Jedi skills do you want to master first? ")
print(f"Got it! Let's build your skills in {favorite_topic}.")
