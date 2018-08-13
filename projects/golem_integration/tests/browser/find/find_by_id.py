from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find method can find a web element by id'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'button-one'
    actions.step('Find element by id')
    click_me_button = browser.find(id=selector)
    assert type(click_me_button) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    assert click_me_button.text == 'Click Me'
    assert click_me_button.selector_type == 'id'
    assert click_me_button.selector_value == selector
    assert click_me_button.name == selector
