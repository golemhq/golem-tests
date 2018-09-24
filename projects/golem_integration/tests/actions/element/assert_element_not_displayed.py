from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_not_displayed action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.assert_element_not_displayed('#hidden-input')
    golem_steps.assert_last_step_message('Assert element #hidden-input is not displayed')
    with expected_exception(AssertionError, 'element #double-click-one is displayed'):
        actions.assert_element_not_displayed('#double-click-one')
