from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webelement.find_all method can find a web element by id'


def test(data):
    actions.navigate(data.env.url+'elements/')
    container = actions.get_browser().find('#button-one-container')
    selector = 'button-one'
    actions.step('Find all elements by id')
    click_me_buttons = container.find_all(id=selector)
    assert len(click_me_buttons) == 1
    first_button = click_me_buttons[0]
    assert type(first_button) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    assert first_button.text == 'Click Me'
    assert first_button.selector_type == 'id'
    assert first_button.selector_value == selector
    assert first_button.name == selector
