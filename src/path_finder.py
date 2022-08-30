class PathFinder:
    def __init__(self, print_wrapper):
        self.printer = print_wrapper

    def best_path_for_travel_by(self, mode_of_transportation):
        self.printer.print(f"I'll get you home by {mode_of_transportation}!")
