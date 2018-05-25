from golem import actions
from golem import execution


description = 'Verify the webdriver.find method using timeout equals 0'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    actions.step('Find element by id with timeout equals zero')
    button = browser.find(id='button-one', timeout=0)
    assert button.text == 'Click Me'
