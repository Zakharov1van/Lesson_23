from pages.dropdown_menu import DropdownMenu

url = "https://delassus.com/en/"


def test_dropdown_open(browser):
    page = DropdownMenu(browser, url)
    page.go_to_site()
    page.go_to_main_page()
    page.click_dropdown_open()
    assert page.check_dropdown_is_open() is True


def test_dropdown_close(browser):
    page = DropdownMenu(browser, url)
    page.go_to_site()
    page.go_to_main_page()
    page.click_dropdown_open()
    page.click_dropdown_close()
    assert page.check_dropdown_is_open() is False


def test_names_in_dropdown(browser):
    page = DropdownMenu(browser, url)
    page.go_to_site()
    page.go_to_main_page()
    page.click_dropdown_open()
    assert page.check_names_nav_bar() == ['01.\nProducts', '02.\nAbout', '03.\nR&D', '04.\nCSR', 'Snacking\ntomatoes',
                                          'Citrus', 'Grapes', 'Avocados', 'Flowers']


def test_links_in_dropdown_main(browser):
    page = DropdownMenu(browser, url)
    page.go_to_site()
    page.go_to_main_page()
    page.click_dropdown_open()
    assert page.check_links_main_bar() == ['https://delassus.com/en/', 'https://delassus.com/en/about',
                                           'https://delassus.com/en/r-d', 'https://delassus.com/en/csr']


def test_links_in_dropdown_subproducts(browser):
    page = DropdownMenu(browser, url)
    page.go_to_site()
    page.go_to_main_page()
    page.click_dropdown_open()
    assert page.check_links_sub_bar() == ['https://delassus.com/en/products/tomatoes', 'https://delassus.com/en/products/citrus',
                                          'https://delassus.com/en/products/grapes', 'https://delassus.com/en/products/avocados',
                                          'https://delassus.com/en/products/flowers']


def test_logo_link(browser):
    page = DropdownMenu(browser, url)
    page.go_to_site()
    page.go_to_main_page()
    page.click_dropdown_open()
    assert page.get_logo_link() == "https://delassus.com/en/"
