from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_amount_of_windows'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.assert_amount_of_windows(1)
    assert golem_steps.get_last_step_message() == 'Assert amount of open windows is 1'
    actions.click('#openTab')
    actions.wait_for_window_present_by_title('Tab', 3)
    actions.assert_amount_of_windows(2)
    with expected_exception(AssertionError, 'expected 3 windows but got 2'):
        actions.assert_amount_of_windows(3)
