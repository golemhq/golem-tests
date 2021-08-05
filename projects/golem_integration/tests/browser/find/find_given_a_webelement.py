from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.webelement import FirefoxWebElement
from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find method returns a ExtendedWebElement when a WebElement or ExtendedWebElement is passed as argument'


def test(data):
    valid_element_classes = [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selenium_element = browser.find_element_by_id('button-one')
    assert type(selenium_element) in [WebElement, FirefoxWebElement]
    # pass a selenium webelement to find
    # element is converted to ExtendedRemoteWebElement or ExtendedFirefoxWebElement
    golem_element = browser.find(selenium_element)
    assert type(golem_element) in valid_element_classes
    # pass a golem webelement to find
    # the same element is returned
    golem_element = browser.find(golem_element)
    assert type(golem_element) in valid_element_classes
