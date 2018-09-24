from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_present action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.assert_element_present('#double-click-one')
    golem_steps.assert_last_step_message('Assert element is present')
    with expected_exception(AssertionError, 'element #does-not-exist is not present'):
        actions.assert_element_present('#does-not-exist')
