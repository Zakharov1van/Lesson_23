from pages.base import BasePage
from pages.locators import Locators
from selenium.common.exceptions import TimeoutException
import time


class DropdownMenu(BasePage):
    def go_to_main_page(self):
        self.find_clickable_element(Locators.ACCEPT_COOKIES).click()
        time.sleep(2)
        self.find_clickable_element(Locators.SKIP_BUTTON).click()
        time.sleep(2)

    def click_dropdown_open(self):
        self.find_clickable_element(Locators.DROPDOWN_MENU_OPEN).click()
        time.sleep(2)

    def click_dropdown_close(self):
        self.find_clickable_element(Locators.DROPDOWN_MENU_CLOSE).click()
        time.sleep(2)

    def check_dropdown_is_open(self):
        try:
            self.find_element(Locators.DROPDOWN_MENU_IS_OPEN)
            return True
        except TimeoutException:
            return False

    def check_names_nav_bar(self):
        item_list = self.find_elements(Locators.DROPDOWN_ITEMS)
        names_list = [item.text for item in item_list]
        return names_list

    def check_links_main_bar(self):
        item_list = self.find_elements(Locators.DROPDOWN_MAIN_ITEMS)
        links_list = [item.get_attribute("href") for item in item_list]
        return links_list

    def check_links_sub_bar(self):
        item_list = self.find_elements(Locators.DROPDOWN_SUB_ITEMS)
        links_list = [item.get_attribute("href") for item in item_list]
        return links_list

    def get_logo_link(self):
        logo = self.find_element(Locators.LOGO)
        return logo.get_attribute("href")
