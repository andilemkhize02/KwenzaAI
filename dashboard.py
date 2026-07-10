"""
Kwenza AI - Dashboard v1.0

Displays AI system information.
"""


from learning import run_learning
from performance import run_performance
from backtest import run_backtest



def show_dashboard():

    print("=" * 50)
    print("        KWENZA AI DASHBOARD")
    print("=" * 50)


    print("\n🧠 Learning Statistics")

    learning = run_learning()

    print(learning)



    print("\n📊 Performance")

    performance = run_performance()

    print(performance)



    print("\n📈 Backtest Results")

    backtest = run_backtest()

    print(backtest)



    print("\nSYSTEM STATUS: ONLINE")

    print("=" * 50)




if __name__ == "__main__":

    show_dashboard()