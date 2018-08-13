from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find method can find a web element by link text'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'this is a link to index'
    actions.step('Find element by link_text')
    link = browser.find(link_text=selector)
    assert type(link) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    assert link.text == selector
    assert link.selector_type == 'link_text'
    assert link.selector_value == selector
    assert link.name == selector
