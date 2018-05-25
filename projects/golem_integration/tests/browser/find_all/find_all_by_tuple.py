from golem import actions
from golem.webdriver.extended_webelement import ExtendedWebElement


description = 'Verify that the webdriver.find_all method can find all web elements by passing a tuple definition to it'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'input[type="checkbox"]'
    actions.step('Find element by tuple')
    checkboxes = browser.find_all(('css', selector, 'Checkbox'))
    assert len(checkboxes) == 2
    for checkbox in checkboxes:
        assert checkbox.selector_type == 'css'
        assert checkbox.selector_value == selector
        assert checkbox.name == 'Checkbox'
