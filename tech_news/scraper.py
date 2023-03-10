import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        return response.text if response.status_code == 200 else None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css(".archive-main h2 a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    nextButton = selector.css(".nav-links .next::attr(href)").get()
    return nextButton if nextButton else None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    num_comments = selector.css(".post-comments .title-block::text").re(r"\d+")
    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),

        "title": selector.css(".entry-title::text").get().rstrip(" \xa0"),

        "timestamp": selector.css(".meta-date::text").get(),

        "writer": selector.css(".author a::text").get(),

        "comments_count": int(num_comments[0]) if num_comments else 0,

        "summary": selector.css(
            ".entry-content p").xpath("string()").get().rstrip(" \xa0"),

        "tags": selector.css(".post-tags a *::text").getall(),

        "category": selector.css(".meta-category .label::text").get()
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    news = []

    while len(news) < amount:
        html_content = fetch(url)
        links = scrape_updates(html_content)

        for link in links:
            if len(news) < amount:
                news.append(scrape_news(fetch(link)))

        url = scrape_next_page_link(html_content)
        if not url:
            break

    create_news(news)
    return news
