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
    """Seu código deve vir aqui"""
