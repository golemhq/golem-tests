from golem import actions
from golem.browser import element


description = 'Verify webelement.mouse_over method'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    button = actions.get_browser().find('#mouse-over-one')
    button.mouse_over()
    assert element('#mouse-over-one-result').text == 'Mouse over!'
