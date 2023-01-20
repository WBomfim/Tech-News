from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    sorted_news = sorted(
        news,
        key=lambda
        item: (item["comments_count"], item["title"]),
        reverse=True
    )
    return [(new["title"], new["url"]) for new in sorted_news[:5]]


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = {}

    for new in news:
        if new["category"] not in categories:
            categories[new["category"]] = 0
        categories[new["category"]] += 1

    sorted_categories = sorted(
        categories.items(),
        key=lambda
        item: (-item[1], item[0])
    )
    return [category[0] for category in sorted_categories[:5]]
