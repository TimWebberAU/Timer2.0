#
#     Author: Tim W
#       Date: 28th Dec 2023
#    Project: Creation of a timer app for fun and utility. I use timers for
#             productivity and haven't enjoyed the web-based or Mac varieties.
#  Component: App Manager + Graphical User Interface (Kivy)
#


from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from timer import TimerDisplay, TimerDisplayInterface
from kivy.core.window import Window


class TimerLayout(MDBoxLayout):
    """Management of the app and layout."""

    # Used only to pass-in engine class objects during instantiation.
    def __init__(self, timer_display_object, **kwargs):
        super(TimerLayout, self).__init__(**kwargs)

        self.timer_display_object = timer_display_object


    # Variables that interact with the .kv style sheet
    hours = ObjectProperty(None)
    minutes = ObjectProperty(None)
    seconds = ObjectProperty(None)
    

    def begin_btn(self):
        print(f"Hours: {int(self.hours.value)}, Minutes: {int(self.minutes.value)}, Seconds: {int(self.seconds.value)}")

        Clock.unschedule(self.timer_display)            # Remove existing schedule
        self.timer_seconds = int(self.seconds.value)    # Create trackable SEC variable
        self.timer_minutes = int(self.minutes.value)    # Create trackable MIN variable
        self.timer_hours = int(self.hours.value)        # Create trackable HR variable

        # Ensure timer only starts if a value exists
        if self.timer_seconds > 0 or self.timer_minutes > 0 or self.timer_hours > 0:
            Clock.schedule_interval(self.timer_display, 1)  # Kivy scheduler, 1 sec interval


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
        return f"{str(self.timer_hours)} : {str(self.timer_minutes)} : {str(self.timer_seconds)}"



class TimerApp(MDApp):
    """Main entry point of Kivy App."""

    def build(self):

        # Instantiate engine objects
        # self.timer_display_object = TimerDisplay()

        Window.minimum_width, Window.minimum_height = 200, 420

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "800"

        return TimerLayout(TimerDisplay())  # Pass-in engine class as well


if __name__ == '__main__':
    TimerApp().run()          # The run method is a part of the App parent class.