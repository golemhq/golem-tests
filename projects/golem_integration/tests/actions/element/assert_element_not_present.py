from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_not_present action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.assert_element_not_present('#does-not-exist')
    golem_steps.assert_last_step_message('Assert element is not present')
    with expected_exception(AssertionError, 'element #double-click-one is present'):
        actions.assert_element_not_present('#double-click-one')
