from pages.other_pages import OtherPage

url = "https://delassus.com/en/products/tomatoes"


def test_logo_link(browser):
    page = OtherPage(browser, url)
    page.go_to_site()
    page.page_is_loaded()
    assert page.get_logo_link() == "https://delassus.com/en/"


def test_link_contact_us(browser):
    page = OtherPage(browser, url)
    page.go_to_site()
    page.page_is_loaded()
    assert page.get_link_contact_us() == "mailto:contact@duroc.ma"


def test_products_block_links(browser):
    page = OtherPage(browser, url)
    page.go_to_site()
    page.page_is_loaded()
    assert page.get_products_block_links() == ['https://delassus.com/en/products/citrus', 'https://delassus.com/en/products/grapes',
                                               'https://delassus.com/en/products/avocados', 'https://delassus.com/en/products/flowers']


def test_h2(browser):
    page = OtherPage(browser, url)
    page.go_to_site()
    page.page_is_loaded()
    assert page.get_h2() == "Products"
