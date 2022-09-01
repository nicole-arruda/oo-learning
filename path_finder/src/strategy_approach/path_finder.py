from strategy_approach.path_finder_strategy import PathFinderStrategy


class PathFinder:
    def __init__(self, print_wrapper):
        self.printer = print_wrapper

    def best_path_for_travel_by(self, strategy: PathFinderStrategy):
        self.printer.print(strategy.find_path())
