#
#     Author: Tim W
#       Date: 28th Dec 2023
#    Project: Creation of a timer app for fun and utility. I use timers for
#             productivity and haven't enjoyed the web-based or Mac varieties.
#  Component: App Manager + Graphical User Interface (Kivy)
#


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from input import UserInput, UserInputInterface
from timer import TimerDisplay, TimerDisplayInterface


class TimerLayout(GridLayout):
    """Management of the app and layout."""

    def __init__(self, **kwargs):
        super(TimerLayout, self).__init__(**kwargs)

        # The following isn't correct - Instantiation should occur one step back
        # and the objects are passed in but reference the interfaces - Liskov
        # I'm also instantiating the abstract classes here - the interfaces
        # self.__user_input_object = UserInputInterface()
        # self.__timer_display_object = TimerDisplayInterface()

        self.cols = 1   # Outer Grid

        self.internal_layout = GridLayout(cols=3, spacing=10)

        self.add_widget(Label(text="ENTER A TIME"))

        self.internal_layout.add_widget(Label(text="HOURS (0-24)"))
        self.internal_layout.add_widget(Label(text="MINUTES (0-60)"))
        self.internal_layout.add_widget(Label(text="SECONDS (0-60)"))

        self.hours_spinner = Spinner(text="0",
                               values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                       "10", "11", "12", "13", "14", "15", "16", "17", 
                                       "18", "19", "20", "21", "22", "23", "24"),
                               size_hint=(None, None),
                               size=(80, 40))
        self.internal_layout.add_widget(self.hours_spinner)

        self.minutes_spinner = Spinner(text="0",
                               values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                       "10", "11", "12", "13", "14", "15", "16", "17", "18",
                                       "19", "20", "21", "22", "23", "24", "25", "26", "27",
                                       "28", "29", "30", "31", "32", "33", "34", "35", "36",
                                       "37", "38", "39", "40", "41", "42", "43", "44", "45",
                                       "46", "47", "48", "49", "50", "51", "52", "53", "54",
                                       "55", "56", "57", "58", "59", "60"),
                               size_hint=(None, None),
                               size=(80, 40))
        self.internal_layout.add_widget(self.minutes_spinner)

        self.seconds_spinner = Spinner(text="0",
                               values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                       "10", "11", "12", "13", "14", "15", "16", "17", "18",
                                       "19", "20", "21", "22", "23", "24", "25", "26", "27",
                                       "28", "29", "30", "31", "32", "33", "34", "35", "36",
                                       "37", "38", "39", "40", "41", "42", "43", "44", "45",
                                       "46", "47", "48", "49", "50", "51", "52", "53", "54",
                                       "55", "56", "57", "58", "59", "60"),
                               size_hint=(None, None),
                               size=(80, 40),
                               pos_hint={"center_x": .5, "center_y": .5})
        self.internal_layout.add_widget(self.seconds_spinner)

        self.add_widget(self.internal_layout)   # Add internal grid to outer grid

        self.submit_button = Button(text="Begin", font_size=20)
        self.add_widget(self.submit_button)


class TimerApp(App):
    """Main entry point of Kivy App."""

    def build(self):
        return TimerLayout()


if __name__ == '__main__':
    TimerApp().run()          # The run method is a part of the App parent class.