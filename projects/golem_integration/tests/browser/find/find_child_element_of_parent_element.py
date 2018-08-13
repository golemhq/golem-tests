from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find method can be called from another webelement'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    actions.step('Find parent element by id')
    container = browser.find(id='button-one-container')
    actions.step('Find child element by id')
    click_button = container.find(id='button-one')
    assert type(click_button) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    assert click_button.text == 'Click Me'

