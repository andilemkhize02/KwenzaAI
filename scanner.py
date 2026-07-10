"""
Kwenza AI - Market Scanner v1.0

Scans multiple trading instruments and prepares them
for analysis and strategy decisions.
"""


class MarketScanner:

    def __init__(self):
        self.name = "Kwenza AI Scanner"

        self.watchlist = [
            "EURUSD",
            "GBPUSD",
            "XAUUSD",
            "NAS100",
            "BTCUSD"
        ]


    def get_markets(self):
        """
        Return available markets.
        """

        return self.watchlist



    def scan(self):
        """
        Basic scanner output.
        Later this connects to live price feeds.
        """

        results = []

        for market in self.watchlist:

            results.append({
                "symbol": market,
                "status": "READY",
                "message": "Waiting for analysis"
            })

        return results



def run_scanner():

    scanner = MarketScanner()

    return scanner.scan()



if __name__ == "__main__":

    markets = run_scanner()

    print("Kwenza AI Market Scanner")
    
    for item in markets:
        print(item)