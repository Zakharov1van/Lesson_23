from pages.main_page import MainPage


def test_accept_cookies(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    assert page.check_cookies_block_closed() is True


def test_refuse_cookies(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.refuse_cookies()
    assert page.check_cookies_block_closed() is True


def test_learn_more(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.click_learn_more()
    assert page.current_url() == "https://delassus.com/en/legals"


def test_skip_video(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    assert page.check_intro_video_is_closed() is True


def test_slider_names(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    assert page.check_slider_names() == ['Snacking\ntomatoes', 'Citrus', 'Grapes', 'Avocados', 'Flowers']


def test_ru_button(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    page.click_ru_button()
    assert page.current_url() == "https://delassus.com/ru/"


def test_legals_button(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    page.click_legals()
    assert page.current_url() == "https://delassus.com/en/legals"


def test_replay_video_button(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    page.click_replay_video()
    assert page.current_url() == "https://delassus.com/en/film"


def test_replay_video_is_closed(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    page.click_replay_video()
    page.close_replay()
    assert page.current_url() == "https://delassus.com/en/"


def test_discover_button_tomatoes(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    page.click_slider_tomatoes()
    page.click_discover_button()
    assert page.current_url() == "https://delassus.com/en/products/tomatoes"


def test_discover_button_citrus(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    page.click_slider_citrus()
    page.click_discover_button()
    assert page.current_url() == "https://delassus.com/en/products/citrus"


def test_discover_button_grapes(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    page.click_slider_grapes()
    page.click_discover_button()
    assert page.current_url() == "https://delassus.com/en/products/grapes"


def test_discover_button_avocados(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    page.click_slider_avocados()
    page.click_discover_button()
    assert page.current_url() == "https://delassus.com/en/products/avocados"


def test_discover_button_flowers(browser):
    page = MainPage(browser)
    page.go_to_site()
    page.accept_cookies()
    page.skip_video()
    page.click_slider_flowers()
    page.click_discover_button()
    assert page.current_url() == "https://delassus.com/en/products/flowers"
