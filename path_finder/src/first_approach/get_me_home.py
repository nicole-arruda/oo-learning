from first_approach.path_finder import PathFinder
from print_wrapper import PrintWrapper


class GetMeHome:

    def __init__(self, print_wrapper=PrintWrapper()):
        self.path_finder = PathFinder(print_wrapper)

    def run(self, mode_of_transportation, weather):
        self.path_finder.best_path_for_travel_by(mode_of_transportation, weather)
