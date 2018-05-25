from selenium.webdriver.remote.webelement import WebElement

from golem import actions
from golem.webdriver.extended_webelement import ExtendedWebElement


description = 'Verify that the webdriver.find method returns a ExtendedWebElement when a WebElement or ExtendedWebElement is passed as argument'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    click_me_button = browser.find_element_by_id('button-one')
    assert type(click_me_button) == WebElement
    actions.step('Find element given a WebElement')
    result_click_me_button = browser.find(click_me_button)
    assert type(result_click_me_button) == ExtendedWebElement
    actions.step('Find element given a ExtendedWebElement')
    result_click_me_button = browser.find(click_me_button)
    assert type(result_click_me_button) == ExtendedWebElement
