from strategy_approach.path_finder_strategy.path_finder_strategy import PathFinderStrategy


class PathFinder:
    def __init__(self, print_wrapper):
        self.printer = print_wrapper

    def best_path_for_travel_by(self, strategy: PathFinderStrategy):
        path = strategy.find_path()
        path += "\n=====\n"

        self.printer.print(path)
