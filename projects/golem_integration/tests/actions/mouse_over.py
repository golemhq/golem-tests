from golem import actions
from golem.browser import element


description = 'Verify mouse_over action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.mouse_over(('id', 'mouse-over-one'))
    assert element(('id', 'mouse-over-one-result')).text == 'Mouse over!'
