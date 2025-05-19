from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

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
    def get_cards(self, pages_count):
        data = []
        for page in range(pages_count):
            page_link = f"{self.link}&page={page+1}"
            self.driver.get(page_link)
            super().scroll(3, 1)
            cards = self.driver.find_elements(By.CLASS_NAME, "product-card__wrapper")
            for card in cards:
                card_data = self.get_card_data(card)
                card_data["Описание"] = self.get_card_desc(card_link=card_data["Ссылка"])
                data.append(card_data)
                print(card_data)
        return data
    

    def get_card_desc(self, card_link):
        self.driver.execute_script(f'''window.open("{card_link}","_blank");''')
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.scroll(1, 1)
        
        desc_btn = self.driver.find_element(By.CSS_SELECTOR, "button.product-page__btn-detail.j-wba-card-item.j-wba-card-item-show.j-wba-card-item-observe")
        desc_btn.click()
        time.sleep(1)

        desc = self.driver.find_element(By.CLASS_NAME, "option__text").text

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)

        return desc

    def get_card_data(self, card):

        wrapper = card.find_element(By.CLASS_NAME, "product-card__link")
        
        
        
        link = wrapper.get_attribute("href")
        label = wrapper.get_attribute("aria-label")

        img_link = card.find_element(By.TAG_NAME, "img").get_attribute("src")
        
        brand = card.find_element(By.CLASS_NAME, "product-card__brand").text
        try:
            lower_price = card.find_element(By.CLASS_NAME, "price__lower-price").text.replace(" ", "")
            normal_price = card.find_element(By.TAG_NAME, "del").text.replace(" ", "")
        except NoSuchElementException:
            normal_price = card.find_element(By.CLASS_NAME, "price__lower-price").text.replace(" ", "")
            lower_price = None

        rating = card.find_element(By.CLASS_NAME, "address-rate-mini").text


        data = {
            "Ссылка": link,
            "Название": label,
            "Изображение": img_link,
            "Производитель": brand,
            "Цена со скидкой": lower_price if lower_price else normal_price,
            "Цена без скидки": normal_price,
            "Рейтинг": rating
        }   

        return data
