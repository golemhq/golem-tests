from golem import actions
from golem.webdriver.extended_webelement import ExtendedWebElement


description = 'Verify that the webdriver.find method can find a web element by partial link text'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'this is a link to'
    actions.step('Find element by partial_link_text')
    link = browser.find(partial_link_text=selector)
    assert type(link) == ExtendedWebElement
    assert link.text == 'this is a link to index'
    assert link.selector_type == 'partial_link_text'
    assert link.selector_value == selector
    assert link.name == selector
