from golem import actions


description = 'Verify that with wait_displayed True webdriver.find waits until the element is present and displayed'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=5')
    browser = actions.get_browser()
    actions.step('Find element by id with timeout')
    button = browser.find(id='button-one', timeout=10, wait_displayed=True)
    assert button.text == 'Click Me'
