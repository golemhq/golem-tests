from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find method can find a web element by xpath positional arg'


def test(data):
    actions.navigate(data.env.url+'elements/')
    selector = '//img[@id="image1"]'
    img = actions.get_browser().find(selector)
    assert type(img) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    assert img.selector_type == 'xpath'
    assert img.selector_value == selector
    assert img.name == selector
