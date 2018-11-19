from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_not_enabled action'

def test(data):
    actions.navigate(data.env.url+'disabled-elements/')
    actions.assert_element_not_enabled('#text')
    golem_steps.assert_last_step_message('Assert element #text is not enabled')
    actions.navigate(data.env.url+'elements/')
    with expected_exception(AssertionError, 'element #input-one is enabled'):
        actions.assert_element_not_enabled('#input-one')
