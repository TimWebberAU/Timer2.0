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
from time import sleep
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

    # KIVY DOESNT LIKE SLEEP FUNCTION - REPLACE WITH KIVY.CLOCK INSTEAD ********
    def timer_display(self):
        timer_seconds = int(self.seconds.value)

        for i in range(timer_seconds, 0, -1):
            print(i)
            self.ids.timer.text = str(i)
            sleep(1)


class TimerApp(App):
    """Main entry point of Kivy App."""

    def build(self):
        return TimerLayout()


if __name__ == '__main__':
    TimerApp().run()          # The run method is a part of the App parent class.