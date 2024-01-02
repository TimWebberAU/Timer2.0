#
#     Author: Tim W
#       Date: 28th Dec 2023
#    Project: Creation of a timer app for fun and utility. I use timers for
#             productivity and haven't enjoyed the web-based or Mac varieties.
#  Component: Program manager
#


from dataclasses import dataclass


@dataclass
class TimerManager:
    """Handles high-level timer instantiation."""

    def run_timer(self):
        pass


if __name__ == '__main__':
    run_app = TimerManager()
    run_app.run_timer()