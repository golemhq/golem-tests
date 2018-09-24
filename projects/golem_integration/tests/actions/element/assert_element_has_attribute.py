from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_has_attribute action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_has_attribute('#button-one', 'onclick')
    golem_steps.assert_last_step_message('Assert element #button-one has attribute onclick')
    msg = 'element #button-one does not have attribute not-this-one'
    with expected_exception(AssertionError, msg):
        actions.assert_element_has_attribute('#button-one', 'not-this-one')
