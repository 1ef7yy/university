from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time




class Parser:
    def __init__(self, link):
        self.link = link
        self.driver = webdriver.Chrome()
        



class WBParser(Parser):
    def get_cards(self):
        self.driver.get(self.link)
        time.sleep(10)
        cards = self.driver.find_elements(By.CLASS_NAME, "product-card__wrapper")
        return cards
    

    def get_card_data(self, card):

        wrapper = card.find_element(By.CLASS_NAME, "product-card__link")
        link = wrapper.get_attribute("href")
        label = wrapper.get_attribute("aria-label")


        lower_price = card.find_element(By.CLASS_NAME, "price__lower-price").text
        prev_price = card.find_element(By.TAG_NAME, "del").text



        data = {
            "link": link,
            "label": label,
            "curr_price": lower_price if lower_price else None,
            "prev_price": prev_price if prev_price else None
        }

        return data
    
    

