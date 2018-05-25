from golem import actions
from golem.webdriver.extended_webelement import ExtendedWebElement


description = 'Verify that the webdriver.find_all method can find all web elements by tag name'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    actions.step('Find all elements by tag_name')
    inputs = browser.find_all(tag_name='input')
    assert len(inputs) == 5

