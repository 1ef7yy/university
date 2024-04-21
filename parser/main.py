from parser import WBParser


wb_parser = WBParser("https://www.wildberries.ru/")

cards = wb_parser.get_cards()


print(wb_parser.get_card_data(cards[0]))