import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


text_menu = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.\n"""


options_exec = {
    '0': lambda: get_tech_news(
        int(input("Digite quantas notícias serão buscadas:\n"))
    ),
    '1': lambda: search_by_title(input("Digite o título:\n")),
    '2': lambda: search_by_date(
        input("Digite a data no formato aaaa-mm-dd:\n")
    ),
    '3': lambda: search_by_tag(input("Digite a tag:\n")),
    '4': lambda: search_by_category(input("Digite a categoria:\n")),
    '5': lambda: top_5_news(),
    '6': lambda: top_5_categories(),
    '7': lambda: sys.stdout.write("Encerrando script\n"),
}


# Requisito 12
def analyzer_menu():
    option = input(text_menu)
    try:
        return options_exec[option]()

    except KeyError:
        return sys.stderr.write("Opção inválida\n")
