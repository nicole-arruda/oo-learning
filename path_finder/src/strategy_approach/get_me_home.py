from random import randint

from strategy_approach.path_finder import PathFinder
from print_wrapper import PrintWrapper


class GetMeHome:
    def __init__(self):
        self.weather = ["sun", "rain", "snow"]

    def run(self):
        path_finder = PathFinder(PrintWrapper())

        while True:
            weather = self.weather[randint(0, 2)]
            print(f"Today's weather: {weather}")
            print()

            print("How do you want to get home?")
            print("  [bike]\n  [car]\n  [metro]\n  [foot]")
            print("  [quit] to stop")

            user_choice = input()
            if user_choice == "quit":
                break

            mode_of_transportation = user_choice

            path_finder.best_path_for_travel_by(mode_of_transportation, weather)
            print("=====")
            print()
