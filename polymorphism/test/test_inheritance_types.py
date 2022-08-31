from typing import List
from unittest import TestCase

from inheritance_types import Mallard, RubberDucky, Decoy, Duck


class TestInheritanceTypes(TestCase):
    def test_duck_quacks(self):
        duck = Duck()
        duck.quack()

    def test_mallard_quacks(self):
        duck = Mallard()
        duck.quack()

    def test_rubber_ducky_quacks(self):
        duck = RubberDucky()
        duck.quack()

    def test_decoy_quacks(self):
        duck = Decoy()
        duck.quack()

    def test_all_ducks_quack(self):
        # The compiler will not allow me to add a Human to this list.
        ducks: List[Duck] = [Mallard(), RubberDucky(), Decoy()]
        for duck in ducks:
            duck.quack()
