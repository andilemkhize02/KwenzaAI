"""
Kwenza AI Legacy
Android Dashboard
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from command_center import AICommandCenter
from chart_view import ChartView
from ai_chat import AIChat
from voice_screen import VoiceScreen


class Dashboard(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 10

        self.command = AICommandCenter()

        self.show_home()

    def show_home(self):

        self.clear_widgets()

        self.add_widget(
            Label(
                text="KWENZA AI LEGACY ONLINE",
                font_size=22
            )
        )

        buttons = [

            ("Live Gold Price", "price"),
            ("Analyse XAUUSD", "analysis"),
            ("Signal XAUUSD", "signal"),
            ("Strategy XAUUSD", "strategy"),
            ("Market Scanner", "scanner"),
            ("News & Session Filter", "news"),
            ("Trading Journal", "journal"),
            ("AI Status", "status")

        ]

        for text, command in buttons:

            btn = Button(
                text=text,
                size_hint=(1, 0.09)
            )

            btn.bind(
                on_press=lambda instance, cmd=command:
                self.run_command(cmd)
            )

            self.add_widget(btn)

        chart = Button(
            text="Market Chart",
            size_hint=(1, 0.09)
        )
        chart.bind(on_press=self.open_chart)
        self.add_widget(chart)

        chat = Button(
            text="AI Assistant",
            size_hint=(1, 0.09)
        )
        chat.bind(on_press=self.open_chat)
        self.add_widget(chat)

        voice = Button(
            text="Voice Assistant",
            size_hint=(1, 0.09)
        )
        voice.bind(on_press=self.open_voice)
        self.add_widget(voice)

    def run_command(self, command):

        result = self.command.execute(command)

        self.show_page(str(result))

    def show_page(self, text):

        self.clear_widgets()

        self.add_widget(
            Label(
                text=text,
                font_size=16
            )
        )

        back = Button(text="Back")

        back.bind(
            on_press=lambda x: self.show_home()
        )

        self.add_widget(back)

    def open_chart(self, instance):

        self.clear_widgets()

        try:

            self.add_widget(
                ChartView(
                    "XAUUSD",
                    back_callback=self.show_home
                )
            )

        except Exception as e:

            self.show_page(f"Chart Error\n\n{e}")

    def open_chat(self, instance):

        self.clear_widgets()

        try:

            self.add_widget(
                AIChat(
                    back_callback=self.show_home
                )
            )

        except Exception as e:

            self.show_page(f"AI Chat Error\n\n{e}")

    def open_voice(self, instance):

        self.clear_widgets()

        try:

            self.add_widget(
                VoiceScreen(
                    back_callback=self.show_home
                )
            )

        except Exception as e:

            self.show_page(f"Voice Error\n\n{e}")