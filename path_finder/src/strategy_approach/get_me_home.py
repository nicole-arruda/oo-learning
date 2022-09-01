from strategy_approach.path_finder_strategy.by_bike import ByBike
from strategy_approach.path_finder_strategy.by_car import ByCar
from strategy_approach.path_finder_strategy.by_foot import ByFoot
from strategy_approach.path_finder_strategy.by_metro import ByMetro
from strategy_approach.path_finder_strategy.by_unknown_transportation import ByUnknownTransportation
from strategy_approach.path_finder import PathFinder
from print_wrapper import PrintWrapper


class GetMeHome:

    def __init__(self, print_wrapper=PrintWrapper()):
        self.path_finder = PathFinder(print_wrapper)

    def run(self, mode_of_transportation, weather):
        if mode_of_transportation == "bike":
            strategy = ByBike()
        elif mode_of_transportation == "car":
            strategy = ByCar()
        elif mode_of_transportation == "metro":
            strategy = ByMetro()
        elif mode_of_transportation == "foot":
            strategy = ByFoot(weather)
        else:
            strategy = ByUnknownTransportation()

        self.path_finder.best_path_for_travel_by(strategy)
