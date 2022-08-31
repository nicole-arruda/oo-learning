from unittest import TestCase

from duck_types import Mallard, RubberDucky, Decoy, Human


class TestDuckTypes(TestCase):
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
        # I can add a Human to this list, but I'll get an exception if it tries to quack.
        ducks = [Mallard(), RubberDucky(), Decoy()]
        for duck in ducks:
            duck.quack()
