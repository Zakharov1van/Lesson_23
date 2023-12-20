import time

from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Locators:
    ACCEPT_COOKIES = (By.XPATH, "//button[@data-btn = 'yes']")
    REFUSE_COOKIES = (By.XPATH, "//button[@data-btn = 'no']")
    COOKIES_BLOCK = (By.XPATH, "//div[@id = 'Cks']")
    SKIP_BUTTON = (By.XPATH, "//button[@data-btn = 'skip']")
    LEARN_MORE_BUTTON = (By.XPATH, "//a[@rel = 'noopener']")
    SOUND_BUTTON = (By.XPATH, "//button[@class = 'o-B o-BCircle js-show']")
    INTRO_IS_OVER = (By.XPATH, "//div[@class = 'c-Intro u-fixed u-post-tl u-fit u-hidden']")
    DROPDOWN_MENU_OPEN = (By.XPATH, "//button[@class = 'o-B o-BBurger']")
    DROPDOWN_MENU_IS_OPEN = (By.XPATH, "//div[@style = 'visibility: visible;']")
    DROPDOWN_MENU_CLOSE = (By.XPATH, "//button[@class = 'o-B o-BClose']")
    DROPDOWN_ITEMS = (By.XPATH, "//li[@class = 'js-it']")
    DROPDOWN_MAIN_ITEMS = (By.XPATH, "//a[contains(@class, 'o-B o-BS o-BS-invert js-btn')]")
    DROPDOWN_SUB_ITEMS = (By.XPATH, "//a[contains(@class, 'o-B o-BS o-BSubProduct o-BS-invert js-btn')]")
    SLIDER_ITEMS = (By.XPATH, "//span[@class = 'o-P1 -L js-l']")
    SLIDER_TOMATOES = (By.XPATH, "//button[@data-id = 'tomatoes']")
    SLIDER_CITRUS = (By.XPATH, "//button[@data-id = 'citrus']")
    SLIDER_GRAPES = (By.XPATH, "//button[@data-id = 'grapes']")
    SLIDER_AVOCADOS = (By.XPATH, "//button[@data-id = 'avocados']")
    SLIDER_FLOWERS = (By.XPATH, "//button[@data-id = 'flowers']")
    LEGALS_BUTTON = (By.XPATH, "//a[@data-btn = 'legals']")
    RU_BUTTON = (By.XPATH, "//a[@data-lang = 'ru']")
    REPLAY_VIDEO = (By.XPATH, "//a[@data-btn = 'replay']")
    VIDEO_IS_PLAYING = (By.XPATH, "//div[@class= 'c-Player is-playing']")
    CLOSE_REPLAY = (By.XPATH, "//a[@class= 'o-B o-BClose']")
    DISCOVER_BUTTON = (By.XPATH, "//a[@data-btn = 'discover']")
    PAGE_H3 = (By.XPATH, "//h3")
    PAGE_H2 = (By.XPATH, "//h2")
    PAGE_PRODUCT_BLOCK = (By.XPATH, "//a[@data-id = 'card']")
    ANY_QUESTIONS_BLOCK = (By.XPATH, "//div[@class = 'l-S l-S--l ']")
    SECOND_BLOCK = (By.XPATH, "//div[@class = 'l-IC']")
    CONTACT_US_BUTTON = (By.XPATH, "//a[@data-btn = 'contact']")
    LOGO = (By.XPATH, "//a[@class = 'o-B']")


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


class MainPage(BasePage):
    def accept_cookies(self):
        return self.find_clickable_element(Locators.ACCEPT_COOKIES).click()

    def refuse_cookies(self):
        return self.find_clickable_element(Locators.REFUSE_COOKIES).click()

    def check_cookies_block_closed(self):
        try:
            self.find_element(Locators.COOKIES_BLOCK)
            return False
        except TimeoutException:
            return True

    def click_learn_more(self):
        return self.find_clickable_element(Locators.LEARN_MORE_BUTTON).click()

    def skip_video(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.SKIP_BUTTON).click()

    def turn_sound(self):
        return self.find_clickable_element(Locators.SOUND_BUTTON).click()

    def check_intro_video_is_closed(self):
        try:
            self.find_element(Locators.INTRO_IS_OVER)
            return True
        except TimeoutException:
            return False

    def check_slider_names(self):
        time.sleep(2)
        slider_items = self.find_elements(Locators.SLIDER_ITEMS)
        slider_names = [item.text for item in slider_items]
        return slider_names

    def click_slider_tomatoes(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.SLIDER_TOMATOES).click()

    def click_slider_citrus(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.SLIDER_CITRUS).click()

    def click_slider_grapes(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.SLIDER_GRAPES).click()

    def click_slider_avocados(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.SLIDER_AVOCADOS).click()

    def click_slider_flowers(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.SLIDER_FLOWERS).click()

    def click_legals(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.LEGALS_BUTTON).click()

    def click_ru_button(self):
        return self.find_clickable_element(Locators.RU_BUTTON).click()

    def click_replay_video(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.REPLAY_VIDEO).click()

    def close_replay(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.CLOSE_REPLAY).click()

    def check_video_is_closed(self):
        try:
            self.find_element(Locators.VIDEO_IS_PLAYING)
            return False
        except TimeoutException:
            return True

    def click_discover_button(self):
        time.sleep(2)
        return self.find_clickable_element(Locators.DISCOVER_BUTTON).click()

    def wait_till_page_is_loaded(self):
        return self.find_clickable_element(Locators.DISCOVER_BUTTON)

class OtherPage(BasePage):
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
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_link_contact_us(self):
        contact_us = self.find_element(Locators.CONTACT_US_BUTTON)
        return contact_us.get_attribute("href")

    def get_logo_link(self):
        logo = self.find_element(Locators.LOGO)
        return logo.get_attribute("href")
