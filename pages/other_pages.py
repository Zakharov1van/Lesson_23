from pages.base import BasePage
from pages.locators import Locators
from selenium.common.exceptions import TimeoutException
import time


class OtherPage(BasePage):
    def page_is_loaded(self):
        time.sleep(2)

    def get_h3(self):
        item_list = self.find_elements(Locators.PAGE_H3)
        headers_list = [item.text for item in item_list]
        return headers_list

    def get_h2(self):
        return self.find_element(Locators.PAGE_H2).text

    def get_products_block_links(self):
        item_list = self.find_elements(Locators.PAGE_PRODUCT_BLOCK)
        product_links = [item.get_attribute("href") for item in item_list]
        return product_links

    def scroll_to_contact_us(self):
        element = self.find_element(Locators.ANY_QUESTIONS_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

    def scroll_to_second_block(self):
        element = self.find_element(Locators.SECOND_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_page_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_link_contact_us(self):
        contact_us = self.find_element(Locators.CONTACT_US_BUTTON)
        return contact_us.get_attribute("href")

    def get_logo_link(self):
        logo = self.find_element(Locators.LOGO)
        return logo.get_attribute("href")
