# https://github.com/1ef7yy/university/tree/main/parser

from parsing import WBParser
from excel import write_to_excel


if __name__ == "__main__":
    pen_parser = WBParser("https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%80%D1%83%D1%87%D0%BA%D0%B8%20%D0%B3%D0%B5%D0%BB%D0%B5%D0%B2%D1%8B%D0%B5")

    pens = pen_parser.get_cards(pages_count=5)
    write_to_excel(pens)
    print("Данные сохранены в wildberries.xlsx!")
    