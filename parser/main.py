from parser import WBParser
from openpyxl import Workbook


def get_cards_data():
    pen_parser = WBParser("https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%80%D1%83%D1%87%D0%BA%D0%B8%20%D0%B3%D0%B5%D0%BB%D0%B5%D0%B2%D1%8B%D0%B5")

    cards = pen_parser.get_cards(pages_count=5)

    return cards


def write_to_excel(items):
    wb = Workbook()
    ws = wb.active
    ws.append(list(items[0].keys()))
    for item in items:
        ws.append(list(item.values()))

    wb.save("parser/wildberries.xlsx")


if __name__ == "__main__":
    items = get_cards_data()
    write_to_excel(items)
    print("Данные сохранены в wildberries.xlsx!")