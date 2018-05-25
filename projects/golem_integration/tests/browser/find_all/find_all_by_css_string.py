from golem import actions
from golem.webdriver.extended_webelement import ExtendedWebElement


description = 'Verify that the webdriver.find_all method can find all web elements by passing a css string directly'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'input[type="checkbox"]'
    actions.step('Find all elements by css')
    checkboxes = browser.find_all(selector)
    assert len(checkboxes) == 2
    for checkbox in checkboxes:
        assert type(checkbox) == ExtendedWebElement
        assert checkbox.selector_type == 'css'
        assert checkbox.selector_value == selector
        assert checkbox.name == selector
