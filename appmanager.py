#
#     Author: Tim W
#       Date: 28th Dec 2023
#    Project: Creation of a timer app for fun and utility. I use timers for
#             productivity and haven't enjoyed the web-based or Mac varieties.
#  Component: App Manager + Graphical User Interface (Kivy)
#


from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader


class TimerLayout(MDBoxLayout):
    """Management of the app and layout."""

    # Variables that interact with the .kv style sheet
    hours = ObjectProperty(None)
    minutes = ObjectProperty(None)
    seconds = ObjectProperty(None)


    def begin_btn(self):
        """Enables timer related events to begin by recording the input and scheduling the timer."""

        Clock.unschedule(self.timer_logic)              # Remove existing schedule
        self.timer_seconds = int(self.seconds.value)    # Create trackable SEC variable
        self.timer_minutes = int(self.minutes.value)    # Create trackable MIN variable
        self.timer_hours = int(self.hours.value)        # Create trackable HR variable

        # Reset text on buttons
        self.ids.begin.text = "Reset"
        self.ids.pause.text = "Pause"

        # Enable pause and stop buttons
        self.ids.pause.disabled = False
        self.ids.stop.disabled = False

        # Ensure timer only starts if a value exists
        if self.timer_seconds > 0 or self.timer_minutes > 0 or self.timer_hours > 0:
            Clock.schedule_interval(self.timer_logic, 1)  # Kivy scheduler, 1 sec interval


    def timer_logic(self, dt_time_elapsed):
        """Allows the timer to operate accurately."""

        self.ids.timer.text = self.timer_format()         # Update GUI timer

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
            Clock.unschedule(self.timer_logic)
            self.play_alarm()

            self.ids.begin.text = "Begin"

            self.ids.pause.disabled = True
            self.ids.stop.disabled = True
        
        self.timer_seconds -= 1
    

    def timer_format(self):
        """Called to change the display of the timer on the go. It edits the .kv file text."""

        return f"{str(self.timer_hours)} : {str(self.timer_minutes)} : {str(self.timer_seconds)}"
    

    def pause_btn(self):
        """Enables pausing and playing of the timer once it's already running."""

        if self.timer_seconds > 0 or self.timer_minutes > 0 or self.timer_hours > 0:
            if self.ids.pause.text == "Pause":
                Clock.unschedule(self.timer_logic)
                self.ids.pause.text = "Play"
            else:
                Clock.schedule_interval(self.timer_logic, 1)
                self.ids.pause.text = "Pause"
    

    def stop_btn(self):
        """Stops the running timer under any circumstance."""

        if self.timer_seconds > 0 or self.timer_minutes > 0 or self.timer_hours > 0:
            Clock.unschedule(self.timer_logic)
            self.ids.timer.text = "0 : 0 : 0"

            # Reset variables for next timer activation
            self.timer_hours = 0
            self.timer_minutes = 0
            self.timer_seconds = 0

            # Reset button text values
            self.ids.begin.text = "Begin"
            self.ids.pause.text = "Pause"

            # Disable buttons while no timer activated
            self.ids.pause.disabled = True
            self.ids.stop.disabled = True


    def play_alarm(self):
        """Plays the end of timer sound."""

        alarm = SoundLoader.load("Sounds/pipe_sound.wav")
        alarm.play()


class TimerApp(MDApp):
    """Main entry point of Kivy App."""

    def build(self):
        """Required method in Kivy Apps."""

        Window.minimum_width, Window.minimum_height = 250, 440

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "400"

        return TimerLayout()


if __name__ == '__main__':
    TimerApp().run()          # The run method is a part of the App parent class.