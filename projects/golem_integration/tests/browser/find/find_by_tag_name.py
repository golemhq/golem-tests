from golem import actions
from golem.webdriver.extended_webelement import ExtendedRemoteWebElement
from golem.webdriver.extended_webelement import ExtendedFirefoxWebElement


description = 'Verify that the webdriver.find method can find a web element by tag name'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'img'
    actions.step('Find element by tag_name')
    img = browser.find(tag_name=selector)
    assert type(img) in [ExtendedRemoteWebElement, ExtendedFirefoxWebElement]
    assert img.selector_type == 'tag_name'
    assert img.selector_value == selector
    assert img.name == selector
    assert '/static/images/cat-image.jpg' in img.get_attribute('src')
