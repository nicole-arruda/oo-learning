from unittest import TestCase
from unittest.mock import patch

from first_approach.get_me_home import GetMeHome
# from strategy_approach.get_me_home import GetMeHome


class TestGetMeHome(TestCase):

    # noinspection PyPep8Naming
    @patch("print_wrapper.PrintWrapper")
    def setUp(self, MockPrinter):
        self.NO_WEATHER = "no weather"
        self.mock_printer = MockPrinter()
        self.get_me_home = GetMeHome(self.mock_printer)

    def test_best_path_for_travel_by_unrecognized_mode(self):
        self.get_me_home.run("unicorn", self.NO_WEATHER)

        self.mock_printer.print.assert_called_with("I don't know how to handle that...\n"
                                                   "=====\n")

    def test_best_path_for_travel_by_bike(self):
        self.get_me_home.run("bike", self.NO_WEATHER)

        self.mock_printer.print.assert_called_with("1. Make sure to wear your helmet!\n"
                                                   "2. Head north on Main Street.\n"
                                                   "3. Take the path through the diag.\n"
                                                   "4. Head west on Lakeshore Drive.\n"
                                                   "5. You're home!\n"
                                                   "=====\n")

    def test_best_path_for_travel_by_car(self):
        self.get_me_home.run("car", self.NO_WEATHER)

        self.mock_printer.print.assert_called_with("1. Head north on Main Street.\n"
                                                   "2. Head east on College Street.\n"
                                                   "3. Head north on University Ave.\n"
                                                   "4. Head west on Lakeshore Drive.\n"
                                                   "5. You're home!\n"
                                                   "=====\n")

    def test_best_path_for_travel_by_metro(self):
        self.get_me_home.run("metro", self.NO_WEATHER)

        self.mock_printer.print.assert_called_with(f"Just hop on the Indigo Line, easy peasy!\n"
                                                   f"Here's your metro card:\n"
                                                   f"  ----------------\n"
                                                   f"  > TOTAL: $5.70 <\n"
                                                   f"  ----------------\n"
                                                   "=====\n")

    def test_best_path_for_travel_by_foot(self):
        self.get_me_home.run("foot", self.NO_WEATHER)

        self.mock_printer.print.assert_called_with("1. Head west on First Ave.\n"
                                                   "2. Cut north through the high school.\n"
                                                   "3. Head west on College Street.\n"
                                                   "4. Take the path through the diag.\n"
                                                   "5. Head west on Lakeshore Drive.\n"
                                                   "6. You're home!\n"
                                                   "=====\n")

    def test_best_path_for_travel_by_foot_when_rain(self):
        self.get_me_home.run("foot", "rain")

        self.mock_printer.print.assert_called_with("1. Make sure to take your umbrella!\n"
                                                   "2. Head west on First Ave.\n"
                                                   "3. Go past the high school (too muddy to cut through).\n"
                                                   "4. Head north on Cherry Lane.\n"
                                                   "5. Head east on College Street.\n"
                                                   "6. Take the path through the diag.\n"
                                                   "7. Head west on Lakeshore Drive.\n"
                                                   "8. You're home!\n"
                                                   "=====\n")

    def test_two_sets_of_steps_in_a_row_prints_only_second_set(self):
        self.get_me_home.run("car", self.NO_WEATHER)
        self.get_me_home.run("foot", self.NO_WEATHER)
        self.get_me_home.run("bike", self.NO_WEATHER)

        self.mock_printer.print.assert_called_with("1. Make sure to wear your helmet!\n"
                                                   "2. Head north on Main Street.\n"
                                                   "3. Take the path through the diag.\n"
                                                   "4. Head west on Lakeshore Drive.\n"
                                                   "5. You're home!\n"
                                                   "=====\n")
