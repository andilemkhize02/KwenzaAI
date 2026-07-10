"""
Kwenza AI - Learning System v1.0

Learns from stored AI memory.
"""

from memory import get_memory



class AILearning:

    def __init__(self):

        self.history = get_memory()



    def total_records(self):

        return len(self.history)



    def decisions_summary(self):

        summary = {
            "BUY": 0,
            "SELL": 0,
            "WAIT": 0
        }


        for item in self.history:

            decision = item.get("decision", "WAIT")

            if decision in summary:
                summary[decision] += 1


        return summary



    def confidence_average(self):

        if not self.history:
            return 0


        total = 0


        for item in self.history:

            total += item.get("confidence", 0)


        return round(total / len(self.history), 2)



def run_learning():

    ai = AILearning()


    return {

        "total_trades": ai.total_records(),

        "decisions": ai.decisions_summary(),

        "average_confidence": ai.confidence_average()

    }



if __name__ == "__main__":


    result = run_learning()


    print("Kwenza AI Learning")

    print(result)