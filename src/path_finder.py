class PathFinder:
    def __init__(self, print_wrapper):
        self.printer = print_wrapper
        self.steps = ""

    def best_path_for_travel_by(self, mode_of_transportation):
        if mode_of_transportation == "bike":
            self._add_step("1. Make sure to wear your helmet!")
            self._add_step("2. Head north on Main Street.")
            self._add_step("3. Take the path through the diag.")
            self._add_step("4. Head west on Lakeshore Drive.")
            self._add_step("5. You're home!")

            self.printer.print(self.steps)
        else:
            self.printer.print("I don't know how to handle that...")

    def _add_step(self, step):
        if len(self.steps) == 0:
            self.steps += f"{step}"
        else:
            self.steps += f"\n{step}"
