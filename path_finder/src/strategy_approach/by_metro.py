from metro_card import MetroCard
from strategy_approach.path_finder_strategy import PathFinderStrategy


class ByMetro(PathFinderStrategy):

    def find_path(self) -> str:
        metro_card = MetroCard(5.7)

        return f"Just hop on the Indigo Line, easy peasy!\n" \
               f"Here's your metro card:\n" \
               f"  ----------------\n" \
               f"  > TOTAL: {metro_card.total_on_card} <\n" \
               f"  ----------------"
