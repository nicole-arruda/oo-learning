from strategy_approach.path_finder_strategy import PathFinderStrategy


class ByFoot(PathFinderStrategy):
    def __init__(self):
        self.steps = ""

    def find_path(self) -> str:
        self._add_step("1. Head west on First Ave.")
        self._add_step("2. Cut north through the high school.")
        self._add_step("3. Head west on College Street.")
        self._add_step("4. Take the path through the diag.")
        self._add_step("5. Head west on Lakeshore Drive.")
        self._add_step("6. You're home!")

        return self.steps

    def _add_step(self, step):
        if len(self.steps) == 0:
            self.steps += f"{step}"
        else:
            self.steps += f"\n{step}"
