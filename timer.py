#
#     Author: Tim W
#       Date: 28th Dec 2023
#    Project: Creation of a timer app for fun and utility. I use timers for
#             productivity and haven't enjoyed the web-based or Mac varieties.
#  Component: Timer display and functionality
#


from abc import ABC, abstractmethod
from dataclasses import dataclass


class TimerDisplayInterface(ABC):
    """Interface providing extensibility for the method of displaying a timer."""

    pass


@dataclass
class TimerDisplay(TimerDisplayInterface):
    """Method of displaying a timer."""

    pass

