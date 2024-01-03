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
from input import UserInput, UserInputInterface
from timer import TimerDisplay, TimerDisplayInterface


class TimerLayout(GridLayout):
    """Management of the app and layout."""

    def __init__(self, **kwargs):
        super(TimerLayout, self).__init__(**kwargs)

        # The following isn't correct - Instantiation should occur one step back
        # and the objects are passed in but reference the interfaces - Liskov
        # I'm also instantiating the parent classes here - the interfaces
        # self.__user_input_object = UserInputInterface()
        # self.__timer_display_object = TimerDisplayInterface()

        self.cols = 1

        self.add_widget(Label(text="ENTER A TIME"))

        self.user_input_hours = TextInput(hint_text="HOURS (0-24)", multiline=False, input_filter=self.filter_hours)
        self.add_widget(self.user_input_hours)
        self.user_input_minutes = TextInput(hint_text="MINUTES",multiline=False)
        self.add_widget(self.user_input_minutes)
        self.user_input_seconds = TextInput(hint_text="SECONDS",multiline=False)
        self.add_widget(self.user_input_seconds)

        self.submit_button = Button(text="Begin", font_size=20)

        self.add_widget(self.submit_button)
    

    def filter_hours(self, input_text, from_undo=False):
        """Assess correct input for hours."""

        if input_text.isdigit() and 0 <= int(input_text) <= 24:
            return input_text
        
    
# CREATE A CLASS FOR OVERRIDING TEXTINPUT
# https://kivy.org/doc/stable/api-kivy.uix.textinput.html#filtering



class TimerApp(App):
    """Main entry point of Kivy App."""

    def build(self):
        return TimerLayout()


if __name__ == '__main__':
    TimerApp().run()          # The run method is a part of the App parent class.