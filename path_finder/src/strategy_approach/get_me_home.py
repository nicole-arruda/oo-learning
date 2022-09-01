from random import randint

from strategy_approach.by_bike import ByBike
from strategy_approach.by_car import ByCar
from strategy_approach.by_foot import ByFoot
from strategy_approach.by_metro import ByMetro
from strategy_approach.by_unknown_transportation import ByUnknownTransportation
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

            if user_choice == "bike":
                strategy = ByBike()
            elif user_choice == "car":
                strategy = ByCar()
            elif user_choice == "metro":
                strategy = ByMetro()
            elif user_choice == "foot":
                strategy = ByFoot()
            else:
                strategy = ByUnknownTransportation()

            path_finder.best_path_for_travel_by(strategy)
            print("=====")
            print()
