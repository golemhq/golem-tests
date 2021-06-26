from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_has_not_attribute action'


def test_assert_element_has_not_attribute(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_has_not_attribute('#button-one', 'not-this-one')
    golem_steps.assert_last_step_message('Assert element #button-one has not attribute not-this-one')
    with expected_exception(AssertionError, 'element #button-one has attribute onclick'):
        actions.assert_element_has_not_attribute('#button-one', 'onclick')
