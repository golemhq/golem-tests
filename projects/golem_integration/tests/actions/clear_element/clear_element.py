from golem import actions
from golem import browser


description = 'Verify clear_element action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    element = ('id', 'input-one')
    actions.send_keys(element, 'test text')
    b = browser.get_browser()
    assert b.find(element).get_attribute('value') == 'test text'
    actions.clear_element(element)
    assert b.find(element).get_attribute('value') == ''

