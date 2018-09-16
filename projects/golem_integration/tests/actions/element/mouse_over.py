from golem import actions
from golem.browser import element

from projects.golem_integration.pages import golem_steps


description = 'Verify mouse_over action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.mouse_over(('id', 'mouse-over-one'))
    golem_steps.assert_last_step_message("Mouse over element 'mouse-over-one'")
    assert element(('id', 'mouse-over-one-result')).text == 'Mouse over!'
