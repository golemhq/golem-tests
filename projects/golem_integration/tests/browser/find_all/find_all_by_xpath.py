from golem import actions
from golem.webdriver.extended_webelement import ExtendedWebElement


description = 'Verify that the webdriver.find_all method can find all web elements by xpath'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = '//input[@type="checkbox"]'
    actions.step('Find all elements by xpath')
    checkboxes = browser.find_all(xpath=selector)
    assert len(checkboxes) == 2

