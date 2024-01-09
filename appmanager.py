#
#     Author: Tim W
#       Date: 28th Dec 2023
#    Project: Creation of a timer app for fun and utility. I use timers for
#             productivity and haven't enjoyed the web-based or Mac varieties.
#  Component: App Manager + Graphical User Interface (Kivy)
#


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from input import UserInput, UserInputInterface
from timer import TimerDisplay, TimerDisplayInterface


class TimerLayout(Widget):
    """Management of the app and layout."""

    hours = ObjectProperty(None)
    minutes = ObjectProperty(None)
    seconds = ObjectProperty(None)


        # The following isn't correct - Instantiation should occur one step back
        # and the objects are passed in but reference the interfaces - Liskov
        # I'm also instantiating the abstract classes here - the interfaces
        # self.__user_input_object = UserInputInterface()
        # self.__timer_display_object = TimerDisplayInterface()
    

    def begin_btn(self):
        print(f"Hours: {int(self.hours.value)}, Minutes: {int(self.minutes.value)}, Seconds: {int(self.seconds.value)}")

        self.timer_seconds = int(self.seconds.value)    # Create trackable variable
        Clock.schedule_interval(self.timer_display, 1)  # Kivy scheduler, 1 sec interval


    def timer_display(self, dt_time_elapsed):

        self.ids.timer.text = str(self.timer_seconds)   # Update GUI timer

        if self.timer_seconds <= 0:
            Clock.unschedule(self.timer_display)
        
        self.timer_seconds -= 1



class TimerApp(App):
    """Main entry point of Kivy App."""

    def build(self):
        return TimerLayout()


if __name__ == '__main__':
    TimerApp().run()          # The run method is a part of the App parent class.