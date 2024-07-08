from collections import defaultdict

def news_parser():
    news = []
    news_filename = "data/news.txt"
    for line in open(news_filename):
        if line.strip() == "##":
            news.append(defaultdict())
        elif "date" not in news[-1]:
            news[-1]["date"] = line.strip()
            news[-1]["content"] = ""
        else:
            news[-1]["content"] += line
    return news