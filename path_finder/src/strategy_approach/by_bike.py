from strategy_approach.path_finder_strategy import PathFinderStrategy


class ByBike(PathFinderStrategy):
    def __init__(self):
        self.steps = ""

    def find_path(self) -> str:
        self._add_step("1. Make sure to wear your helmet!")
        self._add_step("2. Head north on Main Street.")
        self._add_step("3. Take the path through the diag.")
        self._add_step("4. Head west on Lakeshore Drive.")
        self._add_step("5. You're home!")

        return self.steps

    def _add_step(self, step):
        if len(self.steps) == 0:
            self.steps += f"{step}"
        else:
            self.steps += f"\n{step}"
