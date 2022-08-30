from path_finder import PathFinder
from print_wrapper import PrintWrapper


class GetMeHome:
    def __init__(self):
        self.mode_of_transportation = None

    def run(self):
        path_finder = PathFinder(PrintWrapper())

        while True:
            print("How do you want to get home?")
            print("  [bike]\n  [car]\n  [train]\n  [foot]")
            print("  [quit] to stop")

            user_choice = input()
            if user_choice == "quit":
                break

            self.mode_of_transportation = user_choice

            path_finder.best_path_for_travel_by(self.mode_of_transportation)
            print()
