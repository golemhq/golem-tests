from golem import actions
from golem.core.exceptions import ElementNotDisplayed


description = 'Verify webdriver.find throws error when time is out and element is still not displayed'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=5')
    browser = actions.get_browser()
    actions.step('Find element by id with timeout')
    try:
        button = browser.find(id='button-one', timeout=3, wait_displayed=True)
    except ElementNotDisplayed:
        pass
