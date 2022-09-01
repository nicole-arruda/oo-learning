from abc import ABC, abstractmethod


class PathFinderStrategy(ABC):
    @abstractmethod
    def find_path(self) -> str:
        pass
