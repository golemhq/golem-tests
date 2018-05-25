from golem import actions
from golem.core.exceptions import ElementNotFound

description = 'Verify the webdriver.find method throws error when element is not found'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = '.invalid-selector-value'
    actions.step('Find element by css')
    try:
        elem = browser.find(css=selector)
    except ElementNotFound:
        pass

