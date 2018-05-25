from golem import actions


description = 'Verify the user can pass timeout value to webdriver.find method and it waits until the element is present'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=5')
    browser = actions.get_browser()
    actions.step('Find element by id with timeout')
    button = browser.find(id='button-five', timeout=10)
    assert button.text == 'Click Me'
