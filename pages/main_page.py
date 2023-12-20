from base import BasePage
from locators import Locators
from selenium.common.exceptions import TimeoutException
import time


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
