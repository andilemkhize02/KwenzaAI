"""
Kwenza AI - Risk Manager v1.0

Controls trading risk before execution.
"""


class RiskManager:

    def __init__(self, balance=100):
        self.balance = balance
        self.max_risk = 2   # percentage


    def check_trade(self, confidence):

        result = {
            "allowed": False,
            "risk_level": "HIGH",
            "message": ""
        }


        if confidence < 60:
            result["message"] = "Confidence too low. Trade blocked."
            return result


        result["allowed"] = True


        if confidence >= 80:
            result["risk_level"] = "MEDIUM"

        else:
            result["risk_level"] = "LOW"


        result["message"] = "Trade approved by risk manager."

        return result



    def calculate_position(self):

        risk_amount = self.balance * (self.max_risk / 100)

        return {
            "account_balance": self.balance,
            "risk_amount": risk_amount
        }



def run_risk(confidence, balance=100):

    manager = RiskManager(balance)

    approval = manager.check_trade(confidence)

    position = manager.calculate_position()

    return {
        "approval": approval,
        "position": position
    }



if __name__ == "__main__":

    result = run_risk(85, 100)

    print("Kwenza AI Risk Manager")
    print(result)