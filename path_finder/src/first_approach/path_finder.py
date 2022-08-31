from first_approach.metro_card import MetroCard


class PathFinder:
    def __init__(self, print_wrapper):
        self.printer = print_wrapper
        self.steps = ""

    def best_path_for_travel_by(self, mode_of_transportation, weather):
        if mode_of_transportation == "bike":
            self._add_step("1. Make sure to wear your helmet!")
            self._add_step("2. Head north on Main Street.")
            self._add_step("3. Take the path through the diag.")
            self._add_step("4. Head west on Lakeshore Drive.")
            self._add_step("5. You're home!")

            self.printer.print(self.steps)
            self.steps = ""
        elif mode_of_transportation == "car":
            self._add_step("1. Head north on Main Street.")
            self._add_step("2. Head east on College Street.")
            self._add_step("3. Head north on University Ave.")
            self._add_step("4. Head west on Lakeshore Drive.")
            self._add_step("5. You're home!")

            self.printer.print(self.steps)
            self.steps = ""
        elif mode_of_transportation == "metro":
            metro_card = MetroCard(5.7)
            self.printer.print(f"Just hop on the Indigo Line, easy peasy!\n"
                               f"Here's your metro card:\n"
                               f"  ----------------\n"
                               f"  > TOTAL: {metro_card.total_on_card} <\n"
                               f"  ----------------")
        elif mode_of_transportation == "foot":
            if weather == "rain":
                self._add_step("1. Make sure to take your umbrella!")
                self._add_step("2. Head west on First Ave.")
                self._add_step("3. Go past the high school (too muddy to cut through).")
                self._add_step("4. Head north on Cherry Lane.")
                self._add_step("5. Head east on College Street.")
                self._add_step("6. Take the path through the diag.")
                self._add_step("7. Head west on Lakeshore Drive.")
                self._add_step("8. You're home!")

                self.printer.print(self.steps)
                self.steps = ""
            else:
                self._add_step("1. Head west on First Ave.")
                self._add_step("2. Cut north through the high school.")
                self._add_step("3. Head west on College Street.")
                self._add_step("4. Take the path through the diag.")
                self._add_step("5. Head west on Lakeshore Drive.")
                self._add_step("6. You're home!")

                self.printer.print(self.steps)
                self.steps = ""

        else:
            self.printer.print("I don't know how to handle that...")

    def _add_step(self, step):
        if len(self.steps) == 0:
            self.steps += f"{step}"
        else:
            self.steps += f"\n{step}"
