import pytest
from selenium import webdriver
BASE_URL = "https://delassus.com/en/"


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    # driver.get(BASE_URL)
    yield driver
    driver.close()