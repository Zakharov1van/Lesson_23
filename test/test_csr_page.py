from pages.other_pages import OtherPage

url = "https://delassus.com/en/csr"


def test_logo_link(browser):
    page = OtherPage(browser, url)
    page.go_to_site()
    page.page_is_loaded()
    assert page.get_logo_link() == "https://delassus.com/en/"


def test_link_contact_us(browser):
    page = OtherPage(browser, url)
    page.go_to_site()
    page.page_is_loaded()
    assert page.get_link_contact_us() == "mailto:contact@delassus.com"


def test_products_block_links(browser):
    page = OtherPage(browser, url)
    page.go_to_site()
    page.page_is_loaded()
    assert page.get_products_block_links() == ['https://delassus.com/en/', 'https://delassus.com/en/about',
                                               'https://delassus.com/en/r-d']


def test_h2(browser):
    page = OtherPage(browser, url)
    page.go_to_site()
    page.page_is_loaded()
    assert page.get_h2() == "Corporate Social Responsibility"
