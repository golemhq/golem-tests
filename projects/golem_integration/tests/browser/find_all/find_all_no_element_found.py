from golem import actions
from golem.core.exceptions import ElementNotFound

description = 'Verify the webdriver.find_all method returns empty list when no element is not found'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = '.invalid-selector-value'
    actions.step('Find all elements by css')
    elems = browser.find_all(css=selector)
    assert type(elems) == list
    assert len(elems) == 0

