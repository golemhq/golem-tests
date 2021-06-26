from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_has_not_focus action'


def test_assert_element_has_not_focus(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_has_not_focus('#input-one')
    golem_steps.assert_last_step_message('Assert element #input-one does not have focus')
    actions.focus_element('#input-one')
    with expected_exception(AssertionError, 'element #input-one has focus'):
        actions.assert_element_has_not_focus('#input-one')
