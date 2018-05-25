from golem import actions
from golem import execution


description = 'Verify the webdriver.find method uses the timeout defined in settings and settings timeout is 0'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    execution.settings['implicit_wait'] = 0
    actions.step('Find element by id with settings timeout equals zero')
    button = browser.find(id='button-one')
    assert button.text == 'Click Me'
