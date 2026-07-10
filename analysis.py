"""
====================================================
KWENZA AI LEGACY
MARKET ANALYSIS ENGINE V1.0
====================================================
"""

from datetime import datetime
import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


MARKETS = {
    "XAUUSD": "GC=F",
    "GOLD": "GC=F",
    "SILVER": "SI=F",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "USDJPY": "JPY=X",
    "BTC": "BTC-USD",
    "BTCUSD": "BTC-USD",
    "ETH": "ETH-USD",
    "ETHUSD": "ETH-USD",
    "NAS100": "^NDX",
    "SP500": "^GSPC",
    "US30": "^DJI",
    "DXY": "DX-Y.NYB"
}


def analyse_market(symbol):

    symbol = symbol.upper().strip()

    if symbol not in MARKETS:
        return f"Market '{symbol}' is not supported."

    ticker = MARKETS[symbol]

    try:

        url = (
            f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        )

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        meta = data["chart"]["result"][0]["meta"]

        current = meta.get("regularMarketPrice", 0)
        previous = meta.get("previousClose", 0)
        currency = meta.get("currency", "")
        exchange = meta.get("exchangeName", "Unknown")

        if current > previous:
            trend = "BULLISH"
            bias = "BUY"
            confidence = 75
        elif current < previous:
            trend = "BEARISH"
            bias = "SELL"
            confidence = 75
        else:
            trend = "NEUTRAL"
            bias = "WAIT"
            confidence = 50

        if previous != 0:
            change = current - previous
            percent = (change / previous) * 100
        else:
            change = 0
            percent = 0

        report = []

        report.append("========== KWENZA AI ANALYSIS ==========")
        report.append("")
        report.append(f"Market : {symbol}")
        report.append(f"Current Price : {current} {currency}")
        report.append(f"Previous Close : {previous}")
        report.append(f"Change : {change:.2f}")
        report.append(f"Percent : {percent:.2f}%")
        report.append("")
        report.append(f"Trend : {trend}")
        report.append(f"Bias : {bias}")
        report.append(f"Confidence : {confidence}%")
        report.append("")

        if bias == "BUY":
            report.append("Recommendation : Look for buying opportunities.")
        elif bias == "SELL":
            report.append("Recommendation : Look for selling opportunities.")
        else:
            report.append("Recommendation : Wait for confirmation.")

        report.append("")
        report.append(f"Exchange : {exchange}")
        report.append("Status : LIVE")
        report.append(
            "Updated : " +
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        report.append("")
        report.append("========================================")

        return "\n".join(report)

    except requests.exceptions.Timeout:
        return "Connection timed out."

    except requests.exceptions.ConnectionError:
        return "Unable to connect to Yahoo Finance."

    except Exception as e:
        return f"Analysis failed.\n\n{e}"


if __name__ == "__main__":

    print(analyse_market("XAUUSD"))