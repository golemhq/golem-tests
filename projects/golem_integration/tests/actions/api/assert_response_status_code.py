from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_response_status_code action'

def test(data):
    actions.http_get(data.env.url)
    actions.assert_response_status_code(data.last_response, 200)
    golem_steps.assert_last_step_message('Assert response status code is 200')
    try:
        actions.assert_response_status_code(data.last_response, 201)
    except AssertionError as e:
        assert 'expected response status code to be 201 but was 200' in e.args[0]
