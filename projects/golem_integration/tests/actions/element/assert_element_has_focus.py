from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_has_focus action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.focus_element('#input-one')
    actions.assert_element_has_focus('#input-one')
    golem_steps.assert_last_step_message('Assert element #input-one has focus')
    actions.focus_element('#textarea-1')
    actions.assert_element_has_focus('#textarea-1')
    with expected_exception(AssertionError, 'element #input-one does not have focus'):
        actions.assert_element_has_focus('#input-one')
