from unittest import TestCase
from unittest.mock import MagicMock, patch

from path_finder import PathFinder


class TestPathFinder(TestCase):

    # noinspection PyPep8Naming
    @patch("print_wrapper.PrintWrapper")
    def setUp(self, MockPrinter):
        self.mock_printer = MockPrinter()
        self.path_finder = PathFinder(self.mock_printer)

    def test_best_path_for_travel_by_unrecognized_mode(self):
        self.path_finder.best_path_for_travel_by("unicorn")

        self.mock_printer.print.assert_called_with("I don't know how to handle that...")

    def test_best_path_for_travel_by_bike(self):
        self.path_finder.best_path_for_travel_by("bike")

        self.mock_printer.print.assert_called_with("1. Make sure to wear your helmet!\n"
                                                   "2. Head north on Main Street.\n"
                                                   "3. Take the path through the diag.\n"
                                                   "4. Head west on Lakeshore Drive.\n"
                                                   "5. You're home!")
