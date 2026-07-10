"""
Kwenza AI - Performance Tracker v1.0

Tracks AI decision performance.
"""

from memory import get_memory



class PerformanceTracker:

    def __init__(self):

        self.history = get_memory()



    def total_decisions(self):

        return len(self.history)



    def decision_count(self):

        result = {
            "BUY": 0,
            "SELL": 0,
            "WAIT": 0
        }


        for item in self.history:

            action = item.get("decision", "WAIT")

            if action in result:
                result[action] += 1


        return result



    def confidence_score(self):

        if not self.history:
            return 0


        total = 0

        for item in self.history:
            total += item.get("confidence", 0)


        return round(total / len(self.history), 2)



    def report(self):

        return {

            "total_decisions": self.total_decisions(),

            "decision_history": self.decision_count(),

            "average_confidence": self.confidence_score()

        }



def run_performance():

    tracker = PerformanceTracker()

    return tracker.report()



if __name__ == "__main__":

    print("Kwenza AI Performance Report")

    print(run_performance())