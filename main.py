"""
Kwenza AI - Main Controller v1.9

Flow:
Scanner → News → Analysis → Strategy → Risk → Memory → Learning → Performance → Backtest → Dashboard
"""

from scanner import run_scanner
import analysis
from strategy import run_strategy
from risk import run_risk
from news_filter import run_news_filter
from memory import save_memory
from learning import run_learning
from performance import run_performance
from backtest import run_backtest

from dashboard import show_dashboard



def get_analysis():

    if hasattr(analysis, "run_analysis"):
        return analysis.run_analysis()

    elif hasattr(analysis, "analyze"):
        return analysis.analyze()

    elif hasattr(analysis, "analysis"):
        return analysis.analysis()

    else:
        return {
            "trend": "unknown",
            "signal": "wait",
            "strength": 0
        }



def run_ai():

    print("=" * 40)
    print("Kwenza AI System Starting")
    print("=" * 40)


    print("\n[1] Scanning Markets...")

    markets = run_scanner()

    for market in markets:
        print("-", market["symbol"])



    print("\n[2] Checking News Risk...")

    news = run_news_filter()

    print(news)


    if not news["trading_allowed"]:
        print("Trading blocked.")
        return



    print("\n[3] Running Analysis...")

    analysis_result = get_analysis()

    print(analysis_result)



    print("\n[4] Strategy Decision...")

    decision = run_strategy(analysis_result)

    print(decision)



    print("\n[5] Risk Check...")

    risk = run_risk(
        decision["confidence"],
        balance=100
    )

    print(risk)



    print("\n[6] Saving Memory...")

    save_memory({

        "symbol": markets[0]["symbol"],
        "decision": decision["action"],
        "confidence": decision["confidence"],
        "risk": risk["approval"]["risk_level"]

    })


    print("\n[7] Dashboard")

    show_dashboard()



    print("\nKwenza AI Cycle Complete")



if __name__ == "__main__":
    run_ai()