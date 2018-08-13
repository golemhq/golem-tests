from golem import actions


description = 'Verify http_post action'

def test(data):
    url = data.env.url + 'ajax-request-process/'
    params = {'numberOne': '1', 'numberTwo': '1', 'delay': '0'}
    actions.http_post(url, data=params)
    assert data.last_response.status_code == 200
    assert data.last_response.text == '2'