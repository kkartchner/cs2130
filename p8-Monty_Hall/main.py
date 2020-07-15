__author__ = "Ky Kartchner"

"""Monty hall probability of winning:
I came across this problem a few years ago, but the percentages of winning when
you switch doors compared to when you don't was still fresh on my mind. I think
at first glance I would have been in the 50/50 chance club, but I soon learned 
that it is 1/3 chance if you stay with your pick and 2/3 chance if you switch. 
This can be proved by simulating it.
"""
import random
from helpers import get_user_choice


def main() -> None:
    """Simulates the Monty Hall 3 doors game and gives the percentage of wins
    for when the contestant switches vs. when they don't switch.
    """

    print("\nWelcome to the Monty Hall 3 Doors Game simulator!\n")
    simulation()
    while get_user_choice("\nRun another simulation?", ['y'], 'n') == 'y':
        simulation()


def simulation() -> None:
    wins_by_not_switching = 0
    wins_by_switching = 0
    number_of_trial_runs = 100_000

    for _ in range(number_of_trial_runs):
        if trial_run(False):
            wins_by_not_switching += 1
        if trial_run(True):
            wins_by_switching += 1

    print(f"You won {wins_by_switching:,} out of {number_of_trial_runs:,} times"
          + f" ({wins_by_switching / number_of_trial_runs:.5%}) by switching.")
    print(f"You won {wins_by_not_switching:,} out of {number_of_trial_runs:,}"
          + f" times ({wins_by_not_switching / number_of_trial_runs:.5%})"
          + " by NOT switching.")


def trial_run(switch_doors: bool) -> bool:
    """Runs a single 3 doors game simulation.

    Args:
        switch_doors (bool): Contestant will switch doors if true
            or keep their original pick if false.

    Returns:
        bool: True if contestant wins; false if they lose.
    """

    unpicked_doors = [1, 2, 3]
    # Randomly choose the winning door.
    winning_door = pick_random(unpicked_doors, False)
    # Then randomly choose one of the 3 doors as the contestant's choice.
    # Host cannot pick contestant door to reveal, so remove it from options
    contestant_choice = pick_random(unpicked_doors, True)

    # Show host cannot reveal the winning door so remove it from pickable doors
    # if it is still there (throws ValueError if not there):
    try:
        unpicked_doors.remove(winning_door)
        switch_door = winning_door
        # host_reveal_door = unpicked_doors[0]
    except ValueError:
        pick_random(unpicked_doors, True)  # host_reveal_door
        switch_door = unpicked_doors[0]

    if switch_doors:
        contestant_choice = switch_door

    return contestant_choice == winning_door


def pick_random(options: [], remove_picked: bool) -> object:
    """Picks a random item from the provided options.

    Args:
        options (list): List of options to choose from.
        remove_picked (bool): If true, removes the random pick from the options;
            else it only returns the random pick without removing it.
    
    Returns:
        object: The randomly selected object.
    """

    random_pick = options[random.randint(0, len(options)-1)]
    if remove_picked:
        options.remove(random_pick)
    return random_pick


if __name__ == "__main__":
    main()
