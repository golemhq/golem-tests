from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find_all method can find all web elements by css'


def test(data):
    actions.navigate(data.env.url+'elements/')
    selector = 'input[type="checkbox"]'
    checkboxes = actions.get_browser().find_all(css=selector)
    assert len(checkboxes) == 2
    for checkbox in checkboxes:
        assert type(checkbox) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
        assert checkbox.selector_type == 'css'
        assert checkbox.selector_value == selector
        assert checkbox.name == selector
