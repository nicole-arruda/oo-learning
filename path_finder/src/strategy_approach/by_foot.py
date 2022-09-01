from strategy_approach.path_finder_strategy import PathFinderStrategy


class ByFoot(PathFinderStrategy):
    def __init__(self, weather):
        self.steps = ""
        self.is_it_raining = weather == "rain"

    def find_path(self) -> str:
        if self.is_it_raining:
            self._foot_path_during_rain()
        else:
            self._foot_path_usual()

        return self.steps

    def _foot_path_usual(self):
        self._add_step("1. Head west on First Ave.")
        self._add_step("2. Cut north through the high school.")
        self._add_step("3. Head west on College Street.")
        self._add_step("4. Take the path through the diag.")
        self._add_step("5. Head west on Lakeshore Drive.")
        self._add_step("6. You're home!")

    def _foot_path_during_rain(self):
        self._add_step("1. Make sure to take your umbrella!")
        self._add_step("2. Head west on First Ave.")
        self._add_step("3. Go past the high school (too muddy to cut through).")
        self._add_step("4. Head north on Cherry Lane.")
        self._add_step("5. Head east on College Street.")
        self._add_step("6. Take the path through the diag.")
        self._add_step("7. Head west on Lakeshore Drive.")
        self._add_step("8. You're home!")

    def _add_step(self, step):
        if len(self.steps) == 0:
            self.steps += f"{step}"
        else:
            self.steps += f"\n{step}"
