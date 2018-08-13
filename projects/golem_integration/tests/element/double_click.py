from golem import actions
from golem.browser import element


description = 'Verify webelement.double_click method'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    button = actions.get_browser().find('#double-click-one')
    button.double_click()
    assert element('#double-click-one-result').text == 'Double Clicked!'
