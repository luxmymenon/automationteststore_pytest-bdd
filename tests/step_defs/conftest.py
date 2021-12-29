import pytest
from pytest_bdd import given, parsers
from selenium import webdriver
# from utilities.config import Config


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome:  ")
    parser.addoption("--env", action="store", help="Environment to test against eg: dev or qa")


@pytest.fixture(scope="class")
def browser_init():
    chrome_path = "C:/Users/luxmy/Automation/chromedriver_win32/chromedriver.exe"
    web_driver = webdriver.Chrome(chrome_path)
    web_driver.maximize_window()
    yield web_driver

    # browser = request.config.getoption("--browser")
    # if browser == "chrome":
    #     chrome_path = "C:/Users/luxmy/Automation/chromedriver_win32/chromedriver.exe"
    #     web_driver = webdriver.Chrome(chrome_path)
    # elif browser == "edge":
    #     edge_path = "C:/Users/luxmy/Automation/edgedriver_win32/msedgedriver.exe"
    #     web_driver = webdriver.Edge(edge_path)
    # request.cls.driver = web_driver
    # return request.cls.driver
    #yield web_driver
    # web_driver.close()


# def access_url(self):
#     self.driver.get(self.url)

@given(parsers.parse('I have navigated to the "{page_url}" page'))
def access_url(browser_init, page_url):
    browser_init.get("https://" + page_url)


