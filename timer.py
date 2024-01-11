#
#     Author: Tim W
#       Date: 28th Dec 2023
#    Project: Creation of a timer app for fun and utility. I use timers for
#             productivity and haven't enjoyed the web-based or Mac varieties.
#  Component: Timer display and functionality
#


from abc import ABC, abstractmethod
from dataclasses import dataclass
# from Kivy.clock import Clock


class TimerDisplayInterface(ABC):
    """Interface providing extensibility for the method of displaying a timer."""

    @abstractmethod
    def timer_display(self, dt_time_elapsed):
        pass

    @abstractmethod
    def timer_format(self):
        pass


@dataclass
class TimerDisplay(TimerDisplayInterface):
    """Method of displaying a timer."""

    # timer_seconds: int
    # timer_minuntes: int
    # timer_hours: int

    def timer_display(self, dt_time_elapsed):
                        
        self.ids.timer.text = self.timer_format()       # Update GUI timer

        if self.timer_seconds == 0:

            if self.timer_minutes > 0:
                self.timer_minutes -= 1
                self.timer_seconds = 60
            
            if self.timer_minutes == 0:

                if self.timer_hours > 0:
                    self.timer_hours -= 1
                    self.timer_minutes = 59
                    self.timer_seconds = 60

        if self.timer_seconds <= 0 and self.timer_minutes <= 0 and self.timer_hours <= 0:
            Clock.unschedule(self.timer_display)
        
        self.timer_seconds -= 1
    

    def timer_format(self):
        return f"Hr: {str(self.timer_hours)}  Min: {str(self.timer_minutes)}  Sec: {str(self.timer_seconds)}"

