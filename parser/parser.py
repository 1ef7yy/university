from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time




class Parser:
    def __init__(self, link):
        self.link = link
        self.driver = webdriver.Chrome()

    def scroll(self, count, delay):
        for _ in range(count):
            self.driver.execute_script("""
        window.scrollTo(0, document.body.scrollHeight);
                                       """)
            time.sleep(delay)
        



class WBParser(Parser):
    def get_cards(self):
        self.driver.get(self.link)
        super().scroll(10, 1)
        cards = self.driver.find_elements(By.CLASS_NAME, "product-card__wrapper")
        return cards
    

    


    def get_card_data(self, card):

        wrapper = card.find_element(By.CLASS_NAME, "product-card__link")
        
        
        
        link = wrapper.get_attribute("href")
        label = wrapper.get_attribute("aria-label")

        img_link = card.find_element(By.TAG_NAME, "img").get_attribute("src")
        
        brand = card.find_element(By.CLASS_NAME, "product-card__brand").text

        lower_price = card.find_element(By.CLASS_NAME, "price__lower-price").text
        prev_price = card.find_element(By.TAG_NAME, "del").text

        rating = card.find_element(By.CLASS_NAME, "address-rate-mini").text

        data = {
            "link": link,
            "label": label,
            "img": img_link,
            "brand": brand,
            "curr_price": lower_price if lower_price else None,
            "prev_price": prev_price if prev_price else None,
            "rating": rating
        }   

        return data
    
    

