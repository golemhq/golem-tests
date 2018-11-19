from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_displayed action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.assert_element_displayed('#double-click-one')
    golem_steps.assert_last_step_message('Assert element #double-click-one is displayed')
    with expected_exception(AssertionError, 'element #hidden-button is not displayed'):
        actions.assert_element_displayed('#hidden-button')
