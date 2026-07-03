
computer_counter = 0
user_counter = 0

def compare_choice_to_list(value, list_of_choices):
    return list_of_choices.index(value)


def calculate_round_winner(user_value, computer_value):
    # It's a tie
    if user_value == computer_value:
        print("Draw")

    # computer wins
    if user_value == 2 and computer_value == 0:
        add_to_counter("computer")
        declare_round_winner(1)
    if user_value == 1 and computer_value == 2:
        add_to_counter("computer")
        declare_round_winner(2)
    if user_value == 0 and computer_value == 1:
        add_to_counter("computer")
        declare_round_winner(3)

    # user wins
    if user_value == 0 and computer_value == 2:
        add_to_counter("user")
        declare_round_winner(1)
    if user_value == 2 and computer_value == 1:
        add_to_counter("user")
        declare_round_winner(2)
    if user_value == 1 and computer_value == 0:
        add_to_counter("user")
        declare_round_winner(3)


def add_to_counter(value):
    if value == "computer":
        global computer_counter
        computer_counter += 1
    if value == "user":
        global user_counter
        user_counter += 1


def declare_round_winner(value):
    if value == 1:
        print("Rock beats Scissors")
    if value == 2:
        print("Scissors beats Paper")
    if value == 3:
        print("Paper beats Rock")


def check_end_condition():
    if computer_counter == 2:
        print("Computer wins!")
        return True
    if user_counter == 2:
        print("User wins!")
        return True
    else:
        return False