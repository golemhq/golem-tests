from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify verify_response_status_code action'

def test(data):
    url = data.env.url + 'ajax-request-process/'
    params = {'numberOne': '1', 'numberTwo': '1', 'delay': '0'}
    actions.http_post(url, data=params)
    actions.verify_response_status_code(data.last_response, 200)
    golem_steps.assert_last_step_message('Verify response status code is 200')
