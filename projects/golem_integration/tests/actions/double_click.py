from golem import actions
from golem.browser import element


description = 'Verify double_click action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.double_click(('id', 'double-click-one'))
    assert element(('id', 'double-click-one-result')).text == 'Double Clicked!'
