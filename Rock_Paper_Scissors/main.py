import random
from calculator_manager import (compare_choice_to_list,
                                calculate_round_winner,
                                check_end_condition,)

# Create a list of possible choices
list_of_choices = ["rock", "paper", "scissors"]
while True:
    # Computer picks a random item on the list
    computer_input = random.choice(list_of_choices)
    computer_input = compare_choice_to_list(computer_input, list_of_choices)

    # Define index position on the list
    user_input = input("Rock, Paper, Scissors: ")
    user_input = user_input.strip().lower()
    if user_input not in list_of_choices:
        print("Please enter rock, paper, or scissors\n\n")
        continue
    user_input = compare_choice_to_list(user_input, list_of_choices)

    # Calculate the round winner
    print(f"Computer chose: {list_of_choices[computer_input]}")
    calculate_round_winner(user_input, computer_input)

    # When finishing
    we_have_a_winner = check_end_condition()
    if we_have_a_winner:
        break