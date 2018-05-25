from golem import actions
from golem.webdriver.extended_webelement import ExtendedWebElement


description = 'Verify that the webdriver.find method can find a web element by id'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'button-one'
    actions.step('Find element by id')
    click_me_button = browser.find(id=selector)
    assert type(click_me_button) == ExtendedWebElement
    assert click_me_button.text == 'Click Me'
    assert click_me_button.selector_type == 'id'
    assert click_me_button.selector_value == selector
    assert click_me_button.name == selector
