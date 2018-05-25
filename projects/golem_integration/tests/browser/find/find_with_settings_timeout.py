from golem import actions
from golem import execution


description = 'Verify the webdriver.find method uses the timeout defined in settings'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=5')
    browser = actions.get_browser()
    execution.settings['implicit_wait'] = 10
    actions.step('Find element by id with settings timeout')
    button = browser.find(id='button-five')
    assert button.text == 'Click Me'
