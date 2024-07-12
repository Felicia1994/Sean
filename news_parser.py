from collections import defaultdict

dict_month = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}

def format_date(date_raw):
    # date: yyyy-mm
    l = date_raw.split('-')
    return dict_month[int(l[1])] + ", " + l[0]

def news_parser():
    news = []
    news_filename = "data/news.txt"
    for line in open(news_filename):
        if line.strip() == "##":
            news.append(defaultdict())
            news[-1]["date_raw"] = ""
            news[-1]["date"] = ""
            news[-1]["content"] = ""
        elif line.startswith("date: "):
            news[-1]["date_raw"] = line.strip()[6:]
            news[-1]["date"] = format_date(news[-1]["date_raw"])
        else:
            news[-1]["content"] += line
    return news