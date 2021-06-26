from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_response_status_code action'


def test_assert_response_status_code(data):
    actions.http_get(data.env.url)
    actions.assert_response_status_code(data.last_response, 200)
    golem_steps.assert_last_step_message('Assert response status code is 200')
    msg = 'expected response status code to be 201 but was 200'
    with expected_exception(AssertionError, msg):
        actions.assert_response_status_code(data.last_response, 201)
