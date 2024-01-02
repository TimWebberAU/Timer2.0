#
#     Author: Tim W
#       Date: 28th Dec 2023
#    Project: Creation of a timer app for fun and utility. I use timers for
#             productivity and haven't enjoyed the web-based or Mac varieties.
#  Component: Graphical User Interface
#


import kivy
from abc import ABC, abstractmethod
from dataclasses import dataclass


class GUIinterface(ABC):
    """Interface providing extensibility for alternative GUI's."""

    pass


@dataclass
class GUIoriginal(GUIinterface):
    """Graphical User Interface - version 1."""

    pass