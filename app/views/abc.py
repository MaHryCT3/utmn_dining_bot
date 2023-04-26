from abc import ABC, abstractmethod


class ABCView(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    def render(self, *args, **kwargs) -> str:
        """Method that will render view for user in telegram"""
