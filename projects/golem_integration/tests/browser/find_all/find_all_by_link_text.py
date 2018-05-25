from golem import actions
from golem.webdriver.extended_webelement import ExtendedWebElement


description = 'Verify that the webdriver.find_all method can find all web elements by link text'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    selector = 'this is a link to index'
    actions.step('Find all elements by link_text')
    links = browser.find_all(link_text=selector)
    assert len(links) == 1
