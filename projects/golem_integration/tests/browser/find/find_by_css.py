from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find method can find a web element by css'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'img#image1'
    actions.step('Find element by css')
    img = browser.find(css=selector)
    assert type(img) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    assert img.selector_type == 'css'
    assert img.selector_value == selector
    assert img.name == selector
