"""
Kwenza AI Legacy
AI Chat Screen v1.0
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from command_center import AICommandCenter


class AIChat(BoxLayout):

    def __init__(self, back_callback=None, **kwargs):

        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        self.back_callback = back_callback

        self.ai = AICommandCenter()

        self.history = []

        self.build_ui()

    def build_ui(self):

        title = Label(
            text="KWENZA AI LEGACY",
            font_size=22,
            size_hint=(1, 0.1)
        )

        self.add_widget(title)

        self.chat = Label(
            text="🤖 Hello Andile.\nAsk me anything.",
            halign="left",
            valign="top",
            size_hint_y=None
        )

        self.chat.bind(texture_size=self.resize_chat)

        scroll = ScrollView(size_hint=(1, 0.6))

        scroll.add_widget(self.chat)

        self.add_widget(scroll)

        self.input = TextInput(
            multiline=False,
            hint_text="Type a message...",
            size_hint=(1, 0.1)
        )

        self.input.bind(on_text_validate=self.send)

        self.add_widget(self.input)

        send = Button(
            text="Send",
            size_hint=(1, 0.1)
        )

        send.bind(on_press=self.send)

        self.add_widget(send)

        back = Button(
            text="Back",
            size_hint=(1, 0.1)
        )

        back.bind(on_press=self.go_back)

        self.add_widget(back)

    def resize_chat(self, instance, value):

        instance.text_size = (self.width - 20, None)
        instance.height = value[1]

    def send(self, instance):

        message = self.input.text.strip()

        if message == "":
            return

        self.history.append("👤 You: " + message)

        reply = self.ai.execute(message)

        self.history.append("🤖 AI: " + str(reply))

        self.chat.text = "\n\n".join(self.history)

        self.input.text = ""

    def go_back(self, instance):

        if self.back_callback:

            self.back_callback()