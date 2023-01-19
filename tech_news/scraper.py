import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        if response.status_code == 200:
            return response.text

    except requests.Timeout:
        return None
    else:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css(".archive-main h2 a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    nextButton = selector.css(".nav-links .next::attr(href)").get()
    if not nextButton:
        return None
    return nextButton


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
