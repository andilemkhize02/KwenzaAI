"""
Kwenza AI Legacy
Voice Assistant v1.0
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class VoiceScreen(BoxLayout):

    def __init__(self, back_callback=None, **kwargs):

        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 10

        self.back_callback = back_callback

        self.status = Label(
            text="Voice Assistant Ready\n\nStatus : Idle",
            font_size=20
        )

        self.add_widget(self.status)

        start = Button(
            text="Start Listening",
            size_hint=(1, 0.12)
        )

        start.bind(on_press=self.start_voice)

        self.add_widget(start)

        stop = Button(
            text="Stop Listening",
            size_hint=(1, 0.12)
        )

        stop.bind(on_press=self.stop_voice)

        self.add_widget(stop)

        back = Button(
            text="Back",
            size_hint=(1, 0.12)
        )

        back.bind(on_press=self.go_back)

        self.add_widget(back)

    def start_voice(self, instance):

        self.status.text = (
            "Voice Assistant\n\n"
            "Status : Listening...\n\n"
            "Speech recognition will be added in v2.0"
        )

    def stop_voice(self, instance):

        self.status.text = (
            "Voice Assistant\n\n"
            "Status : Stopped"
        )

    def go_back(self, instance):

        if self.back_callback:

            self.back_callback()