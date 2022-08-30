from unittest import TestCase
from unittest.mock import MagicMock, patch

from path_finder import PathFinder


class TestPathFinder(TestCase):

    # noinspection PyPep8Naming
    @patch("print_wrapper.PrintWrapper")
    def setUp(self, MockPrinter):
        self.mock_printer = MockPrinter()
        self.path_finder = PathFinder(self.mock_printer)

    def test_best_path_for_travel_by(self):
        self.path_finder.best_path_for_travel_by("any means necessary")
        self.mock_printer.print.assert_called_with("I'll get you home by any means necessary!")