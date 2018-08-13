from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find method can find a web element by name'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'textarea-name'
    actions.step('Find element by name')
    text_area = browser.find(name=selector)
    assert type(text_area) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    assert text_area.text == ''
    assert text_area.selector_type == 'name'
    assert text_area.selector_value == selector
    assert text_area.name == selector
