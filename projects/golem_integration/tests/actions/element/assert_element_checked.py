from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_checked action'


def test_assert_element_checked(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_checked('#selected-checkbox')
    golem_steps.assert_last_step_message('Assert element #selected-checkbox is checked')
    with expected_exception(AssertionError, 'element #unselected-checkbox is not checked'):
        actions.assert_element_checked('#unselected-checkbox')
    # radio button
    actions.assert_element_checked('#exampleRadios1')
    with expected_exception(AssertionError, 'element #exampleRadios2 is not checked'):
        actions.assert_element_checked('#exampleRadios2')
