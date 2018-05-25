from golem import actions
from golem.webdriver.extended_webelement import ExtendedWebElement


description = 'Verify that the webdriver.find_all method can find all web elements by name'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'exampleRadioButtons'
    actions.step('Find all elements by name')
    radio_buttons = browser.find_all(name=selector)
    assert len(radio_buttons) == 2
    for radio in radio_buttons:
        assert type(radio) == ExtendedWebElement

