from strategy_approach.path_finder_strategy.path_finder_strategy import PathFinderStrategy


class ByUnknownTransportation(PathFinderStrategy):

    def find_path(self) -> str:
        return "I don't know how to handle that..."
