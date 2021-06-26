from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify http_post action'


def test_http_post(data):
    url = data.env.url + 'form-basic-result/'
    payload = {
        'name': 'name',
        'planet': 'alderaan',
        'lightsaber': True,
        'alignment': 'Light Side'
    }
    response = actions.http_post(url, data=payload)
    golem_steps.assert_last_step_message('Make a POST request to {}'.format(url))
    assert response == data.last_response
    assert response.status_code == 200
