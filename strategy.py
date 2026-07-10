"""
Kwenza AI - Strategy Engine v1.0

Receives analysis results and creates a trade decision.
"""

class StrategyEngine:

    def __init__(self):
        self.name = "Kwenza AI Strategy Engine"

    def evaluate(self, analysis):
        """
        Convert AI analysis into a trading plan.
        """

        decision = {
            "action": "WAIT",
            "confidence": 0,
            "reason": "",
            "risk": "LOW"
        }

        if analysis is None:
            decision["reason"] = "No analysis received"
            return decision


        trend = str(analysis.get("trend", "")).lower()
        signal = str(analysis.get("signal", "")).lower()
        strength = analysis.get("strength", 0)


        # BUY CONDITIONS
        if (
            "bull" in trend
            or "buy" in signal
        ):
            decision["action"] = "BUY"
            decision["confidence"] = 70
            decision["reason"] = "Bullish market structure detected"


        # SELL CONDITIONS
        elif (
            "bear" in trend
            or "sell" in signal
        ):
            decision["action"] = "SELL"
            decision["confidence"] = 70
            decision["reason"] = "Bearish market structure detected"


        # WAIT CONDITION
        else:
            decision["action"] = "WAIT"
            decision["confidence"] = 40
            decision["reason"] = "No strong setup"


        # Confidence adjustment
        if isinstance(strength, (int, float)):
            decision["confidence"] += strength


        # Risk calculation
        if decision["confidence"] >= 80:
            decision["risk"] = "MEDIUM"

        if decision["confidence"] >= 90:
            decision["risk"] = "HIGH"


        return decision



def run_strategy(analysis):
    engine = StrategyEngine()
    return engine.evaluate(analysis)



if __name__ == "__main__":

    test_analysis = {
        "trend": "bullish",
        "signal": "buy",
        "strength": 15
    }


    result = run_strategy(test_analysis)

    print("Kwenza AI Strategy Result")
    print(result)