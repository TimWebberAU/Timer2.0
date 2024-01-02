#
#     Author: Tim W
#       Date: 28th Dec 2023
#    Project: Creation of a timer app for fun and utility. I use timers for
#             productivity and haven't enjoyed the web-based or Mac varieties.
#  Component: Handling User Input.
#


from abc import ABC, abstractmethod
from dataclasses import dataclass


class UserInputInterface(ABC):
    """Interface providing extensibility for the way user input is gathered."""

    pass


@dataclass
class UserInput(UserInputInterface):
    """Gather and filter user input."""

    pass
