from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find method can find a web element by passing a tuple definition without element name'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    actions.step('Find element by tuple without element name')
    click_me_button = browser.find(('id', 'button-one'))
    assert type(click_me_button) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    assert click_me_button.text == 'Click Me'
    assert click_me_button.selector_type == 'id'
    assert click_me_button.selector_value == 'button-one'
    assert click_me_button.name == 'button-one'
