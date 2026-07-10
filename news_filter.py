"""
Kwenza AI - News Filter v1.0

Protects the AI from trading during risky news periods.
"""


class NewsFilter:

    def __init__(self):
        self.major_news = [
            "NFP",
            "FOMC",
            "Interest Rate",
            "CPI",
            "GDP"
        ]


    def check_news(self, news_event=None):

        result = {
            "trading_allowed": True,
            "risk": "NORMAL",
            "message": "No major news detected"
        }


        if news_event:

            event = str(news_event).lower()


            for item in self.major_news:

                if item.lower() in event:

                    result["trading_allowed"] = False
                    result["risk"] = "HIGH"
                    result["message"] = (
                        "Trading blocked due to major news: "
                        + item
                    )

                    return result


        return result



def run_news_filter(news_event=None):

    filter_system = NewsFilter()

    return filter_system.check_news(news_event)



if __name__ == "__main__":

    result = run_news_filter("NFP")

    print("Kwenza AI News Filter")

    print(result)