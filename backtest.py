"""
Kwenza AI - Backtesting Engine v1.0

Tests strategy performance on sample historical data.
"""


class BacktestEngine:

    def __init__(self):

        self.results = {
            "wins": 0,
            "losses": 0,
            "total": 0
        }


    def run(self, trades):

        for trade in trades:

            self.results["total"] += 1


            if trade["result"] == "WIN":

                self.results["wins"] += 1


            elif trade["result"] == "LOSS":

                self.results["losses"] += 1



        return self.report()



    def report(self):

        total = self.results["total"]


        if total == 0:

            accuracy = 0

        else:

            accuracy = round(
                (self.results["wins"] / total) * 100,
                2
            )


        return {

            "total_trades": total,
            "wins": self.results["wins"],
            "losses": self.results["losses"],
            "accuracy": accuracy

        }



def run_backtest():

    engine = BacktestEngine()


    sample_history = [

        {
            "symbol": "EURUSD",
            "decision": "BUY",
            "result": "WIN"
        },

        {
            "symbol": "XAUUSD",
            "decision": "SELL",
            "result": "LOSS"
        },

        {
            "symbol": "BTCUSD",
            "decision": "BUY",
            "result": "WIN"
        }

    ]


    return engine.run(sample_history)



if __name__ == "__main__":

    print("Kwenza AI Backtest Report")

    print(run_backtest())