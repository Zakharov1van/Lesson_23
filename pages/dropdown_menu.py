from base import BasePage
from locators import Locators
from selenium.common.exceptions import TimeoutException
import time


class DropdownMenu(BasePage):
    def click_dropdown(self):
        return self.find_clickable_element(Locators.DROPDOWN_MENU_OPEN).click()

    def check_names_nav_bar(self):
        item_list = self.find_elements(Locators.DROPDOWN_ITEMS)
        names_list = [item.text for item in item_list]
        return names_list

    def check_links_nav_bar(self):
        item_list = self.find_elements(Locators.DROPDOWN_ITEMS)
        links_list = [item.get_attribute("href") for item in item_list]
        return links_list

    # def cursor_hover(self):
    #     actions = ActionChains(self.driver)
    #     element = self.find_element()
