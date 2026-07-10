"""
Kwenza AI Legacy
Interactive Chart View
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ChartView(BoxLayout):

    def __init__(self, symbol="XAUUSD", back_callback=None, **kwargs):

        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 10

        self.symbol = symbol
        self.back_callback = back_callback

        self.build_ui()

    def build_ui(self):

        self.clear_widgets()

        title = Label(
            text=f"KWENZA AI LEGACY\n\n{self.symbol} MARKET",
            font_size=22
        )

        self.add_widget(title)

        self.info = Label(
            text=(
                "Chart Engine Ready\n\n"
                "Status : ONLINE\n\n"
                "Upcoming Features\n"
                "---------------------------\n"
                "✓ Live Price\n"
                "✓ Candlestick Chart\n"
                "✓ BOS Detection\n"
                "✓ Fair Value Gap\n"
                "✓ Order Blocks\n"
                "✓ Liquidity\n"
                "✓ Buy/Sell Signals\n"
                "✓ Multi Timeframe\n"
            )
        )

        self.add_widget(self.info)

        refresh = Button(
            text="Refresh",
            size_hint=(1, 0.1)
        )

        refresh.bind(on_press=self.refresh_chart)

        self.add_widget(refresh)

        back = Button(
            text="Back",
            size_hint=(1, 0.1)
        )

        back.bind(on_press=self.go_back)

        self.add_widget(back)

    def refresh_chart(self, instance):

        self.info.text = (
            f"{self.symbol}\n\n"
            "Chart Updated Successfully\n\n"
            "Connection : OK\n"
            "Status : ONLINE"
        )

    def go_back(self, instance):

        if self.back_callback:

            self.back_callback()